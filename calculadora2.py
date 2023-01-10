from math import sqrt, sin , cos , tan

opcion = "si"

while opcion != "no":
    print(""" ><Calculadora><
          
          Operacion a realizar:"
          
          1) Sumar
          2) Restar 
          3) Multiplicar 
          4) Dividir
          5) Raiz
          6) Exponente
          7) Seno
          8) Coseno
          9) Tangente
          10) Salir de la calculadora 
          
          """)
    
    opcion = int(input("Ingresa la operacion:"))
    
    if opcion >= 10:
        print("gracias por usar mi calculadora")
        opcion = "no"
        
    else:
        x=int(input("Ingrese el primer numero para calcular: "))
        
        if opcion==1:
            y=int(input("Ingrese el segundo numero para calcular: "))
            print("la suma es ", x+y)
        elif opcion==2:
            y=int(input("Ingrese el segundo numero para calcular: "))
            print("la resta es ", x-y)
        elif opcion==3:
            y=int(input("Ingrese el segundo numero para calcular: "))
            print("la multiplicacion es ", x*y)
        elif opcion==4:
            y=int(input("Ingrese el segundo numero para calcular: "))
            print("la division es ",x/y)
        elif opcion==5:
            print("la raiz es ",sqrt(x))
        elif opcion==6:
            y=int(input("Ingrese el segundo numero para calcular: "))
            print("El exponente es ",x**y)
        elif opcion==7:
            print("El seno es ",sin(x))
        elif opcion==8:
            print("El coseno es ",cos(x))
        elif opcion==9:
            print("El tangente es ",tan(x))
    

        opcion = input("Desea realizar otra operacion 'si' o 'no': ")
   
    
   