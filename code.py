from enum import Flag
import random

class Carte:
    def __init__(self,name,price,description,degats,hp):
        self.__name = name
        self.__price = price
        self.__description = description
        self.__degats = degats
        self.__hp = hp
    
    def getName (self):
        return self.__name
    
    def getPrice (self):
        return self.__price

    def getDescription (self):
        return self.__description

    def getDegats (self):
        return self.__degats

    def getHP (self):
        return self.__hp

class Cristal(Carte):
    def __init__(self):
        Carte.__init__(self,"cristal",5,"Vous avez augmentez votre mana max de 25",0,0)
    
    def getNouveauManaMax (self):
        manaAugm = 25
        return manaAugm

class Creature(Carte):
    def __init__(self,name,price,description,degats,hp):
        Carte.__init__(self,name,price,description,degats,hp)

    def setHp(self,degats):
        self.__hp -= degats
        if self.__hp <= 0:
            print("Votre créature est morte")

class Blast(Carte):
    def __init__(self):
        Carte.__init__(self,"blast 1",40,"Vous jouez un blast, vous infligez 40 degats",40,0)

class Mage:
    def __init__(self,name,hp,mana):
        self.__name = name
        self.__hp = hp
        self.__mana = mana
        self.__manaMax = 100
        self.__carteCreature1 = 3
        self.__carteCreature2 = 3
        self.__carteCristal = 3
        self.__carteBlast = True
    
    def getName (self):
        return self.__name

    def getTest (self):
        return self.__manaMax
    
    def getHP (self):
        return self.__hp

    def setHP (self,degats):
        self.__hp -= degats

    def getMana (self):
        return self.__mana

    def getValeurActuelle(self,valAct):
        return valAct

    def recupMana(self):
        self.__mana += 20
        print("Vous récupérez 20 de mana")

    def setMana (self,price):
        self.__mana += price

        if self.__mana > self.__manaMax:
            self.__mana = self.__manaMax

    def upManaMax(self,up):
        self.__manaMax += up


    def jouer(self,price):
        self.__mana -= price

    def getDefausse(self,carteCreature1,carteCreature2,carteCristal,carteBlast):
        if carteCreature1 == False:
            print("Vous ne possédez plus de carte Créature")

        if carteCreature2 == False:
            print("Vous ne possédez plus de carte Créature surpuissante")

        if carteCristal == True:
            print("Vous ne possédez plus de carte Cristal")

        if carteBlast == False:
            print("Vous ne possédez plus de carte Blast")

    def getJeu(self,carteCreature1,carteCreature2,carteCristal,carteBlast):
        if carteCreature1 > 0 :
            print("Vous possédez ",carteCreature1," carte : créature")

        if carteCreature2 > 0:
            print("Vous possédez ",carteCreature2," carte : créature surpuissante ")

        if carteCristal > 0:
            print("Vous possédez ",carteCristal," carte : Cristal, vous pouvez augmentez votre mana max ")

        if carteBlast == True:
            print("Vous possédez une carte : Blast , il fait de gros dégats, utilisable 1 seule fois")

    def getCreature1(self):
        return self.__carteCreature1

    def setCreature1(self):
        self.__carteCreature1 -= 1
        return self.__carteCreature1

    def getCreature2(self):
        return self.__carteCreature2

    def setCreature2(self):
        self.__carteCreature2 -= 1
        return self.__carteCreature2 

    def getCristal(self):
        return self.__carteCristal

    def setCristal(self):
        self.__carteCristal -= 1
        return self.__carteCristal

    def getBlast(self):
        return self.__carteBlast

    def setBlast(self):
        self.__carteBlast = False
        return self.__carteBlast

creature1 = Creature("creature 1",5,"Vous jouez la 1e créature",10,20)
creature2 = Creature("creature 2",15,"Vous jouez la 2e créature trop forte",20,45)
cristal = Cristal()
blast = Blast()

nomJoueur1 = input("Joueur 1, quel est ton nom ? -> ")
nomJoueur2 = input("Joueur 1, quel est ton nom ? -> ")


mage1 = Mage(nomJoueur1,50,100)
mage2 = Mage(nomJoueur2,50,100)

print(mage2.getJeu(mage2.getCreature1(),mage2.getCreature2(),mage2.getCristal(),mage2.getBlast()))
choixJoueur1 = int(input("Quelle carte veux tu joeur ?"))




while mage1.getHP() > 0 and mage2.getHP() > 0 :
    print("Au tour du 1e mage de jouer :")

    print(mage1.getJeu(mage1.getCreature1(),mage1.getCreature2(),mage1.getCristal(),mage1.getBlast()))
    choixJoueur1 = int(input("Quelle carte veux tu joueur ? (1 : créature 1 / 2 : créature 2 / 3: cristal / 4 : Blast) " ))

    if choixJoueur1 == 1:
        mage1.setCreature1()
        carteActuelle = creature1

    if choixJoueur1 == 2:
        mage1.setCreature2()
        carteActuelle = creature2

    if choixJoueur1 == 3:
        mage1.setCristal()
        carteActuelle = cristal

    if choixJoueur1 == 4:
        mage1.setBlast()
        carteActuelle = blast

    print(carteActuelle.getDescription()," vous infligez ",carteActuelle.getDegats()," dégats !")
    



