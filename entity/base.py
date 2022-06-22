from abc import ABC, ABCMeta, abstractmethod

class Base:
    """ Base entity that holds commun attirbutes """

    def __init__(self, x: float, y: float, capacity: float) -> None:
        self.__x = x
        self.__y = y
        self.__capacity = capacity
    
    def set_x(self, x: float) -> float:
        self.__x = x

    def get_x(self) -> float:
        return self.__x

    def set_y(self, y: float) -> float:
        self.__y = y

    def get_y(self) -> float:
        return self.__y

    def set_capacity(self, capacity: float) -> float:
        self.__capacity = capacity

    def get_capacity(self) -> float:
        return self.__capacity


if __name__ == "__main__":

    b = Base(1, 2, 50)
    print(b.get_x(), b.get_x(), b.get_capacity())