''' O dicionário possue métodos destinados a interação sobre seus elementos,
você consegue interar diretamente sobre o dicionário usando o laço For

* O métodos keys() retonará uma lista de todas as chaves do dicionário,

* O método values() retornará uma lista de todos os valores no dicionário. 

* É possivel fazer o desenpacotamento usando o método itens()

* o método items() retornará cada item em um dicionário, como tuplas em uma lista.

* A lista retornada é uma visão dos itens do dicionário, o que significa que qualquer 
das alterações feitas no dicionário serão refletidas na lista de itens. 

* o método pop() remove o item com o nome de chave especificado: 
'''
print('Interação de Dicionário')

linguas = {'br' : 'português', 'eua' : 'inglês', 'es' : 'espanhol' }
print(linguas)
print()
print('Chave')
for chave in linguas:
    print(chave)

print()

print('Valor')
for chave in linguas.values():
    print(chave)
print()

print('Desenpacotamento')
for chave, valor in linguas.items():
    print(chave, valor)
print()

print(linguas)
print()

print('Removendo valor')
linguas.pop('br')
print(linguas)
print()

