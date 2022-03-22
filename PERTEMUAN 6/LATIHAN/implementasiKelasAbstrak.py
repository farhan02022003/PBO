from abc import ABC, abstractclassmethod, abstractmethod
class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        return self.__sisi * self.__sisi

    @abstractmethod
    def keliling(self):
       return 4*self.__sisi

class persegi(Bentuk):
    def __init__(self,sisi):
        self.__sisi = sisi

    def luas(self):
       return self.__sisi * self.__sisi

    def keliling(self):
       return 4*self.__sisi

persegi = persegi(6)
print(persegi.luas())
print(persegi.keliling())