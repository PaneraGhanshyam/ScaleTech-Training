from itertools import (
    combinations,
    permutations,
    product
)


features = [
    "WiFi",
    "Bluetooth",
    "GPS",
    "NFC"
]



print("=== Feature Combinations ===")

for combo in combinations(features, 2):
    print(combo)


print("\n=== Feature Permutations ===")

servers = [
    "Server-A",
    "Server-B",
    "Server-C"
]

for order in permutations(servers, 2):
    print(order)


print("\n=== Product Configurations ===")

colors = [
    "Black",
    "Silver"
]

storage = [
    "512GB",
    "1TB"
]

for configuration in product(colors, storage):
    print(configuration)