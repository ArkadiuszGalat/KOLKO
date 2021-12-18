#%%
# ctr-A i ctr-/  komentuje wszystko zaznacze
# class MojaKlasa:
#     def wyswietl(y):
#         return ('Witaj')

# x = MojaKlasa()
# print(x.wyswietl())

class prostopadloscian:
    def __init__(self): #konstruktor 
        self.bok_a=0
        self.bok_b=0
        self.bok_c=0
    def objetosc(self):
        return self.bok_a*self.bok_b*self.bok_c

wtc=prostopadloscian
wtc.bok_a=2
wtc.bok_b=2
wtc.bok_c=100
print(wtc.objetosc())
