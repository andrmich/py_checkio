text = 'Never send a human to do a machine\'s job.'
begin = 'Never'
end = 'do'


try:
    if text.find(begin) == 0:
        text = text.replace(begin, '')

    elif text.find(begin) > 0:
        text = text.split(begin)[1]

    else:
        try:
            if text.find(end) > 0:
                text = text.split(end)[0]
                return text
            else:
                return text
        except ValueError:
            return ''
except ValueError:
    return ''
