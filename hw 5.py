class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age


class Driver(Person):
    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number =number

    def show_info(self):
        return f"Name: {self.name}, Age: {self.get_age()}, Number: {self.number}"


driver = Driver("Nick", 35, "2112")
print(driver.show_info())
