from  matematica.base.mat import soma as s
print(s(4, 5))

'''
Pacotes

* Pacotes são pastas nas quais você irá colocar módulos para 
organizar seus programas

* Podemos renomear o pacote para inportar o módulo, no entando devemos fazer a 
referência ultlizando o ponto para separar o pacote .mat

* Ultilizamos um atalho para importar o pacote Python usamos o from

from matematica import mat
print(mat.soma)

* Veja que referênciamos o modulo mat 

* Pode acontece que você tenha 2 nomes de módulos diferentes mais que tenha a mesma denominação
Você pode alterar o apelido pelo qual vai ser chamada dentro desse módulo colocando o as s

from matematica.mat import soma as s
print(soma(4 , 5))

* Os pacotes te ajudam a organizar seu código e eles podem estar em qualquer nivel, 
criamos um pacote aninhado dentro do pacote mátematica, nomeamos de base, porém 
precisamos refatorar o códico para ser incluído transformando assim em:

from matematica.base.mat import soma as s
print(soma(4, 5))
'''