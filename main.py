import json
import random
import personaje
import ataque

#from Juego-LOL.personaje import Personaje

with open('data/personajes.json', encoding="utf-8") as f:
    lista_personajes = json.load(f)

# errors='ignore'
with open('data/ataques.json', encoding="utf-8") as f:
    lista_attacks = json.load(f)

# for p in lista_personajes['personajes']:
#     for a in p['ataques']:
#         print(a)

#print(lista_personajes['personajes'])
# print(lista_attacks)

# Mensaje para mostrar el nombre de ataque y puntaje
def mensaje(nombre_personaje, nombre_ataque, puntaje_ataque):
    print("\n**************JUGADOR",nombre_personaje, "**************")
    print("\nNombre de ataque :", nombre_ataque, "| Puntaje de ataque : ", puntaje_ataque)

# Mensaje para mostrar al jugador si gano.
def mensaje_winner( jugador ):
    print("\n\n💯💯💯💯💯💯💯💯💯💯💯💯💯 WINNER 💯💯💯💯💯💯💯💯💯💯💯💯💯\n\n")
    print("\t\tVida del jugador", jugador.nombre, "en :", jugador.vida)
    print("\n\n💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯\n\n")
    print("\nDesea volver a elegir el personaje a atacar? SI o NO")

# Mensaje para mostrar al jugador si perdio.
def mensaje_loser( jugador ):
    print("\n\n☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀 GAME OVER ☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀\n\n")
    print("\t\tVida del jugador", jugador.nombre, "en :", jugador.vida)
    print("\n\n☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀☠️💀💀☠️💀☠️\n\n")
    print("\nDesea volver a jugar LOL? SI o NO")


respuesta = 'SI'

print("\n+++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n\t\tBIENVENIDO/A AL JUEGO DE LOL\n")
print("+++++++++++++++++++++++++++++++++++++++++++++++++")


while lista_personajes['personajes'] != [] and respuesta == 'SI':
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t\t MENU DE PERSONAJES")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")

    # personajes disponibles para jugar
    for p in lista_personajes['personajes']:
        print("|------>", p['opcion'], "-", p['nombre'])
        
    # selección de un personaje para jugar
    op_elegida = int(input("\nIngresa una opcion de personaje para jugar: "))
    # Creación de un objeto Personaje para jugar, con el id_personaje, nombre, vida. 
    for p in lista_personajes['personajes']:
        if p['id_personaje'] == op_elegida:
            p1 = personaje.Personaje(p['id_personaje'], p['nombre'],p['vida'])
            print(p1.id_personaje, p1.nombre, p1.vida)
            break

    match op_elegida:
        case 0 | 1 | 2 | 3 | 4 | 5:
            # control de las respuestas de las preguntas
            while respuesta == 'SI': 
                # personajes disponibles para atacar
                for p in lista_personajes['personajes']:
                    if p['id_personaje'] != op_elegida:
                        print("|------>", p['id_personaje'], "-", p['nombre'])

                # selección de personaje a atacar                   
                op_personaje = int(input("\nIngresa una opcion de personaje a atacar: "))

                # Creación de un objeto Personaje para atacar, con el id_personaje, nombre, vida. 
                for p in lista_personajes['personajes']:
                    if p['id_personaje'] == op_personaje:
                        p2 = personaje.Personaje(p['id_personaje'], p['nombre'],p['vida'])
                        print(p2.id_personaje, p2.nombre, p2.vida)
                        break
                while lista_personajes['personajes'] != []:
                    # ataques disponibles
                    print("\nHABILIDADES DE ATAQUES DISPONIBLES : \n")
                    for p in lista_personajes['personajes']:
                        if p['id_personaje'] == op_elegida:
                            for a in p['ataques']:
                                print("|------>", a['id_ataque'], "-", a['nombre'])

                    # selección de ataque
                    op_ataque = int(input("\nIngresa una opcion de ataque: "))
                    # Creación de un objeto Ataque para atacar, con el id_ataque, nombre, puntaje. 
                    for p in lista_personajes['personajes']:
                        if p['id_personaje'] == op_elegida:
                            for a in p['ataques']:
                                if a['id_ataque'] == op_ataque:
                                    a = ataque.Ataque(['id_ataque'], a['nombre'], a['puntaje'])
                                    mensaje(p1.nombre, a.nombre, a.puntaje)
                                    break
                            break
                    match op_ataque:
                        case 0 | 1 | 2 | 3 | 4 | 5:     
                            #p1 ataca a p2
                            #Verifico que el jugador p1 tenga vida para que pueda realizar un ataque.
                            if p1.vida > 0:
                                p1.atacar(p2, a)
                                print("Vida restante de jugador", p2.nombre, p2.vida)
                            else:
                                mensaje_loser(p1)
                                respuesta = input().upper()
                                break
                            # Verifico que el jugador contricante p2 tenga vida para que este pueda realizar un ataque.
                            if p2.vida > 0:

                                #ataque_random(lista_personajes['personajes'], op_personaje)
                                random_ataque = ataque.Ataque.ataque_random(lista_personajes['personajes'], op_personaje)

                                # Creación de una instancia de clase Ataque de forma random
                                for p in lista_personajes['personajes']:
                                    if p['id_personaje'] == op_personaje:
                                        for ataque_p2 in p['ataques']:
                                            if ataque_p2['id_ataque'] == random_ataque['id_ataque']:
                                                ataque_p2 = ataque.Ataque(ataque_p2['id_ataque'], ataque_p2['nombre'], ataque_p2['puntaje'])
                                                mensaje(p2.nombre, ataque_p2.nombre, ataque_p2.puntaje)
                                                break
                                        break
                                # p2 ataca a p1 
                                p2.atacar(p1, ataque_p2)
                                print("Vida restante de jugador", p1.nombre , p1.vida)
                            else:
                                mensaje_winner(p1)
                                respuesta = input().upper()
                                break                            
                        case _:
                            print("Error, elija un personaje disponible")
                            break                                                      
        case _: 
            print("Error, elija un personaje disponible")
            break








