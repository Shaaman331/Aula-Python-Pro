def contar_caracteres(s):
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    resultado = {}

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1 
        else:
            resultado[caracter_anterior] = contagem
            caracter_anterior = caracter
            contagem = 1 
    resultado[caracter_anterior] = contagem

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('Tarcisio'))
    print()
    print(contar_caracteres('Lucca'))

print()

print('Forma Simplificada')

def contar_caracteres(s):
    
    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter]= contagem

    return resultado 


if __name__ == '__main__':
    print(contar_caracteres('Marcola'))
    print()
    print(contar_caracteres('Raquel'))


