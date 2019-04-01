def checkio(text: str) -> str:
    # replace this for solution
    for letter in text:
        if not letter.isalpha():
            text = text.replace(letter, '')
    new_text = list(text.replace(' ', '').lower())
    #print(new_text)
    import collections
    most_frequent = tuple(collections.Counter(new_text).most_common())
    import operator
    sort = sorted(most_frequent, key=operator.itemgetter(0))
    print(sort)
    sort_1 = sorted(sort, key=operator.itemgetter(1), reverse=True)
    print(sort_1)
    return sort_1[0][0]

    # text = text.lower()
    # return max(string.ascii_lowercase, key=text.count)



if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    # assert checkio("How do you do?") == "o", "O is most wanted"
    # assert checkio("One") == "e", "All letter only once."
    # assert checkio("Oops!") == "o", "Don't forget about lower case."
    # assert checkio("AAaooo!!!!") == "a", "Only letters."
    # assert checkio("abe") == "a", "The First."
    # print("Start the long test")
    # assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    # print("The local tests are done.")
