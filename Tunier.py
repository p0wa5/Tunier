#Tunier - KO - System
import random
import math

playerName = []
playerCount = int(input("How many player are there "))
rounds = int(math.log(playerCount,2))
FinalWinner = playerName

def getPlayer():
    count = 0 #Counter für getPlayer while loop
    while count < playerCount:
        playerName.append(input("Spieler: "))
        count += 1
    print("Welcome", playerName)
    print("Das Tunier wird aus ", rounds, "runden Bestehen")

def getWin():
    y = 0
    print("Bitte geben sie Die Gewinner von runde 1 und 2 ein")
    while y != 2:
        playerName.append(input(":"))
        print("Gewinner der ",y ,"Runde: ")
        y += 1
    print(playerName)


def randomize():
    x = 0
    while x < rounds:
        keyPlayer = random.choice(playerName)
        playerName.remove(keyPlayer)

        keyPlayer2 = random.choice(playerName)
        playerName.remove(keyPlayer2)
        x += 1

        print("Runde", x, keyPlayer, "vs", keyPlayer2)
    getWin()



getPlayer()
randomize()





