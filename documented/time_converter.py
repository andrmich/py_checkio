''' Input: Time in a 12-hour format (as a string).

Output: Time in a 24-hour format (as a string). '''


def time_converter(time):
    if len(time) != 10:
        time = '0{time}'.format(time=time)
    if time[-4:] == 'a.m.':
        if time[:2] == '12':
            return '00{time}'.format(time=time[2:5])
        return str(time[:5])
    else:
        hour = int(time[:2]) + 12
        if hour != 24:
            return '{hour}{time}'.format(hour=hour, time=time[2:5])
        return '12{time}'.format(time=time[2:5])


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:00 a.m.'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
