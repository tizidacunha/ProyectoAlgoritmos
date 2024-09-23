producto = [["Manzana", 10, 100], ["Pera", 5, 25], ["Sprite", 4, 1000]]
historial_compra = [[("Manzana", 2), ("Pera", 2), "tizidac2004"]]
usuario_contrasena = [{"usuario": "tizidac2004", "contrasena": "admin"}]


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def Recomendar_productos(compras_realizadas, usuario):
    recomendar_productos = []
    for compra in historial_compra:
        if compra[-1] == usuario:
            for item in compra[:-1]:
                producto = item[0] 
                if producto not in compras_realizadas and producto not in recomendar_productos:  
                    recomendar_productos.append(producto)

    return recomendar_productos


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def comprar_producto(pago ,producto):
    nombre = input("Ingrese el nombre del producto que quiera comprar o -1 para terminar: ")
    compras_realizadas = [] 
    
    while nombre != "-1":
        encontrado = False
        for i in producto:
            if i[0] == nombre:
                encontrado = True
                
                cantidad_compra = int(input("¿Cuánto desea comprar? "))
                while cantidad_compra < 1:
                    print("Ingrese un valor válido.")
                    cantidad_compra = int(input("¿Cuánto desea comprar? "))
                
                if cantidad_compra < i[1]:
                    i[1] -= cantidad_compra
                    pago += i[2] * cantidad_compra
                    compras_realizadas.append((i[0], cantidad_compra))
                
                elif cantidad_compra == i[1]:
                    pago += i[2] * i[1]
                    compras_realizadas.append((i[0], i[1]))
                    del producto[producto.index(i)]
                    
                else:
                    print(f"Solo tenemos disponible en stock {i[1]}.")
                    accion = input("¿Desea comprar lo disponible? Ingrese 'si' o 'no': ")
                    
                    if accion.lower() == "si":
                        pago += i[2] * i[1]
                        compras_realizadas.append((i[0], i[1]))
                        del producto[producto.index(i)]
                    else:
                        print("Gracias, ¡Vuelva pronto!")
        
        if not encontrado:
            print("Producto no encontrado, ingrese otro.")

        nombre = input("Ingrese el nombre del producto que quiera comprar o -1 para terminar: ")
    
    return compras_realizadas, pago




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def ver_productos():
    print()
    print("Productos: ")
    if producto == []:
        print("No hay productos en stock")
    else:
        for i in producto:
            print("Nombre:", i[0]," , Cantidad: ", i[1]," y Precio: $", i[2])

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def detalles_productos():
    #Esta funcion permitira que el comprador vea unos detalles breves del producto que seleccione
    pass


# carrito = comprar_producto(banco=0, producto=producto)


carrito = [("Manzana", 10)]
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def gestionar_carrito(carrito):
    opcion = 1

    if not carrito:
        return print("El carrito está vacío.")
    
    while opcion != "4" :
        print("\nCarrito actual:")

        for i in range(len(carrito)):
            print(f"{i+1}. {carrito[i][0]}: {carrito[i][1]} unidades")



        print("\nOpciones del gestor del carrito:")
        print("1. Modificar cantidad de un producto")
        print("2. Eliminar un producto del carrito")
        print("3. Vaciar el carrito")
        print("4. Salir del gestor del carrito")

        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            # Modificar cantidad de un producto
            numero_producto = int(input("Ingrese el número del producto que desea modificar: ")) - 1
            if 0 <= numero_producto < len(carrito):
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {carrito[numero_producto][0]}: "))
                if nueva_cantidad <= 0:
                    print("Debe ingresar una cantidad válida mayor a 0.")
                else:
                    # Actualizar la cantidad en el carrito
                    producto, _ = carrito[numero_producto]
                    carrito[numero_producto] = (producto, nueva_cantidad)
                    print(f"La cantidad de {producto} ha sido actualizada a {nueva_cantidad}.")
            else:
                print("Número de producto no válido.")
        
        elif opcion == "2":
            # Eliminar un producto del carrito
            numero_producto = int(input("Ingrese el número del producto que desea eliminar: ")) - 1
            if 0 <= numero_producto < len(carrito):
                producto_eliminado = carrito.pop(numero_producto)
                print(f"{producto_eliminado[0]} ha sido eliminado del carrito.")
            else:
                print("Número de producto no válido.")
        
        elif opcion == "3":
            # Vaciar el carrito
            confirmar = input("¿Está seguro que desea vaciar el carrito? (si/no): ").lower()
            if confirmar == "si":
                carrito.clear()
                print("El carrito ha sido vaciado.")
                opcion = "4"  # Salir del carrito
        
        elif opcion == "4":
            # Salir del carrito
            print("Saliendo del gestor del carrito.")
        
        else:
            print("Opción no válida. Intente de nuevo.")


# gestionar_carrito(carrito)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def iniciar_sesion(compras_realizadas, usuario):
    crear_iniciar = input("Desea crear cuenta (1) o iniciar sesion (2). -1 para finalizar ? ")

    if crear_iniciar == "1":
        usuario = validar_usuario()
        contrasena = validar_contraseña()
        
        usuario_contrasena.append({"usuario": usuario, "contrasena": contrasena})
        historial_compra.append([*compras_realizadas, usuario]) 
        print(f"Su cuenta ha sido creada con el usuario: {usuario}")

    elif crear_iniciar == "2":
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contrasena: ")
        
        for credenciales in usuario_contrasena:
            if credenciales["usuario"] == usuario and credenciales["contrasena"] == contrasena:
                print("¡Bienvenido!")
                historial_compra.append([*compras_realizadas, usuario])
                


                productos_recomendados = Recomendar_productos(usuario=usuario, compras_realizadas=compras_realizadas)
                print("Productos que podrías considerar comprar nuevamente:")
                for producto in productos_recomendados:
                    if producto not in [compra[0] for compra in compras_realizadas]:
                        print(f"- {producto}")



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def validar_usuario():
    caracteres_especiales = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/"]

    valido = False 
    while valido == False:
        valido = True 

        #Se ingresa el nombre de usuario
        usuario = input("Ingrese su nombre de usuario: ")

        #Se valida que el usuario ya no se encuentre creado
        for i in usuario_contrasena:
            if i["usuario"] == usuario :
                print("Este usuario ya se encuentra")
                valido = False

        #Se valida que la cantidad maxima de caracteres sea 20
        if len(usuario) > 20:
            print("tiene que tener menos caracteres ")
            valido = False

        #Se valida que la cantidad minima de caracteres sea 8
        if len(usuario) < 8:
            print("tiene que tener mas caracteres ")
            valido = False

        #Se valida que el usuario solo contenga letras o numeros
        for i in usuario:
            if i in caracteres_especiales:
                print("no puede contener caracteres especiales el usuario ")
                valido = False

    return usuario



def validar_contraseña():
    valido = False 
    contador_caracteres = 0
    contador_mayusculas = 0
    contador_numeros = 0
    caracteres_especiales = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/"]


    while not valido:
        valido = True 

        contrasena = input("Ingrese su contraseña de usuario: ")

        #Valido que la contraseña tenga menos de 20 caracteres
        if len(contrasena) > 20:
            print("La contraseña tiene que tener menos de 20 caracteres.")
            valido = False

        #Valido que la contraseña tenga mas de 8 caracteres
        if len(contrasena) < 8:
            print("La contraseña tiene que tener al menos 5 caracteres.")
            valido = False

        #Valido la cantidad de caracteres especiales, mayusculas y numeros 
        for i in contrasena:
            if i in caracteres_especiales:
                contador_caracteres += 1
            if i.isalpha() and i == i.upper():
                contador_mayusculas += 1
            if i.isalnum():
                contador_numeros += 1


        if contador_caracteres < 2:
            print("La contraseña tiene que contener al menos 2 caracteres especiales.")
            valido = False

        if contador_mayusculas < 1:
            print("La contraseña tiene que contener al menos 1 letra mayúscula.")
            valido = False

        if contador_numeros < 1:
            print("La contraseña tiene que contener al menos 1 numero.")
            valido = False

    return contrasena

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_, dinero =comprar_producto(pago=0, producto=producto)



def validar_tarjeta():
    opcion = ""
    numero_tarjeta = input("Ingrese el numero de su tarjeta: ")

    while opcion != "transferencia" and opcion != "tarjeta":

        if numero_tarjeta[0] == "4" and (len(numero_tarjeta) == 13 or len(numero_tarjeta) == 16):
            tarjeta = "Visa"
            validar = True
        elif numero_tarjeta[0:2] in ['51', '52', '53', '54', '55'] and len(numero_tarjeta) == 16:
            tarjeta = "MasterCard"
            validar = True
        else:
            validar = False

        fecha_vencimiento = input("Ingrese la fecha de vencimiento MM/AAAA: ")
        fecha_hoy = "09/2024"

        if int(fecha_hoy[3:7]) > int(fecha_vencimiento[3:7]): 
            print("tarjeta vencida")
            validar = False
        elif int(fecha_hoy[3:7]) == int(fecha_vencimiento[3:7]) and int(fecha_hoy[0:2]) > int(fecha_vencimiento[0:2]):
            print("tarjeta vencida por mes")
            validar = False

        cvv = int(input("Ingrese el codigo de seguridad: "))
        if cvv < 0 or cvv > 999:
            print("codigo de seguridad incorrecto")
            validar = False
        
        if validar == True:
            opcion = "tarjeta"
        elif validar == False:
            opcion = int(input('''
Los datos de la tarjeta que ingreso son incorrectos:
Desea:
(1) Ingresar otros datos de tarjeta
(2)Pagar con transferencia: '''))

            while opcion !=1 or opcion !=2:
                opcion = int(input("Ingresa una opcion correcta))
                                   
            if opcion == 1:
                numero_tarjeta = input("Ingrese el numero de su tarjeta: ")
            else:
                print("Paga con transferencia")#pagar_transferencia()
                opcion = "tranferencia"
                tarjeta = None

    return opcion, tarjeta

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def calcular_descuento(monto_total, descuento):
    descuento = monto_total * descuento #0.10
    monto_con_descuento = monto_total - descuento
    return monto_con_descuento

def pago(monto_total):
    print(f"El monto total es: ${monto_total}")
    print("Selecciona el metodo de pago:")
    print("1. Tarjeta")
    print("2. Transferencia bancaria")

    opcion = input("Ingresa el numero de la opcion elegida: ")

    if opcion == "1":
        print("Elegiste pagar con tarjeta.")
        print("Te contamos que pagando con tarjeta Visa tienes un 5% de decuento y pagando con MasterCard tienes un 10%")
        tipo_pago, tipo_tarjeta = validar_tarjeta()
        if tipo_pago == "tarjeta":
            if tipo_tarjeta == "Visa":

                print(f"Se cobró ${calcular_descuento(monto_total, descuento= 0.05)} en tu tarjeta Visa.")
            elif tipo_tarjeta == "MasterCard":
                print(f"Se cobró ${calcular_descuento(monto_total, descuento= 0.10)} en tu tarjeta MasterCard.")
        else:
            opcion = "2"


    if opcion == "2":
        print("Elegiste pagar con transferencia bancaria.")
        cuenta = input("Ingresa tu número de cuenta: ")
        while len(cuenta) != 22:
            print("Ingresa un numero de cuenta correcto")
            cuenta = input("Ingresa tu número de cuenta: ")

        print(f"Recibiste un descuento del 20%. El monto final es: ${calcular_descuento(monto_total, descuento= 0.20)}")

    else:
        print("Opcion invalida. Intentalo de nuevo.")
        pago(monto_total)




    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def historial_compras():
    #Esta funcion permitira que el comprador tenga un registro de sus compras y las pueda volver a repetir
    #Para esta funcion se necesita tener un archivo de datos, algo que agregaremos para la segunda entrega
    pass



# iniciar_sesion(compras_realizadas=["Manzana"], usuario="tizidac2004")
