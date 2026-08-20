import csv


students = [
    ["Ghanshyam", 19, 95],
    ["Alice", 20, 87],
    ["Bob", 21, 76],
]


with open(
    "students.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])

    writer.writerows(students)


with open(
    "students.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    print("Student Data:")

    for row in reader:
        print(row)