print('-'*5,'CLASS MINUMAN','-'*5)
class minuman:
    def __init__(self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
nmn1 = minuman('jus jambu','jus jambu merah tanpa gula',8500)
nmn2 = minuman('jus alpukat ori','jus alpukat dengan tambahan air gula merah',5000)
nmn3 = minuman('jus alpukat xtra milk','jus alpukat dengan campuran susu coklat dengan taburan kepingan choco',15000)
nmn4 = minuman('red & smooth','smoothie pisang susu',17000)
pilihan_minuman = [nmn1,nmn2,nmn3,nmn4]
for i in pilihan_minuman:
    t = '{} harga {}'.format(i.nama,i.harga,i.deskripsi)
    print(t)