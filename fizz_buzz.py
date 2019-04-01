# Your optional code here
# You can import some modules or create additional functions
def divide_3(number):
    if number % 3 == 0:
        return True
    else:
        return False


def divide_5(number):
    if number % 5 == 0:
        return True
    else:
        return False


def checkio(number: int) -> str:
    if divide_3(number) and divide_5(number) is True:
        return 'Fizz Buzz'
    elif divide_3(number) == True and divide_5(number) == False:
        return 'Fizz'
    elif divide_3(number) == False and divide_5(number) == True:
        return 'Buzz'
    else:
        return str(number)

# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
