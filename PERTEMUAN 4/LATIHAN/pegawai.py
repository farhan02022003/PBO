class pegawai(): # Pembuatan class pegawai
    __nama = ''     # Atribut nama
    __alamat = ''   # Atribut alamat
    __gaji = ''     # Atribut gaji
    def __init__(self,nama,alamat):
        self.__nama = nama
        self.__alamat = alamat

    def hitungGaji(self): # Pembuatan Method hitungGaji
        upahLembur = 20000 # Atribut UpahLembur
        gajiPokok = 2000000 # Atribut 2 gajiPokok
        jmlLembur = int(input('Total jam lembur : '))   # Atribut jmlLembur
        self.__gaji = (upahLembur*jmlLembur)+gajiPokok

    def tampilDetail(self): #Pembuatan Method tampilDetail
        print('--- Menghitung dan menampilkan detail gaji pegawai ---')
        print('nama',self.__nama)       # Menampilkan Artibut Nama
        print('alamat',self.__alamat)   # Menampilkan Artibut Alamat
        self.hitungGaji()
        print('Total Gaji',self.__gaji) # Menampilkan Artibut gaji

pgw = pegawai('mikasa ackerman','wall rose')    # objek 1
pgw.tampilDetail()  #pemanggilan Method tampilDetail
pgw2 = pegawai('saya kisaragi','profektur nagano')  # objek 2
pgw2.tampilDetail() # #pemanggilan Method tampilDetail









