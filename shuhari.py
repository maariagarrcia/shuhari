import random

def showMenu():
    print("1. Nivel Shu. \n2. Nivel Ha. \n3. Nivel Ri(inglés)."
    while True:
        level = input("Escoge el nivel que quieres: ")
        try:
            level = int(level)
        except:
            pass
        else:
            if 1 <= level <= 3:
                break
    return level

level = showMenu()

def selectlevel():
    if level == 1:
        shu()
    if level == 2: 
        ha()
    if level == 3:
        ri()

def shu():
    from random import choice, sample

    cartas = {
        chr(0x1f0a1): 11,
        chr(0x1f0a2): 2,
        chr(0x1f0a3): 3,
        chr(0x1f0a4): 4,
        chr(0x1f0a5): 5,
        chr(0x1f0a6): 6,
        chr(0x1f0a7): 7,
        chr(0x1f0a8): 8,
        chr(0x1f0a9): 9,
        chr(0x1f0aa): 10,
        chr(0x1f0ab): 10,
        chr(0x1f0ad): 10,
        chr(0x1f0ae): 10,
    }

    print("Cartas: {}".format(" ".join(cartas.keys())))
    print("Puntos: {}".format(list(cartas.values())))

    print("1\ Iteración estándar sobre un diccionario")
    for carta, valor in cartas.items():
        print("la carta {} vale {}".format(carta, valor))

    print("2\ Iteración ordenada sobre un diccionario")
    for carta in sorted(cartas.keys()):
        print("la carta {} vale {}".format(carta, cartas[carta]))

    print("3\ Black Jack")
    lista_cartas = list(cartas)

    print("Ha seleccionado:", end=" ")
    carta = choice(lista_cartas)
    score = cartas[carta]
    print(carta, end=" ")
    carta = choice(lista_cartas)
    score += cartas[carta]
    print(carta, end=" ")
    print(" >>> su puntuación es de", score)

    main_banca = sample(lista_cartas, 2)
    score_banca = sum(cartas[carta] for carta in main_banca)
    print("La banca tiene: {} {}  >> su score es {}".format(main_banca[0], main_banca[1], score_banca))

def ha():
    print("Cartas: {}".format(" ".join(cartas.keys()))) # .format me da q todo lo q haya dentro del () me lo da entre las {} anterior. .keys para que me de las key de las cartas. join para unir el blanco con el resto
    print("Puntos: {}".format(list(cartas.values()))) #Con esto consigo que el programa me de las diferentes cartas y los puntos posibles que he definido en la lista. list para que me lo de en una lista lo q tenia en un diccionario

    print("1\ Iteración estándar sobre un diccionario")
    for carta, valor in cartas.items():               #Aqui se define carta como el valor de cada item de la lista cartas. Quiero recorrer mi diccionario cartas y que me de un valor(para eso se utiliza item)
        print("la carta {} vale {}".format(carta, valor)) #Con esto consigo darle a cada carta el valor correspondiente
    #Para que nos salga valor por valor, 1 por 1.  .items coge una carta(empieza por 0 a no ser que dentro del parentesis le pongas un numero). El for lo que hace es recorrer todo tu diccionario
    print("2\ Iteración ordenada sobre un diccionario")
    for carta in sorted(cartas.keys()): #para que me salgan los valores segun el orden que yo defina, carta[cartas] es de mi diccionario que se llama cartas, la carta que asocie el valor que le estoy dando, me las ordenara de menor a mayor(por defecto) o de mayor a menor. shorted es para ordenar las cartas
        print("la carta {} vale {}".format(carta, cartas[carta]))

    print("Comienza Black Jack:")

    lista_cartas = list(cartas)


    print("Tus cartas son:", end=" ") 
    carta = choice(lista_cartas) 
    tus_puntos = cartas[carta]
    print(carta, end=" ") 
    carta = choice(lista_cartas)
    tus_puntos += cartas[carta] #sumar al anterior cartas[carta] el siguiente
    print(carta, end=" ")
    print("y tus puntos son:", tus_puntos)

    sus_cartas = sample(lista_cartas, 2)
    sus_puntos = sum(cartas[carta] for carta in sus_cartas)
    print ("Las cartas del crupier son: {} y {} y sus puntos son: {}".format(sus_cartas[0], sus_cartas[1], sus_puntos))

    while True:
        x = tus_puntos
        y = sus_puntos
        if x <= 21 and y <= 21:
            if x < y:
                if x < 21 and y == 21:
                    print ("El crupier tiene BlackJack, has perdido")
                    break
                else:
                    print ("El crupier se ha acercado mas a 21, has perdido")
                break
            elif x > y:
                if x == 21 and y < 21:
                    print ("Tienes BlackJack, Has ganado!!")
                    break
                else:
                    print("Tu puntuacion ha sido mayor, Has ganado!!")
                break
            else:
                print("Ha habido empate, se devuelven las fichas")
                break

def ri():
    import random

    def updateDeck ():
        max_cards = len(deck)
        return max_cards

    def selectCard():
        max_cards = updateDeck()
        while True:
            card = input("Please, choose a card between 1 and " + str(max_cards) + ": ")
            try:
                card = int(card)
            except:
                pass
            else: 
                if 1 <= card <= 52:
                    break
        return card-1

    def yourGame():
        points = 0
        while True:
            card = selectCard()
            card1 = deck[card]
            points = points + card_values[card1]
            deck.remove(card1)
            print ("The card you have chosen is " + card1 + ".")
            print("You have got " + str(points) + " points so far.")
            if points > 21:
                print("You have more than 21 points! You have lost this game.")
                score.append(points)
                break
            end = input("Do you want another card? [Y]/N: ")
            if str.upper(end) == "N":
                break
        score.append(points)

    def dealerGame():
        pointsD = 0
        while True:
            card = random.randint(1,len(deck))
            card1 = deck[card]
            pointsD = pointsD + card_values[card1]
            deck.remove(card1)
            print ("The card the Dealer has chosen is " + card1 + ".")
            print("The Dealer has " + str(pointsD) + " points so far.")
            if pointsD > 21:
                print("The Dealer has over 21 points! You have won this game.")
                score.append(pointsD)
                break
            if pointsD >= 16:
                break
        score.append(pointsD)

    def winner ():
        if score[0] > score[1]:
            print("Congratulations! You have won this game.")
        elif score[0] < score[1]:
            print("You have lost this game!")
        elif score[0] == score[1]:
            print("You have lost this game!")
        print("These are the final results: You " + str(score[0]) + " points, the Dealer " + str(score[1]) + " points.")

    card_values = { 
        chr(0x1f0a1): 11, 
        chr(0x1f0a2): 2, 
        chr(0x1f0a3): 3, 
        chr(0x1f0a4): 4, 
        chr(0x1f0a5): 5, 
        chr(0x1f0a6): 6, 
        chr(0x1f0a7): 7, 
        chr(0x1f0a8): 8, 
        chr(0x1f0a9): 9, 
        chr(0x1f0aa): 10,
        chr(0x1f0ab): 10, 
        chr(0x1f0ad): 10, 
        chr(0x1f0ae): 10, 
    } 

    while True:
        score = []
        deck = [chr(0x1f0a1), chr(0x1f0a2), chr(0x1f0a3), chr(0x1f0a4), chr(0x1f0a5), chr(0x1f0a6), chr(0x1f0a7), chr(0x1f0a8), chr(0x1f0a9), chr(0x1f0aa), chr(0x1f0ab), chr(0x1f0ad), chr(0x1f0ae)]*4
        random.shuffle(deck)
        while True: 
            yourGame()
            if score[0] > 21:
                break
            print("Now it is the Dealers' turn!")
            dealerGame()
            if score[1] > 21:
                break
            winner()
            break
        choice = input("Would you like to play again? [Y]/N: ")
        if str.upper(choice) == "N":
            break

def showMenu()
def selectlevel()
def shu()
def ha()
def ri()