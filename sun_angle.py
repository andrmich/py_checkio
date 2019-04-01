def sun_angle(time):
    hours = int(time.split(':')[0])
    minutes_1 = int(time.split(':')[1])
    minutes = hours*60 + minutes_1
    angle = 180 / (60*12)
    if hours < 6: return "I don't see the sun!"
    elif hours == 18 and minutes_1 > 0: return "I don't see the sun!"
    else:
        return round(((minutes - (6*60))*angle),2)





if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
