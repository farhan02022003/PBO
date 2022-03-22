class pegawai:
    jumlah = 0
    def __init__(self,nama,gaji):
        self.nama = nama
        self.gaji = gaji
        self.jumlah += 1

    def tampiljumlah(self):
       print('total pegawai = ',self.jumlah)

    def tampilpegawai(self):
       print('nama pegawai = ',self.nama,'gaji = ',self.gaji)
    # method overloading
    def tunjangan(self, istri = None, anak = None):
        if anak != None and istri != None:
            total = anak+istri
            print('tunjangan anak + istri ',total)
        else:
            total = istri
            print('tunjangan istri = ', total)

peg1 = pegawai('eren',2000)
peg2 = pegawai('luffy',6000)
peg1.tampilpegawai()
peg2.tampilpegawai()
peg1.tunjangan(2500,2000)
peg2.tunjangan(2500)
print('total pegawai %d' % pegawai.jumlah)
rataGaji = (peg1.gaji + peg2.gaji)/pegawai.jumlah
print('rata-rata gaji '+str(rataGaji))