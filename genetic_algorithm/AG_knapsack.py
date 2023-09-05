import random
import logging
from table_test import valores, pesos, tamanhos


PROBABILIDADE_MUTACAO = 0.10
MAX_ITERACOES = 300
POPULACAO = 300

NUMERO_ITENS = 1000
VOLUME_MAX = 50000
PESO_MAX = 20000

choice = [0,1]
individuos = []
selecionados = []
ciclos_total = 0

class Population:
    def __init__(self):
        self.vetor = []
        self.peso = 0
        self.volume = 0
        self.avaliativa = 0
        self.ap = 0

def vetor_aleatorio(tam, choice):
    vetor = []
    for _ in range (1,tam):
        vetor.append(random.choice(choice))
    return vetor

def vetor_nulo(tam):
    vetor = []
    for _ in range (1,tam):
        vetor.append(0)
    return vetor

def avaliativa(individuo):
    valor = 0
    j = 0
    for i in individuo.vetor:
        valor += individuo.vetor[j]*valores[j]
        j+=1
    return valor

def generate():
    for individuo in individuos:
        individuo.vetor = vetor_aleatorio(NUMERO_ITENS,choice)
        x = 0
        individuo.peso = 0
        individuo.volume = 0
        for j in individuo.vetor:
            individuo.peso += j*pesos[x]
            individuo.volume += j*tamanhos[x]
            x+=1
        if individuo.peso > PESO_MAX or individuo.volume > VOLUME_MAX:
            individuo.vetor = vetor_nulo(NUMERO_ITENS)

def cruzamento(selecionado1, selecionado2, corte, bool):
    buffer1 = []
    buffer2 = []
    buffer3 = []
    buffer4 = []
    for i in range(0,corte):
        buffer1.append(selecionado1.vetor[i])
        buffer3.append(selecionado2.vetor[i])
    j = 0
    for i in range(corte,NUMERO_ITENS-1):
        buffer2.append(selecionado1.vetor[i])
        buffer4.append(selecionado2.vetor[i])
        j+=1
    
    if(bool):
        return buffer1 + buffer4
    else:
        return buffer3 + buffer2


if __name__ == '__main__':

    for _ in range(1,POPULACAO+1):
        individuos.append(Population())
        selecionados.append(Population())
    for cycle in range(1,6):
        logging.basicConfig(level=logging.INFO, filename="test_POP300_MAXITER300_PM10V095_"+str(cycle)+".log", format="")
        choice = [0,1]
        while 1:
            generate()
            choice.append(0)
            num_aval_nulas = 0
            for individuo in individuos:
                if avaliativa(individuo) == 0:
                    num_aval_nulas +=1
            if(num_aval_nulas == 0):
                break
        
        for i in range(1,MAX_ITERACOES):
            #print('Iteração ')
            #print(i)
            soma_avaliativa = 0
            aux = True
            for individuo in individuos:
                individuo.avaliativa=avaliativa(individuo)
                soma_avaliativa += individuo.avaliativa
                #print('avaliativa:')
                #print(individuo.avaliativa)
                if aux:
                    aux = False
                    logging.info(individuo.avaliativa)
            for individuo in individuos:
                individuo.ap = individuo.avaliativa/soma_avaliativa
            choice_weights = []
            
            for individuo in individuos:
                choice_weights.append(100*individuo.ap) 
            print(choice_weights)
            selecionados = random.choices(individuos, choice_weights, k = POPULACAO)
        
            for par in range(0,int(POPULACAO/2)):
                corte = random.randint(1,NUMERO_ITENS-2)
                individuos[2*par].vetor = cruzamento(selecionados[2*par], selecionados[2*par+1], corte, False)
                individuos[2*par+1].vetor = cruzamento(selecionados[2*par], selecionados[2*par+1], corte, True)
                print(individuos[par].vetor)
        
            for individuo in individuos:
                if(random.random()<=PROBABILIDADE_MUTACAO):
                    pos = random.randint(1,NUMERO_ITENS-2)
                    if(individuo.vetor[pos] == 0):
                        individuo.vetor[pos] = 1
                    else:
                        individuo.vetor[pos] = 0
            PROBABILIDADE_MUTACAO = PROBABILIDADE_MUTACAO*0.95
            for individuo in individuos:
                individuo.peso = 0
                individuo.volume = 0
                for j in individuo.vetor:
                    individuo.peso += j*pesos[j]
                    individuo.volume += j*tamanhos[j]
                if individuo.peso > PESO_MAX or individuo.volume > VOLUME_MAX:
                    individuo.vetor = vetor_nulo(NUMERO_ITENS)