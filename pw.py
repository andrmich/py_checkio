# between_markers("Never send a human to do a machine's job.","Never","do")

text = 'Never send a human to do a machine\'s job.'
begin = 'Never'
end = 'do'

if text.find(begin) == 0:
    text = text.replace(begin, '')
elif text.find(begin) > 0:
    text = text.split(begin)[1]
else:
    text = text

if text.find(end):
    text = text.split(end)[0]
else:
    return text
return text

