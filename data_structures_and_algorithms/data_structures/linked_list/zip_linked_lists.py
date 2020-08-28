
def zip(linked_list1,linked_list2):
    '''
    function to zip 2 of linked list
    input-> 
        l1=    <apple> <orange>  
        l2=    <yazan> <rami>    
    
    output-> 
       <apple><yazan><orange><rami>

    '''
    if linked_list1.length()==0 and linked_list2.length()==0:
        return 'Null'

    if linked_list1.length()==0:
        return linked_list2.__str__()
    
    if linked_list2.length()==0:
        return linked_list1.__str__()  

    current1=linked_list1.head
    more_step1=current1.next

    current2=linked_list2.head
    more_step2=current2.next
 


    while current1:
        if current2:
            current1.next=current2
            current1=more_step1
            if more_step1:
                more_step1=more_step1.next
            if current1:
                current2.next=current1
                current2=more_step2
                if more_step2:
                    more_step2=more_step2.next
        else:
            break            

    return linked_list1.__str__()


