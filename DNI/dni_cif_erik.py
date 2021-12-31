

class Dni:
    def __init__(self, cadena=""):
        self.dni = cadena
        self.numeroSano = False
        self.tabla = {0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D', 10: 'X', 11: 'B', 12: 'N', 13: 'J',
                      14: 'Z', 15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C', 21: 'K', 22: 'E'}

    ### Interfaz Pública ###

    def setDni(self, nuevo_dni):
        self.dni = nuevo_dni

    def getDni(self):
        return self.dni

    def setnumeroSano(self, valor):
        self.numeroSano = valor

    def getnumeroSano(self):
        return self.numeroSano

    def setLetra_dni(self, letra):
        self.dni = self.dni[:-1] + letra

    def getLetra_dni(self):
        return self.dni

    ### Interfaz Privada ###

    def dni_longitud_valida(self):
        return len(self.dni) == 9

    def calcular_letra(self):
        numero_letra = self.dni_parte_numerica() % 23
        return self.tabla[numero_letra]

    def dni_valido(self):
        self.setnumeroSano(self.dni_longitud_valida and self.numero_valido())
        return self.dni[:-1] + self.calcular_letra()

    def validacion(self):
        return self.getnumeroSano()

    def letra_valida(self):
        letra_dni = self.dni[-1]
        return self.calcular_letra() == letra_dni

    def letra_dni(self):
        return self.dni[-1]

    def numero_valido(self):
        return self.dni[:-1].isdigit()

    def dni_parte_numerica(self):
        if self.getnumeroSano():
            return int(self.dni[:-1])
        else:
            return False


if __name__ == '__main__':

    import math
    import random

    ### Casos test ALEATORIOS ###

    casosTest = []
    numeroCasos = 25

    for i in range(1, numeroCasos + 1):
        caso = ""
        for j in range(1, 9):
            # random.randrange(start, stop[, step])
            # numeroAleatorio = random.randint(0, 9)
            # ASCII 48-57 = 0-9    65-90 = A-Z   58 = ":"
            # generamos un numero aleatorio entre 48 y 58
            caracterAscii = random.randrange(48, 58 + 1, 1)
            # convertimos el numero ASCII a caracter. chr() toma el argumento como codigo ASCII de un caracter
            caso = caso + chr(caracterAscii)
        # en la ultima posicion añado una letra A-Z
        caso = caso + chr(random.randrange(65, 90 + 1, 1))
        casosTest = casosTest + [caso]

    print(casosTest)

    for dni in casosTest:
        objeto = Dni(dni)
        print(objeto.getDni())
        objeto.letra_valida()
        print('dni deberia ser', objeto.dni_valido())
        # print(objeto.calcularLetra())
        print('Letra deberia ser', objeto.calcular_letra())
        print('La letra es', objeto.letra_dni())
        print('El DNI es --->', objeto.validacion())

    ### Casos test OK ###

    casosTest = [  # casos OK
        "78484464T", "72376173A", "01817200Q", "95882054E", "63587725Q",
        "26861694V", "21616083Q", "26868974Y", "40135330P", "89044648X",
        "80117501Z", "34168723S", "76857238R", "66714505S", "66499420A"]

    print("\n #### CASOS OK #### \n")

    for dni in casosTest:
        objeto = Dni(dni)
        print(objeto.getDni())
        objeto.letra_valida()
        print('dni deberia ser --->', objeto.dni_valido())
        # print(objeto.calcularLetra())
        print('Letra deberia ser --->', objeto.calcular_letra())
        print('La letra es -->', objeto.letra_dni())
        print('El DNI es --->', objeto.validacion())
