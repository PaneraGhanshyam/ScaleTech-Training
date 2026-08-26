class LoggerMixin:

    def log(self, message):
        print(f"[LOG] {message}")


class EmailMixin:

    def send_email(self, message):
        print(f"[EMAIL] Sending email: {message}")


class Employee(LoggerMixin, EmailMixin):

    company = "ScaleTech"

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self._salary = salary
        self.__employee_id = employee_id

    def __str__(self):
        return (
            f"Employee("
            f"name='{self.name}', "
            f"id='{self.employee_id}', "
            f"salary={self._salary}"
            f")"
        )

    def __repr__(self):
        return (
            f"Employee("
            f"{self.name!r}, "
            f"{self.employee_id!r}, "
            f"{self._salary!r}"
            f")"
        )

    def give_raise(self, amount):
        if amount <= 0:
            raise ValueError(
                "Raise amount must be greater than zero."
            )

        self._salary += amount

        self.log(
            f"{self.name} received a raise of ₹{amount}"
        )

    def show_private_id(self):
        print(
            f"Private ID: {self.__employee_id}"
        )


employee = Employee(
    "Ghanshyam",
    "ST-001",
    50000
)

print("=== Employee Information ===")
print(employee)

print("\n=== Logging ===")
employee.log("Employee object created.")

print("\n=== Email ===")
employee.send_email(
    "Welcome to ScaleTech!"
)

print("\n=== Access Modifiers ===")

print(f"Public name: {employee.name}")

print(f"Internal salary: {employee._salary}")

employee.show_private_id()

print("\n=== Raise ===")

employee.give_raise(5000)

print(employee)

print("\n=== Escape Characters ===")

print("Employee:\tGhanshyam")
print("Company:\tScaleTech")
print("Message:\t\"Welcome to the team!\"")
print("Path:\tC:\\Users\\Ghanshyam")

print("\n=== MRO ===")

print(Employee.mro())
