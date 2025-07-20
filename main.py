"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Aneta Michulková
email: michulkova.aneta@gmail.com
"""
#-------------------------------------

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
prihlasovaci_jmeno = input("Zadej své přihlašovací jméno: ")
heslo = input("Zadej heslo: ")
uzivatele = {
    "bob" : 123,
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}
if prihlasovaci_jmeno in uzivatele:
    print(uzivatel, heslo)


# statistiky:
pocet_slov = len()
počet_slov začínajících velkým písmenem,
počet slov psaných velkými písmeny,
počet slov psaných malými písmeny,
počet čísel (ne cifer),
sumu všech čísel (ne cifer) v textu.