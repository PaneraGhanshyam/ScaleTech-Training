logs = [
    "INFO | 2026-08-19 | User login successful | user=ghanshyam",
    "ERROR | 2026-08-19 | Database connection failed | host=localhost",
    "INFO | 2026-08-19 | User logout successful | user=alice",
    "WARNING | 2026-08-19 | High memory usage | usage=87%",
    "ERROR | 2026-08-19 | Authentication failed | user=bob",
]


print("========== LOG ANALYZER ==========")

for log in logs:

    # Remove unnecessary whitespace
    log = log.strip()

    # Split the log into components
    parts = log.split(" | ")

    level = parts[0]
    date = parts[1]
    message = parts[2]
    metadata = parts[3]

    print(f"\nLevel    : {level}")
    print(f"Date     : {date}")
    print(f"Message  : {message}")
    print(f"Metadata : {metadata}")


print("\n========== ERROR LOGS ==========")

for log in logs:

    if log.startswith("ERROR"):
        print(log)


print("\n========== USERS ==========")

for log in logs:

    if "user=" in log:

        user = log.split("user=")[1]

        print(f"User: {user}")


print("\n========== LOG STATISTICS ==========")

error_count = 0
info_count = 0
warning_count = 0

for log in logs:

    if log.startswith("ERROR"):
        error_count += 1

    elif log.startswith("INFO"):
        info_count += 1

    elif log.startswith("WARNING"):
        warning_count += 1


print(f"Errors   : {error_count}")
print(f"Info     : {info_count}")
print(f"Warnings : {warning_count}")