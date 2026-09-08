# sum of even numbers in an array

def evensum(arr:list[int])-> int:
    total=0
    length = len(arr)
    for i in range(length):
        if arr[i]%2 == 0:
            total= total+arr[i]

    return total        