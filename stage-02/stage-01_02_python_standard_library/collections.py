from collections import Counter, defaultdict, deque

activities = [
    "login",
    "view_product",
    "login",
    "purchase",
    "view_product",
    "login",
    "logout",
    "purchase",
    "login"
]

activity_count = Counter(activities)

print("=== Activity Count ===")

for activity, count in activity_count.items():
    print(f"{activity:<15}: {count}")


print("\nMost Common Activities:")

for activity, count in activity_count.most_common(3):
    print(f"{activity:<15}: {count}")

employees = [
    ("Ghanshyam", "Engineering"),
    ("Alice", "HR"),
    ("Bob", "Engineering"),
    ("Charlie", "Marketing"),
    ("David", "Engineering"),
    ("Eva", "HR")
]

employees_by_department = defaultdict(list)

for name, department in employees:
    employees_by_department[department].append(name)


print("\n=== Employees by Department ===")

for department, names in employees_by_department.items():
    print(f"{department}: {names}")


requests = deque([
    "Request-101",
    "Request-102",
    "Request-103"
])

print("\n=== Request Queue ===")

requests.append("Request-104")

while requests:

    current_request = requests.popleft()

    print(
        f"Processing {current_request}"
    )