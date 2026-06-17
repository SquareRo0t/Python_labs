"""
import copy
#definerar en klass som heter Point
class Point:
    x=0.0       #attribut
    y=0.0       #attribut

Att anropa metoder benämns ofta som att skicka
meddelanden i objekt-orienterade språk

#skapar ett objekt eller en instans
p1=Point()
p2=Point()
p2.x=1
p2.y=2
p3=copy.copy(p2)    #kopierar värden
p4=p2   #ger samma adress
p=Point()
pk=Point()
pk.x=1.0    #uppdatera attributen
pk.y=2.0    #uppdatera attributen

#testar att skriva ut attributen x och y
print('x is', p.x, 'and y is', p.y)
print('x is', pk.x, 'and y is', pk.y)

# Exempel Kayan
class human:
    name = "none"
    age = 0
    height = 0

    def growHeight(self):
        self.height = self.height + 2

kayan = human()
print(kayan.name, kayan.age, kayan.height )
jacky = human()
kayan.name = "Kayan"
kayan.age = 18
kayan.height = 180
kayan.färg = "gul"

jacky.name = "bajs"
jacky.age=60
jacky.height = 120

print(kayan.name, kayan.age, kayan.height )
print(jacky.name, jacky.age, jacky.height )


a = 0
b = a
b=1
print (a, b)

x1 = [1,2,3]
x2 = [1,2,3]
x3=x2
"""


class Board:
    def __init__(self, msg):
        self.message = msg

    def board_msg(self):
        return "{}".format(self.message)

    def add_msg(self, new_msg):
        self.message = self.message + " " + new_msg


def main():
    board1 = Board("Board1: Godmorgon")
    board2 = Board("Board2: Hello")

    name1 = "Kim"
    name2 = "Chris"

    kim = board1  # Kim är board 1
    chris = board2  # Chris är board 2

    print("\n=== Bulletin board system ===")
    print(name1 + " reads message: " + kim.board_msg())
    print(name2 + " reads message: " + board2.board_msg())

    while True:

        print("\n1: Direct Kim to other board")
        print("2: Direct Chris to other board")
        print("3: Tell Kim to post a message")
        print("4: Tell Chris to post a message")
        print("0: Exit")
        print("Enter choice:")
        choice = input()

        if choice == "1":
            print("Directs Kim to other board")
            if kim == board1:
                kim = board2
            else:
                kim = board1

        elif choice == "2":
            print("Direct Chris to other board")
            if chris == board2:
                chris = board1
            else:
                chris = board2

        elif choice == "3":
            print("Post your message: ")
            message = input()
            kim.add_msg(message)
            print("The message in the board is: " + kim.board_msg())

        elif choice == "4":
            print("Post your message")
            message = input()
            chris.add_msg(message)
            print("This message:" + chris.board_msg())
        elif choice == "0":
            break

    print("Program has ended!")


# main()
# [a, b, c] = userinput.split()
# krav 1: Kommando en rad lång
# krav 2: ett eller flera whitespace mellan
# krav 3: Unika namn
# krav 4: Unika nummer
# krav 5: 4 kommando: add, lookup, alias, change


class Telefonlista:  # skapar en class Telefonlista
    def __init__(self, name, number):  # initialiseringsmetod
        self.name = name  # attribut
        self.number = number  # attribut


""" 1. skapar objekt av klassen telefonlista
    2. lägger till objektet i dictionary där nyckeln är namnet"""


def add_to_telebook(telefonbok, name, number):
    user_obj = Telefonlista(name, number)  # skapar ett objekt: user_obj
    telefonbok[name] = (
        user_obj  # dictionary - lägger till namn som nyckel och objekt som värde
    )
    # dictionary[nyckel] = värde -> generella förklaringen
    # telefonbok[name].name = user_obj.name
    # print('lägger till i telefonbok')
    # print(telefonbok[name])
    # print(telefonbok[name].name)
    # print(telefonbok[name].number)


def add(telefonbok, user_input_splitted):
    name_or_number_exists = 0  # flagga för om namn eller numret finns. 0: finns ej. 1: namn eller nummer finns
    if (
        len(user_input_splitted) == 3
    ):  # kollar om user_input_splitted/kommando innehåller 3 ord

        if (
            user_input_splitted[1] in telefonbok
        ):  # kollar om user_input_splitted[1] finns i telefonbok
            name_or_number_exists = (
                1  # flagga för om namn eller numret finns = 1: namn finns redan
            )
            print("name already exists")

        for i in telefonbok:  # går igenom hela telefonboken, en efter en
            if (
                user_input_splitted[2] == telefonbok[i].number
            ):  # är numret jag skrev in == nåt nummer i telefonbok?
                name_or_number_exists = (
                    1  ##flagga för om namn eller numret finns = 1: numret finns redan
                )
                print("number already exists")

        if (
            name_or_number_exists == 0
        ):  # om name_or_number_exists=0, betyder att varken namn eller nummer finns
            add_to_telebook(
                telefonbok, user_input_splitted[1], user_input_splitted[2]
            )  # anropar funktionn add_to_telebook med arg
    else:
        print("Please follow this format: add namme number")


def lookup(telefonbok, user_input_splitted):
    if (
        len(user_input_splitted) == 2
    ):  # kollar om user_input_splitted/kommando innehåller 2 ord
        name = user_input_splitted[
            1
        ]  # sätter namn = andra elementet i user_input_splitted
        if name in telefonbok:  # kollar om name finns telefonbook
            print(
                telefonbok[name].number
            )  # om det finns, skriver ut nummret för det namn man söker på
        else:
            print("number not found")
    else:
        print("Please follow this format: lookup name")


def alias(telefonbok, user_input_splitted):
    if (
        len(user_input_splitted) == 3
    ):  # kollar om user_input_splitted/kommando innehåller 3 ord
        name = user_input_splitted[1]  # orginal namn
        newname = user_input_splitted[2]  # nytt namn

        if not newname in telefonbok:  # newname ska inte finnas i telefonboken
            if name in telefonbok:  # kollar sedan om orginal namnet finns i telefonbok
                telefonbok[newname] = telefonbok[
                    name
                ]  # om den finns lägg till 'newname' nyckel i telefonbok så att den har samma objekt som 'name' nyckel
            else:
                print("name does not exist")
        else:
            print("alias already exist")

    else:
        print("Please follow this format: alias name newname")


def change(telefonbok, user_input_splitted):
    # gamla numret - telefonbok[namn].number,
    # nya numret - user_input_splitted[2]
    # gamla numret = nya numret
    number_exists = (
        0  # flagga för om numret finns eller ej. 0: finns ej. 1: finns i telefonboken.
    )
    if (
        len(user_input_splitted) == 3
    ):  # kollar om user_input_splitted/kommando innehåller 3 ord
        name = user_input_splitted[1]  # varibel name = user_input_splitted[1]
        for i in telefonbok:  # går igenom telefonboken
            if (
                user_input_splitted[2] == telefonbok[i].number
            ):  # kollar user_input_splitted[2]/user_input_numret är likamed ett exisiterande nummer
                number_exists = (
                    1  # sätter lika med 1 för att numret finns i telefonboken
                )
                print("number already exist")

        # ändra numret endast om båda vilkoren uppfylls.
        # 1a: namnet måste finnas i telefonboken
        # 2a: numret FÅR EJ vara i telefonboken
        if (name in telefonbok) and (
            number_exists == 0
        ):  # kollar om name finns i telefonbok och att number_exists är lika med 0
            telefonbok[name].number = user_input_splitted[2]  # uppdatera numret
        elif name not in telefonbok:
            print("name does not exist")

    else:
        print("'Please follow this format: change name number")


def save(telefonbok, user_input_splitted):
    if (
        len(user_input_splitted) == 2
    ):  # kollar om user_input_splitted/kommando innehåller 2 ord
        filename = user_input_splitted[1]  # varibel filname = user_input_splitted[1]
        f = open(
            filename + ".txt", "w"
        )  # ex: filename = "fil"+".txt" = "fil.txt" -"concancate"
        for name in telefonbok:  # går igenom hela telefonbok
            f.write(telefonbok[name].number + ";" + telefonbok[name].name + ";\n")
        f.close()  # stänger filen
    else:
        print("Please follow this format: save filename")


def load(telefonbok, user_input_splitted):
    if (
        len(user_input_splitted) == 2
    ):  # kollar om user_input_splitted/kommando innehåller 2 ord
        try:  # testar ett kodblock för fel
            f = open(
                user_input_splitted[1] + ".txt", "r"
            )  # Att öppna filen user_input_splitted[1 för läsning]
            telefonbok.clear()  # rensar dictionary
            for line in f:  # går igenom hela f
                read_split = line.split(";")  # splittar raderna vid en semikolon
                # print(read_split[0], read_split[1])
                add_to_telebook(telefonbok, read_split[1], read_split[0])
            f.close()  # stänger filen
        except IOError:  # blocket låter dig hantera felet
            print("File not accessible")
    else:
        print("Please follow this format: load filename")


def main_telebok():  # skapar funktionen main_telebok

    telefonbok = {}  # skapar en lista

    while True:  # skapar while loop med villkor True

        user_input = input("telebok> ")  # det användaren skriver in
        user_input_splitted = user_input.split()  # splittar user_input
        kommando = user_input_splitted[0]  # sätter första ordet som kommando
        # print(user_input_splitted)
        # print(user_input_splitted[0])

        if kommando == "add":
            add(telefonbok, user_input_splitted)  # Anropar funktionen med 2 argument

        elif kommando == "lookup":
            lookup(telefonbok, user_input_splitted)  # Anropar funktionen med 2 argument

        elif kommando == "alias":
            alias(telefonbok, user_input_splitted)  # Anropar funktionen med 2 argument

        elif kommando == "change":
            change(telefonbok, user_input_splitted)  # Anropar funktionen med 2 argument

        elif kommando == "save":
            save(telefonbok, user_input_splitted)  # Anropar funktionen med 2 argument

        elif kommando == "load":
            load(telefonbok, user_input_splitted)  # Anropar funktionen med 2 argument

        elif kommando == "quit":
            print("Quitting program")
            break

        else:
            print("please try again")


main_telebok()
