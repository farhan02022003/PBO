class Operator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Penambahan(Operator):
    def _init_(self,x,y):
        self.x = x
        self.y = y

    def tambah(self):
        print("Hasil Penjumlahan: ",self.x + self.y)

class Pengurangan(Operator):
    def _init_(self,x,y):
        self.x = x
        self.y = y

    def kurang(self):
        print("Hasil Pengurangan: ",self.x - self.y)

class Perkalian(Operator):
    def _init_(self,x,y):
        self.x = x
        self.y = y

    def kali(self):
        print("Hasil Perkalian: ",self.x * self.y)

class Pembagian(Operator):
    def _init_(self,x,y):
        self.x = x
        self.y = y

    def bagi(self):
        print("Hasil Pembagian: ",self.x / self.y)


metode = int(input("1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\nMasukkan metode : "))
if metode == 1:
    x = int(input("Masukan angka x : "))
    y = int(input("Masukan angka y : "))
    kal = Penambahan(x,y)
    kal.tambah()
    wait = input("\nPress enter to continue...")
elif metode == 2:
    x = int(input("Masukan angka x : "))
    y = int(input("Masukan angka y : "))
    kal = Pengurangan(x,y)
    kal.kurang()
    wait = input("\nPress enter to continue...")
elif metode == 3:
    x = int(input("Masukan angka x : "))
    y = int(input("Masukan angka y : "))
    kal = Perkalian(x,y)
    kal.kali()
    wait = input("\nPress enter to continue...")
elif metode == 4:
    x = int(input("Masukan angka x : "))
    y = int(input("Masukan angka y : "))
    kal = Pembagian(x,y)
    kal.bagi()
    wait = input("\nPress enter to continue...")
else:
    print("Salah input kalii")