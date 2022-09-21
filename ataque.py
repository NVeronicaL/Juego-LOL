import random

class Ataque():


    def __init__(self, id_ataque, nombre, puntaje):
        self.id_ataque = id_ataque
        self.nombre = nombre
        self.puntaje = puntaje

        
    def create_ataque(id_ataque, nombre, puntaje):
        new_ataque = Ataque(id_ataque, nombre, puntaje) 
        return new_ataque


    def create_ataque_random(lista_personajes, op_personaje):
        # Ataque aleatorio
        for p in lista_personajes:
            #Veo que id_personaje sea del jugador al que quiero atacar
            if p['id_personaje'] == op_personaje:
                random_ataque = random.choice(p['ataques'])
                break
        return random_ataque


    def ataques_disponibles(lista_personajes, op_personaje):
        for p in lista_personajes:
            if p['id_personaje'] == op_personaje:
                for a in p['ataques']:
                    print("|------>", a['id_ataque'], "-", a['nombre'])
        