# ZAD 1
print("Zadanie 1")
lista_1=[1,2,3,4,5,6,7,8,9,10]
dlugosc = len(lista_1)
srodek = dlugosc // 2
pierwsza_polowa = lista_1[:srodek]
druga_polowa = lista_1[srodek:]
print(pierwsza_polowa)
print(druga_polowa)
print('\n')

# ZAD 2
print("Zadanie 2")
lista_2 = [*pierwsza_polowa, *druga_polowa]
print(lista_2)
lista_2.insert(0,0)
print(lista_2)
kopia_lista2=lista_2.copy()
kopia_lista2.sort(reverse=True)
print(kopia_lista2)
print('\n')

# ZAD 3
print('Zadanie 3')
tekst = input("Podaj przykładowy tekst:\n").lower()
unikalne_znaki=set(tekst)
unikalne_znaki1=list(unikalne_znaki)
unikalne_znaki1.sort()
print(unikalne_znaki1)
print('\n')

# ZAD 4
print('Zadanie 4')
slownik = dict([(1, 'Styczen'), (2, 'Luty'),(3, 'Marzec'),(4,'Kwiecien'),(5,'Maj'),(6,'Czerwiec'),(7,'Lipiec'),(8,'Sierpien'),(9,'Wrzesien'),(10,'Pazdziernik'),(11,'Listopad'),(12,'Grudzień')])
print(slownik.keys())
print(slownik.values())
print('\n')

# ZAD 5
print('Zadanie 5')

print('\n')



