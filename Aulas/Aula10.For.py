'''
For 
* Um loop for é usado para iterar sobre uma sequência (que é uma lista, uma tupla, um dicionário, 
um conjunto ou uma string).

* Isso é menos parecido com a palavra-chave for em outras linguagens de programação e funciona mais 
como um método iterador encontrado em outras linguagens de programação orientadas a objetos.

* Com o loop for, podemos executar um conjunto de instruções, uma vez para cada item em uma lista,
tupla, conjunto etc.
'''

nome = "Tarcisio"
for v in nome:
    print(v)
print()

for i in range(len(nome)):
    print(i, nome[i])
print()

for i, v in enumerate(nome):
    print(i, nome[i])
print()

for i, v in enumerate(nome):
    print(i, v)
print()


