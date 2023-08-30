import random
from table_test import valores, pesos, tamanhos

PROBABILIDADE_MUTACAO = 0.1
MAX_ITERACOES = 500
POPULACAO = 3

NUMERO_ITENS = 300
VOLUME_MAX = 50000
PESO_MAX = 20000

class Population:
    def __init__(self):
        self.vetor = []
        self.peso = 0
        self.volume = 0
        self.avaliativa = 0
        self.ap = 0

def vetor_aleatorio(tam):
    vetor = []
    for _ in range (1,tam):
        vetor.append(random.randint(0,1))
    return vetor

def vetor_nulo(tam):
    vetor = []
    for _ in range (1,tam):
        vetor.append(0)
    return vetor

def avaliativa(individuo):
    valor = 0
    for i in individuo.vetor:
        valor += i*valores[j]
    return valor

def cruzamento(selecionado1, selecionado2, corte, bool):
    buffer1 = []
    buffer2 = []
    buffer3 = []
    buffer4 = []
    for i in range(0,corte):
        buffer1.append(selecionado1.vetor[i])
        buffer3.append(selecionado2.vetor[i])
    j = 0
    for i in range(corte+1,NUMERO_ITENS-1):
        buffer2.append(selecionado1.vetor[i])
        buffer4.append(selecionado2.vetor[i])
        j+=1
    
    if(bool):
        return buffer1 + buffer4
    else:
        return buffer3 + buffer2


if __name__ == '__main__':
    individuos = []
    selecionados = []
    for i in range(1,POPULACAO):
        individuos.append(Population())
        selecionados.append(Population())
    for individuo in individuos:
        individuo.vetor = vetor_aleatorio(NUMERO_ITENS)
        for j in individuo.vetor:
            individuo.peso += j*pesos[j]
            individuo.volume += j*tamanhos[j]
        if individuo.peso > PESO_MAX or individuo.volume > VOLUME_MAX:
            individuo.vetor = vetor_nulo(NUMERO_ITENS)

    for i in range(1,MAX_ITERACOES):
        soma_avaliativa = 0
        for individuo in individuos:
            individuo.avaliativa=avaliativa(individuo)
            soma_avaliativa += individuo.avaliativa
            print(individuo.avaliativa)
        for individuo in individuos:
            individuo.ap = individuo.avaliativa/soma_avaliativa
            print(individuo.ap)
        for selecionado in selecionados:
            prob = random.random()
            print("Probabilidade")
            print(prob)
            somaProb = 0
            for individuo in individuos:
                somaProb += individuo.ap
                if somaProb >= prob:
                    selecionado.vetor = individuo.vetor
                    break
        for par in range(1,int(POPULACAO/2)):
            corte = random.randint(1,NUMERO_ITENS-2)
            individuos[par].vetor = cruzamento(selecionados[par], selecionados[par+1], corte, False)
            individuos[par+1].vetor = cruzamento(selecionados[par], selecionados[par+1], corte, True)
        
        for individuo in individuos:
            if(random.random()>=PROBABILIDADE_MUTACAO):
                pos = random.randint(0,NUMERO_ITENS-2)
                print(pos)
                if(individuo.vetor[pos] == 0):
                    individuo.vetor[pos] = 1
                else:
                    individuo.vetor[pos] = 0
        for individuo in individuos:
            individuo.vetor = vetor_aleatorio(NUMERO_ITENS)
            for j in individuo.vetor:
                individuo.peso += j*pesos[j]
                individuo.volume += j*tamanhos[j]
            if individuo.peso > PESO_MAX or individuo.volume > VOLUME_MAX:
                individuo.vetor = vetor_nulo(NUMERO_ITENS)