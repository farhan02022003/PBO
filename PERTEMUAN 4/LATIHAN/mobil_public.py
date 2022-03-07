# Semua variabel bersifat Public
class Mobil():
    def __init__(self,jendela,pintu,mesin) :
        self.jendela = jendela
        self.pintu = pintu
        self.mesin = mesin

    def tampil(self):
        print('merk jendela :',self.jendela)
        print('jenis pintu :',self.pintu)
        print('jenis mesin :',self.mesin)

mobil1 = Mobil('Huper Optik',' Scissor doors (pintu gunting)',' external combustion engine (ECE)')
mobil1.tampil()









