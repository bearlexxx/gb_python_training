import sys

nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as f:
    if len(nums) > 1:
        start_i = int(nums[0])
        end_i = int(nums[1])
    elif len(nums) == 0:
        start_i = 0
        end_i = sum(1 for line in f)
        f.seek(0)
    else:
        start_i = int(nums[0])
        end_i = sum(1 for line in f)
        f.seek(0)

    for i, line in enumerate(f):
        if start_i <= i + 1 <= end_i:
            print(line.strip())


