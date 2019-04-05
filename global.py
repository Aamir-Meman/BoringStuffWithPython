"""
The global keyword will allow the global variable message to be assigned to within the main function without producing
a new local variable
"""

message = "This is a global!"


def main():
    global message
    message = "This is a local"
    print(message)


main()
# outputs "This is a local"
print(message)