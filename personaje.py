class Personaje():
    

    def __init__(self, id_personaje, nombre, vida):
        self.id_personaje = id_personaje
        self.nombre = nombre
        self.vida = vida


    def atacar(self, p, ataque):
        if self.vida > 0 and p.vida > 0:
            p.vida -= ataque.puntaje

    
    def create_personaje( id_personaje, nombre, vida):
        new_personaje = Personaje(id_personaje, nombre, vida)
        return new_personaje


    def personajes_disponibles(lista_personajes):
        for p in lista_personajes:
            print("|------>", p['opcion'], "-", p['nombre'])


    def tiene_vida( personaje ):
        if personaje.vida > 0:
            return True
        else: 
            return False
