venda1 = int(input('Digite o total das vendas de Segunda: '))
venda2 = int(input('Digite o total das vendas de Terça: '))
venda3 = int(input('Digite o total das vendas de Quarta: '))
venda4 = int(input('Digite o total das vendas de Quinta: '))
venda5 = int(input('Digite o total das vendas de Sexta: '))
venda6 = int(input('Digite o total das vendas de Sabado: '))
venda7 = int(input('Digite o total das vendas de Domingo: '))

dic_vendas = {'Segunda': venda1, 'Terça': venda2, 'Quarta': venda3, 'Quinta': venda4, 'Sexta': venda5, 'Sabado': venda6, 'Domingo': venda7}
print(dic_vendas)


total_vendas = venda1 + venda2 + venda3 + venda4 + venda5 + venda6 + venda7
print ('O total de vendas da semana é:', total_vendas)

media = (venda1 + venda2 + venda3 + venda4 + venda5 + venda6 + venda7) / 7 
print ('A média de vendas da semana é:', media)      

