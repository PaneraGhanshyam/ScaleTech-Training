def calculate_total(price, quantity, discount):
    subtotal = price * quantity
    discount_amount = subtotal * discount / 100
    total = subtotal - discount_amount

    return total


price = 1000
quantity = 3
discount = 10

result = calculate_total(price, quantity, discount)

print("Final total:", result)