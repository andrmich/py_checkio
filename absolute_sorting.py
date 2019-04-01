def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    from collections import Counter
    answer = Counter(data).most_common(1)
    return (answer[0][0])

    # # create list of tuples with counts
    #
    # listOfTuples = list(zip(map(data.count, data), data))
    #
    # # sort tuples by counts
    #
    # sortedList = sorted(listOfTuples, key=lambda x: x[0], reverse=True)
    #
    # return sortedList[0][1]

#return max(data, key=data.count)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
