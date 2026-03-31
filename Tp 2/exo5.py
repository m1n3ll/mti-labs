from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod # Every child class must implement this method
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a key.")
    
    def stop_engine(self):
        print("Car engine stopped.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with a button.")
    
    def stop_engine(self):
        print("Bike engine stopped.")

class Truck(Vehicle):
    def start_engine(self):
        print("Truck engine roars to life!")
    
    def stop_engine(self):
        print("Truck engine shut down.")


vehicles = [
    Car(),
    Bike(),
    Truck()
]

for v in vehicles:
    v.start_engine()
    v.stop_engine()
