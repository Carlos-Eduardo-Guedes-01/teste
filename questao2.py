valor=13
fib=0
ant=0
aux=1
if(fib==valor):
    print('O número ',fib,' pertence a sequência')
print(fib)
while(fib<=(valor+1)):
    if(fib==valor):
        print('O número ',fib,' pertence a sequência')
    print(fib)
    fib=ant+aux
    aux=ant
    ant=fib
    