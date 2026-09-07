import requests
import pandas as pd


BASE_URL = "https://6a9ec3a02f89be7fb70e9677.mockapi.io/api/v1/user"


# -------------------------
# READ - Get all users
# -------------------------
def get_users():
    response = requests.get(BASE_URL)
    response.raise_for_status()

    return response.json()


# -------------------------
# READ - Get one user
# -------------------------
def get_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    response.raise_for_status()

    return response.json()


# -------------------------
# CREATE - Add a user
# -------------------------
def create_user(name, address):
    user = {
        "name": name,
        "address": address
    }

    response = requests.post(BASE_URL, json=user)
    response.raise_for_status()

    return response.json()


# -------------------------
# UPDATE - Replace user
# -------------------------
def update_user(user_id, name, address):
    user = {
        "name": name,
        "address": address
    }

    response = requests.put(
        f"{BASE_URL}/{user_id}",
        json=user
    )

    response.raise_for_status()

    return response.json()


# -------------------------
# PARTIAL UPDATE - PATCH
# -------------------------
def patch_user(user_id, name=None, address=None):
    user = {}

    if name is not None:
        user["name"] = name

    if address is not None:
        user["address"] = address

    response = requests.patch(
        f"{BASE_URL}/{user_id}",
        json=user
    )

    response.raise_for_status()

    return response.json()


# -------------------------
# DELETE - Remove user
# -------------------------
def delete_user(user_id):
    response = requests.delete(
        f"{BASE_URL}/{user_id}"
    )

    response.raise_for_status()

    return response.json()


# -------------------------
# Pandas Analysis
# -------------------------
def analyze_users(users):
    df = pd.DataFrame(users)

    print("\n===== USER DATA =====")
    print(df[["id", "name", "address"]])

    print("\n===== TOTAL USERS =====")
    print(len(df))

    print("\n===== USERS BY ADDRESS =====")
    print(df["address"].value_counts())

    print("\n===== SORTED BY NAME =====")
    print(
        df.sort_values("name")[["id", "name", "address"]]
    )

    return df


# -------------------------
# Main Program
# -------------------------
def main():

    # GET - Read all users
    users = get_users()

    print("Initial users:")
    print(users)

    # POST - Create
    print("\nCreating user...")

    new_user = create_user(
        "Ghanshyam",
        "Ahmedabad"
    )

    print("Created:", new_user)

    # GET - Read one user
    user_id = new_user["id"]

    print("\nGetting created user...")

    user = get_user(user_id)

    print(user)

    # PUT - Update entire user
    print("\nUpdating user using PUT...")

    updated_user = update_user(
        user_id,
        "Ghanshyam Updated",
        "Gujarat"
    )

    print("Updated:", updated_user)

    # PATCH - Update only one field
    print("\nUpdating user using PATCH...")

    patched_user = patch_user(
        user_id,
        name="Ghanshyam Patched"
    )

    print("Patched:", patched_user)

    # GET - Get all users after changes
    users = get_users()

    # Pandas analysis
    df = analyze_users(users)

    # Save data
    df.to_csv("users.csv", index=False)

    print("\nData saved to users.csv")

    # DELETE
    print("\nDeleting created user...")

    deleted_user = delete_user(user_id)

    print("Deleted:", deleted_user)

    print("\nCRUD operations completed.")


if __name__ == "__main__":
    main()