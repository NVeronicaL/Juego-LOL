import json
import random
import personaje
import ataque

#from Juego-LOL.personaje import Personaje

with open('data/personajes.json') as f:
    lista_personajes = json.load(f)

# errors='ignore'
with open('data/ataques.json', encoding="utf-8") as f:
    lista_attacks = json.load(f)


# print(lista_personajes)

# print(lista_attacks)

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
                for a in lista_attacks['ataques']:
                    print("|------>", a['id_ataque'], "-", a['nombre'])

                # selección de ataque
                op_ataque = int(input("\nIngresa una opcion de ataque: "))
                # Creación de un objeto Ataque para atacar, con el id_ataque, nombre, puntaje. 
                for a in lista_attacks['ataques']:
                    if a['id_ataque'] == op_ataque:
                        a = ataque.Ataque(['id_ataque'], a['nombre'], a['puntaje'])
                        print("Nombre de ataque de p1: ", a.nombre)
                        print("Puntaje del ataque de p1: ", a.puntaje)
                        break
                match op_ataque:
                    case 0 | 1 | 2 | 3 | 4 |5:     

                        p1.atacar(p2, a)
                        print("Vida restante de p2", p2.vida)

                        # Ataque aleatorio del jugador contrincante
                        ramdom_ataque = random.choice(lista_attacks['ataques'])
                        for ataque_p2 in lista_attacks['ataques']:
                            if ataque_p2['id_ataque'] == ramdom_ataque['id_ataque']:
                                ataque_p2 = ataque.Ataque(ataque_p2['id_ataque'], ataque_p2['nombre'], ataque_p2['puntaje'])
                                print("Nombre de ataque de p2: ", ataque_p2.nombre)
                                print("Puntaje de ataque de p2: ", ataque_p2.puntaje)
                                break
                        p2.atacar(p1, ataque_p2)
                        print("Vida restante de p1", p1.vida)
                        if p1.vida <= 0:
                            print("***********************************************")
                            print("*******************GAME OVER*******************")
                            print("Vida del jugador", p1.nombre, "en :", p1.vida)
                            print("***********************************************")
                            print("\nDesea volver a jugar LOL? SI o NO")
                            respuesta = input().upper()
                            break
                        elif p2.vida <= 0:
                            print("***********************************************")
                            print("*******************GAME OVER*******************")
                            print("Vida del jugador", p2.nombre, "en :", p2.vida)
                            print("***********************************************")
                            print("\nDesea volver a elegir el personaje a atacar? SI o NO")
                            respuesta = input().upper()
                            break
                    case _:
                        print("Error, elija un personaje disponible")
                        break                                                      
                                
        case _: 
            print("Error, elija un personaje disponible")
            break








