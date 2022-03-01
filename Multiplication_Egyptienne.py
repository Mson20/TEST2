def multplication_egyptienne(a,b):
    i=0
    while a != 0:
        if (a%2) == 1:
            i=i+b
        b=b*2
        a=a//2
        return(i)
resultat=multplication_egyptienne(34,32)
print(resultat)            