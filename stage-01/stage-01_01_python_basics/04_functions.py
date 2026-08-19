def create_student(**kwargs):
    """Create and return a student dictionary."""
    return kwargs


def calculate_total(*marks):
    """Return the total of any number of marks."""
    return sum(marks)


def calculate_average(*marks):
    """Return the average of any number of marks."""
    if not marks:
        return 0

    return sum(marks) / len(marks)


def get_grade(average):
    """Determine grade based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_eligibility(student):
    """Check whether the student satisfies admission requirements."""

    if student["age"] < 18:
        return False, "Student must be at least 18 years old."

    if student["percentage"] < 50:
        return False, "Minimum percentage requirement is 50%."

    if not student["has_documents"]:
        return False, "Required documents are missing."

    return True, "Student is eligible."


def display_report(student, total, average, grade, eligibility, message):
    """Display the final student report."""

    print("\n" + "=" * 40)
    print("         STUDENT REPORT")
    print("=" * 40)

    print(f"Name       : {student['name']}")
    print(f"Age        : {student['age']}")
    print(f"City       : {student['city']}")
    print(f"Percentage : {student['percentage']}%")
    print(f"Documents  : {student['has_documents']}")

    print("-" * 40)

    print(f"Total Marks: {total}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")

    print("-" * 40)

    if eligibility:
        print(f"Status     : ACCEPTED")
    else:
        print(f"Status     : REJECTED")

    print(f"Message    : {message}")

    print("=" * 40)


print("Student Management System")

name = input("Enter student name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")
percentage = float(input("Enter previous percentage: "))

documents_input = input("Does the student have all documents? (yes/no): ")
has_documents = documents_input.lower() == "yes"

marks = []

print("\nEnter marks for 5 subjects:")

for i in range(1, 6):
    mark = float(input(f"Subject {i}: "))
    marks.append(mark)


student = create_student(
    name=name,
    age=age,
    city=city,
    percentage=percentage,
    has_documents=has_documents
)

total = calculate_total(*marks)
average = calculate_average(*marks)
grade = get_grade(average)

eligibility, message = check_eligibility(student)

display_report(
    student,
    total,
    average,
    grade,
    eligibility,
    message
)