'''
Lista e Range

* Lista em Python pode ser definido como um vetor dinâmico 
entre as linguagens, sigfica que você pode adicionar e remover 
elementos da lista

* Range permite difinir uma progressão aritimética na hora de 
criar uma lista

* Sort O método sort () classifica a lista em ordem crescente por padrão. 

* Pop método que remove um elemento da lista

* Append método que insere elemento

* Extend método que  insere vários elementos ao final da lista

* Split função que separa os elementos por lista

* Strings e lista possuem uma semelhança muito grande 

* Join método que pega todos os itens em um iterável e os une em uma string.

Uma string deve ser especificada como separador. 



'''

a = [1, 2, 3]
print(a)
print(type([]))

lista = list(range(10))
print(lista)

lista = list(range(1, 10, 2))
print(lista)

lista = list(range(10, 0, -2))
print(lista)

lista.sort()
print(lista)

lista.append(12)
print(lista)
 
 
lista.extend([12, 13])
print(lista)

lista+[16, 18]
print(lista)

a = ('Python Pro'.split())
print(a)

b = ('Python-Pro'.split('-'))
print(b)

lista = ['Python', 'Pro']
x = "#".join(lista)
print(x)


