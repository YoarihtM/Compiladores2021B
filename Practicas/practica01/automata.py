class Transicion:
    __nodoOrigen = 0
    __nodoDestino = 1
    __caracterTransicion = ''
    
    def getOrigen(self):
        return self.__nodoOrigen

    def getDestino(self):
        return self.__nodoDestino
    
    def getCaracter(self):
        return self.__caracterTransicion
    
    def setOrigen(self, origen):
        self.__nodoOrigen = origen
    
    def setDestino(self, destino):
        self.__nodoDestino = destino
    
    def setCaracter(self, caracter):
        self.__caracterTransicion = caracter

class TransicionEpsilon(Transicion):
    def __init__(self, origen, destino):
        self.setOrigen(origen)
        self.setDestino(destino)
        self.setCaracter('ε')

    def getTransicion(self):
        return self.getOrigen(), self.getDestino(), self.getCaracter()

class TransicionSimple(Transicion):
    def __init__(self, origen, destino, caracter):
        self.setOrigen(origen)
        self.setDestino(destino)
        self.setCaracter(caracter)
    
    def getTransicion(self):
        return self.getOrigen(), self.getDestino(), self.getCaracter()

class TransicionEstrella(Transicion):
    __destinoBucle = 0
    __caracterSalida = 'ε'

    def getSalida(self):
        return self.__caracterSalida
    
    def getDestinoBucle(self):
        return self.__destinoBucle

    def getTransicion(self):
        return self.getOrigen(), self.getDestino(), self.getDestinoBucle(), self.getCaracter(), self.getSalida()

    def setDestinoBucle(self):
        self.__destinoBucle = self.getOrigen()
    
    def setTransicion(self, origen, expresion):
        self.setOrigen(origen)

