
# message = "Global message"
message = 2


def main():
    message2 = "Local message"
    print(type(message))
    print(type(message2))

    message2 = True
    print(type(message2))
    message2 = 34
    print(type(message2))


if __name__ == "__main__":
    main()
