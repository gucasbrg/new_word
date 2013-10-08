#-*- coding: utf-8 -*-
import re
import chardet
from util import *

def labeldic(files,interval):
     
    text=open(files).read()

    encodeing=chardet.detect(text).get('encoding') 

    text=text.decode(encodeing).replace(' ','').replace('\n','  ') 

    textli=list(text)
    

    lable=[]
    value=[]

    for i in range(0,len(textli)):
        if textli[i] not in lable and textli[i] not in exclude and re.match(ur"([\u4E00-\u9FA5#]+)",textli[i])!=None:
            lable.append(textli[i])
            value.append([i])        
        elif textli[i] not in exclude and re.match(ur"([\u4E00-\u9FA5+#]+)",textli[i])!=None:
            index=lable.index(textli[i])
            value[index].append(i)    
        
        
    dicts=[]
    for i in range(0,len(value)):
        if len(value[i])>=interval:
            dicts.append({lable[i]:value[i]})

  
    return dicts,textli
