def create_student(
    student_id,
    name,
    city,
    marks,
    skills
):
    return {
        "id": student_id,
        "name": name,
        "location": (city, "India"),  # Tuple
        "marks": marks,               # List
        "skills": set(skills)         # Set
    }


# --------------------------------------------------
# STUDENT DATA
# --------------------------------------------------

students = [

    create_student(
        101,
        "Ghanshyam",
        "Ahmedabad",
        [95, 88, 92, 90, 97],
        ["Python", "Git", "Linux", "AI"]
    ),

    create_student(
        102,
        "Alice",
        "Rajkot",
        [78, 85, 82, 80, 75],
        ["Python", "SQL", "Git"]
    ),

    create_student(
        103,
        "Bob",
        "Ahmedabad",
        [45, 52, 48, 55, 40],
        ["Java", "SQL"]
    ),

    create_student(
        104,
        "Charlie",
        "Surat",
        [92, 96, 89, 94, 91],
        ["Python", "AI", "Linux", "Docker"]
    )
]


# --------------------------------------------------
# LIST
# --------------------------------------------------

print("\n========== STUDENTS ==========")

for student in students:
    print(student["name"])


# --------------------------------------------------
# TUPLE
# --------------------------------------------------

print("\n========== LOCATIONS ==========")

for student in students:
    city, country = student["location"]

    print(
        f"{student['name']}: "
        f"{city}, {country}"
    )


# --------------------------------------------------
# SET
# --------------------------------------------------

print("\n========== UNIQUE SKILLS ==========")

all_skills = set()

for student in students:
    all_skills.update(student["skills"])

print("All skills:", all_skills)


# --------------------------------------------------
# SET OPERATIONS
# --------------------------------------------------

python_skills = {
    "Python",
    "Django",
    "FastAPI",
    "Flask"
}

ghanshyam_skills = students[0]["skills"]

print("\nGhanshyam skills:", ghanshyam_skills)

print(
    "Python-related skills:",
    ghanshyam_skills & python_skills
)


# --------------------------------------------------
# LIST COMPREHENSION
# --------------------------------------------------

print("\n========== LIST COMPREHENSION ==========")

student_names = [
    student["name"]
    for student in students
]

print("Names:", student_names)


# Students who have Python skill

python_students = [
    student["name"]
    for student in students
    if "Python" in student["skills"]
]

print("Python students:", python_students)


# --------------------------------------------------
# DICTIONARY COMPREHENSION
# --------------------------------------------------

print("\n========== DICTIONARY COMPREHENSION ==========")

student_averages = {
    student["name"]: sum(student["marks"]) / len(student["marks"])
    for student in students
}

print("Student averages:")

for name, average in student_averages.items():
    print(f"{name}: {average:.2f}")


# --------------------------------------------------
# ANOTHER DICTIONARY COMPREHENSION
# --------------------------------------------------

passed_students = {
    student["name"]: average
    for student, average in [
        (
            student,
            sum(student["marks"]) / len(student["marks"])
        )
        for student in students
    ]
    if average >= 50
}

print("\nPassed students:")

for name, average in passed_students.items():
    print(f"{name}: {average:.2f}")


# --------------------------------------------------
# PRACTICAL SKILL ANALYSIS
# --------------------------------------------------

print("\n========== SKILL ANALYSIS ==========")

required_skills = {
    "Python",
    "Git",
    "Linux"
}

for student in students:

    student_skills = student["skills"]

    missing_skills = required_skills - student_skills

    if missing_skills:
        print(
            f"{student['name']} is missing: "
            f"{missing_skills}"
        )
    else:
        print(
            f"{student['name']} has all required skills."
        )