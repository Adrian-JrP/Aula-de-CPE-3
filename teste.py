letras=['a', 'b', 'c', 'd','e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letras.index('m') # o index mostra a posição de alguma coisa na lista
for indice,letra in enumerate(letras):
    print(indice, "-", letras)
#• : Inicia o loop que vai repetir o bloco de código para cada item da lista.
#• indice: É a variável que guarda a posição atual do item na lista (em Python, a contagem começa em 0).
#• letra: É a variável que guarda o valor/conteúdo real daquela posição (o caractere em si).
#• in enumerate(letras): Diz ao Python para pegar a sequência letras e "empacotar" cada item junto com o seu respectivo número de ordem.