def checkio(data: str) -> bool:

    #replace this for solution
    if len(data) >= 10:
        if not data.isalpha() and not data.isdecimal():
            if not data.islower():
                if not data.isupper():
                    return True
    return False

#import re
    # x = re.search("[1-9]", data)
    #
    # y = re.search("[a-z]", data)
    #
    # z = re.search("[A-Z]", data)
    #
    # # replace this for solution
    #
    # return x and y and z and len(data) >= 10

#re.match (\A(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{10,64}\Z)
#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
