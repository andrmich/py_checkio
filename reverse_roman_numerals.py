import string

first_ten_num = list(range(0, 10))
first_ten_rom = ('0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')

second_ten_rom = ('0', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C')
second_ten_num = list(range(0, 111, 10))
third_ten = ('0', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M')

fourth_ten = ('0', 'M', 'MM', 'MMM')

# first_ten = tuple(zip(first_ten_num, first_ten_rom))
candy = dict(zip(first_ten_rom, first_ten_num))
crisps = dict(zip(second_ten_rom, second_ten_num))


def reverse_roman(roman_string):
    if roman_string in first_ten_rom:
        print(candy[roman_string])

    answer = 0

    # jednosci
    for n in range(len(roman_string[-4:]), 0, -1):
        if roman_string[-n:] in first_ten_rom:
            answer += (candy[roman_string[n:]])
            roman_string = roman_string[:n]
            break

    # dziesiatki
    if len(roman_string) >= 4:
        for n in range(0, (len(roman_string[-4:]))):
            for m in roman_string[-4:]:
                if roman_string[-4:] in second_ten_rom:
                    answer += (crisps[roman_string[n:]])
                    roman_string = roman_string[:n]
                    break
    else:
        for n in range(0, (len(roman_string))):
            for m in roman_string[::-1]:
                if roman_string[n:] in second_ten_rom:
                    answer += (crisps[roman_string[n:]])
                    roman_string = roman_string[:n]
                    break


    print(roman_string)
    print(answer)
    # print(decimal)


reverse_roman('LXXIII')

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert reverse_roman('VI') == 6, '6'
#     assert reverse_roman('LXXVI') == 76, '76'
#     assert reverse_roman('CDXCIX') == 499, '499'
#     assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
#     print('Great! It is time to Check your code!');
