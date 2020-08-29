from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import (Stack,Queue)

def test_stack_push():
    people=Stack()
    people.push('yazan')
    expected='yazan'
    actual=people.top.value
    assert actual==expected

def test_pop():
    people=Stack()
    people.push('yazan')
    people.push('ahmad')
   
    expected='ahmad'
    actual= people.pop()
    assert actual==expected

def test_pop_all():
    people=Stack()
    people.push('yazan')
    people.push('ahmad')
    people.pop()
    people.pop()
    expected='Null stack'
    actual= people.pop()
    assert actual==expected

def test_stack_multiple_push():
    pass

def test():
    pass

def test_peek():
    people=Stack()
    people.push('yazan')
    people.push('ahmad')
  
    expected='ahmad'
    actual= people.peek()
    assert actual==expected

def test_stack_pop_all():
    people=Stack()
    people.push('yazan')
    people.push('ahmad')
    people.pop()
    people.pop()
    expected='Null stack'
    actual= people.pop()
    assert actual==expected    

# def test_stack_empty_init():
#     people=Stack()
#     expected=''
#     actual= people.__str__
#     assert actual==expected

def test_empty_stack_peek():
    people=Stack()
    expected="you can't retrieve from empty stack"
    actual= people.peek()
    assert actual==expected

def test_queue_multiple_enqueue():
    pass 




def test_queue_enqueue():
    people=Queue()
    people.enqueue('yazan')
    expected="yazan"
    actual= people.front.value
    assert actual==expected

def test_queue_dequeue():
    people=Queue()
    people.enqueue('yazan')
    expected="yazan"
    actual= people.dequeue()
    assert actual==expected

def test_queue_peek():
    people=Queue()
    people.enqueue('yazan')
    people.enqueue('ahmad')
    people.enqueue('rami')
    expected="yazan"
    actual= people.peek()
    assert actual==expected 


def test_queue_multiple_dequeue():
    people=Queue()
    people.enqueue('yazan')
    people.enqueue('ahmad')
    people.dequeue()
    people.dequeue()
    expected=None
    actual= people.front
    assert actual==expected   




def test_empty_queue_peek():
    people=Queue()
    expected="empty queue"
    actual= people.peek()
    assert actual==expected   
      