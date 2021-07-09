import random
from warnings import simplefilter

class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        
        if (level):
            self.level = level
        else:
            self.level = random.randint(1, 100)
        
        if(nome):
            self.nome = nome
        else:
            self.nome = especie
            
        self.ataque = self.level * 3
        self.vida = self.level * 6.25
        
    def __str__(self):
        return "{}(nv.{})".format( self.nome,  self.level)
    
    def atacar(self, alvo):
        ataque = round(self.ataque * random.random()*1.5, 2)
        alvo.vida -=  ataque
        print("{} perdeu {}".format(alvo, ataque))
        
        if alvo.vida <= 0:
            print("{} faleceu".format(alvo))
            alvo.vida = self.level * 6.25
            return True
        else:
            return False
            
        

class PokemonEletrico(Pokemon):
    tipo = "eletrico"
    
    def atacar(self, alvo):
        print("{} lançou um ataque elétrico em {}".format(self, alvo))
        return super().atacar(alvo)



class PokemonFogo(Pokemon):
    tipo = "fogo"
    
    def atacar(self, alvo):
        print("{} lançou um ataque de fogo em {}".format(self, alvo))
        return super().atacar(alvo)
        
        
    
class PokemonAgua(Pokemon):
    tipo = "água"
    
    def atacar(self, alvo):
        print("{} lançou um ataque de água em {}".format(self, alvo))
        return super().atacar(alvo)
    
   


    



