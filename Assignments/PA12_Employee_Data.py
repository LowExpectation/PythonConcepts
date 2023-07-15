# Caleb Woods
# PA 12 - Employee Data
# 07-16-2023


class employee:
    # Initialize the class variables
    def __init__(self, emp_number, name, department, *yearly_salary) -> None:
        string_salary = "".join(yearly_salary)
        self.employee_data = dict(
            {
                "emp_number": emp_number,
                "name": name,
                "department": department,
                "yearly_salary": string_salary,
            }
        )
        self.data_evaluation = True

    # Create helper to display string output
    def __str__(self) -> str:
        output_helper = """
        Employee Number:    {}
        Employee Name:      {}
        Employee Department {}
        Employee Salary:    {} """

        return output_helper.format(
            self.employee_data["emp_number"],
            self.employee_data["name"],
            self.employee_data["department"],
            self.employee_data["yearly_salary"],
        )

    def update_department(self, department) -> None:
        self.employee_data["department"] = department

    def update_salary(self, salary) -> None:
        self.employee_data["yearly_salary"] = salary


# Get the employee number and validate
print("Please enter the employee details when prompted and press enter when finished")
print()
emp_number = input("Please enter the employee number: ")
while emp_number.isspace() or emp_number == "" or not emp_number.isdigit():
    print()
    print("Please enter a valid numeric employee number")
    print()
    emp_number = input("Please enter the employee number: ")
# Get employee Name and validate
print()
name = input("Please enter the full employee name: ")
while name.isspace() or name == "":
    print()
    print("Please enter a valid employee name")
    print()
    name = input("Please enter the full employee name: ")
# Get employee department and validate
print()
department = input("Please enter the employee department: ")
while department.isspace() or department == "":
    print()
    print("Please enter a valid employee department")
    print()
    department = input("Please enter the employee department: ")
# Get employee salary and validate
print()
yearly_salary = input("Please enter the employee salary: ")
while yearly_salary.isspace() or yearly_salary == "" or not yearly_salary.isdigit():
    print()
    print("Please enter a valid, non-formated, numeric employee salary")
    print()
    yearly_salary = input("Please enter the employee salary: ")

# Create reference and instantiate
emp_ref = employee(emp_number, name, department, yearly_salary)
print()
print("Employee Information:")
print(str(emp_ref))

# Update the department
emp_ref.update_department("Finance")

# Update the salary
emp_ref.update_salary(60000)
print()
print("Updated Employee Information:")
print(str(emp_ref))
