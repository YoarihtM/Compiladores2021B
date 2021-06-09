# A -> aBa
# B -> bAb
# B -> a

def consume(lista):
    l = lista.copy()
    l.reverse()
    l.pop()
    # print(f'esto es l {l}')
    l1 = l.copy()
    l1.reverse()
    # print(f'esto es l1 {l1}')
    return l1

def A(entrada):
    if entrada[0] == 'a':
        try:
            cons1 = consume(entrada)
            print(f'"a" consumida en A, cadena a evaluar en B({cons1})')
            bSal = B(cons1)
            print(f'regreso de B en A, cadena a consumir: {bSal}')
            try:
                cons2 = consume(bSal)
                print(f'Regla A terminada')
                return cons2
            except:
                print('La cadena no forma parte de la gramatica A3')
                # exit(1)
        except:
            print('La cadena no forma parte de la gramatica A2')
            # exit(1)
    else:
        print('La cadena no forma parte de la gramatica A1')
        # exit(1)

def B(entrada):
    if entrada[0] == 'a':
        print(f'"a" consumida en B, cadena consumida {entrada}')
        return consume(entrada)
    elif entrada[0] == 'b':
        try:
            cons1 = consume(entrada)
            print(f'"b" consumida en B, cadena a evaular en A({cons1})')
            aSal = A(cons1)
            print(f'Regreso de A en B, cadena a consumir: {aSal}')
            try:
                cons2 = consume(aSal)
                print(f'Regla B terminada, cadena consumida {cons2}')
                return cons2
            except:
                print('La cadena no forma parte de la gramatica B3')
                # exit(1)
        except:
            print('La cadena no forma parte de la gramatica B2')
            # exit(1)
    else:
        print('La cadena no forma parte de la gramatica B1')
        # exit(1)

def main():
    cadena = input('Introduce la cadena a evaluar\n')
    lCadena = list(cadena)
    
    A(lCadena)

if __name__ == '__main__':
    main()
