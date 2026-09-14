# find the sum of even numbers nad odd numbers in an array


def evodsum(arr:list[int])->int,int:
    even_sum=0
    odd_sum=0
    for num in arr:
        if num%2==0:
            even_sum+=num
        else: 
            odd_sum+=num
    return even_sum,odd_sum        


