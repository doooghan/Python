print("Give me two numbers, and I'll add them.")
# print("Enter 'q' to quit")

while True:
    print()
    try:
        first_number = int(input("First number: "))
    except ValueError:
        print("please enter number")
    else:
        print()
        try:
            last_number = int(input("last number: "))
        except ValueError:
            print("please enter number")
        else:
            print("answer: %s" % (first_number+last_number))
