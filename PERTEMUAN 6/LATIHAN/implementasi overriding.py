class segiempat:
    def __init__(self,panjang,lebar):
        self.panjang= panjang
        self.lebar= lebar

    def hitungluas(self):
        print('luas segiempat =',self.panjang*self.lebar,'m^2')

class bujursangkar:
    def __init__(self,sisi):
        self.side= sisi
        segiempat.__init__(self,sisi,sisi)

    def hitungluas(self):
        print('luas bujur sangkar =',self.side*self.side,'m^2')


b = bujursangkar(4)
s = segiempat(2,3)
b.hitungluas()
s.hitungluas()


