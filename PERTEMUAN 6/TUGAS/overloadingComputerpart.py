class ComputerPart():
    def __init__(self,nama,pabrikan,jenis,harga):
        self.pabrikan = pabrikan
        self.harga = harga
        self.nama = nama
        self.jenis = jenis

class Prosesor(ComputerPart):
    def __init__(self, nama, pabrikan, harga,speed,jumlah_core):
        super().__init__(nama, pabrikan,'processor', harga)
        self.jumlah_core = jumlah_core
        self.speed = speed
    def hitungharga(self, diskon=None ):
        jumlah_barang = int(input(f'masukan jumlah {self.nama} yang di beli : '))
        hargatotal = jumlah_barang*self.harga
        if hargatotal > 500000:
            diskon =  hargatotal*0.4
            print('anda mendapatkan total diskon 40%')
            print('total harga :',diskon)
        else:
            diskon = diskon

class RandomAccessMemory(ComputerPart):
    def __init__(self, nama, pabrikan, harga,kapasitas):
        super().__init__(nama, pabrikan,'RAM', harga)
        self.kapasitas = kapasitas
    def hitungharga(self, diskon=None ):
        jumlah_barang = int(input(f'masukan jumlah {self.nama}  yang di beli : '))
        hargatotal = jumlah_barang*self.harga
        if hargatotal > 500000:
            diskon =  hargatotal*0.4
            print('anda mendapatkan total diskon 40%')
            print('total harga :',diskon)
        else:
            diskon = diskon

class HardDiskSATA(ComputerPart):
    def __init__(self, nama,pabrikan, harga,kapasitas,rpm):
        super().__init__(nama, pabrikan,'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm
    def hitungharga(self, diskon=None ):
        jumlah_barang = int(input(f'masukan jumlah {self.nama} yang di beli : '))
        hargatotal = jumlah_barang*self.harga
        if hargatotal > 500000:
            diskon =  hargatotal*0.4
            print('anda mendapatkan total diskon 40%')
            print('total harga :',diskon)
        else:
            diskon = diskon

p = Prosesor('Intel','Core i 7 7740X',4350000,4,'4.3GHz')
m = RandomAccessMemory('V - Gen','DDR S0Dimm PC19200/2400MHz',328000,'4GB')
hdd = HardDiskSATA('seagate','HDD 2.5 inc',295000,'500GB',7200)
parts = [p,m,hdd]
for i in parts:
    print('-'*25)
    print('{} {} produksi {} harga perbarang {}'.format(i.jenis,i.nama,i.pabrikan,i.harga))
    i.hitungharga()