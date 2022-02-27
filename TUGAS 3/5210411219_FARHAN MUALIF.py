# CLASS TITIK
class titik:
    def __init__(self,a,b):
        self.a = a
        self.b = b
titik_a = titik(3,6)
titik_b = titik(7,2)
print('titik X memiliki koordinat ({},{})'.format(titik_a.a,titik_a.b))
print('titik Y memiliki koordinat ({},{})'.format(titik_b.a,titik_b.b))

# objek baru
print('--- OBJEK BARU ---')
class titik:
    def __init__(self,x,y):
        self.x = x
        self.y = y
titik_x = titik(2,8)
titik_y = titik(9,2)
print('titik X memiliki koordinat ({},{})'.format(titik_x.x,titik_x.y))
print('titik Y memiliki koordinat ({},{})'.format(titik_y.x,titik_y.y))
        

# CLASS MINUMAN
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

# objek baru
class minuman: 
    def __init__(self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
nmn5 = minuman('Es Teh','Tanpa Gula',5000)
nmn6 = minuman('Capuchino','Tambahan Cincau',10000)
objek_baru = [nmn5,nmn6]
print('----- OBJEK BARU -----')
for x in objek_baru:
    p = '{} harga {}'.format(x.nama,x.harga,x.deskripsi)
    print(p)



# CLASS MAHASISWA
print()
print('-'*5,'CLASS MAHASISWA','-'*5)
class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
m1 = Mahasiswa('udin',5210411219,'informatika',2021)
print('nama {} dengan nim {} jurusan {} tahun masuk {}'.format(m1.nama,m1.nim,m1.prodi,m1.thn_masuk))

# objek baru
print('--- OBJEK BARU ---')
class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
m2 = Mahasiswa('siti',5210411223,'Teknik Komputer',2020)
m3 = Mahasiswa('gauzi',5210411453,'Sistem Informasi',2029)
mahas = [m2,m3]
for i in mahas:
    print('nama {} dengan nim {} jurusan {} tahun masuk {}'.format(i.nama,i.nim,i.prodi,i.thn_masuk))



    

# CLASS BUKU
print()
print('-'*5,'CLASS BUKU','-'*5)
class Buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
buku = Buku('tenggelamnya kapal van der wijck','HAMKA',1938)
print('buku {} karangan {} pertama kali di terbitkan pada tahun {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit))

# objek baru
print('--- OBJEK BARU ---')
class Buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
buku1 = Buku('ayat - ayat cinta','Habiburrahman El Shirazy',2004)
buku2 = Buku('Dilan','Pidi Baiq',2005)
buk = [buku1,buku2]
for x in buk:
    print('buku {} karangan {} pertama kali di terbitkan pada tahun {}'.format(x.judul,x.pengarang,x.tahun_terbit))