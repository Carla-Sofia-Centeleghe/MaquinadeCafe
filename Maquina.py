# Cafetera
# Carla S. Centeleghe

#Clase de Reserva de Ingredientes inicializada en vacio
class Ingredientes:
    def __init__(self) -> None:
        self.azucar = 0
        self.agua = 0
        self.hierbas = 0
        self.cafe = 0
        self.chocolate = 0
        self.leche = 0
    
    #Almacenamiento de Ingredientes
    def almacenar(self, azucar:int, agua:int, hierbas:int, cafe:int, chocolate:int, leche:int):
        self.azucar += azucar
        self.agua += agua
        self.hierbas += hierbas
        self.cafe += cafe
        self.chocolate += chocolate
        self.leche += leche

#Clase de Preparacion de Cafes
class Tipos_Cafe:
    def __init__(self) -> None:
        self.ingredientes = Ingredientes()

    #Funcion que hace cafesolo
    def preparacionCafeSolo(self):
        ingredienteCafe = 3 #Indica la cantidad del ingrediente utiliza
        if self.ingredientes.cafe > 3:
            self.ingredientes.cafe - ingredienteCafe
            return True
        return False

    #Funcion que hace cafe dulce
    def preparacionCafeDulce(self):
        ingredienteCafe = 3  # Indica la cantidad del ingrediente utiliza
        ingredienteAzucar = 5
        if self.ingredientes.cafe > 3 and self.ingredientes.azucar > 5: #son dos variables las que resto
            self.ingredientes.cafe - ingredienteCafe
            self.ingredientes.azucar - ingredienteAzucar
            return True
        return False

    #Funcion que hace cafedoble
    def preparacionCafeDoble(self):
        ingredienteCafe = 6  # Indica la cantidad del ingrediente utiliza
        if self.ingredientes.cafe > 6:
            self.ingredientes.cafe - ingredienteCafe
            return True
        return False

    #Funcion que hace cafe con leche
    def preparacionCafeConLeche(self):
        ingredienteCafe = 3  # Indica la cantidad del ingrediente utiliza
        ingredienteLeche = 2
        if self.ingredientes.cafe > 3 and self.ingredientes.leche > 2:  # son dos variables las que resto
            self.ingredientes.cafe - ingredienteCafe
            self.ingredientes.leche - ingredienteLeche
            return True
        return False
    
    #Funcion que hace te
    def preparacionTe(self):
        ingredienteHierbas = 2  # Indica la cantidad del ingrediente utiliza
        ingredienteAgua = 10
        if self.ingredientes.hierbas > 2 and self.ingredientes.agua > 10:  # son dos variables las que resto
            self.ingredientes.hierbas - ingredienteHierbas
            self.ingredientes.agua - ingredienteAgua
            return True
        return False

    #Funcion que hace chocolate
    def preparacionChocolate(self):
        ingredienteChocolate = 7  # Indica la cantidad del ingrediente utiliza
        if self.ingredientes.chocolate > 7:
            self.ingredientes.chocolate - ingredienteChocolate
            return True
        return False

    #Funcion que hace choclate con leche y dulce
    def preparacionChocolate_con_leche_y_azucar(self):
        ingredienteChocolate = 5  # Indica la cantidad del ingrediente utiliza
        ingredienteLeche = 2
        ingredienteAzucar = 3
        if self.ingredientes.chocolate > 5 and self.ingredientes.leche > 2 and self.ingredientes.azucar > 3:  # son tres variables las que resto
            self.ingredientes.chocolate - ingredienteChocolate
            self.ingredientes.leche - ingredienteLeche
            self.ingredientes.azucar - ingredienteAzucar
            return True
        return False



if __name__ == '__main__':
    cafe = Tipos_Cafe()