''''
Tuplas são imutaveis, significa que você não vai conseguir inserir 
ou remover itens dela



'''
tpl = (1, 2)
print(type(tpl))

x = tuple(range(6))
print(x)

z = 2 + 3 + 4
print(z)

w = (2 + 3) * 4
print(z)

print("Desempacotamento")

registro = ('Tarcisio, 31 ')
registro_2 = ('Lucca. 3')
x = registro + registro_2
print(x)

y =id(registro)
print(y)

z = id(registro_2)
print(z)

