
class TreeNode:
    def __init__(self,value,listset,layer):
        self.value=value
        self.layer=layer
        self.listset=listset
        self.subleaf=False
        
        self.children = []
        self.parent=None 

    def addChild(self, child):

        self.children.append(child)
        child.parent = self
    
    def getParent(self):

        return self.parent    