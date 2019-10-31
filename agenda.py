def menu():
    print('******MENU******')
    #print('1.- Crear Agenda')
    print('2.- Ingresar datos en la agenda')
    print('3.- Busqueda en Agenda')
    print('4.- Editar la Agenda')
    print('5.- Mostrar Agenda')
    print('6.- Salir')
    print()
 
def menu2():
    print('a.- Busqueda por nombre')
    print('b.- Busqueda por telefono')
    print('c.- Busqueda por email')
 
def menu3():
    print("Editar lista")
    print('1.- Eliminar un contacto')
    print('2.- Editar un contacto')

nombre_de_lista="Agenda"
directorio = []
telefonos = {}
nombres = {}
emailes = {}
apodos = {}
opcionmenu = 0
menu()
x=0
while opcionmenu != 6:
    opcionmenu = int(input("Inserta un numero para elegir una opcion: "))
    """if opcionmenu == 1:
    #    print('Ingrese el nombre de la lista:')
        #nombre_de_lista=input()
        #nombre_de_lista="Agenda"
        print("Agenda creada con exito")
        menu()"""
 
 
    #elif opcionmenu == 2:
    if opcionmenu == 2:
        print("Agregar: Nombre, telefono y email")
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        email = input("email: ")
        #apodo = input("Apodo: ")
        telefonos[nombre] = telefono
        nombres[telefono] = nombre
        emailes[email] = nombre
        directorio.append([nombre, telefono, email])
        menu()
 
    elif opcionmenu == 3:
        print("Busqueda")
        menu2()
        opcionmenu2 = input("Inserta una letra para elegir una opcion: ")
        if opcionmenu2=="a":
            nombre = input("Nombre: ")
            if nombre in telefonos:
                print("El telefono es", telefonos[nombre])
            else:
                print(nombre, "no se encuentra")
 
        if opcionmenu2=="b":
            telefono = input("Telefono: ")
            if telefono in nombres:
                print("El Nombre es", nombres[telefono])
            else:
                print(telefono, "no se encuentra")
 
        if opcionmenu2=="c":
            email = input("email: ")
            for linea in emailes:
                linea = linea.rstrip()
                if not linea.startswith(email) : continue
                palabras = linea.split()
                print()
            else:
                print(email, "no se encuentra")
        menu()
    elif opcionmenu == 4:
        menu3()
        opcionmenu3 = input("Inserta un numero para elegir una opcion: ")
        if opcionmenu3=="1":
            nombre = input("Nombre: ")
            if nombre in directorio[0:10]:
                print('borrado')
            else:
                print(nombre, "no encontrado")
        else:
            menu()
        menu()
 
    elif opcionmenu == 5:
 
        print("\nNombre de la Agenda: ",nombre_de_lista)
        print("     Nombre   ||   Telefono   ||   Email")
        for e in directorio:
            print("\nLa Agenda es: ",directorio)
        menu()
 
 
    elif opcionmenu == 6:
        exit()