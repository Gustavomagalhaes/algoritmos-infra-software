import time

class processo:
    def __init__(self,nome,tempoExecucao,tempoChegada,quantum):
        self.nome=nome
        self.tempoExecucao=tempoExecucao
        self.tempoChegada=tempoChegada
        self.tempoInicio=0
        self.tempoFinal=0
        self.tempoEspera=0
        self.quantum=quantum

    def executar(self):
            return "%s executando"%(self.nome)

def RR(filaProcessos):
    quantidadeProcessos = 3
    tempoAtual = 0
    quantum = 4
    p=0

    #ordena a lista baseado no tempo de chegada
    filaProcessos.sort(key=lambda x: x.tempoChegada)

    #corre a fila de processos ordenada
    while(p<len(filaProcessos)):
        
        if(filaProcessos[p].quantum > filaProcessos[p].tempoExecucao):
            filaProcessos[p].quantum = filaProcessos[p].tempoExecucao

        while(filaProcessos[p].quantum>0):
                time.sleep(1)
                filaProcessos[p].tempoExecucao-=1
                filaProcessos[p].quantum-=1
                print filaProcessos[p].executar()
                tempoAtual+=1

                if(p==0):
                    filaProcessos[p].tempoInicio = filaProcessos[p].tempoChegada
                else:
                    filaProcessos[p].tempoInicio = filaProcessos[p-1].tempoFinal

                filaProcessos[p].tempoFinal = tempoAtual
                filaProcessos[p].tempoEspera = filaProcessos[p].tempoInicio - filaProcessos[p].tempoChegada

                if(filaProcessos[p].quantum==0 and filaProcessos[p].tempoExecucao > 0):
                    novoProcesso = processo(filaProcessos[p].nome,filaProcessos[p].tempoExecucao,
                             filaProcessos[p].tempoFinal,quantum)
                    novoProcesso.quantum = quantum
                    filaProcessos.append(novoProcesso)
        p+=1
                
                

    #imprime a tabela
    print""
    for p in range(0,len(filaProcessos)):
        print "%d %s %d"%(filaProcessos[p].tempoInicio,
                          filaProcessos[p].nome,filaProcessos[p].tempoFinal)
    print

    tempoEspera=0
    resultado=[]
    somatorio=0
    for i in range(0,quantidadeProcessos):
        for p in range(0,len(filaProcessos)):
            if(filaProcessos[p].nome == "Processo %s"%(i+1)):
                tempoEspera+=filaProcessos[p].tempoEspera
        resultado.append(tempoEspera)
        print "Tempo de espera Processo %s: %d"%(i+1,tempoEspera)
        somatorio+=tempoEspera
        tempoEspera=0

    print "Tempo de espera médio: %f"%(float(somatorio)/quantidadeProcessos)

                  

filaProcessos = [processo("Processo 1", 24,0,4),processo("Processo 2",3,0,4),
                processo("Processo 3",3,0,4)]

RR(filaProcessos)

                
                
