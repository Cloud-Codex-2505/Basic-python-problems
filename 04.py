# count the digits of a number

def numofdigits(num:int)->int:
    count=0
    while num!=0:
        num=num//10
        count+=1
    return count     