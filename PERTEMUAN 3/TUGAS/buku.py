class Buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
buku = Buku('tenggelamnya kapal van der wijck','HAMKA',1938)
buku1 = Buku('ayat - ayat cinta','Habiburrahman El Shirazy',2004)
buku2 = Buku('Dilan','Pidi Baiq',2005)
buk = [buku,buku1,buku2]
for x in buk:
    print('buku {} karangan {} pertama kali di terbitkan pada tahun {}'.format(x.judul,x.pengarang,x.tahun_terbit))