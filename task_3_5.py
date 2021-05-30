import random
def get_jokes(n, flag):
    """
        This function generates jokes
        :param n: number of jokes
        :param flag: repeat words as a joke: yes or no
        :return: list of jokes
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    if flag.lower() == 'yes':
        for i in range(n):
            jokes.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    elif flag.lower() == 'no':
        try:
            for i in range(n):
                random.shuffle(nouns)
                random.shuffle(adverbs)
                random.shuffle(adjectives)
                jokes.append(f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}')
        except IndexError:
            print('Закончились слова для генератора шуток!')
    else:
        print('Неизвестное значение')
    return jokes

n = int(input('Введите количество шуток: '))
flag = input('Повторять слова в шутках? (yes/no): ')
print(get_jokes(n, flag))
