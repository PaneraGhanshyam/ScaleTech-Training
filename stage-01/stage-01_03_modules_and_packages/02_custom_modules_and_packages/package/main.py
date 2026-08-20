from employee import (
    calculate_gross_salary,
    calculate_net_salary,
    validate_salary
)


employee_name = "Ghanshyam"

basic_salary = 30000
allowance = 5000
deduction = 2000


if validate_salary(basic_salary):

    gross_salary = calculate_gross_salary(
        basic_salary,
        allowance
    )

    net_salary = calculate_net_salary(
        gross_salary,
        deduction
    )

    print(f"Employee       : {employee_name}")
    print(f"Basic Salary   : ₹{basic_salary}")
    print(f"Allowance      : ₹{allowance}")
    print(f"Gross Salary   : ₹{gross_salary}")
    print(f"Deduction      : ₹{deduction}")
    print(f"Net Salary     : ₹{net_salary}")

else:
    print("Invalid salary")