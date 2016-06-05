import time

class process:
    def __init__(self,name,time):
        self.name=name
        self.time=time

    def execute(self):
        while(self.time>0):
            time.sleep(1)
            self.time-=1;
            print "%s executando"%(self.name)
            


def FCFS(processQueue):
    for p in range(0,len(processQueue)):
        processQueue[p].execute();
        
        


processQueue = [process("processo 1",5),process("processo 2",4),process("processo 3",2),process("processo 4",8)]

FCFS(processQueue)

