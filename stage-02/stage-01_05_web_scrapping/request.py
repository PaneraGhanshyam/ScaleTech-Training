import requests


url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)


print("=== HTTP Response ===")

print("Status Code:", response.status_code)
print("Content Type:", response.headers.get("Content-Type"))


if response.status_code == 200:

    users = response.json()

    print("\n=== Users ===")

    for user in users:

        print(
            f"ID: {user['id']} | "
            f"Name: {user['name']} | "
            f"Email: {user['email']}"
        )

else:

    print("Request failed.")