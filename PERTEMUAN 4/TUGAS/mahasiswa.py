class Mahasiswa:
    __alamat = ''
    def __init__(self,nama,nim,prodi,thn_masuk,alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
        self.__alamat = alamat

    def tampil(self):
        print('Nim :',self.nim)
        print('Nama :',self.nama)
        print('alamat',self.__alamat)
        print('Prodi :',self.prodi)
        print('Tahun Masuk :',self.thn_masuk)
        print('-'*25)

m1 = Mahasiswa('udin',5210411219,'informatika',2021,'Yogyakarta')
m2 = Mahasiswa('siti',5210411223,'Teknik Komputer',2020,'Malang')
m3 = Mahasiswa('gauzi',5210411453,'Sistem Informasi',2029,'Surabaya')
mahas = [m1,m2,m3]
print('-'*5,' DAFTAR MAHASISWA','-'*5)
for i in mahas:
    i.tampil()

