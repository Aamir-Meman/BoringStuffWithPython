
"""Shadowing"""

message = "This is a global!"


def main():
    message = "This is a local"
    print(message)


main()
# outputs "This is global!"
# 2 variables reference for message variable
print(message)