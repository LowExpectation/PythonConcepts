# PA12- Employee Data

# Reminder: When prompting the user,
# you must always include text which lets
# the user know what should be inputted.

# Project details:

# Create a Employee class with four instance attributes:

#     emp_number as an int
#     name as a string
#     department as a string
#     yearly_salary as an int

# The class should include an __init__() method to initialize
# an Employee object and a __str__() method to describe an
# initialized Employee object. The class should include two instance methods:

# one called update_department(),
# which takes a string as an argument
# and updates the employee's department attribute
# one called update_salary(), which takes an int as an argument
# and updates the employee's salary attribute.

# After the Employee class code,
# prompt the user to enter the
# emp_number, name, department and salary.
# Instantiate an Employee object by passing
# in the user's input as the arguments and print out the Employee's
# attributes by calling the __str__() method.
# No prompting for input should be included in the Employee class.

# Test the update_department() and update_salary() methods
# by calling both methods and passing in a new
# department and salary for the Employee object that you created.
# Call the __str__() to display the updated Employee's information.

# Save the program in a file named employee.py
# and attach the employee.py file to this assignment.
# Add the required comments to top of your .py file:
# You must include comments in your code following industry standards.
# Not including comments in your code or random comments that do not
# pertain to your code will result in points being deducted.

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
