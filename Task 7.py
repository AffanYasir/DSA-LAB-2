class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print("Department:", self.department)

manager = Manager("John", 50000, "HR")
manager.display_details()
