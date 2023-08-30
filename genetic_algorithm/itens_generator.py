import random

NUMERO_ITENS = 1000
VALOR_MAX = 20000
PESO_MAX = 150
TAMANHO_MAX = 4500

valores = []
pesos = []
tamanhos = []

for i in range(1,NUMERO_ITENS):
    valores.append(random.randrange(1, VALOR_MAX))
    pesos.append(random.randrange(1, PESO_MAX))
    tamanhos.append(random.randrange(1, TAMANHO_MAX))

print("valores = ")
print(valores)
print("pesos = ")
print(pesos)
print("tamanhos = ")
print(tamanhos)


#with open('teste.txt', 'w') as arquivo:
#    arquivo.write(valores)
#    arquivo.write(pesos)
#    arquivo.write(tamanhos)
