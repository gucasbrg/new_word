#-*- coding: utf-8 -*-
from com.index.TreeNode import *
from Queue import Queue
import re



def buildtree(dicts,text,interval):
    listout=[]
    
    for i in range(0,len(dicts)):
               
        value=dicts[i].keys()[0]
        listset=dicts[i][value] 
        root=TreeNode(value,listset,0)

        act_queue=Queue()
        act_queue.put(root)

        while(act_queue.empty()==False):
            cur_node=act_queue.get() 
            listset=cur_node.listset
            
            index=[]
            setval=[]
            value=[]
            
            for j in range(0,len(listset)):
                if (listset[j]+cur_node.layer+1)>len(text)-1:
                    pass
                else: 
                                             
                    if text[listset[j]+cur_node.layer+1]==' ':
                        pass
                    else:
                        hash_index=hash(text[listset[j]+cur_node.layer+1])
                        if hash_index not in index:
                            index.append(hash_index)
                            setval.append([listset[j]])
                            value.append(text[listset[j]+cur_node.layer+1])
                        else:
                            setval[index.index(hash_index)].append(listset[j])
                   
            for k in range(0,len(setval)):
                if len(setval[k])>=interval:
                    
                    new_node=TreeNode(value[k],setval[k],cur_node.layer+1)
                    cur_node.addChild(new_node)
                    act_queue.put(new_node)
                else:
                    cur_node.subleaf=True 
        
        outdics=outsum(root,interval)
        if len(outdics)!=0:
            listout.append(outdics)
       
    
    
    return listout    
                   
 
def outsum(root,interval):
    dicts={}
    stack=[]
    outstr(root,interval,dicts,stack)
    return dicts
             
def outstr(root,interval,dicts,stack):
   
    if len(root.children)!=0:
        stack.append(root.value)
        if root.subleaf==True:
            if len(stack)>2:
                if re.match(ur"([a-zA-Z0-9-（(，,。－《+#]+)",root.value)!=None:
                    pass
                else:
                    key=''.join(stack)
                    if findbracket(key):                        
                        dicts[key]=len(root.listset)
        
        children=root.children
        for i in range(0,len(children)):
           
            outstr(children[i],interval,dicts,stack)
        stack.pop()
    else:
        stack.append(root.value)
        if len(stack)>=2:
            if re.match(ur"([a-zA-Z0-9-（，,。－《+#]+)",root.value)!=None:
                pass
            else:
                key=''.join(stack)
                if findbracket(key):                    
                    dicts[key]=len(root.listset)
        stack.pop()



def findbracket(key):
    if key.find('(')!=-1 or key.find(u'（')!=-1 or  key.find(u'《')!=-1:
        if key.find(')')!=-1 or key.find(u'）')!=-1 or  key.find(u'》')!=-1:
            return True
        else:
            return False
    
    if key.find(')')!=-1 or key.find(u'）')!=-1 or  key.find(u'》')!=-1:
        if key.find('(')!=-1 or key.find(u'（')!=-1 or  key.find(u'《')!=-1:
            return True
        else:
            return False
        
    if key.find('，')!=-1:
        return False
    
    return True
