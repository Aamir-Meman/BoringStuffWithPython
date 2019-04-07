nums = [1, 2, 3, 4, 5]  # if nums is empty then also else block will run
nums.append(6)

for num in nums:
    print(num)
else:
    print("sum: {}".format(sum(nums)))
