class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
              
class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        super().__init__(name, id_number)
        self.salary = salary
        self.post = post
    
    def display(self):
        super().display()
        print(f"Salary: {self.salary}")
        print(f"Post: {self.post}")
        
person = Person("Dolores", 12345)
print("Person Information:")
person.display()

print("------------------------------------------------")

employee = Employee("James", 67890, 50000, "Manager")
print("Employee Information:")
employee.display()