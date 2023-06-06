n = int(input('Ingrese un numero: '))
a = 1
b = 1
c = 0
controlador = 0

if n <= 0:
    print('Error vuelva a ingresar un valor positivo')
elif n == 1:
    print(a)
else:
    while controlador < n:
        print(a)
        c = a + b
        a = b
        b = c
        controlador += 1