class Buku:
    __kodeBuku = 0
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

    def kodeBuku(self):
        kodeBuku = int(input('masukanKode buku :'))
        self.__kodeBuku = kodeBuku

    def tampil(self):
        print('judul buku :',self.judul)
        self.kodeBuku()
        print('pengarang buku :',self.pengarang)
        print('tahun terbit :',self.tahun_terbit)
        print('kode buku :',self.__kodeBuku)

buku1 = Buku('tenggelamnya kapal van der wijck','HAMKA',1938)
buku2 = Buku('ayat - ayat cinta','Habiburrahman El Shirazy',2004)
buku3 = Buku('Dilan','Pidi Baiq',2005)
buk = [buku1,buku2,buku3]
for i in buk:
    i.tampil()
    print('---------------------')










