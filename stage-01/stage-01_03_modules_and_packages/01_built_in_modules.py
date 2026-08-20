import math
import random
import os
from datetime import datetime


# ==========================================
# SYSTEM INFORMATION
# ==========================================

print("========== SYSTEM INFORMATION ==========")

print(f"Current Directory : {os.getcwd()}")
print(f"Process ID        : {os.getpid()}")
print(f"CPU Count         : {os.cpu_count()}")


# ==========================================
# DATE AND TIME
# ==========================================

print("\n========== DATE & TIME ==========")

current_time = datetime.now()

print(f"Current Date      : {current_time.date()}")
print(f"Current Time      : {current_time.time()}")
print(f"Formatted Date    : {current_time.strftime('%d-%m-%Y %H:%M:%S')}")


# ==========================================
# RANDOM VALUES
# ==========================================

print("\n========== RANDOM DATA ==========")

dice = random.randint(1, 6)
random_number = random.uniform(10, 100)

languages = ["Python", "C++", "Rust", "Java"]
selected_language = random.choice(languages)

print(f"Dice Roll         : {dice}")
print(f"Random Number     : {random_number:.2f}")
print(f"Selected Language : {selected_language}")


# ==========================================
# MATHEMATICAL OPERATIONS
# ==========================================

print("\n========== MATHEMATICS ==========")

number = random.randint(1, 100)

print(f"Number            : {number}")
print(f"Square Root       : {math.sqrt(number):.2f}")
print(f"Square            : {math.pow(number, 2):.0f}")
print(f"Ceiling           : {math.ceil(number / 3)}")
print(f"Floor             : {math.floor(number / 3)}")
print(f"Factorial of 5    : {math.factorial(5)}")
print(f"Value of PI       : {math.pi}")


# ==========================================
# FILESYSTEM
# ==========================================

print("\n========== DIRECTORY CONTENT ==========")

items = os.listdir(".")

for item in items:

    if os.path.isfile(item):
        print(f"[FILE]      {item}")

    elif os.path.isdir(item):
        print(f"[DIRECTORY] {item}")