'''
Módulos 

* Ao sair e entrar de novo no interpretador Python, as definições anteriores (funções e variáveis)
são perdidas. Portanto, se quiser escrever um programa maior, será mais eficiente usar um 
editor de texto para preparar as entradas para o interpretador, e executá-lo usando o 
arquivo como entrada. Isso é conhecido como criar um script. 

* Se o programa se torna ainda maior, é uma boa prática dividi-lo em arquivos menores, 
para facilitar a manutenção. Também é preferível usar um arquivo separado para uma 
função que você escreveria em vários programas diferentes, para não copiar a definição 
de função em cada um deles.

* Para permitir isso, o Python tem uma maneira de colocar as definições em um arquivo e então 
usá-las em um script ou em uma execução interativa do interpretador. Tal arquivo é chamado 
de módulo; definições de um módulo podem ser importadas para outros módulos, ou para o módulo 
principal (a coleção de variáveis a que você tem acesso num script executado como um programa 
e no modo calculadora).

* Um módulo é um arquivo contendo definições e instruções Python. O nome do arquivo é o nome do 
módulo acrescido do sufixo .py. Dentro de um módulo, o nome do módulo (como uma string) está 
disponível como o valor da variável global __name__. 
'''

"Módulos que contem operações matemáticas"
def soma(parcela, parcela_2):

    return parcela + parcela_2

if __name__ == '__main__':
    #Testando a função soma
    print(soma(1, 2)) # imprimindo 


