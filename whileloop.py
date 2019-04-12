nums = [1, 2, 3, 4, 5]
counter = 0

while counter < len(nums):
    print("index: {}, values: {} ".format(counter, nums[counter]))
    counter = counter + 1
else:
    print("sums: {} ".format(sum(nums)))

