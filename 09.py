# armstrong number


def armstrong(num:int)->bool:
    sum=0
    l=len(num)
    while num!=0:
        r=num%10
        sum+=r**l
        num=num//10
    return sum==num   
