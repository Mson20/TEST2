x=int(input("Veuillez entrer le premier terme :"))
 
while x !=1:
    if x%2 == 0 :
        x = x//2
    else:
        x =3*x + 1
    print(x)