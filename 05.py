# find maximum number in the array

def maxnum(arr:list[int])-> int:
    n= len(arr)
    max=arr[0]
    for i in range(n):
        if (arr[i]>max):
            max=arr[i]
    return max        

