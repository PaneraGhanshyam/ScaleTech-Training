from functools import (
    partial,
    reduce,
    lru_cache
)


def calculate_price(price, tax_rate):
    return price + (price * tax_rate)


calculate_gst = partial(
    calculate_price,
    tax_rate=0.18
)

print("=== Partial ===")

price = 1000

final_price = calculate_gst(price)

print(f"Original price: ₹{price}")
print(f"Price with GST: ₹{final_price:.2f}")

prices = [
    100,
    250,
    300,
    150
]

total = reduce(
    lambda x, y: x + y,
    prices
)

print("\n=== Reduce ===")

print(f"Prices: {prices}")
print(f"Total: ₹{total}")


@lru_cache(maxsize=None)
def fibonacci(n):

    if n <= 1:
        return n

    return (
        fibonacci(n - 1)
        + fibonacci(n - 2)
    )


print("\n=== lru_cache ===")

print(
    f"Fibonacci(10): {fibonacci(10)}"
)

print(
    f"Cache information: "
    f"{fibonacci.cache_info()}"
)