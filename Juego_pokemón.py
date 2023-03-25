import time
import numpy as np
import sys

# funcion para imprimir caracter por caracter

def retraso_impresion(s):
    # imprime cada uno de los caracteres a la vez, con un retraso de 0,05 segundos
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Crear las clases

class Pokemon:
    def __init__(Pokemon1, Nombre, Tipo, Movimiento, EVs, salud='==================='):
        # save variables as attributes
        Pokemon1.Nombre = Nombre
        Pokemon1.Tipo = Tipo
        Pokemon1.Movimiento = Movimiento
        Pokemon1.ataque = EVs['ataque']
        Pokemon1.defensa = EVs['defensa']
        Pokemon1.salud = salud
        Pokemon1.barras = 20 # cantidad de barras de salud


    def lucha(Pokemon1, Pokemon2):
        # permite 2 pokemones luchen entre ellos

        # imprimir la información de lucha
        print("-------BATALLA POKEMON-------")
        print(f"\n{Pokemon1.Nombre}")
        print("Tipo/", Pokemon1.Tipo)
        print("Ataque/", Pokemon1.ataque)
        print("Defensa/", Pokemon1.defensa)
        print("Nivel/", 3*(1+np.mean([Pokemon1.ataque,Pokemon1.defensa])))
        print("\nVRS")
        print(f"\n{Pokemon2.Nombre}")
        print("Tipo/", Pokemon2.Tipo)
        print("Ataque/", Pokemon2.ataque)
        print("Defensa/", Pokemon2.defensa)
        print("Nivel/", 3*(1+np.mean([Pokemon2.ataque,Pokemon2.defensa])))

        time.sleep(2)

        # Ventajas por tipo de pokemon
        version = ['fuego', 'agua', 'planta']
        for i,k in enumerate(version):
            if Pokemon1.Tipo == k:
                # Ambos son del mismo tipo
                if Pokemon2.Tipo == k:
                    string_1_ataque = '\n El ataque no fue muy efectivo...'
                    string_2_ataque = '\n El ataque no fue muy efectivo...'

                # Pokemon2 es más fuerte
                if Pokemon2.Tipo == version[(i+1)%3]:
                    Pokemon2.ataque *= 1.5
                    Pokemon2.defensa *= 1.5
                    Pokemon1.ataque /= 1.5
                    Pokemon1.defensa /= 1.5
                    string_1_ataque = '\n El ataque no fue muy efectivo...'
                    string_2_ataque = '\n El ataque fue super efectivo!'

                # Pokemon2 es más debil
                if Pokemon2.Tipo == version[(i+2)%3]:
                    Pokemon1.ataque *= 1.5
                    Pokemon1.defensa *= 1.5
                    Pokemon2.ataque /= 1.5
                    Pokemon2.defensa /= 1.5
                    string_1_ataque = '\n El Atatque fue super efectivo!'
                    string_2_ataque = '\n EL ataque no fue muy efectivo...'


        # Para la lucha ...
        # Mientras los pokemones tengan barras de dalud
        while (Pokemon1.barras > 0) and (Pokemon2.barras > 0):
            # Imprimir la salud de cada pokemon
            print(f"\n{Pokemon1.Nombre}\t\t PS \t{Pokemon1.salud}")
            print(f"{Pokemon2.Nombre}\t\t PS \t{Pokemon2.salud}\n")

            print(f"Adelante {Pokemon1.Nombre}!")
            for i, x in enumerate(Pokemon1.Movimiento):
                print(f"{i+1}.", x)
            index = int(input('Elije un movimiento: '))
            retraso_impresion(f"\n{Pokemon1.Nombre} ha usado {Pokemon1.Movimiento[index-1]}!")
            time.sleep(1)
            retraso_impresion(string_1_ataque)

            # determinar el daño
            Pokemon2.barras -= Pokemon1.ataque
            Pokemon2.salud = ""

            # agregar barras de salud
            for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.salud += "="

            time.sleep(1)
            print(f"\n{Pokemon1.Nombre}\t\t PS \t{Pokemon1.salud}")
            print(f"{Pokemon2.Nombre}\t\t PS \t{Pokemon2.salud}\n")
            time.sleep(.5)

            # Verificar si el pokemon recibio daño
            if Pokemon2.barras <= 0:
                retraso_impresion("\n..." + Pokemon2.Nombre + ' Se ha debilitado.')
                break

            # Turno del Pokemon 2

            print(f"Adelante {Pokemon2.Nombre}!")
            for i, x in enumerate(Pokemon2.Movimiento):
                print(f"{i+1}.", x)
            index = int(input('Elije un moviminto: '))
            retraso_impresion(f"\n{Pokemon2.Nombre} usó {Pokemon2.Movimiento[index-1]}!")
            time.sleep(1)
            retraso_impresion(string_2_ataque)

            # Determinar el daño
            Pokemon1.barras -= Pokemon2.ataque
            Pokemon1.salud = ""

            # Agregar barras de salud
            for j in range(int(Pokemon1.barras+.1*Pokemon1.defensa)):
                Pokemon1.salud += "="

            time.sleep(1)
            print(f"{Pokemon1.Nombre}\t\t PS \t{Pokemon1.salud}")
            print(f"{Pokemon2.Nombre}\t\t PS \t{Pokemon2.salud}\n")
            time.sleep(.5)

            # Verificar si el pokemon recibio daño
            if Pokemon1.barras <= 0:
                retraso_impresion("\n..." + Pokemon1.Nombre + ' fainted.')
                break

        money = np.random.choice(5000)
        retraso_impresion(f"\n EL oponente te ha entregado ${money}.\n")






if __name__ == '__main__':
    #Create Pokemon
    Charizard = Pokemon('Charizard', 'fuego', ['Flama de fuego', 'Volar', 'Cañon infernal', 'Golpe de fuego'], {'ataque':12, 'defensa': 8})
    Blastoise = Pokemon('Blastoise', 'agua', ['Pistola de agua', 'Burbuja', 'Hydro Bomba', 'Surf'],{'ataque': 10, 'defensa':10})
    Venusaur = Pokemon('Venusaur', 'planta', ['Enredadera', 'Hoja Navaja', 'Terremoto', 'Coletazo'],{'ataque':8, 'defensa':12})

    Charmander = Pokemon('Charmander', 'fuego', ['Atrapar', 'Cabezazo', 'Tacleada', 'Golpe de fuego'],{'ataque':4, 'defensa':2})
    Squirtle = Pokemon('Squirtle', 'agua', ['Bubblebeam', 'Tacleada', 'Headbutt', 'Surf'],{'ataque': 3, 'defensa':3})
    Bulbasaur = Pokemon('Bulbasaur', 'planta', ['Enredadera', 'Hoja Navaja', 'Tacleada', 'Golpe Rapido'],{'ataque':2, 'defensa':4})

    Charmeleon = Pokemon('Charmeleon', 'fuego', ['Atrapar', 'Cabezazo', 'Cañon infernal', 'Golpe de Fuego'],{'ataque':6, 'defensa':5})
    Wartortle = Pokemon('Wartortle', 'agua', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ataque': 5, 'defensa':5})
    Ivysaur = Pokemon('Ivysaur\t', 'planta', ['Enredadera', 'Hoja Navaja', 'Bala Semilla', 'Golpe Rapido'],{'ataque':4, 'defensa':6})

    Charizard.lucha(Blastoise) # Para ponerlos a luchar
    