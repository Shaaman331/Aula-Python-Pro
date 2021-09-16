'''
Dicionário

Você pode acessar os itens de um dicionário referindo-se ao nome 
da chave, entre colchetes:

* O método chamado get()isso lhe dará o mesmo resultado:, no método
get você pode passar um segundo paramêtro que se ele não encontrar 
a chave retorna um valor padrão. 

* Para determinar se uma chave especificada está presente em um dicionário,
 use o in palavra-chave: 
'''
print('=====Dicionário====')
linguas = {'br': 'português', 'eua' : 'inglês'}
print(type(linguas))
print(linguas)
print(linguas['br'])
print(linguas['eua'])
print()

print('Método get')
print(linguas.get('es'))
x = linguas.get('es')
print(x)
print(linguas.get('es','não definida'))
x = linguas.get('br', 'não definida')
print(x)
print()

print('Método in')

linguas_x = {'br': 'português', 'eua' : 'inglês'}
print(linguas_x)
print()

if 'br' in linguas_x:
    print('True')
else:
    print('False')
print()

x = list(range(10))
print(x)

if 6 in x:
    print('True')
else:
    print('False')
print()

if 11 in x:
    print('True')
else:
    print('False')
print()



