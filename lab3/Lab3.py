# Lab 3 uppgift Ordlista
# Strängyttryck[Heltalsuttryck] kallas indexering,
# där heltalsuttrycket är ett index
# Inbygga funktion len(length) ger längd av en sträng dvs antal bokstäver ,
# 0 -> inf, -1 -> -inf
# kolon före syftar på bokstäverna framför ex :2 [Or]ange
# kolon efter syftar på bokstäverna bakom ex 2: Or[ange]
# Kolon för sig själv syftar på hela ordet ex : [Orange]
# ASCII=American standard code for information interchange
# Strängar=sekvenser av tecken
# Listor=sekvenser av vad som helst

from Lab2uppgift import *


def func(x):
    return x**2 - 1


def menu():
    ans = True
    while ans:

        print(
            "\nVad vill du göra? \n 1. Köra bounce \n 2. Köra tvarsumman \n 3. Kör newton-raphson \n 4. avsluta programmet"
        )
        choice = input()

        if choice == "1":
            print("Ange en parameter till bounce:")
            parameter = input()  # sträng
            bounce(int(parameter))

        elif choice == "2":
            print("Ange en parameter till tvarsumman:")
            parameter = input()
            print(tvarsumman(int(parameter)))

        elif choice == "3":
            print("Ange ett startvärde till newton-raphson:")
            startvarde = input()
            print(solve(func, int(startvarde), 0.00001))

        elif choice == "4":
            print("Programmet avslutas")
            ans = False


# menu()
"""
def main_dic_list():
    ord=list()
    forklaring=list()
    ans=True
    while ans:
            
        print ('\n Menu for dictionary \n 1: Insert \n 2: Lookup \n 3: Exit program')
        val=input()

        if val=='1':
            print('Choose alternative: 1')
            print('Vilket ord ska läggas till')
            nyttord=input()
            if nyttord in ord:
                print('Ordet finns redan i listan')
            else:
                ord.append(nyttord)
                print('Vilken förklaring har den')
                nyfork=input()
                forklaring.append(nyfork)
        
        elif val=='2':
            print('Choose alternative: 2')
            print('Vilket ord vill du kolla på')
            kolla=input()
            if kolla in ord:
                for idx in range(len(ord)):
                    if kolla==ord[idx]:
                        print('Förklaring:')
                        print(forklaring[idx])
            else:
                print('Order finns inte i listan')



        elif val=='3':
            print('Choose alternative: 3')
            ans=False
"""


# LIST
def main_dic_list_ny():
    ord = list()  # skapar en ord-lista
    forklaring = list()  # skapar en förklarings-lista
    ans = True
    while ans:

        print("\n Menu for dictionary \n 1: Insert \n 2: Lookup \n 3: Exit program")
        val = input()  # frågar efter en input

        if val == "1":
            print("Chose alternative: 1")
            print("Vilket ord ska läggas till")
            nyttord = input()  # frågar efter en input
            insertWord(nyttord, ord, forklaring)  # anropar funktionen med tre argument

        elif val == "2":
            print("Chose alternative: 2")
            print("Vilket ord vill du kolla på?")
            kolla = input()  # frågar efter en input
            findDef(kolla, ord, forklaring)  # anropar funktionen med tre argument

        elif val == "3":
            print("Chose alternative: 3")
            ans = False  # avsluta programmet


def insertWord(word, ord, forklaring):
    if word in ord:  # kolla om word finns i ordlistan
        print("Ordet finns redan i listan")

    else:
        ord.append(word)  # Lägger till word i ord <- listan
        nyfork = input("Vilken förklaring har den? ")
        forklaring.append(nyfork)  # lägger till ny förklaring till förklaring listan


def findDef(word, ord, forklaring):
    if word in ord:  # kollar om word finns i ord -listan
        for idx in range(
            len(ord)
        ):  # idx går igenom alla index i listan. ex om len(ord)==5 -> idx går från 0-4
            if (
                word == ord[idx]
            ):  # kollar om ordet finns på index idx i ordlistan. Kolla vilken index den har
                print("Förklaring:")  # skriv ut 'förklaring'
                print(
                    forklaring[idx]
                )  # skriv ut texten i förklaringslistan på index idx
    else:
        print("Ordet finns inte i listan")


# main_dic_list_ny()


# TUPLE
def main_dic_tuple():
    ordlista = list()  # skapar en tuple
    ans = True
    while ans:

        print("\n Menu for dictionary \n 1: Insert \n 2: Lookup \n 3: Exit program")
        val = input()  # frågar efter en input

        if val == "1":
            print("Chose alternative: 1")
            print("Vilket ord ska läggas till")
            nyttord = input()  # frågar efter en input
            insertWord2(nyttord, ordlista)  # anropar funktionen med två argument

        elif val == "2":
            print("Chose alternative: 2")
            print("Vilket ord vill du kolla på")
            kolla = input()  # frågar efter en input
            findDef2(kolla, ordlista)  # anropar funktionen med två argument

        elif val == "3":
            print("Chose alternative: 3")
            ans = False  # avsluta programmet


def insertWord2(word, ordlista):
    finns = 0  # nolltsäller finns
    for idx in range(
        len(ordlista)
    ):  # idx går igenom alla index i listan. ex om len(ord)==5 -> idx går från 0-4
        currenttuple = ordlista[
            idx
        ]  # sätter currenttuple till tuplen på plats idx i ordlistan. Den kopierar från ordlistan som finns på den index
        if (
            word == currenttuple[0]
        ):  # Kollar om ordet är lika med ordet som finns tuplen.
            finns = 1  # ordet finns i ordlistan -> finns!
            print("Ordet finns redan i listan")
    if finns == 0:
        print("Vilken förklaring har den")
        nyfork = input()  # frågar efter förklaring
        ordlista.append((word, nyfork))  # lägger till ny tuple


def findDef2(word, ordlista):
    finns = 0  # nollställer finns
    for idx in range(
        len(ordlista)
    ):  # idx går igenom alla index i listan. ex om len(ord)==5 -> idx går från 0-4
        currenttuple = ordlista[
            idx
        ]  # sätter currenttuple till tuplen på plats idx i ordlistan. Den kopierar från ordlistan som finns på den index
        if (
            word == currenttuple[0]
        ):  # Kollar om ordet är lika med ordet som finns tuplen.
            print("Förklaring:")
            print(currenttuple[1])
            finns = 1
    if finns == 0:
        print("Ordet finns inte i listan")


# main_dic_tuple()


# DICT
def main_dic_dict():
    """
    dictionary = {
        "himmel": "blå",
        "sol": "gul",
        "apelsin": "orange"
    }
    """
    ordlista = {}  # skapa en tom ordlista
    ans = True
    while ans:

        print("\n Menu for dictionary \n 1: Insert \n 2: Lookup \n 3: Exit program")
        val = input()

        if val == "1":
            print("Chose alternative: 1")
            print("Vilket ord ska läggas till")
            nyttord = input()  # frågar efter en input
            insertWord3(nyttord, ordlista)  # anropar funktionen med två argument

        elif val == "2":
            print("Chose alternative: 2")
            print("Vilket ord vill du kolla på")
            kolla = input()  # frågar efter en input
            findDef3(kolla, ordlista)  # anropar funktionen med två argument

        elif val == "3":
            print("Chose alternative: 3")
            ans = False  # avsluta programmet


def insertWord3(word, dict):
    if word in dict:
        print("Ordet finns redan i listan")
    else:
        print("Vilken förklaring har ordet?")
        nyfork = input()  # frågar efter en input
        dict[word] = nyfork  # Lägg till word med förklaring


def findDef3(word, dict):
    if word in dict:
        print("Förklaring:")
        print(dict.get(word))  # skriver ut förklaringen till ordet word
    else:
        print("Ordet finns inte listan")


# main_dic_dict()
