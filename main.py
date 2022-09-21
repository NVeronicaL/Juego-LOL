import json
import random
# Importo la clase Personaje
from personaje import Personaje
# Importo la clase Ataque
from ataque import Ataque


with open('data/personajes.json', encoding="utf-8") as f:
    lista_personajes = json.load(f)

# errors='ignore'
with open('data/ataques.json', encoding="utf-8") as f:
    lista_attacks = json.load(f)

# for p in lista_personajes['personajes']:
#     for a in p['ataques']:
#         print(a)

#print(lista_personajes['personajes'])

# Mensaje para mostrar el nombre de ataque y puntaje
def mensaje(nombre_personaje, nombre_ataque, puntaje_ataque):
    print("\n**************JUGADOR",nombre_personaje, "**************")
    print("\nNombre de ataque :", nombre_ataque, "| Puntaje de ataque : ", puntaje_ataque)

# Mensaje para mostrar al jugador si gano.
def mensaje_winner( jugador ):
    print("\n\n💯💯💯💯💯💯💯💯💯💯💯💯💯 WINNER 💯💯💯💯💯💯💯💯💯💯💯💯💯\n\n")
    print("\t\tVida del jugador", jugador.nombre, "en :", jugador.vida)
    print("\n\n💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯\n\n")
    print("\nDesea volver a jugar LOL? SI o NO")

# Mensaje para mostrar al jugador si perdio.
def mensaje_loser( jugador ):
    print("\n\n☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀 GAME OVER ☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀\n\n")
    print("\t\tVida del jugador", jugador.nombre, "en :", jugador.vida)
    print("\n\n☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀💀☠️💀☠️\n\n")
    print("\nDesea volver a jugar LOL? SI o NO")

# variable respuesta: me sirve para salir del bucle while 
respuesta = 'SI'

while lista_personajes['personajes'] != [] and respuesta == 'SI':
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n\t\tBIENVENIDO/A AL JUEGO DE LOL\n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t\t MENU DE PERSONAJES")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")

    # Personajes disponibles para jugar
    Personaje.personajes_disponibles(lista_personajes['personajes'])
        
    # selección de un personaje para jugar
    op_personaje1 = int(input("\nIngresa una opcion de personaje para jugar: "))

    # Creación de un objeto Personaje para jugar, con el id_personaje, nombre, vida. 
    for p in lista_personajes['personajes']:
        if p['id_personaje'] == op_personaje1:
            # p1 = personaje.Personaje(p['id_personaje'], p['nombre'],p['vida'])
            p1 = Personaje.create_personaje(p['id_personaje'], p['nombre'],p['vida'])
            print(p1.id_personaje, p1.nombre, p1.vida)
            break

    """
        según la seleccion de personaje que eligio el usuario.
    """
    match op_personaje1:
        case 0 | 1 | 2 | 3 | 4 | 5:
            # personajes disponibles para atacar
            Personaje.personajes_disponibles(lista_personajes['personajes'])

            # selección de personaje a atacar                   
            op_personaje2 = int(input("\nIngresa una opcion de personaje a atacar: "))

            """
                Creación de un objeto Personaje para atacar, con los atributos : 
                id_personaje, nombre, vida, los valores de estos atributos son 
                provenientes de un archivo personajes.json
            """
            for p in lista_personajes['personajes']:
                if p['id_personaje'] == op_personaje2:
                    p2 = Personaje.create_personaje(p['id_personaje'], p['nombre'],p['vida'])
                    print(p2.id_personaje, p2.nombre, p2.vida)
                    break

            """
                Mientras tengan vida los jugadores :  p1 y  p2 ,  podran realizar algún ataque.
            """
            while Personaje.tiene_vida(p1) and Personaje.tiene_vida(p2):
                """
                    Se muestra todas las opciones de ataques disponibles, que tiene cada
                    personaje , en total son 5 ataques que dispone cada personaje.
                """
                print("\nHABILIDADES DE ATAQUES DISPONIBLES DE", p1.nombre, ":\n")
                Ataque.ataques_disponibles(lista_personajes['personajes'], op_personaje1)
                # selección de ataque del personaje p1
                op_ataque_p1 = int(input("\nIngresa una opcion de ataque: "))

                """
                    Creación de un objeto Ataque para lanzar al contrincante, con los atributos : 
                    id_ataque, nombre, puntaje, los valores de estos atributos son 
                    provenientes de un archivo personajes.json
                """
                for p in lista_personajes['personajes']:
                    if p['id_personaje'] == op_personaje1:
                        for a in p['ataques']:
                            if a['id_ataque'] == op_ataque_p1:
                                new_ataque_p1 = Ataque.create_ataque(a['id_ataque'], a['nombre'], a['puntaje'])
                                break
                        break
                
                """
                    según la seleccion de ataque que eligio el jugador, entro en uno de los casos que se enumeran 
                    según el id_ataque.
                """
                match op_ataque_p1:
                    case 0 | 1 | 2 | 3 | 4 | 5:     
                        #personaje "p1" ataca a personaje "p2"
                        p1.atacar(p2, new_ataque_p1)
                        if Personaje.tiene_vida(p1):
                            mensaje(p1.nombre, new_ataque_p1.nombre, new_ataque_p1.puntaje)
                            print("Vida restante de jugador", p2.nombre, p2.vida)

                        # selección de ataque del personaje p2
                        op_ataque_p2 = Ataque.create_ataque_random(lista_personajes['personajes'], op_personaje2)
                        """
                            Creación de un objeto Ataque de forma aleatoria o random para lanzar al contrincante, con los atributos : 
                            id_ataque, nombre, puntaje, los valores de estos atributos son 
                            provenientes de un archivo personajes.json
                        """
                        for p in lista_personajes['personajes']:
                            if p['id_personaje'] == op_personaje2:
                                for a in p['ataques']:
                                    if a['id_ataque'] == op_ataque_p2['id_ataque']:
                                        new_ataque_p2 = Ataque.create_ataque(a['id_ataque'], a['nombre'], a['puntaje'])
                                        break
                                break

                        #personaje "p2" ataca a personaje "p1"
                        p2.atacar(p1, new_ataque_p2)
                        if Personaje.tiene_vida(p2):
                            mensaje(p2.nombre, new_ataque_p2.nombre, new_ataque_p2.puntaje)
                            print("Vida restante de jugador", p1.nombre , p1.vida)                      
                    case _:
                        print("❌ Error : elija un ataque disponible")
                        break
            if Personaje.tiene_vida(p1)  and not Personaje.tiene_vida(p2):
                """
                    mensaje_winer : si el jugador GANO
                """
                mensaje_winner( p1 )
                respuesta = input().upper()
            if not Personaje.tiene_vida(p1) and Personaje.tiene_vida(p2):
                """
                    mensaje_loser : si el jugador PERDIO
                """
                mensaje_loser( p1 )
                respuesta = input().upper()

        case _: 
            print("❌ Error :  elija un personaje disponible")
            break








