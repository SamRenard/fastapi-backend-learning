import datetime
class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def from_string(cls, string):
        name,salary = string.split("-")
        return cls(name,float(salary))
    @staticmethod
    def is_workday(date):
        return date.weekday() < 5
    def __str__(self):
        return f"Employee {self.name},{self.salary}"
employee1 = Employee.from_string("Resul-9.0")
employee2 = Employee.from_string("Thomasine-8.0")
bugun=datetime.date.today()
print(employee1.is_workday(bugun))
print(employee2.is_workday(bugun))
print(employee1)
print(employee2)
