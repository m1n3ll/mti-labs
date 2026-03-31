class Car:
    def __init__(self):
        self.seats = None
        self.transmission = None
        self.engine = None


#Builder
class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_seats(self, seats):
        self.car.seats = seats
        return self

    def set_transmission(self, transmission):
        self.car.transmission = transmission
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def build(self):
        return self.car

#Director
class CarDirector:
    @staticmethod
    def build_economy_car():
        return (CarBuilder()
                .set_seats(4)
                .set_transmission("Manual")
                .set_engine("Standard")
                .build())

    @staticmethod
    def build_sports_car():
        return (CarBuilder()
                .set_seats(2)
                .set_transmission("Automatic")
                .set_engine("Turbocharged")
                .build())
    @staticmethod
    def custom_car():
        return (CarBuilder()
                .set_seats(8)
                .set_transmission("Automatic")
                .set_engine("Turbo Diesel")
                .build())
