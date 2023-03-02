# ZAD 1

zdanie = input('Podaj zdanie z jednolitym separatorem np spacja, średnik itd. : \n')
sep_zr =input('Podaj seprarator którego użyłeś w zdaniu wyżej: \n')
sep_doc =input('Podaj separator docelowy: \n')

zdanie_split = zdanie.split(sep_zr)
zdanie = sep_doc.join(zdanie_split)
print(zdanie)
print(zdanie.replace(sep_zr,sep_doc))
# ZAD 2

lorem = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

# ZAD 3

pierwsza_litera = 'Mateusz'[0]
druga_litera = 'Kuczmarski'[3] 
