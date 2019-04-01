FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    number = str(number)
    if len(number) == 1:
        print(FIRST_TEN[int(number) - 1])

    if len(number) == 2:
        if number[0] == '1':
            print(SECOND_TEN[int(number[1])])
        else:
            print(OTHER_TENS[int(number[0]) - 2] + ' ' + FIRST_TEN[int(number[1]) - 1])

    if len(number) == 3:
        if number[2] == '0':
            if number[1] == '0':
                print(FIRST_TEN[int(number[0]) - 1] + ' ' + HUNDRED)
            else:
                print(FIRST_TEN[int(number[0]) - 1] + ' ' + HUNDRED + ' ' + OTHER_TENS[int(number[0]) - 2])
        else:
            if number[1] == '0':
                print(FIRST_TEN[int(number[0]) - 1] + ' ' + HUNDRED + ' ' + FIRST_TEN[int(number[2]) - 1] )
            else:
                print(FIRST_TEN[int(number[0]) - 1] + ' ' + HUNDRED + ' ' + OTHER_TENS[int(number[1]) - 2] + ' ' + FIRST_TEN[int(number[2]) - 1])


            # replace this for solution
            return 'string representation of n'


checkio(113)

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(4) == 'four', "1st example"
#     assert checkio(133) == 'one hundred thirty three', "2nd example"
#     assert checkio(12) == 'twelve', "3rd example"
#     assert checkio(101) == 'one hundred one', "4th example"
#     assert checkio(212) == 'two hundred twelve', "5th example"
#     assert checkio(40) == 'forty', "6th example"
#     assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
#     print('Done! Go and Check it!')
