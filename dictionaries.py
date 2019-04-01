import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for charakter in message:
    count.setdefault(charakter, 0)
    count [charakter] = count [charakter] + 1

pprint.pprint(count)