# lista3=list() - comando para criar uma lista vazia
# dic4= dict() - comando para criar um dicionário vazio
# tup4= tuple() - comando para criar uma tupla 

# VARIAVEL = VALOR UNICO
# lista = [VALOR1, VALOR2, VALOR3] # sempre feita por colchetes[] - lista é mutável
# dicionario = {CHAVE1: VALOR1, CHAVE2: VALOR2} # sempre feita por chaves{} -  dicionário é mutável
# tupla = (VALOR1, VALOR2, VALOR3) # sempre feita por parenteses() - tupla é imutável
#------------------------------------------------------------------------------------------------------------------------------------------------
# var1 = 10 # variável inteira
# # var2= str
# lista1= [0,'teste',8.85,True]
# lista2= (0,'teste',8.85,True)


# print(lista1)

# # lista1[1]= input('Digite o valor da lista1: ')
# # print(lista1)


# # print(lista2)

# # lista2 = input('Digite o valor da lista2: ')
# # print(lista2)

# lista1.append(input('Digite o valor da lista1: '))
# lista1.insert(1, input('Digite o algo: '))
# print(lista1)
# ---------------------------------------------------------------------------------------------------------------------------------------

dicionario_precos = {'salgado': 5.50, 'cafe': 4.20, 'suco': 9.15, 'torta': 16.00}

# Pesquisar um produto no dicionário

produto_solicitado = input('Digite o produto da Cantina: ')
produto_solicitado = produto_solicitado

if produto_solicitado in dicionario_precos:
    preco=dicionario_precos[produto_solicitado]
    print('O produto{produto_solcitado} custa R$ {preco:.2f}')
else:
    print('O Produto{produto_solicitado} não está disponivel para venda!')
    
print("Fim da pesquisa de preços")

 