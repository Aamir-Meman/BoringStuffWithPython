import math
nums = [1, 2, 3, 4, 5]


def sums():
    var = 0
    for num in nums:
        # global var
        var = var + num
    print("Total: {}".format(var))


def squares():
    counter = 0
    while counter < len(nums):
        for x in nums:
           x = int(math.pow(x, 2))
           print("Index: {}, Value: {}".format(nums[counter], x))
           counter = counter + 1


if __name__ == '__main__':
    squares()
    sums()


