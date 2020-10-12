class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def get_full_name(self):
        return "{} {}".format(self.fname, self.lname)

    def __repr__(self):
        return "Person: {} {}".format(self.fname, self.lname)


p = Person("Aamir", "Meman")

print(p.fname)
print(p.lname)
print(p.get_full_name())
print(p)

""" Outputs

Aamir
Meman
Aamir Meman
Person: Aamir Meman

"""