class Warrior():
    '''like a warrior in game'''

    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_1.health > 0:
        if unit_1.health > 0:
            unit_2.health -= unit_1.attack
            if unit_2.health > 0:
                unit_1.health -= unit_2.attack
            elif unit_2.health <= 0:
                return True

    else:
        # print (False)
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
