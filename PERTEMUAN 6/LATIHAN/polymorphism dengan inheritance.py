# using class
class burung:
    def intro(self):
        print('di dunia ini ada beberapa type berbeda dari spesies burung')

    def terbang(self):
        print('hamppir semua burung dapat terbang , namun ada beberapa yang tidak dapat terbang')

class elang(burung):
    def terbang(self):
        print('burung elang dapat terbang')

class burungUnta(burung):
    def terbang(self):
        print('burung unta tidak dapat terbang')


obj_burung = burung()
obj_elang = elang()
obj_burung_unta = burungUnta()

obj_burung.intro()
obj_burung.terbang()

obj_elang.intro()
obj_elang.terbang()

obj_elang.intro()
obj_elang.terbang()

obj_burung_unta.intro()
obj_burung_unta.terbang()