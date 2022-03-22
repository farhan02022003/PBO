print(len('plymorphism'))
print(len([0,1,2,3]))

# using class
class jerman:
    def ibukota(self):
        print('berlin adalah ibu kota jerman')

class jepang:
    def ibukota(self):
        print('tokyo adalah ibu kota jepang')

negara1 = jerman()
negara2 = jepang()

for country in (negara1,negara2):
    country.ibukota()