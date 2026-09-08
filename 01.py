# Sum of elements in an array

def sumofelements(arr:list[int])-> int:
    total=0
    n = len(arr)
    for i in range(n):
        total=total+arr[i]

    return total      

