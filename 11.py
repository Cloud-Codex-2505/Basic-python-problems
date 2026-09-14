# two sum 
# [28,5,54,1,8,7], target=13



def two_sum(arr:list[int], target:int)->list[int]:
    n= len(arr)
    for i in range (n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return [i,j]
    return []            