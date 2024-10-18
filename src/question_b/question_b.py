#write functions here, don't add input('') statements here!

def is_prime(num):
    answer=True

    for i in range (2,num):
        if num % i ==0:
            answer=False
    return answer