class Personaje():
    

    def __init__(self, id_personaje, nombre, vida):
        self.id_personaje = id_personaje
        self.nombre = nombre
        self.vida = vida


    def atacar(self, p, ataque):
        if p.vida > 0:
            # for ataque in lista_attacks['ataques']:
            #if ataque == ataque['nombre']:
            p.vida -= ataque.puntaje
            #print("entra", p.vida)
                #break
        # else:
        #     print("***********************************************")
        #     print("*******************GAME OVER*******************")
        #     print("Vida del jugador", self.nombre, "en :", self.vida)
        #     print("***********************************************")