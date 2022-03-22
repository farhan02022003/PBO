class ComputerPart():
    def __init__(self,nama,pabrikan,jenis,harga):
        self.pabrikan = pabrikan
        self.harga = harga
        self.nama = nama
        self.jenis = jenis
        self.jumlah = int(input('masukan jumlah {}: '.format(self.nama)))

    def hitungharga(self):
        print('harga total : ',self.harga*self.jumlah)

class Prosesor(ComputerPart):
    def __init__(self, nama, pabrikan, harga,speed,jumlah_core):
        super().__init__(nama, pabrikan,'processor', harga)
        self.jumlah_core = jumlah_core
        self.speed = speed
    def hitungharga(self):
        print('harga total : ',self.harga*self.jumlah)

class RandomAccessMemory(ComputerPart):
    def __init__(self, nama, pabrikan, harga,kapasitas):
        super().__init__(nama, pabrikan,'RAM', harga)
        self.kapasitas = kapasitas
    def hitungharga(self):
        print('harga total : ',self.harga*self.jumlah)

class HardDiskSATA(ComputerPart):
    def __init__(self, nama,pabrikan, harga,kapasitas,rpm):
        super().__init__(nama, pabrikan,'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm
    def hitungharga(self):
        print('harga total : ',self.harga*self.jumlah)

p = Prosesor('Intel','Core i 7 7740X',4350000,4,'4.3GHz')
m = RandomAccessMemory('V - Gen','DDR S0Dimm PC19200/2400MHz',328000,'4GB')
hdd = HardDiskSATA('seagate','HDD 2.5 inc',295000,'500GB',7200)
parts = [p,m,hdd]
for i in parts:
    print('-'*25)
    print('{} {} produksi {} harga perbarang {}'.format(i.jenis,i.nama,i.pabrikan,i.harga))
    i.hitungharga()