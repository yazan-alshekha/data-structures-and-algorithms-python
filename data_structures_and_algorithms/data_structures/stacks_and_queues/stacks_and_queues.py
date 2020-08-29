class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def __str__(self):
        current = self.top
        output = ''
        while current:
            output += f"{current.value}->"
            current = current.next
        output+="]"
        return output 
        

    def push(self,value):
        new_node=Node(value)
        temp=self.top
        self.top=new_node
        new_node.next=temp

    def pop(self):
        if self.isEmpty():
            return 'Null stack'
        temp=self.top
        self.top=self.top.next
        return temp.value

    def peek(self):
        if not self.isEmpty():
            temp=self.top
            return temp.value
        else :
            return "you can't retrieve from empty stack"    

    def isEmpty(self):
        if self.top==None:
            return 1
        else:
            return 0   


class Queue :
    def __init__(self):
        self.front=None
        self.rear=None

    def __str__(self):
        current = self.rear
        output = ''
        while current:
            output += f"{current.value}->"
            current = current.next
        # output+="]"
        return output 

    def enqueue (self,value):
        new_node=Node(value)

        if self.front==None:
            self.front=new_node
            self.rear=new_node
        else:
            temp=self.rear
            self.rear=new_node
            self.rear.next=temp

    def dequeue(self):
        current=self.rear

        if self.rear==self.front:
            temp=self.front
            self.front=None
            self.rear=None
            return temp.value
        
        while current.next.next:
            current=current.next
        
        temp=self.front.value
        self.front=current
        
        return temp   

    def peek(self):

        if self.front== None and  self.rear==None:
            return 'empty queue'

        current=self.rear
        while current.next:
            current=current.next
        return current.value

    def isEmpty(self):
        if self.rear==None and self.front==None:
            return 1
        else:
            return 0


if __name__ == "__main__":
    # fruits=Stack()
    # fruits.push('apple')
    # fruits.push('grap')
    # print(fruits)
    # fruits.pop()
    # print(fruits)
    # print(fruits.isEmpty())
    # fruits.peek()

    people=Queue()
    people.enqueue('yazan')
    people.enqueue('rami')
    people.enqueue('ahmad')
    # people.enqueue('mohhamad')
    print(people)
    
    # print('ss',people.dequeue())
  






            




