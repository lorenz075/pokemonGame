import random

from pokemon import *

NOMES = ["Roger", "Anastacia", "Professor", "Gary", "Barry", "Ash", "Misty", "Brock", "Jessie", "James", "Mãe do Ash"]

POKEMONS = [
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonEletrico("Electabuzz"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Lapras"),
    PokemonAgua("Psyduck"),
    PokemonFogo("Charmander"),
    PokemonFogo("Cyndaquil"),
    PokemonFogo("Magmar"),
]

class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons
        
        self.dinheiro = dinheiro
        
    def __str__(self):
        return self.nome
    
    def mostrar_pokemons(self):
        if(self.pokemons):
            print("Pokemons de {}:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} não tem pokemons".format(self))
    
    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("Player sem pokemons") 
    
    def mostrar_dinheiro(self):
        print("Você possui $ {}".format(self.dinheiro))
    
    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Você ganhou $ {}".format(quantidade))
        self.mostrar_dinheiro()
        
                    
    def batalhar(self, pessoa):
        print("{} iniciou combate com {}".format(self, pessoa))
        
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
        
        seu_pokemon = self.escolher_pokemon()
        
        if seu_pokemon and pokemon_inimigo:
            while True:
                vitoria = seu_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("Você derrotou {}!!".format(pessoa))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 50)
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(seu_pokemon)
                if vitoria_inimiga:
                    print("{} te derrotou".format(pessoa))
                    break
                
        else:
            print("Tentando lutar sozinho? Falta um pokemon")
        
        
            
class Player(Pessoa):
    tipo = "player"
    
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))
        
    def escolher_pokemon(self):
        self.mostrar_pokemons()
        
        if self.pokemons:
            while True:
                escolha = input("Escolha o seu pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho vc!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Tente novamente, escolha inválida")
        else:
            print("Player sem pokemons")
        
    def explorar(self):
        if random.random() <= 0.3:
            pokemon_selvagem = random.choice(POKEMONS)
            print("A wild {} has appeared".format(pokemon_selvagem))
            
            escolha = input("Deseja capturá-lo? (y/n)\n")
            if escolha == "y":
                if ((pokemon_selvagem.level*random.random())/10) <= 1.3:
                    self.capturar(pokemon_selvagem)
                    self.mostrar_pokemons()
                else:
                    print("{} escapou".format(pokemon_selvagem))
            else:
                print("Ok, continue explorando trouxa")
        else:
            print("Continue explorando campeão")
            
         
    
class Inimigo(Pessoa):
    tipo = "inimigo" 
    def gerar_time_adversario(self, nome):
            pokemons_aleatorios = []
            for i in range(6):
                pokemons_aleatorios.append(random.choice(POKEMONS))
        
            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        
    
    def __init__ (self, nome=None, pokemons=None):
        if not (pokemons):
            self.gerar_time_adversario(nome)
        else:
             self.gerar_time_adversario(nome)
                   
        

        
    
        