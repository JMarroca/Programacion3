#EJERCICIO 1
# x = "¡Hola a \'\" todas \"\' y \"\' todos!" 
# print(x)



# EJERCICIO 2
# username = input("Ingrese su Nombre: \n")
# print ("¡Hola ",username, "!")



# EJERCICIO 4
# print("|  A  |  B  |   Q   |")
# print(" ____________________")

# fil1 = 0 and 0
# fil2 = 0 or 1
# fil3 = 1 or 0
# fil4 = 1 and 1

# print("|  0  |  0  |  ",fil1,"  |")
# print(" ____________________")
# print("|  0  |  1  |  ",fil2,"  |")
# print(" ____________________")
# print("|  1  |  0  |  ",fil3,"  |")
# print(" ____________________")
# print("|  1  |  1  |  ",fil4,"  |")
# print(" ____________________")



# EJERCICIO 5
# horadia = float(input("¿Cuantas horas al dia recibe la \n clase de programacion III?\n "))
# vece = int(input("¿Cuantas veces a la semana recibe \n la clase de programacion III?\n "))
# horapr = float(input("¿Cual es su tiempo promedio \n que utiliza para estudiar?\n "))
# vecepr = int(input("¿Cuantas veces en la semana \n estudia por su cuenta?\n "))

# diat = horadia + horapr
# est = horapr * vecepr
# clasem = horadia * vece
# tot = est + clasem

# print ("\nLas horas que usuario estudia al dia es de ", diat ," horas")
# print ("\n\nLa cantidad total de horas que el usuario \n recibe programacion III en la semana es:  ", clasem ," horas")
# print ("\n\nPromedio de horas a la semana\n estudia por aparte es de: ", est, " horas")
# print ("\n\nTotal de horas utilizadas durante \n la semana para estudiar es de: ", tot ," horas")



# EJERCICIO 6
# m = int(input("Ingrese un numero entero: \n"))

# if m <= -1:
#     suma = m * (m+1)/2
#     print("La suma del numero negativo ",m," es igual a: ",suma)

# if m > 1:
#     for i in range(1, m):
#         m += i 

#     print("La suma de enteros es igual a: ",m)



# EJERCICIO 7
# peso = float(input("Ingrese su peso en libras:\n "))
# esta = float(input("Ingrese su estatura en metros: \n "))

# print("\nTu indice de masa corporal es: \n<IMC>  ","{0:.2f}".format(imc), "  <IMC>")



# EJERCICIO 8
# a = float(input("Ingrese un numero con punto decimal: \n"))
# b = float(input("Ingrese otro numero con punto decimal: \n "))

# c = a/b

# d = a % b
# print("\n\nEl cociente de la division entre ",a, "Y ",b," es: ",c)

# print("\nEl resto de la divison entre ",a, "Y ",b," es: ",d)

# print("\n\nEl cociente de la division entre ",a, "Y ",b,"con 3 decimales es: ","{0:.3f}".format(c))
# print("\nEl resto de la division entre ",a, "Y ",b,"con 3 decimales es: ","{0:.3f}".format(d))



#EJERCICIO 9
# print("El interes anual que manejamos es: \n A) Hasta Q.49,999.00 un 5% \n B) Mayor a Q.50,000.00 del 7%\n")
# inver = float(input("Ingrese su monto a invertir: \n"))
# year = int(input("Cantidad de años que invertira: \n "))

# if inver < 50000:
#     for i in range(year):
#         inver+=inver*0.05

#     print("Lo obtenido durante años fue de: Q.","{0:.2f}".format(inver),"\n\n")

# if inver > 50000:  
#     for i in range(year):
#         inver+=inver*0.07

        

#     print("Lo obtenido durante años fue de: Q.","{0:.2f}".format(inver),"\n\n")



# EJERCICIO 10
# print("Buenos dias, Ingrese los datos que se le solicitaran: \n\n")
# barre = int(input("Ingrese Cantidad de barrenos que estan siendo enviados: \n"))
# sierra = int(input("Ingrese Cantidad de sierras que estan siendo enviados: \n"))

# totbarre = barre * 11.2
# totsierra = sierra * 7.5

# total = totsierra + totbarre

# print("El peso total de los barrenos es de ","{0:.2f}".format(totbarre)," Kg.\n")
# print("El peso total de las sierras es de ","{0:.2f}".format(totsierra)," Kg.\n")
# print("El peso total del paquete que sera enviado es de ","{0:.2f}".format(total)," Kg.\n")



# EJERCICIO 11
# print("Precios: \n1)Memorias RAM nuevas a $.20.00 \n2) Memorias usadas tienen 60% de descuento\n\n\n")
# ram = int(input("Ingrese Cantidad de RAM vendidas que no son nuevas: \n"))
# print("El precio habitual de las RAM es de $.20.00 pero por ser usada tiene 60% descuento\n\n")

# des = (ram*20) * 0.40
# desto = (ram*20) * 0.60

# print("El descuento total que se le aplico a sus ventas fue de $.",des,"\n El total a pagar es de $.",desto)

