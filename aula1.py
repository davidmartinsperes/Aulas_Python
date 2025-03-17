# from getpass import getpass
# variavel_01 = 5
# variavel_02 = str   
# variavel_03 = 0.0
# variavel_04 = float
# variavel_05 = ' '
# num, tipo,teste = 1,0.0,str
# variavel_06 = variavel_07 = variavel_08 = True

# lista_01= [True,False,True,0,0.0]



# # if variavel_01 > 5.12354633:
# #     print(variavel_01)
# #     print(type(variavel_01))
# #     if variavel_03 >= 0:
# #         print(variavel_03)
# #         if variavel_04 == float:
# #          print('Teste de Float')
# # print("fim")


# # if (variavel_01 < 5):
# #     print(variavel_01)
# # elif variavel_01 == 0:
# #     print(variavel_03)
# # else:
# #     print(type(variavel_01))

# # mes = int(input('Digite o mês:'))

# # if mes == 1:
# #     print('o mês é Janeiro')
# # elif mes == 2:
# #     print('o mês é Fevereiro')
# # else:
# #     print('depois de março')
# # print(type(mes))

# mes = int(input('Digite um valor do mês:'))

# match mes:
#     case 1:
#         print("Janeiro")
#     case 2:
#         print("Fevereiro")
#     case 3: 
#         print ("Março")




nota1 = int(input('Digite a nota p1:'))
nota2 = int(input('Digite a nota p2:'))

media = (nota1 + nota2) / 2

if media >= 9:
     print ('Aprovado SS, SUA MÉDIA:',media)
elif media >= 5:
        print ('aprovado MS, SUA MÉDIA',media)
elif media == 5:
        print ('Aprovado MM, SUA MÉDIA:',media)

else:
       print('Você está reprovado,melhore no semestre que vem.')