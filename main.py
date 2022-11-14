# str()
# int()
#
# type(1)
#
# isinstance(1, int) # vraci true nebo false, tady se pta, jestli je 1 int
#
# float(2.1) # int() 2
# float(2.5) # int() 2
#
# round(2.5, 0) # cislo ktere se yaokrouhluje a pocet desetinnych mist
#
# bool() # True nebo False, bacha na velka a mala pismena, idiote
#


# promenna = input("yadej neco")
# cisloa = input("yadej cislo")
# print(promenna * int(cisloa))


# #vyceradkovy textovy reteyec
# print("sgjksnfsdjnkf" +
#       "jknsdhfucioakh")
#
# print("""ajbaduvba
#     aofubiuabbuoa""")

# IN cele cislo vetsi nez 0
# OUT obsah a obvod ctverce

#
# cislo = input("Zadej cislo")
# obsah = int(cislo) * int(cislo)
# obvod = int(cislo) * 4
#
# print("obsah je", obsah)
# print("obvod je", obvod)
# print("obvod je {}".format(obvod)) # poyicove formatovani, funguje stejne i s vice promenyma s rozdelenim carkami
# print(f"obvod je {obvod} a obsah je {obsah}") # tohle se uciteli libi nejvic, tohle pouyivej
#
#
# vstup = input("A nebo B")
# if vstup == "A":
#     pass
# elif vstup == "B":
#     print("je to B")
# else
#     print("neco jinzho")
#
# for i in range(10)
#     print(i)
#
# # while se provadi dokud se plni podminka
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1
#     #i +=1
#
# slovo = "python"
#
# for p in slovo:
#     print(p)
#
# for o in range(len(slovo)):
#     print(slovo[o])
#



slovodva = input("zadej slovo")
samohlasky = 0
souhlasky = 0
cisla = 0
ostatni = 0


for znak in slovodva:
    if znak in "aeiouy":
        samohlasky =samohlasky + 1
    elif znak in "qwrtpsdfghjklzxcvbnm":
        souhlasky = souhlasky + 1
    elif znak in "0123456789":
        cisla= cisla + 1
    else:
        ostatni = ostatni + 1

print(f"slovo {slovodva} ma {samohlasky} samohlasek")
print(f"slovo {slovodva} ma {souhlasky} souhlasek")
print(f"slovo {slovodva} ma {cisla} cisel")
print(f"slovo {slovodva} ma {ostatni} ostatni")
