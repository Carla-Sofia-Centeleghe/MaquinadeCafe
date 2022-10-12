# Test para revisar la cafetera
# Carla S. Centeleghe
import unittest
from Maquina import *

class TestMaquina(unittest.TestCase):
    #test para el cafe solo
    def testCafeSolo_1(self):
        tipo_cafe = Tipos_Cafe()
        tipo_cafe.ingredientes.almacenar(10, 10, 10, 10, 10, 10)
        self.assertEqual(tipo_cafe.preparacionCafeSolo(), True)
    
    def testErrorCafe_2(self):
        tipo_cafe = Tipos_Cafe()
        self.assertEqual(tipo_cafe.preparacionCafeSolo(), False)

    #test para el cafe dulce
    def testCafeDulce_3(self):
        tipo_cafe = Tipos_Cafe()
        tipo_cafe.ingredientes.almacenar(20, 20, 20, 20, 20, 20)
        self.assertEqual(tipo_cafe.preparacionCafeDulce(), True)

    def testErrorCafeDulce_4(self):
        tipo_cafe = Tipos_Cafe()
        self.assertEqual(tipo_cafe.preparacionCafeDulce(), False)

    #test para el cafe doble
    def testCafeDoble_5(self):
        tipo_cafe = Tipos_Cafe()
        tipo_cafe.ingredientes.almacenar(15, 15, 15, 15, 15, 15)
        self.assertEqual(tipo_cafe.preparacionCafeDoble(), True)
    
    def testErrorCafeDoble_6(self):
        tipo_cafe = Tipos_Cafe()
        self.assertEqual(tipo_cafe.preparacionCafeDoble(), False)

     #test para el cafe con leche
    def testCafeConLeche_7(self):
        tipo_cafe = Tipos_Cafe()
        tipo_cafe.ingredientes.almacenar(25, 25, 25, 25, 25, 25)
        self.assertEqual(tipo_cafe.preparacionCafeConLeche(), True)

    def testCafeConLeche_8(self):
        tipo_cafe = Tipos_Cafe()
        self.assertEqual(tipo_cafe.preparacionCafeConLeche(), False)

    #test para el te
    def testTe_9(self):
        tipo_cafe = Tipos_Cafe()
        tipo_cafe.ingredientes.almacenar(30, 30, 30, 30, 30, 30)
        self.assertEqual(tipo_cafe.preparacionTe(), True)

    def testErrorTe_10(self):
        tipo_cafe = Tipos_Cafe()
        self.assertEqual(tipo_cafe.preparacionTe(), False)

    #test para el chcolate
    def testTe_11(self):
        tipo_cafe = Tipos_Cafe()
        tipo_cafe.ingredientes.almacenar(35, 35, 35, 35, 35, 35)
        self.assertEqual(tipo_cafe.preparacionChocolate(), True)

    def testErrorChocolate_12(self):
        tipo_cafe = Tipos_Cafe()
        self.assertEqual(tipo_cafe.preparacionChocolate(), False)

    #test para el chcolate con leche y azucar
    def testChocolate_con_leche_y_azucar_13(self):
        tipo_cafe = Tipos_Cafe()
        tipo_cafe.ingredientes.almacenar(40, 40, 40, 35, 40, 40)
        self.assertEqual(tipo_cafe.preparacionChocolate_con_leche_y_azucar(), True)
    
    def testErrorChocolate_con_leche_y_azucar_14(self):
        tipo_cafe = Tipos_Cafe()
        tipo_cafe.ingredientes.almacenar(3, 3, 3, 3, 3, 3)
        self.assertEqual(
            tipo_cafe.preparacionChocolate_con_leche_y_azucar(), False)



if __name__=='__main__':
    unittest.main()