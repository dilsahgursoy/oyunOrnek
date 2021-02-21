from abc import ABC,abstractmethod,abstractproperty
class Hero(ABC): 
    @abstractmethod
    def durum(self):
        pass
    @abstractproperty
    def vurus1(self):
        return self.guc
    @abstractproperty
    def vurus2(self):
        return self.guc//2
    @abstractproperty
    def vurus3(self):
        return self.guc//3
    @abstractmethod 
    def darbe1(self,vurus):
        self.saglik -= vurus
    @abstractmethod 
    def darbe2(self,vurus):
        self.saglik -= vurus//2
    @abstractmethod
    def darbe3(self,vurus):
        self.saglik -= vurus//3




class MarvelHero(Hero):
    def __init__(self,adi,guc,saglik):
        self.guc = guc
        self.saglik = saglik
        self.adi = adi
    def durum(self):
        print(f"{self.adi} Saglik:{self.saglik}")
    @property
    def vurus1(self):
        return self.guc
    @property
    def vurus2(self):
        return self.guc//2
    @property
    def vurus3(self):
        return self.guc//3

    def darbe1(self,vurus):
        self.saglik -= vurus
    def darbe2(self,vurus):
        self.saglik -= vurus//2
    def darbe3(self,vurus):
        self.saglik -= vurus//3
    
    def __del__(self):
        print("R.I.P.",self.adi)

class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool",50,500)

class CaptainAmerica(MarvelHero):
    def __init__(self):
        super().__init__("CaptainAmerica",45,450)

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",55,450)

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("Iron Man",50,450)

class DCHero(Hero):
    def __init__(self,adi,guc,saglik):
        self.guc = guc
        self.saglik = saglik
        self.adi = adi
    def durum(self):
        print(f"{self.adi} Saglik:{self.saglik}")
    @property
    def vurus1(self):
        return self.guc
    @property
    def vurus2(self):
        return self.guc//2
    @property
    def vurus3(self):
        return self.guc//3

    def darbe1(self,vurus):
        self.saglik -= vurus
    def darbe2(self,vurus):
        self.saglik -= vurus//2
    def darbe3(self,vurus):
        self.saglik -= vurus//3
    
    def __del__(self):
        print("R.I.P.",self.adi)

class LexLuther(DCHero):
    def __init__(self):
        super().__init__("Lex Luther",50,550)

class AlfredPennyworth(DCHero):
    def __init__(self):
        super().__init__("Alfred Pennyworth",25,100)

class Joker(DCHero):
    def __init__(self):
        super().__init__("Joker",70,700)


class TurkKahramanlar(Hero):
    def __init__(self,adi,guc,saglik):
        self.guc = guc
        self.saglik = saglik
        self.adi = adi
    def durum(self):
        print(f"{self.adi} Saglik:{self.saglik}")
    @property
    def vurus1(self):
        return self.guc
    @property
    def vurus2(self):
        return self.guc//2
    @property
    def vurus3(self):
        return self.guc//3

    def darbe1(self,vurus):
        self.saglik -= vurus
    def darbe2(self,vurus):
        self.saglik -= vurus//2
    def darbe3(self,vurus):
        self.saglik -= vurus//3
    
    def __del__(self):
        print("Allah Rahmet Eylesin",self.adi)


class KaraMurat(TurkKahramanlar):
    def __init__(self):
        super().__init__("KaraMurat",50,500)

class MalkocOglu(TurkKahramanlar):
    def __init__(self):
        super().__init__("Malkoc Oglu",50,500)


class Tarkan(TurkKahramanlar):
    def __init__(self):
        super().__init__("Tarkan",70,500)

class BattalGazi(TurkKahramanlar):
    def __init__(self):
        super().__init__("Battal Gazi",70,500)


import random
import time
def HareketSec(obj,param): # polymorphism
    vurListe = [obj.vurus1,obj.vurus2,obj.vurus3]
    darbeListe = [obj.darbe1,obj.darbe2,obj.darbe3]
    return random.choice(vurListe if param == 1 else darbeListe)

    
    


MarvelListe = [DeadPool,CaptainAmerica,Hulk,IronMan]
DCListe = [AlfredPennyworth,Joker,LexLuther]
TurkListe = [BattalGazi,KaraMurat,Tarkan,MalkocOglu]
karList = random.choice([MarvelListe,DCListe,TurkListe])
p1 = random.choice(karList)()
karList = random.choice([MarvelListe,DCListe,TurkListe])
p2 = random.choice(karList)()

while p1.saglik > 0 and p2.saglik > 0:
    time.sleep(1)
    HareketSec(p1,2)(HareketSec(p2,1))
    HareketSec(p2,2)(HareketSec(p1,1))
    p1.durum()
    p2.durum()
else:
    if p1.saglik>p2.saglik:
        print(p1.adi,"Kazandı")
    else:
        print(p2.adi,"Kazandı")

input()
