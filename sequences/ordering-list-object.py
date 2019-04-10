class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return "Person: {} {}".format(self.fname, self.lname)


people = [
     Person("Bob", "Smith"),
     Person("Tim", "Johnson"),
     Person("Mike", "Collins")

]

"""
Without Lambda

"""


def comparison_value(p):
    return p.lname


people.sort(key=comparison_value)

# people.sort(key=lambda p: p.lname)

print(people)


