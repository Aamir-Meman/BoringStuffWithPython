
# from calc import add as calcAdd, pi, Person
# import my_math.calc

from my_math.calc import pi, add, Person


def main():
    print("running the program")
    print(add(1, 2))
    print(pi)
    p = Person("Bob", "Smith")
    print(p.get_full_name())


if __name__ == "__main__":
    main()

