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
   
    def length(self):
        if not self.head:
            return 0
        else:
            current=self.head
            counter=0
            while current:
                counter=counter+1
                current=current.next
            return counter    

    def insertBefore(self,value,newValue):
        '''
        insert new node befor specific value:
            input-->('apple','Grape')
            output --> [Grap,apple]

        '''
        new_node=Node(newValue)

        if self.length()==0:
            print("the value you entered not exists")
             
        elif self.length()==1 and self.head.value==value:
            new_node.next=self.head
            self.head=new_node
        else:
            previous_node=self.head
            current=self.head.next
            
            while current:
                # print(current.value)
                if current.value==value:
                    new_node.next=current
                    previous_node.next=new_node
                current=current.next

    def insertAfter(self,value,newValue):
        '''
        insert new node after specific value:
            input-->('apple','Grape')
            output --> [apple,Grap]

        '''
        new_node=Node(newValue)

        if self.length()==0:
            print("the value you entered not exists")
             
        elif self.length()==1 and self.head.value==value:
            self.append(newValue)
        else:
            previous_node=self.head
            current=self.head.next
            
            while current:
                # print(current.value)
                if current.value==value:
                    new_node.next=current.next
                    current.next=new_node
                current=current.next
         

       

       




                        
                
if __name__ == "__main__":
    fruits = LinkedList()
    # fruits.append('apple')
    fruits.append('orange')
    fruits.append('banana')
    # print( fruits.includes('bana'))
    # put your LinkedList implementation here
    print(fruits)
    # fruits.insertBefore('orange','Grape')
    fruits.insertAfter('banana','Grap')
    print(fruits)
    # print(fruits.length())