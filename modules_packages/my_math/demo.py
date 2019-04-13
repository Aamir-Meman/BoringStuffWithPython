
from calc import add as calcAdd, pi, Person


def main():
    print("running the program")
    print(calcAdd(1, 2))
    print(pi)
    p = Person("Bob", "Smith")
    print(p.get_full_name())


if __name__ == "__main__":
    main()

