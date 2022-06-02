#creamos el titulo del programa y lo centramos

print(" Calculadora ISPC ".center(50,"*"))
#creamos el menu
print("""
..: Seleccione la Opcion Deseada del siguiente Menu :..
1 - Sumar
2 - Restar
3 - Multiplicar
4 - Dividir
5 - Salir
""")
# iniciamos un bloque try ("intenta") para capturar el error en 
# caso de que el usuario ingrese otra cosa que no sea un numero
try:    
    #solicitamos el numero de opcion a verificar
    opcion = int(input("ingresa la opcion deseada: "))
#en el exept solo se ingresara en caso de que hubiese un error al seleccionar una opcion
except Exception as e:
    #indicamos al usuario el error
    print("Error, opcion incorrecta, elije una opcion del Menu")
#ingresamos al bloque else solo si no hubo un error previo 
else:

    #con el bloque de condicionales ingresamos nuevamente a otro bloque try...
    if opcion == 1:
        
        try:
            #solicitamos los datos para la operacion de la opcion 1
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
            num3 = float(input("Ingresa el tercer numero: "))
        except Exception as e:
            print("Error solo puedes digitar numeros!, vuelve a intentar")
        else:
            #realizamos la operacion
            resultado = num1 + num2 + num3
            #imprimimos con un "f" str ya que nos da la posibilidad de mostrar datos y 
            # variables de una forma mas prolija... la "\n" es para hacer un salto de linea.
            print(f"De la suma {num1} + {num2} + {num3} el resultado es : {resultado}\n")
elif opcion == 2:
        try:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
            num3 = float(input("Ingresa el tercer numero: "))
        except Exception as e:
            print("Error solo puedes digitar numeros!, vuelve a intentar")
        else:
            #realizamos la operacion
            resultado= num1 - num2  

            print(f"De la suma {num1} - {num2} +  el resultado es : {resultado}\n")
        pass
    elif opcion == 3:
        #a "pass" igual que a este comentario lo eliminan una vez que realicen su parte del codigo...
        # se coloca pass solo para continuar programando y luego rellenar esta porsion de codigom y asi evitar
        #que se rompa el prugrama al ejecutar para pribar la estructura y la primer funcion realizada.
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        print("Terminando operacion, Saliendo....\n")

# como el bloque finally siempre se ejecuta lo utilizamos para saludar al terminar la operacion al usuario
finally:
    print("Gracias por utilizar nuestro programa...")
        


