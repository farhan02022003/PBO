# Semua variabel bersifat protected
class Mobil():
    def __init__(self,jendela,pintu,mesin):
        self._jendela = jendela
        self._pintu = pintu
        self.__mesin = mesin

audi = Mobil(4,4,'diesel')
print(audi._Mobil__mesin)

class Truk(Mobil):
    def __init__(self,jendela,pintu,mesin,tipe):
        super().__init__(jendela,pintu,mesin)
        self.mesin = mesin
        self.tipebak = tipe

truk = Truk(4,4,'diesel','terbuka')
print(truk.mesin)
print(truk.tipebak)











