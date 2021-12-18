#%%
# gra w kółko i krzyżek na 3 
#poszukać biblioteki pretty console
#https://github.com/angelm1974/kolko
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
#komentarz
#drukuj_plansze(plansza_do_gry)
def gra():
    gracz='X'
    ruch_licznik=0
    for i in range(10):
        drukuj_plansze(plansza_do_gry)
        print(f'To jest ruch, gracza {gracz}. Wybierz z klawiatury num gdzie chcesz postawić znak!')
        
        ruch=input()

        if plansza_do_gry[ruch]==' ':
            plansza_do_gry[ruch]=gracz
            ruch_licznik+=1
        else:
            print('To pole jest zajęte!\n')
            continue
        if ruch_licznik>=5:
            if plansza_do_gry['7']==plansza_do_gry['8']==plansza_do_gry['9']!=' ':
                drukuj_plansze(plansza_do_gry)
                print('KONIEC!')
                print(f'Wygrał gracz: {gracz}')
                break
            elif plansza_do_gry['4']==plansza_do_gry['5']==plansza_do_gry['6']!=' ':
                drukuj_plansze(plansza_do_gry)
                print('KONIEC!')
                print(f'Wygrał gracz: {gracz}')
                break
            elif plansza_do_gry['1']==plansza_do_gry['2']==plansza_do_gry['3']!=' ':
                drukuj_plansze(plansza_do_gry)
                print('KONIEC!')
                print(f'Wygrał gracz: {gracz}')
                break
            elif plansza_do_gry['1']==plansza_do_gry['5']==plansza_do_gry['9']!=' ':
                drukuj_plansze(plansza_do_gry)
                print('KONIEC!')
                print(f'Wygrał gracz: {gracz}')
                break
            elif plansza_do_gry['3']==plansza_do_gry['5']==plansza_do_gry['7']!=' ':
                drukuj_plansze(plansza_do_gry)
                print('KONIEC!')
                print(f'Wygrał gracz: {gracz}')
                break
            elif plansza_do_gry['1']==plansza_do_gry['4']==plansza_do_gry['7']!=' ':
                drukuj_plansze(plansza_do_gry)
                print('KONIEC!')
                print(f'Wygrał gracz: {gracz}')
                break
            elif plansza_do_gry['2']==plansza_do_gry['5']==plansza_do_gry['8']!=' ':
                drukuj_plansze(plansza_do_gry)
                print('KONIEC!')
                print(f'Wygrał gracz: {gracz}')
                break
            elif plansza_do_gry['3']==plansza_do_gry['6']==plansza_do_gry['9']!=' ':
                drukuj_plansze(plansza_do_gry)
                print('KONIEC!')
                print(f'Wygrał gracz: {gracz}')
                break
            if licznik==9:
                print('KONIEC!')
                print(f'REMIS')
        if gracz=='X':
            gracz='O'
        else:
            gracz='X'
    restart=input('Czy chcesz dalej grać?/(t/n)')
    if restart=='t':
        for key in klawisze:
            plansza_do_gry[key]=' '
        gra()
if __name__=='__main__':
    gra()

#gra()