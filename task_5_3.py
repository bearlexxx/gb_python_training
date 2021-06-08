import itertools

def mergin_generate(names, klasses):
    if len(names) >= len(klasses):
        for name, klass in itertools.zip_longest(tutors, klasses):
            yield (name, klass)
    else:
        for name, klass in zip(tutors, klasses):
            yield (name, klass)

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Владимир'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б'
]


mergin_list = mergin_generate(tutors, klasses)
print(type(mergin_list))
print(*mergin_list)

