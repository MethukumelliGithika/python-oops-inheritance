class Employee:
    def __init__(self, name):
        self.name = name
        self._access_level = "Basic"   # protected variable

    def show_access(self):
        print(f"{self.name} has {self._access_level} access")


class Manager(Employee):
    def show_access(self):
        self._access_level = "Manager"
        print(f"{self.name} has {self._access_level} access")


class Admin(Employee):
    def show_access(self):
        self._access_level = "Admin"
        print(f"{self.name} has {self._access_level} access")


# Polymorphism
employees = [
    Employee("Githika..."),
    Manager("Vasavi..."),
    Admin("Mahitha...")
]

for emp in employees:
    emp.show_access()
