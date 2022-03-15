class ComputerPart():
    def __init__(self, pabrikan, nama) :
        self.pabrikan = pabrikan
        self.nama = nama

class ComputerPart2():
    def __init__(self, harga) :
        self.harga = harga

class Processor(ComputerPart,ComputerPart2) :
    def __init__(self, pabrikan, nama, harga) :
        ComputerPart.__init__(self,pabrikan,nama)
        ComputerPart2.__init__(self,harga)

    def set(self) :
        print("{} produk dari {}".format(self.nama,self.pabrikan))
        print("Harga : {}".format(self.harga))

class RandomAccessMemory(ComputerPart,ComputerPart2) :
    def __init__(self, pabrikan, nama, harga) :
        ComputerPart.__init__(self,pabrikan,nama)
        ComputerPart2.__init__(self,harga)

    def set(self) :
        print("{} produk dari {}".format(self.nama,self.pabrikan))
        print("Harga : {}".format(self.harga))

class HardDiskSATA(ComputerPart,ComputerPart2) :
    def __init__(self, pabrikan, nama, harga) :
        ComputerPart.__init__(self,pabrikan,nama)
        ComputerPart2.__init__(self,harga)

    def set(self) :
        print("{} produk dari {}".format(self.nama,self.pabrikan))
        print("Harga : {}".format(self.harga))
prosesor = Processor('Intel', 'Core i7', 12000000)
memory = RandomAccessMemory('V-Gen', 'DDR4', 328000)
harddisk = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000)

parts = [prosesor, memory, harddisk]
for i in parts :
    print("")
    i.set()