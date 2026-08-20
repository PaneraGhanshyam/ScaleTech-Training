def register_user(name, age, email):

    if not name:
        raise ValueError(
            "Name cannot be empty."
        )

    if age < 18:
        raise ValueError(
            "User must be at least 18 years old."
        )

    if "@" not in email:
        raise ValueError(
            "Invalid email address."
        )

    return {
        "name": name,
        "age": age,
        "email": email
    }


try:

    user = register_user(
        "Ghanshyam",
        19,
        "ghanshyam@example.com"
    )

    print("Registration successful")
    print(user)

except ValueError as error:

    print(f"Registration failed: {error}")