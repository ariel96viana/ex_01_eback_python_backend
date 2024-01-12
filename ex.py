# EXERCICIO 1

print("Olá Mundo!")
# clicar em + Texto, e embaixo no icone de imagem e fazer o upload

print('\n---------------\n')
# EXERCICIO 2

index = 0
data = ['19/01', '20/01', '23/01']
valor_total_vendas = [0, 834.47, 15378.12]
qtd_total_vendas = [3, 0, 5]
ticket_medio = [320.52, 119.21, 0]

print(f'  Dia  ', ' Valor Total Vendas ', ' Qtd Total Vendas ', ' Ticket Medio ')
while index < len(data):
    if valor_total_vendas[index] == 0:
        valor_total_vendas[index] = qtd_total_vendas[index] * ticket_medio[index]

    elif qtd_total_vendas[index] == 0:
        qtd_total_vendas[index] = round(valor_total_vendas[index] / ticket_medio[index])

    elif ticket_medio[index] == 0:
        ticket_medio[index] = valor_total_vendas[index] / qtd_total_vendas[index]


    print(f'{data[index]} | {valor_total_vendas[index]}   |   {qtd_total_vendas[index]}   |   {ticket_medio[index]}',)
    index+=1

print('\n---------------\n')
#EXERCICIO 3

noticia = 'Selic vai a 2,75% e supera expectativas; é a primeira alta em 6 anos.'
selic = noticia[12:17]
ano = noticia[len(noticia)-7:len(noticia)]
print(f'Taxa Selic: {selic}, em {ano}')


print('\n---------------\n')


#EXERCICIO 4

print(' -------------------------------------')
print(f'| a = False                           |')
print(f'| b = True                            |')
print('|Qual o valor de x, se x = not a & b? |')
print(' -------------------------------------')
print(f'Resposta: x será TRUE')
print("Motivo: a = False, b = Verdadeiro.\nnot a = Verdadeiro\nVerdadeiro && Verdadeiro = Verdadeiro")





