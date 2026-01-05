# Nesta seção, você aprendera a falar com um computador:
# voce vai se familiarizar, realizar conversôes de tipo
# e aprender a usar operadores de string!

print("Conta-me qualquer coisa...")
anything = input()
print("hum..", anything, "...Realmente?")

#exemplo modificado

anything = input("Conta-me qualquer coisa...")
print("Hum...", anything, "...Realmente?")

#anything = input("Digite um número: ")
#something = anything ** 2.0
#print(anything, "elevando a 2 é", something)

#Conversão de tipo de conversão isso é muito simples usa um argumento converte-lo em um número inteiro,
# se falhar, o programa inteiro tambem falhará
# Não é necessario de usar nenhuma variavel como armazenamento intermediario
# vóce pode imaginar como a string inserida pelo usuario flui de input() para print()?
# tente executar o código modificado. Não se esqueça de inserir um número valido.
# Algums valores diferentes, pequeno e grande, negativo e positivo. Zero também.

anything = float(input("digite um número: "))
something = anything ** 2.0
print(anything, "elevando a 2 é", something)

#Ter uma equipe composta por três abre muitas novas possibilidades
#Voce podera escrever programas completos, aceitando dados de forma de número processando-os e exibindo os resultados
# Obviamente, esses programas serão muito primitivos e não muito utilizaveis,
# pois não podem tomar decisões e, portanto, não são capazes de reagir de forma diferente de uma situação!
# mostraremos como superar isso em breve
#Vamos mostrar um programa do programador anterior para o usuario encontrar o comprimento de uma hipotenusa.
# vamos executa-lo e torna-lo capaz de ler os comprimentos das pernas do console

leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2+leg_b**2)** .5
print("O comprimento da hipotenusa é", hypo)

# O programa solicitado ao usuario o comprimento de ambas as pernas, avalia a hipotenusa e imprime o resultado, insera alguns valores negativos.
#O programa infelizmente, não reage a esse erro obvio. Vamos igorar essa fraqueza por enquanto
#observe que, no programa que voce pode ver no editor, a variavel hypo é usada para apenas um objetivo - para salvar o valor calculado entre a execução da linha do código adjacente
# Como a função print() aceita uma expressão como seu argumento, voce pode remover a variavel do código.

leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é ", (leg_a**2+leg_b**2)**.5)


#Hora de voltar a operadores de strigs aritmeticos
#queremos mostrar que eles tem uma segunda função, eles são capazes de fazer mais do que apenas adicionar e multiplicar
#ja vimos eles em ação, onde seus argumentos são números(flutuantes ou números inteiros, não importa)
#Embora de uma forma muito expecifica!


#Operador de concatenação string+string


#Ela simplismente concatena (cola) duas sequencias de caracteres em uma, como seu irmão aritmetico, ele pode ser usado mais de uma vez em uma expressão e, nesse contexto, se comporta de acordo com a ligação do lado esquerdo
#Não é comutativo "ab" +ba" não é o mesmo que "ba"+"ab"
#não se esqueça - se voce quiser um sinal de + seja um concatenador, não um somador, certifique-se de que ambos os argumentos sejam cadeias

fnam = input("Posso ter seu primeiro nome por favor? ")
lnam = input("Posso ter seu sobrenome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é"+ fnam +" "+lnam+".")

#print para os argumentos da palavra concaternar strings de construa a saida de uma maneira mais precisa para a uma função do argumento de palavra-chave
#replicação
#string * number
#nunber * string

#Ele replica a string o mesmo número as vezes especificado pelo número.
#lembre-se este simples programa "desenha" um retãngulo, fazendo uso de um antigo operador (+) em um novo papel de programador!
print("+" +10 * "-"+"+")
print(("|"+" "*10+"|\n")*5, end="")
print("+"+10*"-" + "+")
print("uma string vazia de um retangulo sem fnam sobrenome")

#observe como usamos os parenteses na segunda linha do código, tente criar outras formas ou criar sua propria arte!

#Programa de ângulo reto" novamente:

leg_a= float(input("Insira o comprimento da primeira perna: "))
leg_b= float(input("Insira o comprimento da sugunda perna: "))
print("O comprimento da hipotenusa é " + str((leg_a**2 +leg_b**2)** .5))

#nos modificamos um pouco para mostrar como a função str() funciona. Graças a isso, podemos passar o resultado inteiro para a função, voce fez alguns avanços importantes no caminho para a programação!
# talvez voce não consiga proteger o código de um usuario que deseja dividir por zero.
#não se preocuper com isso por enquanto
#teste seu códigob- ele produz os resultados esperados?
#Não mostraremos nenhum resultado de test - isso seria muito simples.

print("\nIsso ~´e tudo, pessoal!")

#o resultado deve ser atribuido a y, tenha cuidado - observe os operadores e mantenha suas prioridades em mente.
#Voce usa variaveis adicionais para encurtar a expressão(mas não é necessario). teste seu código com cuidado.

#y = 0.600000000000000001
#exemplo de saida sai 10

#exemplo de entrada 100
#exemplo de saida com y = 0.000009090199990
#-5
#y = -0.1925

#x = float(input("Digite o valor para x: "))
#escreva seu código aqui.
#print("y =", y)

x = float(input("digite o valor para x: "))
y = 1./(x - 1./(x +1./(x+1./x)))
print("y=",y)

print(1//2*3)

#Essa função envia dados para o console, enquanto a função input() obtem
#dados do console
#a função input() vem com um parametro opcional a string de prompt. Ele permite que voce escreva uma mensagem antes da entrada do usuario

name = input("Digite seu nome: ")
print("Olá," + name + ".Prazer em conhecê-lo!")

#quando a função input() é chamada, o pluxo do programa é interrompido, o simbolo de prompt fica piscando (ele solicita que o usuario tome medidas quando o console for alternado para o modo de entrada)
#até que o usuario tenha inserido uma entrada e/ou pressionado o Enter chave

#Observação, você pode testar a funcionalidade da função imput() em seu escopo completo
#localmente em sua máquina. por motivos de otimização de recursos, limitamos o tempo máximo de execução do programa no Edube a alguns segundos. Vá para sandbox, copie e cole o snippet acima, execute o programa e não faça nada. apenas espere alguns segundos para ver o que acontece.
#seu programa deve ser interrompido automaticamente apòs um breve momento. Agora abra a IDLE e execute o mesmo programa. você consegui ver a diferencia no programa!
#dica do programador: o recurso mencionado acima da função input() pode ser usado para solicitar que o usuario encerre um programa


name = input("Digite seu nome: ")
print("Olá, " + name +". Prazer em conhecê-lo!")

print("\nPressione Enter para finalizar o programa!")
input()
print("O FIM.")

#O resultado da função é uma string. você pode adicionar strings uma ás outras usando o operador de concatenação (+)

num_1 = input("Digite o primeiro número: ") #Digite 12
num_2 = input("Digite o segundo número: ") #Digite 21

print(num_1 + num_2)# o programador faz retorna 1221

#Você pode multiplicar cadeias(* - replicação), por exemplo:

my_input = input("Enter something: ")# Exemplo de entrada : Hello
print(my_input * 3)

#Teste a seção da função do programa!

x = int(input("Digite um número: ")) #O usuario digite 2
print(x * "5")

#Qual a saida esperada para esse trecho a seguir?
x = input("Digite um número: ") #O usuario digita 2
print(type(x))


#Operadores básicos
#Um operador é um simbolo da linguagem de programação, capaz de operar com os valores esperados!
#Por exemplo, assim como ná aritmétioca, o sinal de (+) (mais) é o operador que é capaz de
#adicionar dois números, dando o resultado da adição

#Na seção, aprenderemos sobre declarações e como usa-las para tomar decisôes, um programador cria um prgrama e o programa faz perguntas para o usuario!
#Um computador executa o programa e fornece as respostas. O programa deve ser
#capaz de reagir de acordo com as respostas recebidas.

#Felizmente, os computadores sabem apenas dois tipos de respostas:
#Sim, isso é verdade
#Não, isso é falso

#Você nunca receberá uma resposta como Dexe-me pensar...,,Não sei, ou provalvemente sim, mas não tenho certeza.

#Para fazer perguntas, usa um conjunto de operadores muito especiais
#vamos examina-los um após o outro, ilustrando seus efeitos em alguns exemplos simples.

#pergunta: os dois valores são iguais?

# = é um operador de atribuição, por exemplo, a = b atribui a com o valor de b;
#== A pergunta é: esses valores são iguais? então a ==b compara a and b
# ela precisa de dois argumentos e verificar se são iguais.
#Para verificar essa pergunta, você usa o operador == (igual igual)
#Operadores igualdade: o operador de igualdade(==)
#O operador == (igual a) compara valores de dois operandos. Se forem iguais, o resultado da comparação é True que é verdadeiro. Se eles não forem iguais, o resultado da comparação é False
#qual o resultado da comparação a variavel vai ser (var == 0)
#Observe que não podemos encontrar a resposta se não soubermos qual valor está armazenado no momento na variavel var.
#se a variavel tiver sido alterada varias vezes durante a execução do programa ou o valor inicial for inserido no console
#A resposta para essa pergunta pode ser dada apenas pelo python e apenas no tempo de execução!
#agora imagine um programador que sofre de insônia e precisa contar ovelhar preto e branco separadamente, desde que haja exatamente o dobro da ovelha negra que a branca

#black_sheep == 2* white_sheep

#execute o código para verificar se você está certo!

#desigualdade: o operador de desigualdade(!=)
#O operador !=(Não é igual a) tambèm compara os valores de dois operadndos. aqui está a diferença: se eles são iguais, o resultado da comparação false. se eles não forem iguais, o resultado da comparação é True verdadeiro!

var = 0 #Atribuindo 0 a var
print(var != 0)

var = 1 # Atribuindo 1 a var
print(var != 0)

#Utilização da resposta de uma operação de comparação) que você obtem do computador?
#Há pelo menos duas possibilidades: primeiro, você pode memorizá-la(armazená-la em uma variavel inteira ou variavel) e usa-la posteiromente. VComo você faz isso?
# bem , você usa uma variavel arbitraria como essa:

#answer = number_of_lions >= number_of_lionesses

#A segunda possibilidade é mais conveniente e muito mais comum:
# você pode usar a resposta para tomar uma decisão sobre o futuro do programa
#Voce precisa de uma instrução especial para esse fim de variavel no software, e nós a discutiremos em breve.
#agora utilizar as tabelas de prioridades e colocar todos os novos operadores nela.

#1   +,-
#2   **
#3   *,/,//,%
#4   +,-
#5   <,<=,>,>=
#6   ==,!=


#você precisa saber fazer perguntas em python, mas ainda não sabe como fazer uso racional das respostas. você precisa ter um mecanismo que permita quer você faça algo se uma condição for atendida, e não faça se não for.
#Na palavra se o tempo estiver bom, vamos dar um passeio, caso contrário, vamos a um teatro!
#agora sabemos o que faremos se as condições forem sobre a variavel programador de software forem atendidas, e o que faremos se não tudo seguir nosso camanho.
#Em outras palavras, temos um "Plano B"
#Se o tempo estiver ruim sabemos apenas que não vamos a o ar livre
# As instrução colocada após é outra if
#Leia os planejamento bom para o domingo de desenvolvedor ou programador de software!

#if the_weather_is_good:
#    if nice_restaurant_is_found:
#        have_lunch()
#    else:
#        eat_a_sandiwich()
#else:
#    if tickets_are_available:
#        go_to_the_theater()
#    else:
#        go_shopping()

#Analise de amostras de código
#agora vamos mostrar alguns programas simples, mas completos. Não vamos explicar detalhamente, porque consideramos(os nomes das variaveis) dentro do cógigo como guias suficientes
#todos os programas resolvem o mesmo problema: no desenvolvimento encontram o maior de vários números e o imprimem.

#como identificar o maior número entre dois
#system programmer software

#ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

#escolha o número maior
if number1 > number2:
    larger_number = number1
else:
    langer_number = number2

#Imprimir o resultado
print("O maior número é:", larger_number)

# lê dois valores inteiros, os compara e descobre qual é o maior.

#Algo mostrar um reculso interessante - veja o código-deve ser bem claro um fato intrigante:

#Lêr dois números
number1 = input(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

#Escolha o número maior
if number1 > number2: larger_number = number1
else: larger_number = number2

#imprimir o resultado
print("O maior número é:", larger_number)

#Em nosso programas futuros, mas definitivamente vale a pena saber se você deseja ler e enteder os programas das outras pessoas igual a operadores!

#não há outras diferenças no código.

#Exemplo vamos encontrar o maior de Três

#Leia três números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

#Assumimos temporariamente que o primeiro número
#é o maior deles
#Em breve verificamos isso.
largest_number = number1

#Nós verificamos se o segundo número é maior que o maior_número atual
#e atualize o maior_nùmero, se necessário.
if number2 > largest_number:
    largest_number = number2

# Nós verificamos se o terceiro número é maior que o maior_número atual
#e atualize o maior_número, se necessàrio verificar em breve!
if number3 > largest_number:
    larges_number = number3

#Imprimir o resultado
print("O maior número é:", largest_number)

#Esse teste significativamente mais simples do que tentar encontrar o maior número de um só vez, ao comparar todos os pares possiveis de números(ou seja, primeiro com o segundo, segundo com o terceiro, terceiro com  o primeiro).

#Pseudocòdigo, loops system
