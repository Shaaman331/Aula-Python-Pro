'''
Desvio Condional

* Um desvio condional serve para executar uma linha do seu programa
ou algumas linhas quando somente se determinada condição for atendida

* Escopo é a limitação do contexto onde seu programa roda

* Para determinar o Escopo no Python nós usamos a identação'''

idade = 3 
if idade < 18:
    print(17)
    print(16)

if idade < 18:
    print(17)
elif idade < 60:
    print(idade)

idade = 65
if idade < 18:
    print(17)
elif idade < 60:
    print(idade)
else:
    print(65)
    