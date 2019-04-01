import itertools

def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    # your code here
    d_new = [number for number in data]
    sorted_d = sorted(d_new)
    result = []
    slice_1= []
    slice_2 = []
    n = 0
    for n in range(len(sorted_d)):
        result.append(n) if sorted_d[n] - sorted_d[n-1] != 1 else ''
    result = sorted(result, reverse=True)

    for r in result:
        slice_1.append(sorted_d[r])
        slice_2.append(sorted_d[(len(sorted_d)-1)])
        del sorted_d[r:(len(sorted_d)+1)]

    answer = sorted(list(zip(slice_1, slice_2)))
    f_answer = (answer)
    # print(sorted_d)
    # print(result)
    # print (slice_1)
    # print (slice_2)
    print (answer)
