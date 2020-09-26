from list import Node,LinkedList

class Hashtable:
    def __init__(self,size=1024):
        self.map=[None]*size
        self.size=size

    def set(self,key,value):
        hashed_key=self.hash(key)

        if self.map[hashed_key]==None:
            self.map[hashed_key]=LinkedList()


        self.map[hashed_key].append((key,value))
    
    def get(self,key):
        pass
    
    def hash(self,key):
        hashed_total=0
        for char in key:
            hashed_total+=ord(char)
        return hashed_total*19% self.size    
    
    
    def contains(self,key):
        pass

