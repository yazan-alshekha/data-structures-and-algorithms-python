from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import *


# def test_():
#     animals=AnimalShelter()

#     cherry=Cat('cherry')
#     oscar=Dog('oscar')

#     animals.enqueue(cherry)
#     animals.enqueue(oscar)
#     expected='rear->oscar->ossccaar-><-front'
#     actual=animals.__str__
#     assert expected==actual

def test_enqueue():
    animals=AnimalShelter()

    cherry=Cat('cherry')
    animals.enqueue(cherry)

    expected='cherry'
    actual=animals.front.name
    assert actual==expected


def test_last_enqueue():
    animals=AnimalShelter()

    cherry=Cat('cherry')
    oscar=Dog('oscar')
    bo=Dog('bo')

    animals.enqueue(cherry)
    animals.enqueue(oscar)
    animals.enqueue(bo)

    expected='bo'
    actual=animals.rear.name
    assert actual==expected

def test_dequeue_first_object():
    animals=AnimalShelter()

    cherry=Cat('cherry')
    oscar=Dog('oscar')

    animals.enqueue(cherry)
    animals.enqueue(oscar)
    expected='cherry'
    actual=animals.dequeue(Cat)


def test_dequeue_second_object():
    animals=AnimalShelter()

    cherry=Cat('cherry')
    oscar=Dog('oscar')
    bella=Cat('bella')

    animals.enqueue(oscar)
    animals.enqueue(bella)
    animals.enqueue(cherry)
    expected='cherry'
    actual=animals.dequeue(Cat)


def test_dequeue_last_object():
    animals=AnimalShelter()

   
    oscar=Dog('oscar')
    bella=Cat('bella')
    bo=Dog('bo')

    animals.enqueue(bo)
    animals.enqueue(oscar)
    animals.enqueue(bella)
    
    expected='bella'
    actual=animals.dequeue(Cat)

def test_dequeue_None():
    animals=AnimalShelter()
    # cherry=Cat('cherry')
    # oscar=Dog('oscar')

    # animals.enqueue(cherry)
    # animals.enqueue(oscar)
    expected='None'
    actual=animals.dequeue(Cat)







