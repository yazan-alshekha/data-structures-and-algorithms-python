def QuickSort(arr,left,right): 
    if left < right: 
  
     
        pi = Partition(arr,left,right) 
  
      
        QuickSort(arr, left, pi-1) 
        QuickSort(arr, pi+1, right) 
    return arr

def Partition(arr,left,right): 
    i = ( left-1 )         
    pivot = arr[right]     
  
    for j in range(left , right): 
  
        
        if   arr[j] < pivot: 
          
           
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    
    
    swaping=swaper(arr,i,j,right)
    return swaping
   


def swaper(arr,i,j,right):
    arr[i+1],arr[right] = arr[right],arr[i+1] 
    return ( i+1 ) 




if __name__ == "__main__":
   pass