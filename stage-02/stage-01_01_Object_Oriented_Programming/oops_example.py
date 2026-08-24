class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def work(self):
        print("Employee is working.")

class Developer(Employee):

    def work(self):
        print(
            f"{self.name} is writing code."
        )

class Designer(Employee):

    def work(self):
        print(
            f"{self.name} is designing UI."
        )

employees = [
    Developer("Ghanshyam", 50000),
    Designer("Alice", 45000)
]

for employee in employees:
    employee.work()