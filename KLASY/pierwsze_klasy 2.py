#%%
#https://github.com/angelm1974/kolko/tree/main/klasy
#tabnine - automatyzuje pisanie, ale chyba pod c-sharpa
# ctr-A i ctr-/  komentuje wszystko zaznacze
# class MojaKlasa:
#     def wyswietl(y):
#         return ('Witaj')

# x = MojaKlasa()
# print(x.wyswietl())

class sciany:
    def __init__(self,a,b,h): #konstruktor 
        self.bok_a=a
        self.bok_b=b
        self.bok_c=h
    def Pomaluj(self):
        return 2*(self.bok_a+self.bok_b)*self.bok_c


farby1= sciany(2,3,5)
farby2= sciany(5,1,2)
print(farby1.Pomaluj())
print(farby2.Pomaluj())
#%% wersja 2
class sciany:
    pomalowaneBudynki=0
    def __init__(self,a,b,h): #konstruktor 
        self.bok_a=a
        self.bok_b=b
        self.bok_c=h
    sciany.pomalowaneBudynki+=1
    def Pomaluj(self):
        return 2*(self.bok_a+self.bok_b)*self.bok_c


farby1= sciany(2,3,5)
farby2= sciany(5,1,2)
print(farby1.Pomaluj())
print(farby2.Pomaluj())
print(farby2.pomalowaneBudynki)

