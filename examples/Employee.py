class Employee:
    """class for employees"""
    EmployeeCount = 0

    def __init__(self, name="deneme", salary=1):
        self.name = name
        self.salary = salary
        Employee.EmployeeCount += 1

    def displayCount(self):
        print("Total Employee:", Employee.EmployeeCount)

    def displayEmployee(self):
        print("Name:", self.name, " Salary:", self.salary)

    def __str__(self):
        return 'Employee(%s, %d)' % (self.name, self.salary)
        # return self.name


emp = Employee("Harun", 1000)
emp.EmployeeCount=11
Employee.salary = 3000
emp.name = "Harun Altay"
emp.displayCount()
emp.displayEmployee()
print("emp.EmployeeCount:", emp.EmployeeCount)
print("Employee.salary:", Employee.salary)
print("emp:", emp)

print()
emp2 = Employee("Tarık", 1500)
emp2.displayCount()
emp2.displayEmployee()

print()
emp3 = Employee()
emp3.displayCount()
emp3.displayEmployee()
