email = input('What is your email adress?:').strip()

user_name = email[:email.index('@')]

domain = email[email.index('@') + 1:]

output = 'Your username is {} and your domain name is {}.'.format(user_name, domain)

print(output)
