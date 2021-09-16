'''
Parâmetros e função 

* Para garantir que uma string será exibida conforme o esperado, 
podemos formatar o resultado com o método format().

Funções

* Uma função é um bloco de código que só é executado quando é chamado.

* Você pode passar dados, conhecidos como parâmetros, para uma função.

* Uma função pode retornar dados como resultado. 

Criação de uma função 

* Em Python, uma função é definida usando a palavra-chave def :

* Para chamar uma função, use o nome da função seguido por parênteses: 

Argumentos

* As informações podem ser passadas para funções como argumentos.

* Os argumentos são especificados após o nome da função, entre parênteses. 
Você pode adicionar quantos argumentos quiser, apenas separe-os com uma vírgula. 
'''
print('===Parametros e função===')

nome = 'Tarcisio'
print('Criando uma função')
def ola(nome):
    return f'Olá {nome}'

print(ola(nome))
print()
print(ola('Lucca'))
print()


def my_function():
    print('Hello from a function')
my_function()
print()

print('Argumentos')

def ola(nome, sobrenome):
    return f'Olá {nome} {sobrenome}'

print(ola('Lucca', 'Marzanno'))
print()

print('Parametros por justa posição')
def ola(nome, sobrenome='Souza'):
    return f'Olá {nome} {sobrenome}'
print(ola('Tarcisio'))
print()

print(ola('Lucca','Souza'))
print()

def ola(nome, sobrenome='Marzanno', idade=3):
    return f'Olá {nome} {sobrenome} {idade}'
print(ola('Lucca'))
print()

print(ola('Tarcisio', 'Souza', '31'))
print()

print(ola('Lucca', idade= 3))
print()

print(ola('Tarcisio', idade=31, sobrenome='Cordeiro'))

