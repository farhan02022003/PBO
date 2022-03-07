class minuman:
    __stok = 15
    def __init__(self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
    def tampil(self):
        print('Nama minuman :',self.nama)
        print('deskripsi :',self.deskripsi)
        print('harga :',self.harga)
        print('stok :',self.__stok)

nmn1 = minuman('jus jambu','jus jambu merah tanpa gula',8500)
nmn2 = minuman('jus alpukat ori','jus alpukat dengan tambahan air gula merah',5000)
nmn3 = minuman('jus alpukat xtra milk','jus alpukat dengan campuran susu coklat dengan taburan kepingan choco',15000)
nmn4 = minuman('red & smooth','smoothie pisang susu',17000)
nmn5 = minuman('Es Teh','Tanpa Gula',5000)
nmn6 = minuman('Capuchino','Tambahan Cincau',10000)
pilihan_minuman = [nmn1,nmn2,nmn3,nmn4,nmn5,nmn6]
print('-'*5,' MENU MINUMAN','-'*5)
for i in pilihan_minuman:
    i.tampil()
    print('-'*20)

