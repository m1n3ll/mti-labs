from abc import ABC, abstractmethod

# Abstract Products
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

class Table(ABC):
    @abstractmethod
    def use(self):
        pass

# Victorian Products
class VictorianChair(Chair):
        pass

class VictorianSofa(Sofa):
        pass

class VictorianTable(Table):
        pass

# Modern Products
class ModernChair(Chair):
        pass

class ModernSofa(Sofa):
        pass

class ModernTable(Table):
        pass

# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

# Concrete Factories
class VictorianFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()

    def create_table(self):
        return VictorianTable()

class ModernFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()

    def create_table(self):
        return ModernTable()
