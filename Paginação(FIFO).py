import time

cont = 0
frames = []

ref = raw_input("Digite as referencias separadas por espaco: ")
references = ref.split(" ")

for x in range(0, len(references)):
    references[x] = int(references[x])

n = input("Digite o tamanho da frame de memoria: ")

for i in range (0,n):
    frames.append(None)

for j in references:
    print("Inserindo o "+str(j)+"\n")
    if (j in frames):
        print("Hit em "+str(j)+" :D")
    else:
        print("Miss :(")
        frames[cont] = j
        cont += 1
        print frames

    if (cont >= len(frames)):
        cont = 0
    print("")

    time.sleep(1)
    
print ("No total ocorream "+str(len(hit))+" hit(s) e "+str(len(miss))+" miss(es).") 
