def calculate_average(*marks):
    """Calculate average marks."""
    if not marks:
        return 0

    return sum(marks) / len(marks)


def create_student(**kwargs):
    """Create and return a student dictionary."""
    return kwargs


students = [
    create_student(
        name="Ghanshyam",
        marks=[95, 88, 92, 90, 97]
    ),
    create_student(
        name="Alice",
        marks=[78, 85, 82, 80, 75]
    ),
    create_student(
        name="Bob",
        marks=[45, 52, 48, 55, 40]
    ),
    create_student(
        name="Charlie",
        marks=[92, 96, 89, 94, 91]
    ),
    create_student(
        name="David",
        marks=[60, 65, 58, 62, 70]
    ),
]


# --------------------------------------------------
# 1. Calculate statistics for every student
# --------------------------------------------------

for student in students:

    marks = student["marks"]

    student["total"] = sum(marks)

    student["average"] = calculate_average(*marks)

    student["highest"] = max(marks)

    student["lowest"] = min(marks)

    student["passed_all"] = all(mark >= 50 for mark in marks)

    student["scored_90_plus"] = any(mark >= 90 for mark in marks)


# --------------------------------------------------
# 2. MAP
# --------------------------------------------------

# Add 2 bonus marks to every subject for Ghanshyam.

original_marks = students[0]["marks"]

bonus_marks = list(
    map(
        lambda mark: mark + 2,
        original_marks
    )
)

print("Original marks:", original_marks)
print("After bonus:", bonus_marks)


# --------------------------------------------------
# 3. FILTER
# --------------------------------------------------

# Keep only students whose average is >= 50.

passed_students = list(
    filter(
        lambda student: student["average"] >= 50,
        students
    )
)


# --------------------------------------------------
# 4. SORTED
# --------------------------------------------------

# Sort students from highest average to lowest.

ranked_students = sorted(
    passed_students,
    key=lambda student: student["average"],
    reverse=True
)


# --------------------------------------------------
# 5. ZIP
# --------------------------------------------------

subjects = [
    "Python",
    "Database",
    "Backend",
    "AI",
    "Algorithms"
]

print("\nGhanshyam's Subject Marks:")

for subject, mark in zip(subjects, students[0]["marks"]):
    print(f"{subject:<12}: {mark}")


# --------------------------------------------------
# 6. ENUMERATE
# --------------------------------------------------

print("\n========== STUDENT RANKING ==========")

for rank, student in enumerate(ranked_students, start=1):

    print(
        f"{rank}. "
        f"{student['name']} - "
        f"Average: {student['average']:.2f}"
    )


# --------------------------------------------------
# 7. ANY / ALL
# --------------------------------------------------

print("\n========== PERFORMANCE ANALYSIS ==========")

for student in students:

    print(f"\nStudent: {student['name']}")

    print(
        f"Passed all subjects: "
        f"{student['passed_all']}"
    )

    print(
        f"Scored 90+ in at least one subject: "
        f"{student['scored_90_plus']}"
    )


# --------------------------------------------------
# 8. BUILT-IN FUNCTIONS
# --------------------------------------------------

all_averages = [
    student["average"]
    for student in students
]

print("\n========== STATISTICS ==========")

print(f"Number of students : {len(students)}")

print(
    f"Highest average    : "
    f"{max(all_averages):.2f}"
)

print(
    f"Lowest average     : "
    f"{min(all_averages):.2f}"
)

print(
    f"Overall average    : "
    f"{round(sum(all_averages) / len(all_averages), 2)}"
)


# --------------------------------------------------
# 9. TYPE / ISINSTANCE
# --------------------------------------------------

print("\n========== TYPE CHECKING ==========")

print("students type:", type(students))

print(
    "students is list:",
    isinstance(students, list)
)

print(
    "first student is dictionary:",
    isinstance(students[0], dict)
)