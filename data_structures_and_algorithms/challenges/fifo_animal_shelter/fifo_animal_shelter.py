


class Dog:
    def __init__(self,dog_name):
        self.name=dog_name
        self.next=None
        self.previous=None    
        self.type='Dog'

class Cat:
    def __init__(self,cat_name):
        self.name=cat_name  
        self.next=None
        self.previous=None  
        self.type='Cat'

class AnimalShelter :
    def __init__(self):
        self.front=None
        self.rear=None
    
    def __str__(self):
        current = self.rear
        output = 'rear->'
        while current:
            output += f"{current.name}->"
            current = current.next
        output+="<-front"
        return output 


    def enqueue(self,animal_name):
        '''
        function   to add object to the queue

            input  -> Dog or Cat object 
            output -> 
        '''

        if self.front==None:
            self.front=animal_name
            self.rear=animal_name
        else:
            temp=self.rear
            self.rear=animal_name
            self.rear.next=temp
            temp.previous=self.rear



    def dequeue(self,animal_type):
        '''
        function   to delete the name of object category from queue

            input  -> Dog or Cat object
            output -> Dog name or cat name or None
        '''

        # if queue is empty
        if self.front==None and self.rear==None:
            return None

        # check last object
        last_object=self.rear

        if last_object.type==animal_type:
            temp=self.rear
            self.rear=self.rear.next
            self.rear.previous=None
            return temp.name

        # check first object
        current=self.front
        
        if  current.type==animal_type:
            temp=self.front
            self.front=self.front.previous
            self.front.next=None
            return temp.name

       
        # loop from front to rear 
        while current:
            if current.type==animal_type:
                temp=current.next
                temp.previous=current.previous
                current.previous.next=temp
                return current.name
            current=current.previous
        # if object not exist    
        return None
      




if __name__ == "__main__":
    sherry=Cat('sherry')
    oscar=Dog('oscar')
    ossccaar=Dog('ossccaar')
    owow=Dog('owow')

    animals=AnimalShelter()

    # animals.enqueue(sherry)
    animals.enqueue(oscar)
    animals.enqueue(ossccaar)
    animals.enqueue(owow)


    print(animals)
    print(animals.dequeue('Cat'))
    print(animals) 
    # print(type(oscar))
    # print(type(animals))


