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

class RandomAccessMemory(ComputerPart):
    def __init__(self, nama, pabrikan, harga,kapasitas):
        super().__init__(nama, pabrikan,'RAM', harga)
        self.kapasitas = kapasitas

class HardDiskSATA(ComputerPart):
    def __init__(self, nama, pabrikan, harga,kapasitas,rpm):
        super().__init__(nama, pabrikan,'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm

p = Prosesor('Intel','Core i 7 7740X',4350000,4,'4.3GHz')
m = RandomAccessMemory('V - Gen','DDR S0Dimm PC19200/2400MHz',328000,'4GB')
hdd = HardDiskSATA('seagate','HDD 2.5 inc',295000,'500GB',7200)
parts = [p,m,hdd]
for i in parts:
    print('{} {} produksi {}'.format(i.jenis,i.nama,i.pabrikan))