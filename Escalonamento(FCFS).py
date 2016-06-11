import time

class processo:
    def __init__(self,nome,tempoExecucao,tempoChegada):
        self.nome=nome
        self.tempoExecucao=tempoExecucao
        self.tempoChegada=tempoChegada
        self.tempoInicio=0
        self.tempoFinal=0
        self.parar=False

    def executar(self):
            return "%s executando"%(self.nome)

    def parar(self):
        self.parar=True
            


def FCFS(filaProcessos):
    tempoAtual = 0
    tempoOcioso = 0
    listaOcioso=[]
    listaPosicao=[]
    
    #Ordena a fila de processos baseado no tempo de chegada
    filaProcessos.sort(key=lambda x: x.tempoChegada)

    #corre a fila de processos já ordenada
    for p in range(0,len(filaProcessos)):

        #loop para executar o processo durante o tempo de execução
        while(filaProcessos[p].tempoExecucao>0):

            #verifica se algum processo já chegou no tempo atual
            if(filaProcessos[p].tempoChegada > tempoAtual):
                # se não tiver chegado ele executa tempo ocioso
                time.sleep(1)
                print "tempo ocioso"
                tempoOcioso+=1
                tempoAtual+=1   

                if(p==0):
                    ocioso=processo("tempo ocioso",0,0)
                    ocioso.tempoInicio=ocioso.tempoChegada
                    ocioso.tempoFinal=tempoOcioso
                else:
                    ocioso=processo("tempo ocioso",0,filaProcessos[p-1].tempoFinal)
                    ocioso.tempoInicio=ocioso.tempoChegada
                    ocioso.tempoFinal=tempoAtual

                if(tempoOcioso>1):
                    listaOcioso.pop()
                    listaPosicao.pop()
                listaOcioso.append(ocioso)
                listaPosicao.append(p)

            else:
                # se tiver chegado ele executa o processo por 1s e subtrai do tempo de execucao
                time.sleep(1)
                filaProcessos[p].tempoExecucao-=1
                print filaProcessos[p].executar()
                tempoAtual+=1

                if(p==0):
                    filaProcessos[p].tempoInicio = filaProcessos[p].tempoChegada
                    filaProcessos[p].tempoFinal = tempoAtual
                else:
                    if(filaProcessos[p].tempoInicio<filaProcessos[p-1].tempoFinal):
                        filaProcessos[p].tempoInicio = filaProcessos[p-1].tempoFinal+tempoOcioso
                        tempoOcioso=0
                    filaProcessos[p].tempoFinal = tempoAtual
    c=0
    for p in range(0,len(listaOcioso)):
        filaProcessos.insert(listaPosicao[p]+c,listaOcioso[p])
        c+=1
        
    print ""
    for p in range(0,len(filaProcessos)):
        print "%d %s %d"%(filaProcessos[p].tempoInicio,
                          filaProcessos[p].nome,filaProcessos[p].tempoFinal)
    print
    somatorio=0
    c=0

    for p in range(0,len(listaOcioso)):
        filaProcessos.pop(listaPosicao[p])
        

    
    c=0
    for p in range(0,len(filaProcessos)):
        tempoEspera = filaProcessos[p].tempoInicio-filaProcessos[p].tempoChegada
        print "tempo de espera %s: %d"%(filaProcessos[p].nome,tempoEspera)
        somatorio+=tempoEspera
        c+=1
    
    print "tempo de espera médio: %f"%(float(somatorio)/float(c))
                                        
    
            

filaProcessos = [processo("processo 1",8,0),processo("processo 2",4,10)
                 ,processo("processo 3",9,11),processo("processo 4",5,25)
                 ,processo("processo 5",10,25),processo("processo 6",14,26)]


FCFS(filaProcessos)
