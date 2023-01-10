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
        y=int(input("Ingrese el segundo numero para calcular: "))
        if opcion==1:
            print("la suma es ", x+y)
        elif opcion==2:
            print("la resta es ", x-y)
        elif opcion==3:
            print("la multiplicacion es ", x*y)
        elif opcion==4:
            print("la division es ",x/y)
    

        opcion = input("Desea realizar otra operacion 'si' o 'no': ")
   
    
   