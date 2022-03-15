class Mahasiswa1():
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

class Mahasiswa2():
    def __init__(self,alamat,jurusan):
        self.jurusan = jurusan
        self.alamat = alamat

class siswa(Mahasiswa1,Mahasiswa2):
    def __init__(self,nama,nim,alamat,jurusan):
        Mahasiswa1.__init__(self,nama,nim)
        Mahasiswa2.__init__(self,alamat,jurusan)

s = siswa('mikasa',1323,'wall rose','informatika')
print('nim',s.nim,'nama',s.nama,'alamat',s.alamat,'jurusan',s.jurusan)