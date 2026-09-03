def generate_numbers(limit):
    for number in range(1, limit + 1):
        yield number


numbers = generate_numbers(5)

for number in numbers:
    print(number)