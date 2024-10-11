class Personaje ():
    def __init__(self, kind):
        self.kind= kind
        self.destiny = " "
        self.starting_force = 0
        self.enemy = " "
        self.power = " "

## Método para definir a los personajes       
    def atributes(self):
        if self.kind == "ELFO":
            self.power = self.power.replace (self.power, "súper agilidad")
            self.starting_force = self.starting_force + 300
            self.enemy = self.enemy.replace (self.enemy , "Saruman")
        elif self.kind == "HUMANO":
            self.power = self.power.replace (self.power, "destreza en armas")
            self.starting_force = self.starting_force + 250
            self.enemy = self.enemy.replace (self.enemy , "Sauron")
        elif self.kind == "ENANO":
            self.power = self.power.replace (self.power, "súper fuerza")
            self.starting_force = self.starting_force + 200
            self.enemy = self.enemy.replace (self.enemy , "balrog")
        elif self.kind == "HOBBIT":
            self.power = self.power.replace (self.power, "sigilo")
            self.starting_force = self.starting_force + 150
            self.enemy = self.enemy.replace (self.enemy , "orco")
        
        print (f"Serás un {self.kind}, tu poder es {self.power} y comenzarás con {self.starting_force} puntos de fuerza. ¡A divertirse en el viaje!")

## Método para defnir el destino
    def change_destiny (self):
        print ("Escoge tu destino, Moria, Gondor, Isengard o Mordor")
        self.destiny = self.destiny.replace(self.destiny, input())#.capitalize      

## Método para definir el desarrollo del viaje
    def travel (self):
        if self.destiny == "MORIA":
            self.enemy= "balrog"
            enemy_force = 60
            if self.kind == "ENANO":
                self.starting_force = self.starting_force + 30
            print ("Fuerza actual ", self.starting_force)
            self.starting_force = self.starting_force - enemy_force

        elif self.destiny == "GONDOR":
            self.enemy = "orco"
            enemy_force = 40
            if self.kind == "HOBBIT":
                self.starting_force = self.starting_force + 30
            print ("Fuerza actual ", self.starting_force)
            self.starting_force = self.starting_force - enemy_force

        elif self.destiny == "ISENGARD":
            self.enemy = "Saruman"
            enemy_force = 100
            if self.kind == "ELFO":
                self.starting_force = self.starting_force + 30
            print ("Fuerza actual ", self.starting_force)
            self.starting_force = self.starting_force - enemy_force

        elif self.destiny == "MORDOR":
            self.enemy = "Sauron"
            enemy_force = 80
            if self.kind == "HUMANO":
                self.starting_force = self.starting_force + 30
                print ("Fuerza actual ", self.starting_force)
            self.starting_force = self.starting_force - enemy_force
        
        print (f"Después de pelear con {self.enemy} quedas con {self.starting_force} puntos de energía")

    ## Método para definir el reto para los personajes
    def challenge (self):
        print ("Deberás escoger el número de uno de los retos propuestos y de acuerdo a tu fuerza pasarás o perderás el podio", 
            "comenzarás con ", self.starting_force, " puntos de fuerza")
        challenge = input ("Los retos son: \n1. Pasar por una escalera destruida. \n2. Cruzar un castillo en ruinas. \n3. Pasar por las minas de los orcos. \n4. Atravesar un campo de lava\n")
        if self.starting_force < 60:
            print ("Perdiste el podio")
        else:
            if challenge == "1":
                self.starting_force = self.starting_force - 40
            elif challenge == "2":
                self.starting_force = self.starting_force - 50
            elif challenge == "3":
                self.starting_force = self.starting_force - 60
            elif challenge == "4":
                self.starting_force = self.starting_force - 70
        print(f"Has pasado el reto con éxito, quedas con {self.starting_force}")
    
    ## Método para definir cómo comen
    def eat (self):
        print ("Hay cuatro tipos de alimentos uno adecuado para cada especie de la comunidad del anillo,", 
            "si aciertas podrás sobrevivir. Escoge un número")
        self.food = " "
        print ("1. Pan de lembas\n2. Pie de manzana\n3. Asado de Mim\n4. Ceviche numenoriano")
        self.food = self.food.replace (self.food , input())#.capitalize
        if self.food == "1" and self.kind == "ELFO":
            self.starting_force = self.starting_force + 30
            print(f"Ahora tienes {self.starting_force} puntos de vida")
        elif self.food == "2" and self.kind == "HOBBIT":
            self.starting_force = self.starting_force + 30
            print(f"Ahora tienes {self.starting_force} puntos de vida")
        elif self.food == "3" and self.kind == "ENANO":
            self.starting_force = self.starting_force + 30
            print(f"Ahora tienes {self.starting_force} puntos de vida")
        elif self.food == "4" and self.kind == "HUMANO":
            self.starting_force = self.starting_force + 30
            print(f"Ahora tienes {self.starting_force} puntos de vida")
        else:
            print ("No sumaste vida")

    ## Método para definir los premios
    def reward (self):
        if self.kind == "ELFO":
            if self.starting_force >= 250:
                print("Ganaste el primer lugar con ", self.starting_force)
            elif self.starting_force > 190 and self.starting_force < 250:
                print("Ganaste el segundo lugar con ", self.starting_force)
            else:
                print("Ganaste el tercer lugar con ", self.starting_force)
        
        if self.kind == "HUMANO":
            if self.starting_force >= 200:
                print("Ganaste el primer lugar con ", self.starting_force)
            elif self.starting_force > 160 and self.starting_force < 200:
                print("Ganaste el segundo lugar con ", self.starting_force)
            else:
                print("Ganaste el tercer lugar con ", self.starting_force)
        
        if self.kind == "ENANO":
            if self.starting_force >= 150:
                print("Ganaste el primer lugar con ", self.starting_force)
            elif self.starting_force > 80 and self.starting_force < 150:
                print("Ganaste el segundo lugar con ", self.starting_force)
            else:
                print("Ganaste el tercer lugar con ", self.starting_force)
                
        if self.kind == "HOBBIT":
            if self.starting_force >= 100:
                print("Ganaste el primer lugar con ", self.starting_force)
            elif self.starting_force > 80 and self.starting_force < 30:
                print("Ganaste el segundo lugar con ", self.starting_force)
            else:
                print("Ganaste el tercer lugar con ", self.starting_force)



player1 = Personaje(input("Escribe el personaje que quieres ser: Elfo, Hobbit, Humano o Enano "))
player1.atributes()
player1.change_destiny()
player1.travel()
player1.challenge()
player1.eat()
player1.reward()