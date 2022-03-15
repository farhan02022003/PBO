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

    def det(self) :
        print("{} produk dari {}".format(self.nama,self.pabrikan))
        print("Harga : {}".format(self.harga))

class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas

    def det(self) :
        print("{} produk dari {}".format(self.nama,self.pabrikan))
        print("Kapasitas : {}".format(self.kapasitas))
        print("Harga : {}".format(self.harga))

class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas
        self.rpm = rpm

    def det(self) :
        print("{} produk dari {}".format(self.nama,self.pabrikan))
        print("Kapasitas : {}".format(self.kapasitas))
        print("RPM : {}".format(self.rpm))
        print("Harga : {}".format(self.harga))

kom1 = Processor('Intel', 'Core i7 ', 4350000)
kom2 = RandomAccessMemory('V-Gen', 'DDR4 ', 328000, "4GB")
kom3 = HardDiskSATA('Seagate', 'HDD ', 295000, '500GB', 7200)

komputer = [kom1, kom2, kom3]
for i in komputer :
    i.det()
    print("")
print("--------------------------------------------------------------------------------\n")