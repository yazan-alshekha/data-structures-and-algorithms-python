def array_shift(arr,value):
    for i in range(len(arr)):
        if arr[i]>=value:
            arr.insert(0,value)
            break
        elif value>arr[-1]:
             arr.append(value)
             break
        if  arr[i]<value and value<=arr[i+1]:
            print('if')
            arr.insert(i+1,value)
            break
     
        
    return arr       

value=10
list=[0,1,2,3,4,5]
array_shift(list,value)