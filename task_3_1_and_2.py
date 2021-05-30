def num_translate_adv(num):
    nums_translate = {
        'zero':'ноль',
        'one':'один',
        'two':'два',
        'three':'три',
        'four':'четыре',
        'five':'пять',
        'six':'шесть',
        'seven':'семь',
        'eight':'восемь',
        'nine':'девять',
        'ten':'десять'
    }
    if num.islower() == True:
        return nums_translate.get(num.lower()).lower()
    elif num.isupper() == True:
        return nums_translate.get(num.lower()).upper()
    elif num.istitle() == True:
        return nums_translate.get(num.lower()).title()

num = input('Введите число прописью на английском: ')
print(num_translate_adv(num))

