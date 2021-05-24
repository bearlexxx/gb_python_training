def sum_character(number): # функция для вычисления суммы цифр числа
    sum_character = 0
    while number != 0:
        sum_character += number % 10
        number = number // 10
    return sum_character

nums = []
for num in range(1, 1000, 2):
    nums.append(num ** 3)
print('Список из кубов нечётных чисел: \n {}'.format(nums))

# Пункт a задачи:
sum_num = 0
for num in nums:
    if sum_character(num) % 7 == 0:
        sum_num += num
print('Сумма чисел из списка, сумма цифр которых делится нацело на 7: {}'.format(sum_num))

# Пункт b и c
for i in range(len(nums)):
    nums[i] += 17
print('Новый список: \n {}'.format(nums))

sum_num = 0
for num in nums:
    if sum_character(num) % 7 == 0:
        sum_num += num
print('Сумма чисел из нового списка, сумма цифр которых делится нацело на 7: {}'.format(sum_num))

