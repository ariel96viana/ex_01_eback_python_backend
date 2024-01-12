# MODELANDO STRINGS

frase = "esta é uma frase para mudar"
print(frase)
print(frase.upper())
print(frase.find('esta'), frase.find('johnson'))
print(frase.replace('frase', 'deregue'))
print(frase[2:12])



latitude = '-22.00532'
longitude = '-47.891040'

latitude_longitude = '-22.00532;-47.891040'

print(latitude, longitude, sep=' separado de ')
print(latitude_longitude, end=' tudo junto\n')

posicao_char_divisao = latitude_longitude.find(';')
latitude_new = latitude_longitude[0:posicao_char_divisao]
longitude_new = latitude_longitude[posicao_char_divisao+1:len(latitude_longitude)]

print(latitude_new)
print(longitude_new)

