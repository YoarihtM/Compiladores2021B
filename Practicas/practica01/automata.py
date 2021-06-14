def inf2post(cadena):
    operadores = []
    cad_resultado = ''
    
    for i in cadena:
        # print('entrada ', i)
        if i == '(':
            operadores.append(i)
            # print('pila ', operadores)
            # print('resultado', cad_resultado)
            
        elif i == '*':
            try:
                # print('pila ', operadores)
                indice = len(operadores) - 1
                fin_oper = operadores[indice]
                # print('ultimo elemento en la pila', fin_oper)
                
                if fin_oper == '*':
                    fin_oper = operadores.pop()
                    
                    while fin_oper == '*':
                        cad_resultado += fin_oper
                        fin_oper = operadores.pop()
                    
                    operadores.append(i)
                    # print('pila ', operadores)
                    # print('resultado', cad_resultado)
                    
                else:
                    operadores.append(i)
                    # print('pila ', operadores)
                    # print('resultado', cad_resultado)
                    
            except:
                operadores.append(i)
                # print('pila ', operadores)
                # print('resultado', cad_resultado)
                
        elif i == '.' or i == '|':
            
            try:
                
                # print('pila ', operadores)
                indice = len(operadores) - 1
                fin_oper = operadores[indice]
                # print('ultimo elemento en la pila', fin_oper)
                
                if fin_oper == '*' or fin_oper == '|' or fin_oper == '.':
                    fin_oper = operadores.pop()
                    
                    while fin_oper == '*' or fin_oper == '|' or fin_oper == '.':
                        cad_resultado += fin_oper
                        fin_oper = operadores.pop()
                        
                    operadores.append(i)
                    # print('pila ', operadores)
                    # print('resultado', cad_resultado)
                
                else:
                    operadores.append(i)
                    # print('pila ', operadores)
                    # print('resultado', cad_resultado)
            
            except:
                operadores.append(i)
                # print('pila ', operadores)
                # print('resultado', cad_resultado)
                
        elif i == ')':
            # print('pila ', operadores)
            fin_oper = operadores.pop()
            while fin_oper != '(':
                # print('pila ', operadores)
                cad_resultado += fin_oper
                try:
                    fin_oper = operadores.pop()
                except:
                    break
            
            # print('pila ', operadores)
            # print('resultado', cad_resultado)
            
        else:
            # print('pila ', operadores)
            cad_resultado += i
            # print('resultado', cad_resultado)
    
        # print('\n------------------------------------------------------\n')
    
    if len(operadores) != 0:
        # print('fin de la entrada con elementos en pila ', operadores)
        
        for operador in operadores:
            cad_resultado += operador
    #         print('resultado', cad_resultado)
    #         print('')
    # else:
    #     print('fin de la entrada con pila vacía')
    #     print('')
    
    return cad_resultado

def concatenacion(simbolo1, simbolo2, estados):
    ultimo_estado = estados[len(estados)-1]
    print('ultimo estado: ', ultimo_estado)
    ultimo_estado += 1
    estados.append(ultimo_estado)
    
    resultado = str(ultimo_estado) + ' - (' + simbolo1 + ') -> '
    ultimo_estado += 1
    estados.append(ultimo_estado)
    resultado += str(ultimo_estado) + ' - (' + simbolo2 + ') -> '
    ultimo_estado += 1
    estados.append(ultimo_estado)
    resultado += str(ultimo_estado)
    
    return resultado, estados

def eleccion(simbolo1, simbolo2, estados):
    ultimo_estado = estados[len(estados)-1]
    print('ultimo estado: ', ultimo_estado)
    ultimo_estado += 1
    estados.append(ultimo_estado)
    
    resultado = str(ultimo_estado) + ' - ε -> ' + str(ultimo_estado+1) + ' - (' + simbolo1 + ') -> ' + str(ultimo_estado+2) + ' - ε -> ' + str(ultimo_estado+5)
    
    resultado += '\n  \ \n   ε -> ' + str(ultimo_estado+3) + ' - (' + simbolo2 + ') -> ' + str(ultimo_estado+4) + ' - ε -> ' + str(ultimo_estado+5)
    ultimo_estado += 1
    estados.append(ultimo_estado)
    ultimo_estado += 1
    estados.append(ultimo_estado)
    ultimo_estado += 1
    estados.append(ultimo_estado)
    ultimo_estado += 1
    estados.append(ultimo_estado)
    ultimo_estado += 1
    estados.append(ultimo_estado)
    
    return resultado, estados

def construirAutomata(cadena):
    pila = []
    estados = [0]
    automata = ''
    
    for caracter in cadena:
        if caracter == '*':
            print('ciclo')
        elif caracter == '|':
            simb1 = pila.pop()
            simb2 = pila.pop()
            # print(f'eleccion entre: {simb2} y {simb1}')
            elec, estados = eleccion(simb2, simb1, estados)
            pila.append(elec)
            # print()
            # print(elec)
            # print('pila ', pila)
            # print('estados ', estados)
        elif caracter == '.':
            simb1 = pila.pop()
            simb2 = pila.pop()
            # print(f'concatenacion de: {simb2} con {simb1}')
            concat, estados = concatenacion(simb2, simb1, estados)
            pila.append(concat)
            # print()
            # print(concat)
            # print('pila ', pila)
            # print('estados ', estados)
        else:
            pila.append(caracter)
            
    resultado = pila.pop() 
    
    return resultado

def main():
    cadena = input('Ingresa la cadena a evaluar\n\t')
    print('')
    
    postfija = inf2post(cadena)
    print('cadena infija: ', cadena)
    print('cadena postfija: ', postfija)
    print()
    automata = construirAutomata(postfija)
    print(automata)
    print()

if __name__ == '__main__':
    main()
    