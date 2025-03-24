# cor1= input('Cor Favorita de Maria?:')
# cor2= input('Cor Favorita de Pedro?:')
# cor3= input('Cor Favorita de Andre?:')
# cor4= input('Cor Favorita de Camila?:')

# cores= print ('A Cor Favorita de Maria é:', cor1)
# cores= print ('A Cor Favorita de Pedro é:', cor2)
# cores= print ('A Cor Favorita de Andreé:', cor3)
# cores= print ('A Cor Favorita de Camila é:', cor4)

# lista_nomes = ['Maria', 'Pedro', 'André','Camila']
# lista_cores = [ ]

# print('Lista atual', lista_nomes)
# altname= input("Digite um nome: ")
# indice_lista = int(input("Digite qual indice vai ser alterado: "))


# lista_nomes[indice_lista]= altname
# print('Nomes Atualizados:',lista_nomes)

lista_nomes = ['Maria', 'Pedro', 'André','Camila']
lista_vendas = [100,300,200,10000,5000,800,300]

#contadores
print('Soma de todos os valores: ', sum(lista_vendas))
print('Quantidade de itens: ', len(lista_vendas))
print('Valor Minimo: ', min(lista_vendas))
print(f'Valor Máximo: ', {max(lista_vendas)})

#ADICIONAR UM ITEM
#lista_nomes.append('Manuel')
#print(lista_nomes)

lista_nomes = ['Maria', 'Pedro', 'André','Camila']
#lista_vendas = [100,300,200,10000,5000,800,300]

lista_nomes.append(input("Digite um nome para ser incluído: "))
nome_temp = input('Digite o nome a ser removido: ')
if nome_temp in lista_nomes:
    lista_nomes.remove(nome_temp)
print(lista_nomes)
