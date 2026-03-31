import threading  #module to handle multi-threaded environments

class Singleton:
    _instance = None
    _lock = threading.Lock() #mutex lock

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # thread-safe : it prevents two threads entering at the same time
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __copy__(self):
        return self

    def __deepcopy__(self, map): #map is kinda of a dictionary that keeps track of objects that were already copied
        return self