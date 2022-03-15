# multilevel

# parent class
class Hewan():
    def bersuara(self):
        print('kucing bersuara')

# child class mewarisi class hewan
class Kucing(Hewan):
    def suara(self):
        print('meong.....meong.....meong.....')

# child class AnakKucing  mewarisi dari anak hewan
class AnakKucing(Kucing):
    def minum(self):
        print('minum susu')

# objek

ak = AnakKucing()
ak.bersuara()
ak.suara()
ak.minum()