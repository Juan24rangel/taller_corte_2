# punto 2
#input
n = int(input("Digite el numero: "))

#processing
invertido = 0

while n>0:
    r = n%10
    invertido = invertido * 10 + r
    n = n//10

#output
print("el inverso es: "+str(invertido))