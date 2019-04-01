spam = ['apples', 'bananas', 'tofu', 'cats']


def and_list(list):
    list[-1] = str('and ' + list[-1])
    # list.insert(-1, 'and')
    # print(list)


import copy

edd_list = []

while True:
    i = 0
    print('Enter the name of element' + str(i + 1) + ' (or enter nothing to stop.): ')
    x = input()
    if x == '':
        break
    edd_list = edd_list + [x]

edd = copy.copy(edd_list)
and_list(edd)
# for x in range(len(edd)):
#    print(edd[x])

str_edd= ' '.join(edd)
print(str_edd)