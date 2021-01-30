print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit!")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    last_number = input("\nLast number: ")
    if last_number == "q":
        break
    try:
        answer = int(first_number) / int(last_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)