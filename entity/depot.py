from base import Base

class Depot(Base):
    
    def __init__(self, x: float, y: float, capacity: float):
        super().__init__(x, y, capacity)

if __name__ == "__main__":

    d = Depot(x=10, y=22, capacity=555)
    print(d.get_x(), d.get_y(), d.get_capacity())