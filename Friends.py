class Friends:
    def __init__(self, connections):
        self.connections = set(frozenset(c) for c in connections)

    def add(self, connection):
        connection = frozenset(connection)
        if connection in self.connections:
            return False
        self.connections.add(connection)
        return True

    def remove(self, connection):
        try:
            self.connections.remove(connection)
            return True
        except KeyError:
            return False

    def names(self):
        result = set()
        for connection in self.connections:
            result = result.union(connection)
        return result

    def connected(self, name):
        result = set()
        for connection in self.connections:
            if name in connection:
                result = result.union({n for n in connection if n != name})
        return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"


## dziedziczenie po secie


class Friends(set):

    def __init__(self, pairs=set()):

        super().__init__(map(frozenset, pairs))

    def add(self, pair):

        if pair in self: return False

        super().add(frozenset(pair))

        return True

    def remove(self, pair):

        if pair not in self: return False

        super().remove(pair)

        return True

    def names(self):

        return set().union(*self)

    def connected(self, name):

        return Friends(filter({name}.issubset, self)).names() - {name}
