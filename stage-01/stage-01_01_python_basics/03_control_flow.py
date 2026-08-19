users = [
    {"name":"ghanshyam","age":19,"percentage":99,"has_documents":True},
    {"name":"abc","age":17,"percentage":89,"has_documents":True},
    {"name":"opq","age":21,"percentage":70,"has_documents":False},
    {"name":"xyz","age":15,"percentage":60,"has_documents":False}
]

for user in users:
    if user["age"] < 18:
        print(f"User : {user['name']} Application rejected: Applicant must be at least 18.")
    elif user["percentage"] < 50:
        print(f"User : {user['name']}Application rejected: Minimum percentage is 50%.")
    elif not user["has_documents"]:
        print(f"User : {user['name']}Application pending: Required documents missing.")
    else:
        print(f"User : {user['name']} application accepted")

