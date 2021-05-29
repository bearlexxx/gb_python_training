price_list = [57.8, 46.51, 97, 18.35, 27, 112.05, 34, 96.5, 61, 78.12, 32, 45.55, 99.99, 123, 54.7, 11.11, 28.05, 20.21, 64.24, 55.05]

#function printing of prices with rubles and pennies in one line
def print_price(price_list):
    for price in price_list:
        if isinstance(price, float):
            print(f'{int(price)} руб. {int((price - int(price))*100):02d} коп., ', end='')
        elif isinstance(price, int):
            print(f'{price} руб. 00 коп., ', end='')
    print()
#A task
print_price(price_list)
print(id(price_list))

#B task
price_list.sort()
print_price(price_list)
print(id(price_list))

#C task
price_list.reverse()
print_price(price_list)

#D task
price_list = price_list[:5:]
price_list.reverse()
print_price(price_list)