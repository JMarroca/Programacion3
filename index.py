from arbol import Arbol

arbolfinal = Arbol(10)
arbolfinal.agregar(7)
arbolfinal.agregar(55)
arbolfinal.agregar(83)
arbolfinal.agregar(17)
arbolfinal.agregar(3)
arbolfinal.agregar(25)
arbolfinal.agregar(50)
arbolfinal.agregar(15)
arbolfinal.agregar(8)
arbolfinal.preorden()
arbolfinal.inorden()
arbolfinal.postorden()

opc = input("Quieres encontrar un numero en el arbol? ")

if opc == 's':
    busqueda = int(input("Ingresa el numero a buscar "))
    n = arbolfinal.buscar(busqueda)
    if n is None:
        print(busqueda," no se encuentra en el arbol")
    else:
        print(busqueda," esta en el arbol")
elif opc == 'n':
    print("Busqueda terminada")
else:
    print("Opcion invalida")