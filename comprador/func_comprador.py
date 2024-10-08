producto = [["Manzana", 10, 100], ["Pera", 5, 25], ["Sprite", 4, 1000]]
historial_compra = [[["Manzana", 2], ["Pera", 2], "tizidac2004"]]
usuario_contrasena = [{"usuario": "tizidac2004", "contrasena": "admin"}]
compras_realizadas = ["Manzana"]
import re


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def Recomendar_productos(compras_realizadas, usuario):
    """ Se corre la lista de historial de compras y se verifica si la ultima posicion de esta lista es igual al usuario, si 
    es igual se itera las listas en la posicion 1 y se verifica si este nombre no esta en la listas de compras realizadas """
    recomendar_productos = [item[0] for compra in historial_compra if compra[-1] == usuario for item in compra[:-1] if item[0] not in compras_realizadas]
    
    return recomendar_productos

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def comprar_producto(producto):
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
                    compras_realizadas.append([i[0], cantidad_compra, i[2]])
                
                elif cantidad_compra == i[1]:
                    compras_realizadas.append([i[0], i[1], i[2]])
                    
                else:
                    print(f"Solo tenemos disponible en stock {i[1]}.")
                    accion = input("¿Desea comprar lo disponible? Ingrese 'si' o 'no': ")
                    
                    if accion.lower() == "si":
                        compras_realizadas.append([i[0], i[1], i[2]])
                    else:
                        print("Gracias, ¡Vuelva pronto!")
        
        if not encontrado:
            print("Producto no encontrado, ingrese otro.")

        nombre = input("Ingrese el nombre del producto que quiera comprar o -1 para terminar: ")
    
    return compras_realizadas




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def ver_productos(producto):
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

#Se ultiliza en el 80%
def detalles_productos():
    #Esta funcion permitira que el comprador vea unos detalles breves del producto que seleccione
    pass


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def gestionar_carrito(carrito, monto_total, producto):
    opcion = 1
    if not carrito:
        opcion = "5"
        print("El carrito está vacío.")
    
    while opcion != "5" :
        if not carrito:
            print("El carrito está vacío.")
            opcion = "5"
        else:
            
            print("\nCarrito actual:")

            for i in range(len(carrito)):
                print(f"{i+1}. {carrito[i][0]}: {carrito[i][1]} unidades")



            print("\nOpciones del gestor del carrito:")
            print("1. Modificar cantidad de un producto")
            print("2. Eliminar un producto del carrito")
            print("3. Vaciar el carrito")
            print("4. Pago")
            print("5. Salir del gestor del carrito")

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
                        carrito[numero_producto][1] = nueva_cantidad
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
                monto_total, carrito, producto = pago(carrito)
            
            elif opcion == '5':
                # Salir del carrito
                print("Saliendo del gestor del carrito.")
                
            else:
                print("Opción no válida. Intente de nuevo.")

    return monto_total, carrito, producto

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def iniciar_sesion(compras_realizadas):
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
        if not re.match("^[a-zA-Z0-9]+$",usuario):
            print("El nombre del usuario solo puede contener letras y numeros, sin caracteres especiales.")
            valido = False

    return usuario

def validar_contraseña():
    
    valido = True
    contrasena = str(input("Ingrese la contraseña: "))
    especiales = r"[\\!\"#$%&'()*+,-./:;<=>?@\[\]^_`\{|\}~]"
    while valido:
        if re.search(especiales,contrasena) and re.search("[A-Z]",contrasena) and re.search("[0-9]",contrasena) and len(contrasena)>=8:
            valido = False
        else:
            print("La contrasena debe tener al menos: 1 numero, 1 mayuscula, 1 caracter especial y al menos 8 caracteres de largo")
            contrasena = (input("Ingrese la contraseña: ")) 
    
    return contrasena

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Se ultiliza en el 80%

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
                opcion = int(input("Ingresa una opcion correcta"))
                                   
            if opcion == 1:
                numero_tarjeta = input("Ingrese el numero de su tarjeta: ")
            else:
                print("Paga con transferencia")
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

def pago(carrito):
    monto_total = 0
    for i in carrito:
        monto_total += i[1] * i[2]
        
    print(f"El monto total es: ${monto_total}")
    opcion = input("Desea pagar? ").lower()
    if opcion == "si":
        print("Gracias por su compra!!")
        print(carrito)
        #[('Manzana', 3, 100)]
        #[["Manzana", 10, 100], ["Pera", 5, 25], ["Sprite", 4, 1000]]
        
        for i in carrito:
            for j in producto:
                if i[0] == j[0]:
                      
                    if i[1] < j[1]:
                        j[1] -= i[1]
                        compras_realizadas.append((i[0], i[1], i[2]))
                        
                    elif i[1] == j[1]:
                        compras_realizadas.append((i[0], i[1], i[2]))
                        del producto[producto.index(j)]
        
        carrito.clear()
    else:
        print("Vuelva pronto!!")
    
    '''        while cantidad_compra < 1:
                    print("Ingrese un valor válido.")
                    cantidad_compra = int(input("¿Cuánto desea comprar? "))
                
                if cantidad_compra < i[1]:
                    i[1] -= cantidad_compra
                    compras_realizadas.append((i[0], cantidad_compra, i[2]))
                
                elif cantidad_compra == i[1]:
                    compras_realizadas.append((i[0], i[1], i[2]))
                    del producto[producto.index(i)]
        carrito.clear()'''
        
    return monto_total, carrito, producto
    '''print("Selecciona el metodo de pago:")
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
'''



    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def historial_compras():
    print("Proximamente...")
    #Esta funcion permitira que el comprador tenga un registro de sus compras y las pueda volver a repetir
    #Para esta funcion se necesita tener un archivo de datos, algo que agregaremos para la segunda entrega
    pass
