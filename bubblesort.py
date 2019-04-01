def bubblesort(lst):
    for passedLeft in range (len(lst)-1, 0, -1):
        for index in range(passedLeft):
            if lst[index] > lst[index+1]:
                lst[index], lst[index + 1] = lst[index+1], lst[index]
    return lst


l = [66,89,49,62,9,53,59]

print(bubblesort(l))

