users = [
    {"id": 1, "name": "Alice", "active": True},
    {"id": 2, "name": "Bob", "active": False},
    {"id": 3, "name": "Charlie", "active": True},
    {"id": 4, "name": "David", "active": True},
    {"id": 5, "name": "Eve", "active": True},
]

TARGET_USER_ID = 4


def future_feature():
    # This feature will be implemented later.
    pass


print("=== User Processing System ===")

for index in range(len(users)):

    user = users[index]

    # Skip inactive users
    if not user["active"]:
        print(f"Skipping {user['name']} - inactive")
        continue

    print(f"Processing {user['name']}")

    # Stop once we find the target user
    if user["id"] == TARGET_USER_ID:
        print(f"Target user found: {user['name']}")
        break


print("\nProcessing completed.")