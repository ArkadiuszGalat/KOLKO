#%%
# gra w kółko i krzyżek na 3 
#poszukać biblioteki pretty console
plansza_do_gry = {'7':' ', '8':' ', '9':' ', '4':' ', '5':' ', '6':' ', '1':' ', '2':' ', '3':' ', }
print(plansza_do_gry)
print(f'')
klawisze = []
for key in plansza_do_gry:
    klawisze.append(key)
print(klawisze)
def drukuj_plansze(pole):
    print(f" {pole['7']} | {pole['8']} | {pole['9']}")
    print('---+---+---')
    print(f" {pole['4']} | {pole['5']} | {pole['6']}")
    print('---+---+---')
    print(f" {pole['1']} | {pole['2']} | {pole['3']}")
    
drukuj_plansze(plansza_do_gry)