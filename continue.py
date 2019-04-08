# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = range(0, 100)
for num in nums:
    if num % 2 == 0:
        continue
    if num == 51:
        break
    print("Odd No: {}".format(num))
else:
    print("sum {}".format(sum(nums)))  # If we are using break this will not print else block
