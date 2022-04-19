class PerpusItem:
    def __init__(self,judul,subjek,lokasi,info,harga):
        self.judul = judul
        self.subjek = subjek
        self.lokasi = lokasi
        self.info = info
        self.harga = harga


    # def lokasiSimpan(self):
    #     self.lokasi = lokasi
    #     self.info = info

class Buku(PerpusItem):
    def __init__(self, judul, subjek, lokasi, info, isbn,pengarang,jmlhal,ukuran,harga):
        super().__init__(judul, 'buku', lokasi, info,harga)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal
        self.ukuran = ukuran
        self.harga = harga

class Majalah(PerpusItem):
    def __init__(self, judul, subjek, lokasi, info,volume,issue,harga):
        super().__init__(judul, 'majalah', lokasi, info,harga)
        self.volume = volume
        self.issue = issue
        self.harga = harga

class DVD(PerpusItem):
    def __init__(self, judul, subjek, lokasi, info,aktor,genre,harga):
        super().__init__(judul, 'DVD', lokasi, info,harga)
        self.aktor = aktor
        self.genre = genre
        self.harga = harga

b = Buku('python','buku cetak','Rak no 1','dipinjam','92-231-123','ilham',2,'23x15',150000)
m = Majalah('dunia komputer','sofcopy','rak no 3','ada','VII','komputer',100000)
d = DVD('doraemon','sofcopy','rak no 3','ada','slamet','karun',120000)

daf = [b,m,d]
for i in daf:
    print('{} {} {}'.format(i.judul,i.subjek,i.lokasi,i.info,i.harga))