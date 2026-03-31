from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self): pass
    @abstractmethod
    def eat(self): pass
    @abstractmethod
    def sleep(self): pass
    @abstractmethod
    def get_salary(self): pass

class Robot(Worker): # Problem: Robots don't eat or sleep!
    pass

 # ISP = Interface Segregation Principle

class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self): pass

class Payable(ABC):
    @abstractmethod
    def get_salary(self): pass

class Human(Workable, Eatable, Sleepable, Payable):
    def work(self): pass
    def eat(self): pass
    def sleep(self): pass
    def get_salary(self): pass

class Robot(Workable, Payable):
    def work(self): pass
    def get_salary(self): pass

