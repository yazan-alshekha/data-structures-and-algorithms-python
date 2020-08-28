# from zip_linked_lists import (zip)
from data_structures_and_algorithms.data_structures.linked_list.zip_linked_lists import zip


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
            return("the value you entered not exists")
             
        elif  self.head.value==value:
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
            return("the value you entered not exists")
             
        elif  self.head.value==value:
            new_node.next=self.head.next
            self.head.next=new_node
        else:
            previous_node=self.head
            current=self.head.next
            
            while current:
                # print(current.value)
                if current.value==value:
                    new_node.next=current.next
                    current.next=new_node
                current=current.next
         
    def kthFromEnd(self,val):
        '''
        method to return value from based on reverse index  

            apple->orange->banana-> NULL 

            input -->ll.kthFromEnd(0)
            output--> banana
        '''
        length_of_list=self.length()-1

        if val<= -1:
            return "you should enter positive value"
       
        if length_of_list < val :
            return "invalid reverse index \n  reverse index should be => length of list"
       
        current=self.head
        index=0
        while current:
            if length_of_list-index==val:
                return current.value
            current=current.next
            index+=1
  
            




       
    

                   
       




                        
                
if __name__ == "__main__":
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('orange')
    fruits.append('grap')
    

    people=LinkedList()
    people.append('yazan')
    people.append('rami')
    people.append('rami')
    people.append('hamza')
    
    

    # pepole.append('yara')
   
    print(zip(fruits,people))
    # print(fruits)

    
    # print( fruits.includes('bana'))
    # put your LinkedList implementation here
    # print(fruits)
    

    
    # fruits.insertBefore('apple','Grape')
    # fruits.insertAfter('apple','Grap')
    # print(fruits)
    # print(fruits.length())