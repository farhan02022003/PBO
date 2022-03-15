# single intheritance
# parent class

class Hewan():
    def bersuara(self):
        print('kucing bersuara')

class Kucing(Hewan):
    def suara(self):
        print('meong.....meong.....meong.....')

# objek

k = Kucing()
k.suara()
k.bersuara()