class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
m1 = Mahasiswa('udin',5210411219,'informatika',2021)
m2 = Mahasiswa('siti',5210411223,'Teknik Komputer',2020)
m3 = Mahasiswa('gauzi',5210411453,'Sistem Informasi',2029)
mahas = [m1,m2,m3]
for i in mahas:
    print('nama {} dengan nim {} jurusan {} tahun masuk {}'.format(i.nama,i.nim,i.prodi,i.thn_masuk))
