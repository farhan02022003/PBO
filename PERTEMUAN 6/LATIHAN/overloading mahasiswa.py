class mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim
        # self.prodi =  prodi
        # self.thn_masuk =  thn_masuk
        # self.semester =  semester

    def tampil(self):
        print('nama :',self.nama,'nim :',self.nim)

    # methode overloading
    def hitungsks(self,jmlsks = None,sks = None):
        if jmlsks != None and sks != None:
            totalsks = jmlsks*sks
            print('total sks : ',totalsks)
        else:
            totalsks = jmlsks
            print('total sks :',totalsks)


# memanggil class
mhs1 = mahasiswa('eren',5210988761)
mhs2 = mahasiswa('luffy',52104111287)
mhs1.tampil()
mhs2.tampil()
mhs1.hitungsks(80,31)
mhs2.hitungsks(93)