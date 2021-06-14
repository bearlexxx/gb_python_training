from itertools import zip_longest
with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    with open('users.csv', encoding='utf-8') as users:
        with open('hobby.csv', encoding='utf-8') as hobbys:
            user_in_line = sum(1 for line in users)
            hobby_in_line = sum(1 for line in hobbys)

            if user_in_line < hobby_in_line:
                exit(1)

            users.seek(0)
            hobbys.seek(0)
            for line_user, line_user_hobby in zip_longest(users, hobbys):
                f.write(f'{line_user.strip()}: '
                        f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')


