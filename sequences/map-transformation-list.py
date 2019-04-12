nums = [1, 2, 3, 4, 5]


def square(x):
    return x**2


print(list(map(square, nums)))

"""
map function iterates over the list, passing each item into the transformation function.
The transformation function returns a new item which is added to a new list


"""