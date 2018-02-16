def fib(n): #Definimos la funcion de fibonacci
    n0=0    #Definimos nuestros numeros que generaran la sucesion de fibonacci
    n1=1
    suma = 0  #Suma comenzara en 0 para que tambien sea sumado jaja
    while n0 <= n:           
        #Poniendo coma hace que no se actualice la igualdad al momento es decir todo a la derecha son los valores anteriores
        n0, n1= n1, n0 + n1    #Acá se va generando la serie   
        if (n0 %2) == 1:       #Con el residuo igual a 1 nos tomamos los numeros impares de la sucesion
           suma += n0   #Sumamos el termino impar de la serie
        else:
            None   #Simplemente no hace nada por lo que regresa al while para que se genere el siguiente numero de la serie
    print(suma)   #Imprime el valor final de la suma de los numeros impares de la serie    
m = int(input("Ingresa un número menor o igual a 100000: ")) 
if m <= 100000: #Añadimos un if para que calcule hasta 100000
    print('La suma es ') 
    fib (m)
else:
    print('El número es mayor a 100000')
  