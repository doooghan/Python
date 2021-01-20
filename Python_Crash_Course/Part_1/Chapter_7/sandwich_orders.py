sandwich_orders = ['pastrami', 'beef sandwich', 'fish sandwich', 'pastrami',
                   'chicken sandwich', 'pastrami']
finished_sandwiches = []

print("The pastrami at the deli is sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("\nI made your tuna sandwich: " + sandwich)
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
