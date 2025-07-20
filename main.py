"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Aneta Michulková
email: michulkova.aneta@gmail.com
"""
#-------------------------------------
from sys import exit

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

jmeno = input("Zadej své přihlašovací jméno: ")

if jmeno in uzivatele:
    heslo = input("Zadej heslo: ")

    if uzivatele[jmeno] == heslo:
        print(
        f"Ahoj, {jmeno}. Můžeš analyzovat jeden z následujících textů:\n\n"
        f"Text č.1: {TEXTS[0]}\n\n"
        f"Text č.2: {TEXTS[1]}\n\n"
        f"Text č.3: {TEXTS[2]}\n"
        )

        vybrany_text = input("Zadej číslo textu od 1 do 3: ")

        if not vybrany_text.isdigit():
            exit("Neplatný vstup - očekávám číslo.")
        elif int(vybrany_text) not in (1, 2, 3):
            exit("Zadané číslo neodpovídá rozsahu 1 až 3.")

        vybrany_text = int(vybrany_text) - 1  # sníží hodnotu o 1 kvůli indexování

        # Analýza textu:
        slova = TEXTS[vybrany_text].split()
        pocet_slov = len(slova)

        first_upper = 0
        all_upper = 0
        all_lower = 0
        cislice = 0
        suma_cisel = 0

        for slovo in slova:
            if slovo and slovo.istitle():
                first_upper += 1
            if slovo and slovo.isupper():
                all_upper += 1
            if slovo and slovo.islower():
                all_lower += 1
            if slovo and slovo.isdigit():
                cislice += 1
                suma_cisel += int(slovo)

        print(
            f"Počet slov: {pocet_slov}\n"
            f"Počet slov s prvním velkým písmenem: {first_upper}\n"
            f"Počet slov psaných velkými písmeny: {all_upper}\n"
            f"Počet slov psaných malými písmeny: {all_lower}\n"
            f"Počet čísel v textu: {cislice}\n"
            f"Součet všech číslic v textu: {suma_cisel}\n\n"
        )
        #slovník pro četnost délek slov:
        delka_slov = {}
        for slovo in slova:
            delka = len(slovo.strip(".,!?\"'"))  # očistí slovo od interpunkce
            if delka > 0:
                delka_slov[delka] = delka_slov.get(delka,0)+1

        #graf podle delky a četnosti slov:
        print("LEN|    OCCURRENCES   |NR.")
        print("-" * 30)
        for delka in sorted(delka_slov): #seřadí klíče od nejmenšího po nejvyšší a postupně je prochází
            pocet = delka_slov[delka] #vrací hodnotu dane delky ze slovniku
            hvezdicky = '*' * pocet
            print(f"{delka:>3}| {hvezdicky:<17}|{pocet:>3}")
            #{delka:>2}: délka slova zarovnaná vpravo na 2 znaky
            #{hvezdicky}: řetězec hvězdiček (vizuální sloupec)
            #{pocet}: číselná hodnota četnosti

    else:
        print("Nesprávné heslo!")

else:
    exit("Nejsi registrovaný!")

