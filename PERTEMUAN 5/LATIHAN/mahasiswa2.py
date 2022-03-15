class Mahasiswa():
    def __init__(self,nama,nim) :
        self.nama = nama
        self.nim = nim

class siswa1(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class siswa2(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

mhs1 = Mahasiswa('mikasa',12334)
mhs2 = siswa1('nezuko',34325)
mhs3 = siswa1('hancock',9873)
print(mhs1.nama, mhs1.nim)
print(mhs2.nim)
print(mhs3.nama)