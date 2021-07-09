import pickle

from os import error
from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    
    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)
    
    print("1- ", pikachu)
    print("2- ", charmander)
    print("3- ", squirtle)
    
    while True:
        escolha = input("Escolha: ")
        
        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Opção inválida")

def salvar_jogo(player):
    try:
        with open("database.db", 'wb') as file:
            pickle.dump(player, file)
            print("Game salvo com sucesso")
    except Exception as error:
        print("Erro ao salvar")
        print(error)

def load_jogo():
    try:
        with open("database.db", 'rb') as file:
            player = pickle.load(file)
            print("Jogo carregado")
            return player
    except Exception as error:
        print("Save não encontrado")
        
    

if __name__ == "__main__":
    print("========================================================================")
    print("§")
    print("§")
    print("§")
    print("                 Bem vindo ao Pokemon de terminal")
    print("                                                                  §")
    print("                                                                  §")
    print("                                                                  §")
    print("========================================================================")
    
    player = load_jogo()
    
    if not player:
    
        nome = input("Fala, qual o seu nome? ")
        player = Player(nome)
        print("Beleza, {}? Capture o máximo de pokemons que conseguir e derrote seus inimigos!".format(player))
        player.mostrar_dinheiro()
        
        if player.pokemons:
            print("Então você já tem alguns pokemons...")
            player.mostrar_pokemons()
        else:
            print("Você não tem pokemons, escolha o seu bixo inicial!")
            escolher_pokemon_inicial(player)
        print("Péssima escolha, mas agora você pode enfrentar seu inimigo mortal, prepare-se:")
        barry = Inimigo(nome="Barry" ,pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(barry)
        salvar_jogo(player)
    
        
    while True:
        print("========================================================================")
        print("O que deseja fazer?")
        print("1 - Explorar a ilha")
        print("2 - Batalhar contra um inimigo")
        print("3 - Ver pokeagenda")
        print("0 - Sair do game")
        escolha = input("Sua escolha: ")
        
        if escolha == "0":
            print("Adios")
            break
        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemons()
        else:
            print("Escolha inválida, não avacalha")
        
        
        
        
    
   
    
 



#inimigo1 = Inimigo( pokemons=[PokemonAgua("Squirtle", level=2)])
#player.batalhar(inimigo1)



