class Engine:
    def __init__(self, power):
        self.power = power
        print(f"Engine with {self.power} created.")

    def __del__(self):
        print(f"Engine with {self.power} destroyed.")


class Car:
    def __init__(self, engine_power):
        self.engine = Engine(engine_power)  # composition
        print("Car created with engine.")

    def __del__(self):
        print("Car destroyed.")
        


class Driver:
    def __init__(self, name, car=None):
        self.name = name
        self.car = car  #aggregation
        print(f"Driver {self.name} created.")

    def drive(self):
        if self.car:
            print(f"{self.name} is driving a car with {self.car.engine.power} engine.")
        else:
            print(f"{self.name} has no car to drive.")

    def __del__(self):
        print(f"Driver {self.name} destroyed.")


driver = Driver("Manel")  
car = Car(150)            
driver.car = car          

driver.drive()
del car 
driver.drive()

#Composition = owns → dies together, Aggregation = uses → independent.