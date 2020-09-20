# Function to do insertion sort 
def insertion_sort(lis): 

  
        # Traverse through 1 to len(lis) 
        for i in range(1, len(lis)): 
    
            key = lis[i] 

            j = i-1
            while j >= 0 and key < lis[j] : 
                    lis[j + 1] = lis[j] 
                    j -= 1
            lis[j + 1] = key
          

if __name__ == "__main__":
    a=[10,5,8,41,62,85] 
    insertion_sort(a) 
    print(a) 
