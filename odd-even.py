students = [24, 48, 4, 39, 47, 3]

for student in students:
    if student % 2 == 0:
        print("Even number: {}".format(student))
    if student % 2 != 0:
        print("Odd number: {} ".format(student))
else:
    print("Sum: {} ".format(sum(students)))
