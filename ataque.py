import random

class Ataque():


    def __init__(self, id_ataque, nombre, puntaje):

        
        self.id_ataque = id_ataque
        self.nombre = nombre
        self.puntaje = puntaje
        
    def ataque_random(lista_personajes, op_personaje):
        # Ataque aleatorio del jugador contrincante (p2)
        for p in lista_personajes:
            #Veo que id_personaje sea del jugador al que quiero atacar
            if p['id_personaje'] == op_personaje:
                random_ataque = random.choice(p['ataques'])
                #print('random_ataque', ramdom_ataque)
                break
        return random_ataque