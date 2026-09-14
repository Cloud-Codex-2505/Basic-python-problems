# factorial of a number

def fac(num:int)->int:
    f=1
    for i in range (1,num+1):
        f=f*i
    return f







    #using recursion

    def fac(num:int)->int:
        if num==0 or num==1:
            return 1
        else:
            return num*fac(num-1)    