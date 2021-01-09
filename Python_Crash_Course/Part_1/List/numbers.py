for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

""" squares """
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

squares_2 = [value**2 for value in range(1, 11)]
print(squares_2)

""" digits """
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
