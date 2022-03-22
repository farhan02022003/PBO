class kucing:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def suara(self):
       print('meow')

class dog:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def suara(self):
       print('guk..gukk')

kucing1 = kucing('tom',3)
anjing1 = dog('spike',4)

for country in (kucing1,anjing1):
    country.suara()