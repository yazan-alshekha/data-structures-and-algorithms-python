# Insertion sort 
Inserton Sort is a sorting algorithm that take a value and insert it in right position 

## Pseudocode
```
insertion_sort(lis):
    
   for i=1 to n :

        key=lis[1]
        j=i-1
        while j >= 0 and key < arr[j] : 
                arr[ j++ ] = arr[j] 
                j--
        arr[ j++ ] = key

```
![](../../../assets/insertion_sort.jpg)

- Time Complexity: O(n*2)

- Space: O(1)
 No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).
