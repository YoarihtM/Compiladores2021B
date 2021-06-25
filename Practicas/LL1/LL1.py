class Gramatica():
    def __init__(self):
        self.terminales = []
        self.no_terminales = []
        self.inicial = ''
        self.producciones = []
    
    def setTerminal(self, simbolo):
        self.terminales.append(simbolo)
    
    def setNoTerminal(self, simbolo):
        self.no_terminales.append(simbolo)
    
    def setInicial(self, simbolo):
        self.inicial = simbolo
    
    def setProduccion(self, izq, der):
        produccion = izq + '-' + der
        self.producciones.append(produccion)
    
    def getTerminales(self):
        return self.terminales
    
    def getNoTerminales(self):
        return self.no_terminales
    
    def getInicial(self):
        return self.inicial
    
    def getProduccion(self):
        return self.producciones
    
    def getGramatica(self):
        return self.terminales, self.no_terminales, self.inicial, self.producciones
    
    # def siguiente(self, simbolo):
        
    # def primero(self, produccion):

gram = Gramatica()

activo = True

while activo:
    print('Que deseas realizar?')
        
    opcion = input('1. Introducir simbolo inicial\n2. Introducir terminal\n3. Introducir no terminal\n4. Introducir produccion\n5. Mostrar gramatica\n6. Generar tabla LL(1)\n7. Salir\n\n')
    
    if opcion == '1':
        inicial = input('Introduce tu simbolo inicial\n')
        gram.setInicial(inicial)
        ingresado = gram.getInicial()
        print(f'Simbolo {ingresado} agregado como inicial\n')
    
    elif opcion == '2':
        inicial = input('Introduce el terminal que deseas agregar\n')
        gram.setTerminal(inicial)
        ingresado = gram.getTerminales()
        print('Simbolos terminales agregados hasta ahora ', ingresado)
        print()
        
    elif opcion == '3':
        inicial = input('Introduce el no terminal que deseas agregar\n')
        gram.setNoTerminal(inicial)
        ingresado = gram.getNoTerminales()
        print('Simbolos terminales agregados hasta ahora ', ingresado)
        
    elif opcion == '4':
        izq = input('Introduce el simbolo del lado izquierdo\n')
        der = input('Introduce el simbolo del lado derecho\n')
        gram.setProduccion(izq, der)
        ingresado = gram.getProduccion()
        print('Producciones agregadas hasta ahora ', ingresado)
        
    elif opcion == '5':
        terminales, no_terminales, inicial, producciones = gram.getGramatica()
        print('Simbolo inicial: ', inicial)
        print('Simbolos terminales: ', terminales)
        print('Simbolos no terminales: ', no_terminales)
        print('Producciones:')
        for produccion in producciones:
            print(produccion)
        
    # elif opcion == '6':
    
    elif opcion == '7':
        activo = False
    else:
        print('Opcion no valida, intenta de nuevo')