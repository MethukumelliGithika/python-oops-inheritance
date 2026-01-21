class Company:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def companyinfo(self):
        print("Company Name:", self.name)
        print("Role:", self.role)


class Employee(Company):
    def __init__(self, name, role, empname, empno):
        super().__init__(name, role)   # parent constructor call

        self.empname = empname
        self.empno = empno

    def employeeinfo(self):
        print("Employee Name:", self.empname)
        print("Employee Number:", self.empno)


# Object creation
e1 = Employee("Google", "IT Company", "Githika", 101)

e1.companyinfo()
e1.employeeinfo()
