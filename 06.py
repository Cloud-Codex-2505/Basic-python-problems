# find the second maximum numbe in the array

def secondmax(arr:list[int])->int:
    max_num=float("-inf")
    second_max_num=float("-inf")
    for num in arr:
        if num>max_num :
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num 
    return second_max_num           