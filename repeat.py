#-*- coding: utf-8 -*-
import sys
from com.index.preproccess import labeldic
from com.index.strmatch import buildtree
from com.index.submerge import merge


if __name__=='__main__':
        
    files=sys.argv[1]
    interval=int(sys.argv[2])
  
    
    dicts,text=labeldic(files,interval)
    listout=buildtree(dicts,text,interval)
    sortdic=merge(listout)
    
    output = open('out.txt', 'a')
    for i in range(0,len(sortdic)):
        listva=sortdic[i]
        if i==len(sortdic)-1:
            output.write(listva[0]+ '\t'+str(listva[1]))
        else:
            output.write(listva[0]+ '\t'+str(listva[1])+'\n')
    output.close()
    print 'programe is finished' 
       
