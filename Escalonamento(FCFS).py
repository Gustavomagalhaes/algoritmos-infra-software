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

                #cria um 'processo ocioso" para imprimir na tabela final
                #se for o primeiro processo o tempo de chegada é 0
                #se não o tempo inicial é o final do último processo
                if(p==0):
                    ocioso=processo("tempo ocioso",0,0)
                    ocioso.tempoInicio=ocioso.tempoChegada
                    ocioso.tempoFinal=tempoOcioso
                else:
                    ocioso=processo("tempo ocioso",0,filaProcessos[p-1].tempoFinal)
                    ocioso.tempoInicio=ocioso.tempoChegada
                    ocioso.tempoFinal=tempoAtual

                #se a duração do tempo ocioso é maior que é 1
                #tira o último objeto 'tempo ocioso' da lista e o substitui
                #pelo com o tempo de duração certa. 
                if(tempoOcioso>1):
                    listaOcioso.pop()
                    listaPosicao.pop()

                #adiciona o objeto de 'tempo ocioso' na lista e a sua posição    
                listaOcioso.append(ocioso)
                listaPosicao.append(p)

            else:
                # se tiver chegado ele executa o processo por 1s e subtrai do tempo de execucao
                time.sleep(1)
                filaProcessos[p].tempoExecucao-=1
                print filaProcessos[p].executar()
                tempoAtual+=1

                #se for o primeiro processo o tempo inicial é o tempo de chegada
                #+ o tempo ocioso anterior (caso n tenha somará 0)
                if(p==0):
                        filaProcessos[p].tempoInicio = filaProcessos[p].tempoChegada+tempoOcioso
                        tempoOcioso=0

                #se não for o primeiro processo o tempo incial é o tempo final
                #do processo anterior + o tempo ocioso do anterior
                else:

                    #so atualiza o tempo de inicio se o tempo que estiver for menor que
                    #o tempo final do anterior, se for maior é pq já foi atualizado.
                    if(filaProcessos[p].tempoInicio<filaProcessos[p-1].tempoFinal):
                        filaProcessos[p].tempoInicio = filaProcessos[p-1].tempoFinal+tempoOcioso
                        tempoOcioso=0

                # o tempo final sempre é igual ao tempo atual
                filaProcessos[p].tempoFinal = tempoAtual

    #coloca os "processos ociosos" na lista para imprimir a tabela
    c=0
    for p in range(0,len(listaOcioso)):
        filaProcessos.insert(listaPosicao[p]+c,listaOcioso[p])
        c+=1
        
    # imprime a tabela
    print ""
    for p in range(0,len(filaProcessos)):
        print "%d %s %d"%(filaProcessos[p].tempoInicio,
                          filaProcessos[p].nome,filaProcessos[p].tempoFinal)
    print

    #tira os processos ociosos da lista para fazer o calculo do tempo de espera
    for p in range(0,len(listaOcioso)):
        filaProcessos.pop(listaPosicao[p])
        

    #faz os calculos de todos os tempos de espera
    somatorio=0
    c=0
    for p in range(0,len(filaProcessos)):
        tempoEspera = filaProcessos[p].tempoInicio-filaProcessos[p].tempoChegada
        print "tempo de espera %s: %d"%(filaProcessos[p].nome,tempoEspera)
        somatorio+=tempoEspera
        c+=1
    
    print "tempo de espera médio: %f"%(float(somatorio)/float(c))
                                        
    
            

filaProcessos = [processo("processo 1",8,2),processo("processo 2",4,10)
                 ,processo("processo 3",9,11),processo("processo 4",5,25)
                 ,processo("processo 5",10,25),processo("processo 6",14,26)]


FCFS(filaProcessos)
