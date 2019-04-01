def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return (3 * int(number) + 1)


print('Pick a number')

number = input()

try:
    int(number)
except ValueError:
    print('Invalid argument')
    exit()

while True:
    number = int(collatz(int(number)))
    print(number)
    if number == 1:
        break
