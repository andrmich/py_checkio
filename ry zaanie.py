text = "No <hi> one"
begin = '>'
end = '<'
try:
    if text.find(begin) == 0:
        text = text.replace(begin, '')

    elif text.find(begin) > 0:
        text = text.split(begin)[1]

    else:
        text = text
    try:
        if text.find(end) < text.find(begin):
            print('')
        elif text.find(end) > 0:
            text = text.split(end)[0]
        else:
            text = text
    except ValueError:
        print(text)
except ValueError:
    print('')

# return ''
# return text
#print(text)
# print('')
