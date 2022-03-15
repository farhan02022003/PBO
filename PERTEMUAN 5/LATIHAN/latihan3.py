# Hierarrchical inheritence

# class parent
class induk():
    def fungsiinduk(self):
        print('fungsi pada parent class')

# class turunan 1
class anak1(induk):
    def fungsianak1(self):
        print('fungsi pada anak1')

# class turunan 2
class anak2(induk):
    def fungsianak2(self):
        print('fungsi pada anak 2')

a1 = anak1()
a2 = anak2()

a1.fungsiinduk()
a1.fungsianak1()

a2.fungsiinduk()
a2.fungsianak2()