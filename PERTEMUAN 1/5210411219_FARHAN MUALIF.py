# diketahui sebuah panjang balok 8 cm, lebar 6 cm, tinggi  4 cm
# hitung luas permukaan balok

# p = 8
# l = 6
# t = 4
# L = 2 * (p*l + p*t + l*t)
# print('diketahui sebuah balok memiliki panjang 8 cm, lebar 6 cm, tinggi  4 cm')
# print('hitung luas permukaan balok')
# print('panjang sebuah balok =',p)
# print('lebar sebuah balok   =',l)
# print('tinggi sebuah balok  =',t)
# print("Luas permukaan balok adalah",L)

def rumus(p,l,t):
  hasil = 2*(p*l+p*t+l*t)
  return print('luas permukaan balok : ',hasil)

def hasil():
    p = int(input('panjang : '))
    l = int(input('lebar : '))
    t = int(input('tinggi : '))
    rumus(p,l,t)

hasil()