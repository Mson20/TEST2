def multplication_egyptienne(A,B):
    a=A
    b=B
    i=0
    while a != 0:
        if (a%2) == 1:
            i=i+b
        b=+b
        a=a//2
    return(i)
print(multplication_egyptienne(34,32))