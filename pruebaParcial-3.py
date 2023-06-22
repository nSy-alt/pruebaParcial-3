def buscar(patenteSolicitada, autos):
    encontrado = 0
    for i in range((nro_autos+1)):
        if autos [i-1,1]==patenteSolicitada:
            print(autos[i-1])
            encontrado = 1
        
        if encontrado == 0:
            print("Valor no encontrado")

while True:
    print("Bienvenido a Auto Seguro")
    print("--"*20)
    print("Seleccione lo que desea hacer: ")
    print("1)Grabar")
    print("2)Buscar")
    print("3)Imprimir certificados")
    print("4)Salir")

    seleccion = int(input("Opcion escogida: "))

    print("--"*20)

    if seleccion == 4:
        break
    
    elif seleccion == 1: #ingresar datos
        nro_autos = 0
        if nro_autos == 0:
            autos = [["","","",0,0,"","",""]]
        else:
            autos.append(["","","",0,0,"","",""])
            nro_autos = nro_autos+1
            
        tipo = str(input("Ingrese Tipo vehiculo: "))
        patente = str(input("Ingrese patente Vehiculo: "))
        marca = "a"

        while len(marca)<2 or len(marca)>15:
            marca = str(input("Ingrese marca de vehiculo: "))
        
        precio = 0
        while precio<5000000:
            precio = int(input("Ingrese precio del vehiculo: "))

        montoMulta = int(input("Ingrese monto multa: "))
        fechaMulta = str(input("Ingrese Fecha multa: "))
        fechaRegistro = str(input("Ingrese Fecha registro: "))
        nombreDueno = str(input("Ingrese Nombre del dueño: "))

        autos[nro_autos, 0]= tipo
        autos[nro_autos, 1]= patente
        autos[nro_autos, 2]= marca
        autos[nro_autos, 3]= precio
        autos[nro_autos, 4]= montoMulta
        autos[nro_autos, 5]= fechaMulta
        autos[nro_autos, 6]= fechaRegistro
        autos[nro_autos, 7]= nombreDueno

        print(autos[nro_autos])
        

    elif seleccion == 2: #buscar datos vehiculo
        patenteSolicitada = str(input("indique patente a Buscar: "))
        buscar(patenteSolicitada, autos)

    elif seleccion == 3: #imprimir certificados
        print("--"*20)
        print("ERROR 404 - Not found")
        print("--"*20)
