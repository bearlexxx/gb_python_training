duration = int(input('Введите продолжительность промежутка времени в секундах: '))

if duration < 60:
    print('{} сек'.format(duration))
elif 60 <= duration < 3600:
    print('{0} мин {1} сек'.format(duration // 60, duration % 60))
elif 3600 <= duration < 86400:
    print('{0} ч {1} мин {2} сек'.format(duration // 3600, (duration % 3600) // 60, duration % 60))
else:
    print('{0} дн {1} ч {2} мин {3} сек'.format(duration // 86400, (duration % 86400) // 3600, (duration % 3600) // 60, duration % 60))