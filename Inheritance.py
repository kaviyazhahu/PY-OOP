# Inherits, extends, override

class Employee: #Base Class
    def __init__(self, name , age,  salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary
    def work(self):
        print(f"{self.name} is working...")


class SoftwareDeveloper(Employee):
    def __init__(self, name, age, salary, level) -> None:
        super().__init__(name, age, salary)
        self.level = level    

class Designer(Employee):
    pass

se=SoftwareDeveloper("Kavi","29",29000,"J")
print(se.name,se.age,se.salary)
se.work()
print(se.level)

d=Designer("Jhon","29",30000)
print(d.name,d.age,d.salary)
d.work()