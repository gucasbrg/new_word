#-*- coding: utf-8 -*-

def merge(listout):
    val={}      
    for i in range(0,len(listout)):
        for j in listout[i]:
            value=reverse(j)
            val[value]=listout[i][j]   
    
    ascendlist=sortdict(val)
    
    
    
    label=[0 for k in range(0,len(ascendlist))]
    

    for i in range(0,len(ascendlist)-1):
        if ascendlist[i+1][0].find(ascendlist[i][0])==0:
            if ascendlist[i+1][1]==ascendlist[i][1] and ascendlist[i+1][0].find('间')==-1:
                label[i]=1
            elif ascendlist[i+1][1]==ascendlist[i][1] and ascendlist[i+1][0].find('间')!=-1:
                label[i+1]=1
            elif ascendlist[i+1][1]!=ascendlist[i][1] and ascendlist[i+1][1]*1.25>ascendlist[i][1]:

                label[i]=1
                
           
    posval={}
    for i in range(0,len(ascendlist)):
        if label[i]!=1:
            posval[reverse(ascendlist[i][0])]=ascendlist[i][1]
    
    posilist=sortdict(posval)
    
    label_pos=[0 for j in range(0,len(posilist))]
    
    for i in range(0,len(posilist)-1):
        if posilist[i+1][0].find(posilist[i][0])==0 and posilist[i+1][1]*1.25>=posilist[i][1]:           
            label_pos[i]=1
    
                           
    outresult=[]
    for i in range(0,len(posilist)):
        if label_pos[i]!=1:
            outresult.append([posilist[i][0],posilist[i][1]])   
    
    bubblesort(outresult)
    
    return outresult


def reverse (s):
    return s[::-1]


def sortdict(dicts):
    dic=[]
    keys = dicts.keys()
    keys.sort()

    values=[dicts[key] for key in keys]
    for i in range(0,len(keys)):
        dic.append([keys[i],values[i]])
    return dic    

def bubblesort(outresult): 
    for i in range(0,len(outresult)):
        for j in range(0,len(outresult)-i-1):
            if(outresult[j+1][1]>=outresult[j][1]):
                val=outresult[j+1]
                outresult[j+1]=outresult[j]
                outresult[j]=val
                  
