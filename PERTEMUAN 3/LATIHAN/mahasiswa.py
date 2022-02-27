class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
m1 = Mahasiswa('udin',5210411219,'informatika',2021)
print('nama {} dengan nim {} jurusan {} tahun masuk {}'.format(m1.nama,m1.nim,m1.prodi,m1.thn_masuk))