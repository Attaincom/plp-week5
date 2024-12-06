class Device:  # Parent class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


class Smartphone(Device):  # Child class
    def __init__(self, brand, model, storage, camera):
        super().__init__(brand, model)  # Call parent constructor
        self.__storage = storage  # Private attribute
        self.camera = camera

    # Encapsulation with a getter for private attribute
    def get_storage(self):
        return self.__storage

    def install_app(self, app_name):
        return f"Installing {app_name} on {self.info()}."

# Creating an object
my_phone = Smartphone("Apple", "iPhone 14", "256GB", "12MP")
print(my_phone.info())  # Output: Apple iPhone 14
print(my_phone.get_storage())  # Output: 256GB
print(my_phone.install_app("Instagram"))  # Output: Installing Instagram on Apple iPhone 14.

class Animal:
    def move(self):
        pass  # Placeholder to be overridden

class Bird(Animal):
    def move(self):
        return "Flying ✈️"

class Fish(Animal):
    def move(self):
        return "Swimming 🐟"

class Snake(Animal):
    def move(self):
        return "Slithering 🐍"

# Demonstrating polymorphism
animals = [Bird(), Fish(), Snake()]

for animal in animals:
    print(animal.move())
