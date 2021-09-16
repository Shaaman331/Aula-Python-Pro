''' 
FUNÇÕES
* Uma função é um bloco de código que só é executado quando é chamado.

* Você pode passar dados, conhecidos como parâmetros, para uma função.

* Uma função pode retornar dados como resultado.

* Em Python, uma função é definida usando o def palavra-chave: 

ARGUMENTOS

* As informações podem ser passadas para funções como argumentos.

* Os argumentos são especificados após o nome da função, entre parênteses. 
Você pode adicionar quantos argumentos quiser, apenas separe-os com uma vírgula. 

Parametros ou Argumentos

*Os termos parâmetro e argumento podem ser usados ​​para a mesma coisa: informações que são passadas para uma função.

*Da perspectiva de uma função:

* Um parâmetro é a variável listada entre parênteses na definição da função.

* Um argumento é o valor enviado para a função quando ela é chamada.

'''
def soma(*parcelas):
    print(parcelas)
    print(type(parcelas))

soma(1)
print()

def soma(*parcelas):
    aux = 0
    for valor in parcelas:
        aux += valor
    return aux

print(soma())

print(soma(2))

print(soma(2, 4, 10))

print(type,(soma))
print()

def f(**kwargs):
    print(kwargs)
    print(type(kwargs))

f()
f(nome = 'Tarcisio', sobrenome = 'Souza')
print()


args = (1, 2, 3)
kwargs = {nome :  'Tarcisio', sobrenome : 'Souza'}

def f(*args, **kargs):
    print(args)
    print(kwargs)

f()
print()
f(1, 2, nome = 'Tarcisio', sobrenome = 'Souza')
