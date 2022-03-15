# Multiple Intheritance

# Parent 1
class perhitunan1:
    def  penjumlahan(self,a,b):
        return a+b

# Patrent 2
class perhitungan2:
    def perkalian(self,a,b):
        return a*b

# Child
class hitung(perhitunan1,perhitungan2):
    def pembagian(self,a,b):
        return a/b

h = hitung()
print(h.penjumlahan(20,30))
print(h.perkalian(5,4))
print(h.pembagian(6,12))