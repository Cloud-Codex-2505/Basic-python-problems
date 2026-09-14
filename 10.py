#prime number


def prime_number(num:int)->bool:
    if num<2:
        print("Not Prime")
    else:
        is_prime= True
    for i in range (2,num**(0.5)+1):
        if num%i==0:
            is_prime= False
            break
    return is_prime                    
