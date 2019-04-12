"""
The reduce function is the one iterative function which can be use
to implement all of the other iterative functions.

The basic idea of reduce is that it reduces the list to a single value.

The single value could be sum as shown below, or any kind of object including a new list
"""


from _functools import reduce

nums = [1, 2, 3, 4, 5]


def sum_number(total, next_val):
    print("total: {}, next_val: {}".format(total, next_val))
    return total + next_val


total_sum = reduce(sum_number, nums)

print(total_sum)
