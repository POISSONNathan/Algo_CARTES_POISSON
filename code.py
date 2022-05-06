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
    def __init__(self,name,price,description,degats,hp):
        Carte.__init__(self,name,price,description,degats,hp)

    

class Mage:
    def __init__(self,name,hp,mana):
        self.__name = name
        self.__hp = hp
        self.__mana = mana
        self.__manaMax = 100
    
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

    def setMana (self,price):
        self.__mana += price

        if self.__mana > self.__manaMax:
            self.__mana = self.__manaMax

    def upManaMax(self,up):
        self.__manaMax += up

    def getValeurActuelle(self,valAct):
        return valAct

    def jouer(self,price):
        self.__mana -= price

    def defausse(self):
        self


creature1 = Creature("creatrure 1",5,"Vous jouez la 1e créature",10,20)

creature2 = Creature("creatrure 1",15,"Vous jouez la 2e créature trop forte",20,45)

blast = Blast("blast 1",40,"Vous jouez un blast, vous infligez 40 degats",40,0)

cristal = Cristal()

mage1 = Mage("MAGE cheat",50,100)

mage2 = Mage("Mage fort",50,100)


while mage1.getHP() > 0 and mage2.getHP() > 0 :
    print("Au tour du 1e mage de jouer :")



    print("Au tour du 2e mage de jouer :")





