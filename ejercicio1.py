salir=False
while not salir:
    print("\nOPCIONES")
    print("1)Crear una Lista")
    print("2)Añadir un Dato")
    print("3)Eliminar un Dato")
    print("4)Modificar algun Dato")
    print("5)Mostrar los Datos")
    print("6)Mostar los Datos de Manera Inversa")
    print("7)Limpiar la Lista")
    print("8)Borrar Lista")
    print("9)Salir")
    opc=input("\n¿Que opcion desea realizar?  ")
                
        
    if(opc=='1'):

        if 'lista' in locals():
            print("\nYa Existe una Lista\n")
        else:
            lista=[]
            print("\nLista Creada\n")

    elif(opc=='2'):
        if 'lista' in locals():
            ll=input("Ingresa un Dato: ")
            lista.append(ll)
            print("\nDato Ingresado\n")
        else:
            print("\nNo Existe Una Lista\n")
            

    elif(opc=='3'):
        if 'lista' in locals():
            lista[0]=''
            print("\nDato no existente\n")
        else:
            print("\nNo Existe Una Lista\n")

    elif(opc=='4'):
        if 'lista' in locals():
            lista[0]=input('\nDato de replazo: ')
            print("\nDato Modificado\n")
        else:
            print("\nNo Existe Una Lista\n")

    elif(opc=='5'):
        if 'lista' in locals():
            print(lista)
        else:
            print("\nNo Existen Datos\n")

    elif(opc=='6'):
        if 'lista' in locals():
            for x in reversed(lista):
                print(x)
        else:
            print("\nNo Existen Datos\n")

    elif(opc=='7'):
        if 'lista' in locals():
            del(lista)
            lista=[]
            print("\nLista Vacia\n")
        else:
            print("\nNo Existen Datos\n")

    elif(opc=='8'):
        if 'lista' in locals():
            del(lista)
            print("\nLista Borrada\n")
        else:
            print("\nNo Existe Una Lista\n")

    elif(opc=='9'):
        salir=True
    else:
        print("\nOpcion Invalida, Por Favor Escoja una Opcion Valida\n\n")
