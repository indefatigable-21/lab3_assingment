class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

# Create a list of employees
employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

# Function to search employees by age
def search_by_age():
    try:
        age_operator = input("Enter age operator (<, >, <=, >=): ")
        age_value = int(input("Enter age value: "))

        for employee in employees:
            if age_operator == '<' and employee.age < age_value:
                print_employee(employee)
            elif age_operator == '>' and employee.age > age_value:
                print_employee(employee)
            elif age_operator == '<=' and employee.age <= age_value:
                print_employee(employee)
            elif age_operator == '>=' and employee.age >= age_value:
                print_employee(employee)
    except ValueError:
        print("Invalid input. Age value must be an integer.")

# Function to search employees by salary
def search_by_salary():
    try:
        salary_operator = input("Enter salary operator (<, >, <=, >=): ")
        salary_value = int(input("Enter salary value: "))

        for employee in employees:
            if salary_operator == '<' and employee.salary < salary_value:
                print_employee(employee)
            elif salary_operator == '>' and employee.salary > salary_value:
                print_employee(employee)
            elif salary_operator == '<=' and employee.salary <= salary_value:
                print_employee(employee)
            elif salary_operator == '>=' and employee.salary >= salary_value:
                print_employee(employee)
    except ValueError:
        print("Invalid input. Salary value must be an integer.")

# Function to search employees by ID
def search_by_employee_id():
    emp_id = input("Enter Employee ID: ")
    for employee in employees:
        if emp_id == employee.emp_id:
            print_employee(employee)
            return
    print("Employee not found.")

# Function to print employee details
def print_employee(employee):
    print(f"Employee ID: {employee.emp_id}")
    print(f"Name: {employee.name}")
    print(f"Age: {employee.age}")
    print(f"Salary: {employee.salary}")
    print()

# Main program
while True:
    print("Menu:")
    print("1. Search by Age")
    print("2. Search by Salary")
    print("3. Search by Employee ID")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        search_by_age()
    elif choice == '2':
        search_by_salary()
    elif choice == '3':
        search_by_employee_id()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
