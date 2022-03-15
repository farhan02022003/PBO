class ComputerPart:
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def set(self) :
        print("{} produk dari {}".format(self.nama,self.pabrikan))
        print("Harga : {}".format(self.harga))

class RandomAccessMemory(Processor) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def set(self) :
        print("{} produk dari {}".format(self.nama,self.pabrikan))
        print("Harga : {}".format(self.harga))

class HardDiskSATA(RandomAccessMemory) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def set(self) :
        print("{} produk dari {}".format(self.nama,self.pabrikan))
        print("Harga : {}".format(self.harga))

memory = RandomAccessMemory('V-Gen', 'DDR4', 328000)
harddisk = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000)
prosesor = Processor('Intel', 'Core i7', 12000000)

parts = [prosesor, memory, harddisk]
for i in parts :
    print("")
    i.set()