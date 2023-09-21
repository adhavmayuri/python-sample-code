class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.year} {self.make} {self.model} is now running.")
        else:
            print(f"{self.year} {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.year} {self.make} {self.model} has been stopped.")
        else:
            print(f"{self.year} {self.make} {self.model} is not running.")

# Create instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Ford", "Mustang", 2023)

# Access attributes and methods of the instances
print(f"Car 1: {car1.year} {car1.make} {car1.model}")
car1.start()
car1.stop()

print(f"\nCar 2: {car2.year} {car2.make} {car2.model}")
car2.start()
car2.stop()
