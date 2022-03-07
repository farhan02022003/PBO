# Semua variabel bersifat Private
class Mobil():
    def __init__(self,jendela,pintu,mesin):
        self.__jendela = jendela
        self.__pintu = pintu
        self.__mesin = mesin

    def tampil(self):
        print('merk jendela :',self.__jendela)
        print('jenis pintu :',self.__pintu)
        print('jenis mesin :',self.__mesin)

mobil1 = Mobil('Solar Gard','Sliding doors (pintu geser)','internal combustion engine (ICE)')
mobil1.tampil()










