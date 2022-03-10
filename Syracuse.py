from itertools import count


x=67
i=0

while x!=1:
    i=i+1
    if (x%2) == 0 :
        x=x//2
    else:
        x=x*3+1
    print(x)
print(i)