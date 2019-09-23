def main():
    calif=[9,8,7,5,2,10]
    calif_2=[5,5,5,5,5,]
    calif_3=[0,1,2]
    calif_4=[4,2,4,5,7,8]
    calif_5=[1,1,1,1]
    porcentaje=0
    if (prom(calif)>=6):
        porcentaje+=1
    if (prom(calif_2)>=6):
        porcentaje+=1
    if (prom(calif_3)>=6):
        porcentaje+=1
    if (prom(calif_4)>=6):
        porcentaje+=1
    if (prom(calif_5)>=6):
        porcentaje+=1
    porcentaje=(porcentaje*100)/5
    print(porcentaje,"%")

def prom(califx):
    sumaaprob=0
    for i in range(0,len(califx)):
        sumaaprob+=califx[i]
    sumaaprob=sumaaprob//len(califx)
    return sumaaprob


main();