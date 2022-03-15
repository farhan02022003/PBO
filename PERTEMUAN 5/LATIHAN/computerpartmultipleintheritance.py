class komputer2():
    def __init__(self,pabrikan,harga):
        self.pabrikan = pabrikan
        self.harga = harga


class komputer1():
    def __init__(self,nama,jenis):
        self.nama = nama
        self.jenis = jenis

class ComputerPart(komputer1,komputer2):
    def __init__(self, nama, jenis, pabrikan, harga):
        komputer1.__init__(self,nama,jenis)
        komputer2.__init__(self,pabrikan,harga)

k = ComputerPart('')