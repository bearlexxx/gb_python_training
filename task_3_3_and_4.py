def thesaurus(names):
    """ Solution of task No. 3 """
    cardfile = {}
    for name in names:
        cardfile.setdefault(name[:1:], [])
        cardfile[name[:1:]].append(name)
    return cardfile

def thesaurus_adv(names_surnames):
    """ Solution of task No. 4 """
    cardfiles = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        cardfiles.setdefault(surname[:1:], {})
        cardfiles[surname[:1:]].setdefault(name[:1:], [])
        cardfiles[surname[:1:]][name[:1:]].append(name_surname)
    return cardfiles

names = ["Иван", "Мария", "Петр", "Илья"]
names_surnames = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]

print(thesaurus(names))
print(thesaurus_adv(names_surnames))

