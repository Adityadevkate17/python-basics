# Create Car class with brand and model.

class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = car("Toyota", "Camry")
print(car.brand)
print(car.model)

