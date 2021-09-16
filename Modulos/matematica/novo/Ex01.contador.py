def contar_caracteres(s):
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem =1
    
    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}:{contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}: {contagem}')
    
if __name__ == '__main__': # teste
    contar_caracteres('Raquel') 
    print()
    contar_caracteres('Lucca')
    print()
    contar_caracteres('Tarcisio')
    

''''
Um contador de elementos em sequências

* Às vezes precisamos realizar a contagem do número de aparições de determinados elementos em uma sequência, 
como uma string ou uma lista. Por

* A solução acima apresentada utiliza uma lista com a função sorted(s) ordenando o caracter como valor para cada letra, 
a quantidade de ocorrências desta. Percorremos a string s letra por letra e, se a letra atual já estiver sendo usada como 
valor ordenado ocorrencias, o valor correspondente a tal letra é incrementado em um (ou seja, encontramos mais uma ocorrência 
da letra na string recebida). Se a letra ainda não estiver aparecendo como valor ordenado, então é criada uma entrada neste 
com a letra sendo usada como valor ordenado e o valor associado contagem = 1. Vamos analisar o teste feito dentro do for

* Esse teste é necessário porque se tentarmos acessar uma chave inexistente de um dicionário, é retornado um KeyError. 
Assim, precisamos testar para verificar se a letra atual já foi anteriormente inserida no dicionário ou não. 
Se foi, daí sim podemos incrementar o valor associado. Se não foi, daí temos que incluir tal valor com o número 1 associado.

'''