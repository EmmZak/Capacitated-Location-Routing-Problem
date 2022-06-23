from entity.base import Base

class Depot(Base):
    
    def __init__(self, x: float, y: float, capacity: float, opening_cost: float):
        super().__init__(x, y, capacity)
        self._opening_cost = opening_cost

    def set_opening_cost(self) -> float:
        return self._opening_cost

    def get_opening_cost(self) -> float:
        return self._opening_cost

if __name__ == "__main__":

    d = Depot(x=10, y=22, capacity=555)
    print(d.get_x(), d.get_y(), d.get_capacity(), d.get_opening_cost())