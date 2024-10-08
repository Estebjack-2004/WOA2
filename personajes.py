import random
from WOA2 import text_speed

class Personaje:
    def __init__(self, nombre, titulo, clan = None):
        self.nombre = nombre
        self.titulo = titulo
        self.clan = clan

    def asignar_clan(self, clan):
        self.clan = clan

    def realizar_ataque(self, objetivo):
        f"{self.nombre} ha realizado un ataque!"
        damage = ((self.fuerza + self.ataque) / ((self.vida_original-self.puntos_vida) + self.vida_original)) / 10
        objetivo.recibir_ataque(damage)

    def recibir_ataque(self, damage):
        f"{self.nombre} ha recibido daño!"
        factor_damage = (self.defensa * damage) / 100
        self.fuerza = round(self.fuerza / (factor_damage + 1))
        self.puntos_vida = round(self.puntos_vida / (factor_damage + 1))
        self.defensa = round(self.defensa / (factor_damage + 1))
        self.ataque = round(self.ataque / (factor_damage + 1))

        if self.puntos_vida > 0:
            print(f"{self.nombre} ha recibido un ataque puntos de vida = {self.puntos_vida}")
        else:
            print(f"El {self.titulo} {self.nombre} ha muerto")

    def __str__(self):
        return (f"{self.titulo}: {self.nombre}\n"
                f"Fuerza: {self.fuerza}, Puntos de Vida: {self.puntos_vida}, "
                f"Defensa: {self.defensa}, Ataque: {self.ataque}, "
                f"Clan: {self.clan}")
        
#***********************************************************************

class Guerrero(Personaje):
    def __init__(self, nombre, titulo = "Guerrero"):
        super().__init__(nombre, titulo)
        self.fuerza = 90
        self.puntos_vida = 100
        self.defensa = 90
        self.ataque = 100
        self.vida_original = self.puntos_vida
        
#***********************************************************************

class Mago(Personaje):
    def __init__(self, nombre, titulo = "Mago"):
        super().__init__(nombre, titulo)
        self.fuerza = 80
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 90
        self.vida_original = self.puntos_vida

#***********************************************************************

class Arquero(Personaje):
    def __init__(self, nombre, titulo = "Arquero"):
        super().__init__(nombre, titulo)
        self.fuerza = 95
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 120
        self.vida_original = self.puntos_vida

#***********************************************************************

class Fundador(Mago):
    def __init__(self, nombre):
        super().__init__(nombre, "Fundador")
        self.fuerza = 100
        self.puntos_vida = 110
        self.defensa = 110
        self.ataque = 110
        self.vida_original = self.puntos_vida
        self.slot_pociones = {}
        print(f"{self.nombre} ha fundado un clan.")
        
    def crear_pociones(self):
        cont_pociones = 0
        cura_aleatoria = random.randint(5, 30)
        if len(self.slot_pociones.keys) <= 3:
            cont_pociones += 1
            self.slot_pociones[cont_pociones] = cura_aleatoria
            text_speed(f"{self.nombre} 🧙‍♂️ has created a new potion! Potion: ({self.slot_pociones.keys} 🥤| Healing: {self.slot_pociones.values} 💗)")
        else:
            text_speed(f"Oops! You can´t have more than 3 potions in your pockets 🥤! {self.slot_pociones.keys}")
        
#***********************************************************************

if __name__=="__main__":
    pass