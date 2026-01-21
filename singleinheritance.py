class Company:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def companyinfo(self):
        print("Company Name:", self.name)
        print("Role:", self.role)


class Employee(Company):
    def __init__(self, cname, role, ename, eno, ework):
        self.name = cname
        self.role = role
        self.empname = ename
        self.enum = eno
        self.eworkk = ework

    def employeeinfo(self):
        print("Employee Name:", self.empname)
        print("Employee Number:", self.enum)
        print("Work:", self.eworkk)


# ---- USER INPUT ----
cname = input("Enter company name: ")
role = input("Enter company role: ")

ename = input("Enter employee name: ")
eno = int(input("Enter employee number: "))
ework = input("Enter employee work: ")

# ---- OBJECT CREATION ----
e1 = Employee(cname, role, ename, eno, ework)

# ---- METHOD CALLS -----
e1.companyinfo()
e1.employeeinfo()
