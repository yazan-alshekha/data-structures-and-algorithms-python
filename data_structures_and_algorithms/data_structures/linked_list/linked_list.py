class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
   
   
    def append(self,value):
        new_node= Node(value)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
  
  
    def __str__(self):  
        current = self.head
        output = ''
        while current:
            output += f"{current.value}->"
            current = current.next
        output+=" NULL"
        return output 
   
   
    def insert(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
        else:
           new_node.next=self.head
           self.head=new_node    
   
    def includes (self,value):
        if self.head==None:
            return -1
        else:
            current=self.head
            while current:
                if current.value==value:
                    return 1
                else :
                    current=current.next    
            return -1        

                        
                
if __name__ == "__main__":
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('orange')
    fruits.insert('banana')
    # print( fruits.includes('bana'))
    # put your LinkedList implementation here
    print(fruits)