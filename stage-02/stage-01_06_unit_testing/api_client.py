import requests


def get_user(user_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )

    response.raise_for_status()

    return response.json()