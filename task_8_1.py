import re
EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    found_info = EMAIL.findall(email)[0]
    if found_info:
        name, domen = found_info
    else:
        raise ValueError(f'wrong email: {email}')
    print(f'Имя пользователя: {name}, почтовый домен: {domen}')

