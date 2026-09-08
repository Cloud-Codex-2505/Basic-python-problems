# multiplication of elements

def pdtofelements(arr:list[int])-> int:
    product=1
    length= len(arr)
    for i in range(length):
        product= product* arr[i]

    return product    
