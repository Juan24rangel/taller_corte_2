# suma de digitos
#input
n = int (input("Digite el numero: "))

#processing

sum = 0
while n>0:
    sum = sum + n % 10
    n = n//10

#output
print ("el valor de la suma es: "+str(sum))