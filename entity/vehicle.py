from base import Base

class Vehicle(Base):
    
    def __init__(self, x: float, y: float, capacity: float, speed: float):
        super().__init__(x, y, capacity)
        self.__speed = speed

    def set_speed(self, speed: float) -> float:
        self.__speed = speed

    def get_speed(self) -> float:
        return self.__speed

if __name__ == "__main__":

    v = Vehicle(x=1, y=2, capacity=1000, speed=50)
    print(v.get_x(), v.get_y(), v.get_capacity(), v.get_speed())