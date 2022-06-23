from entity.base import Base

class Customer(Base):
    
    def __init__(self, x: float, y: float, demand: float, capacity: float = 0):
        super().__init__(x, y, capacity)
        self.__demand = demand

    def set_demand(self, demand: float) -> float:
        self.__demand = demand

    def get_demand(self) -> float:
        return self.__demand

if __name__ == "__main__":

    c = Customer(x=1, y=2, demand=500)
    print(c.get_x(), c.get_y(), c.get_demand())