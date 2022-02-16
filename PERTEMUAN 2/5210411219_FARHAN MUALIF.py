str1 = "aku cinta indonesia"
print(str1)

str2 = str1[:10]+'tanah airku'+str1[9:]
print(str2)

str3 = 'aku cinta tanah air ku indonesia'
str4 = str3[:9]+''+str3[22:]
print(str4)

kelas = 'Praktikum Pemrograman Berorientasi Objek'
up = kelas.upper()
lo = kelas.lower()
print(kelas)
print(up)
print(lo)

s = '     python     '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(len(kelas))

jumlah = len(kelas)
print('panjang string adalah :',jumlah)

s1 = 'python '
s2 = 'programing'
print(s1+s2)

print(kelas.index('a'))
print(kelas)

kelas2 = kelas.replace('Praktikum','praktik')
print(kelas2)

a = 'satu'
b = 'dua'
c = 'tiga'
print('saya mempunyai %s mangga'%(b))

print(kelas.split())

input1 = input('hari ini adalah : ')
print(input1)

data1 = input('angka 1 : ')
data2 = input('angka 2 : ')
data3 = int(data1)+int(data2)
print(data1,' * ',data2,' = ',data3)

list1 = [1,2,3,4,5,6,7,8,9]
print(list1)
print(list1[5])
print(list1[:3])
print(len(list1))
print(list1[10-3:])
print(list1[2:9])
print(list1[-10])
print(list1[0])
list1.append(10)
print(list1)
list1.insert(1,11)
print(list1)

list2 = ['hello']
list1.extend(list2)
print(list1)

list1.extend('hai')
print(list1)

del list1[1]
print(list1)

list1.remove(5)
print(list1)

list1.pop()
print(list1)

a = [50,20,30,40]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(min(a))
print(max(a))
d = {1:100,2:200,3:300,4:400,5:500}
print(d)
print(d[2])
print(d.get(4))
print(d.keys())
print(d.values())
del d[3]
print(d)
d.clear()
len(d)

t=(100,200,300,400)
print(t)
print(t[0])
print(t[3])
print(t.index(200))
t2=(10,20,10,30,10,40,20)
print(t2.count(20))
print(t2.count(10))
print(t2.count(30))

# TUGAS SET (HIMPUNAN)

a = set("hallo")
print(a)
a.add('world')
print(a)
a.update('dunia')
print(a)
a.discard('a')
print(a)
a.clear()
print(a)

no = {1, 2, 3, 4}
no_baru = no.copy()
no_baru.add(5)
print('numbers: ', no)
print('new_numbers: ', no_baru)

x = {"apel", "pisang", "semangka"}
y = {"jambu", "jeruk", "apel"}
z = x.intersection(y)
print(z)

o = {"motor", "mobil", "becak"}
p = {"sepatu", "sendal", "boot"}
q = o.difference(p)
print(q)

k = {"pesawat", "jet", "nuklir"}
l = {"php", "html", "javascript"}
m = k.union(l)
print(m)

g = (5,3,23,6,8,6,3)
num = frozenset(g)
print(num)