#Task 1
def odd_nums(nums):
    for num in range(1, nums + 1, 2):
        yield num

nums = int(input('Введите число для генератора нечетных чисел: '))
odd_to_nums = odd_nums(nums)

#Task2
odd_to_nums2 = (num for num in range(1, nums + 1, 2))

