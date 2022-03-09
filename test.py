import math
import time

class Poo:
    def init(self, x):
        self.x=x

    def syracuse(self):
        U=self.x
        while U != 1:
            if U%2 == 0 :
                U = U // 2
            else :
                U = U*3 + 1
            print(U)
fichier = open("test.txt", "r")
a= int( fichier.readline())

#U = int(input("give the term u0 :"))
#print(U)


var1= Poo(a)  # self vaut les proprietes var1
var1.syracuse()
