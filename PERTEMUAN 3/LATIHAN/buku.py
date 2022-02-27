class Buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
buku = Buku('tenggelamnya kapal van der wijck','HAMKA',1938)
print('buku {} karangan {} pertama kali di terbitkan pada tahun {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit))