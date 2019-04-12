people = [
    ("Bob", "Smith", 34),
    ("Anne", "Bredict", 21),
    ("John", "Smith", 46),
    ("Karen", "Tarkis", 24)
]

print(list(filter(lambda p: p[2] > 30, people)))


"""
 filtering function uses a predicate function to produce a new list of items which return true 
 from the predicate  function.
 A predicate function is a function which receives a set inputs (commonly only one) and returns True or False,
 based upon the logic applied to the inputs.
 In the case of a filter, a new array list values which return true for the predicate is produced.
"""
"""
[('Bob', 'Smith', 34), ('John', 'Smith', 46)]

"""