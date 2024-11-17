import re


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def Recomendar_productos(compras_realizadas, usuario, historial_compra):
    """ Se corre la lista de historial de compras y se verifica si la ultima posicion de esta lista es igual al usuario, si 
    es igual se itera las listas en la posicion 1 y se verifica si este nombre no esta en la listas de compras realizadas """
    recomendar_productos = [item[0] for compra in historial_compra if compra[-1] == usuario for item in compra[:-1] if item[0] not in compras_realizadas]
    
    return recomendar_productos

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def actualizar_carrito(compras_realizadas, carrito):
    for i in compras_realizadas:
        producto_nombre = i[0]  # Nombre del producto
        producto_cantidad = i[1]  # Cantidad comprada del producto

        # Verificar si el producto ya está en el carrito
        producto_en_carrito = False
        for j in carrito:
            if j[0] == producto_nombre:  # Si el producto ya está en el carrito
                # Si el producto ya está en el carrito, solo agregamos la cantidad
                j[1] += producto_cantidad
                producto_en_carrito = True
                break
        
        # Si el producto no está en el carrito, lo agregamos como nuevo
        if not producto_en_carrito:
            carrito.append(i)

    return carrito

def comprar_producto(producto, carrito):
    compras_realizadas = []  # Almacena las compras antes de confirmar

    nombre = input("Ingrese el nombre del producto que quiera comprar o -1 para terminar: ").title()
    print(nombre)
    while nombre != "-1":
        encontrado = False
        for i in producto:
            if i[0] == nombre:
                encontrado = True
                
                if i[1] > 0:
                    cantidad_compra = int(input(f"¿Cuánto desea comprar? Tenemos {i[1]} en stock: "))
                    
                    while cantidad_compra < 1 or cantidad_compra > i[1]:
                        if cantidad_compra > i[1]:
                            print(f"No puedes comprar más de lo disponible en stock ({i[1]}).")
                        else:
                            print("Ingrese un valor válido.")
                        cantidad_compra = int(input(f"¿Cuánto desea comprar? Tenemos {i[1]} en stock: "))
                    
                    # Verificar si ya existe el producto en compras_realizadas
                    producto_en_carrito = False
                    for compra in compras_realizadas:
                        if compra[0] == i[0]:
                            nueva_cantidad = compra[1] + cantidad_compra
                            if nueva_cantidad <= i[1]:
                                compra[1] = nueva_cantidad  # Actualizar cantidad
                                print(f"Cantidad actualizada: {compra[1]} unidades de {i[0]} en el carrito.")
                            else:
                                print(f"No puedes comprar más de lo disponible ({i[1]} unidades).")
                            producto_en_carrito = True
                            break
                    
                    if not producto_en_carrito:
                        # Si no está en el carrito, agregarlo
                        compras_realizadas.append([i[0], cantidad_compra, i[2]])
                        print(f"{cantidad_compra} unidades de {i[0]} agregadas al carrito.")
                        i[1] = i[1] - cantidad_compra
                else:
                    print("Producto sin stock.")

        if not encontrado:
            print("Producto no encontrado, ingrese otro.")
        
        nombre = input("Ingrese el nombre del producto que quiera comprar o -1 para terminar: ").capitalize()

    compras_realizadas = actualizar_carrito(carrito=carrito, compras_realizadas=compras_realizadas)
    return compras_realizadas, producto
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def ver_productos(producto_aux):
    print()
    print("Productos: ")
    if producto_aux == []:
        print("No hay productos en stock")
    else:
        contador = 0
        for i in producto_aux:
            if i[1] > 0:
                print(f"{i[0]}, {i[1]}, ${i[2]}", end=" | ")
                contador += 1
                if contador % 5 == 0:  # Cada 5 productos, imprime una nueva línea
                    print("")
                    print("")
        if contador % 5 != 0:  # Si el último bloque no tiene exactamente 5 productos, termina la línea.
            print("")


def buscar_producto_similar(producto, carrito):

    nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ")
    nombre_buscar = nombre_buscar.lower()

    for j in producto:
        nombre_producto = j[0].lower() 
        contador = 0  

        for i in range(len(nombre_buscar)):
            if i < len(nombre_producto) and nombre_buscar[i] == nombre_producto[i]:
                contador += 1

        if contador > (len(nombre_buscar) // 2):
            print(f"Posible coincidencia encontrada: {j[0]} con {contador} coincidencias.")

            comprar = input(f"Desea comprar el siguiente producto: {j[0]}, ingrese si o no: ").lower()

            if comprar == "si":
                print(f'Ingrese el nombre ""{j[0]}" correctamente a continuacion..')
                carrito, producto = comprar_producto(producto, carrito)
            else:
                print("Muchas Gracias")

    return carrito





categorias = {
    "Comida": [
        "Manzana", "Pera", "Helado de vainilla"],
    "Bebida": [
        "Sprite"
    ],
    "Ropa": [
        "Camiseta Nike", "Pantalon Adidas"
    ],
    "Calzado": [
        "Zapatos Adidas"
    ],
    "Tecnología": [
        "Iphone 12", "Laptop Lenovo"
    ],
    "Electrónica": [
        "Audifonos Sony", "Camara Canon"
    ],
    "Muebles": [
        "Silla de oficina", "Mesa de comedor", "Colchon King Size"
    ],
    "Libros": [
        "Libro Harry Potter"
    ],
    "Cosmética": [
        "Perfume Chanel"
    ],
    "Vehículos": [
        "Moto Yamaha"
    ],
    "Deportes": [
        "Bicicleta Montaña", "Raqueta de tenis"
    ],
    "Juguetes": [
        "Juguete LEGO"
    ],
    "Electrodomésticos": [
        "Cafetera Nespresso"
    ],
    "Música": [
        "Guitarra Fender"
    ],
    "Hogar": [
        "Planta decorativa", "Set de toallas", "Lampara de escritorio"
    ],
    "Cocina": [
        "Juego de ollas"
    ]
}


def categoria():
    elegir_categoria = input("Ingrese el nombre de la categoria: ").capitalize()
    for i in categorias.keys():
        if i == elegir_categoria:
            print(categorias[elegir_categoria])
            for j in categorias[elegir_categoria]:
                for k in producto:
                    if j == k[0]:
                        print(k)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Se ultiliza en el 80%
def detalles_productos():
    # Esta función permitirá que el comprador vea detalles breves del producto que seleccione.
    
    producto_buscado = input("Por favor, introduce el nombre del producto que deseas buscar: ").strip()

    try:
        # Abrir el archivo que contiene los detalles de los productos
        with open('comprador/detalles_productos.txt', 'r') as archivo:
            # Leer cada línea del archivo
            lineas = archivo.readlines()
            

            for linea in lineas:
                if linea.lower().startswith(producto_buscado.lower()):
                    print(f"Detalle del producto '{producto_buscado}': {linea}")
                    return linea
            
            # Si no se encuentra el producto en el archivo
            print(f"Lo siento, no se encontró el producto '{producto_buscado}' en la lista.")
    except Exception:
        print("El archivo no fue encontrado.")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def gestionar_carrito(carrito, monto_total, producto):
    opcion = 1
    if not carrito:
        opcion = "5"
        print("")
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
                # Modificar cantidad de un producto en el carrito
                numero_producto = int(input("Ingrese el número del producto que desea modificar: ")) - 1
                
                if 0 <= numero_producto < len(carrito):   
                    nombre_producto = carrito[numero_producto][0]
                    nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {nombre_producto}: "))

                    if nueva_cantidad <= 0:
                        print("Debe ingresar una cantidad válida mayor a 0.")
                    else:
                        # Buscar el stock original en 'producto' (que no ha sido modificado)
                        for prod in producto:  # Usamos 'producto' en lugar de 'producto_aux' para el stock original
                            if prod[0] == nombre_producto:
                                stock_original = prod[1]  # Este es el stock disponible original
                                cantidad_actual_carrito = carrito[numero_producto][1]  # Cantidad ya en el carrito
                                
                                # Verificar si la nueva cantidad supera el stock original disponible
                                if nueva_cantidad <= stock_original + cantidad_actual_carrito:
                                    nueva_cantidad_producto = carrito[numero_producto][1] + producto[numero_producto][1] - nueva_cantidad
                                    # Actualizar la cantidad en el carrito
                                    carrito[numero_producto][1] = nueva_cantidad
                                    producto[numero_producto][1] = nueva_cantidad_producto
                                    print(f"La cantidad de {nombre_producto} ha sido actualizada a {nueva_cantidad}.")

                                    #producto_aux[numero_producto][1] = producto[numero_producto][1] - nueva_cantidad

                                else:
                                    print(f"No puedes comprar más de lo disponible en stock ({stock_original + cantidad_actual_carrito} unidades).")
                                break
                else:
                    print("Número de producto no válido.")

            elif opcion == "2":
                # Eliminar un producto del carrito
                numero_producto = int(input("Ingrese el número del producto que desea eliminar: ")) - 1
                if 0 <= numero_producto < len(carrito):
                    
                    nueva_cantidad_producto = carrito[numero_producto][1] + producto[numero_producto][1]
                    producto[numero_producto][1] = nueva_cantidad_producto
                    
                    producto_eliminado = carrito.pop(numero_producto)
                    print(f"{producto_eliminado[0]} ha sido eliminado del carrito.")
                else:
                    print("Número de producto no válido.")
            
            elif opcion == "3":
                # Vaciar todo el carrito y reponer los productos
                for i in carrito:
                    nombre_producto = i[0]
                    cantidad_carrito = i[1]
                    
                    # Buscar el producto en la lista de productos y reponer la cantidad
                    for producto_item in producto:
                        if producto_item[0] == nombre_producto:
                            producto_item[1] += cantidad_carrito
                            break
                
                carrito.clear()
                opcion = 4

                print("Todos los productos han sido eliminados del carrito y las cantidades han sido repuestas en la lista de productos.")

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


import json

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"usuarios": []}


def guardar_datos(archivo, datos):
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=4)


import re

def validar_usuario():
    patron_usuario = r'^[a-zA-Z][a-zA-Z0-9._]{2,15}$'
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        if re.match(patron_usuario, usuario):
            return usuario
        print("El nombre de usuario debe cumplir lo siguiente:")
        print("- Comenzar con una letra.")
        print("- Tener entre 3 y 16 caracteres.")
        print("- Solo puede incluir letras, números, guiones bajos (_) y puntos (.)")

def validar_contraseña():
    patron_contrasena = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$'
    while True:
        contrasena = input("Ingrese su contraseña: ")
        if re.match(patron_contrasena, contrasena):
            return contrasena
        print("La contraseña debe cumplir lo siguiente:")
        print("- Tener al menos 8 caracteres.")
        print("- Incluir al menos una letra minúscula.")
        print("- Incluir al menos una letra mayúscula.")
        print("- Incluir al menos un número.")
        print("- Incluir al menos un carácter especial (por ejemplo: !@#$%^&*).")




def iniciar_sesion(archivo_json):
    datos = cargar_datos(archivo_json)

    crear_iniciar = input("¿Desea crear cuenta (1) o iniciar sesión (2)? -1 para finalizar: ")

    if crear_iniciar == "1":
        usuario = validar_usuario()
        contrasena = validar_contraseña()
        
        if any(u['usuario'] == usuario for u in datos["usuarios"]):
            print("El usuario ya existe. Intente con otro nombre.")
        else:
            datos["usuarios"].append({"usuario": usuario, "contrasena": contrasena})
            guardar_datos(archivo_json, datos)
            print(f"Su cuenta ha sido creada con el usuario: {usuario}")

    elif crear_iniciar == "2":
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if any(u["usuario"] == usuario and u["contrasena"] == contrasena for u in datos["usuarios"]):
            print("¡Bienvenido!")
        else:
            print("Usuario o contraseña incorrectos.")

    elif crear_iniciar == "-1":
        print("Programa finalizado.")
    else:
        print("Opción no válida. Intente nuevamente.")



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pago(carrito):
    monto_total = 0
    for i in carrito:
        monto_total += i[1] * i[2]
        
    print(f"El monto total es: ${monto_total}")
    opcion = input("Desea pagar? ").lower()
    if opcion == "si":
        print("Para pagar necesita iniciar sesion o registrarse")
        iniciar_sesion(archivo_json='comprador/usuarios.json')

        print("Gracias por su compra!!")
        carrito.clear()
    else:
        print("Vuelva pronto!!")
    
    return monto_total, carrito


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def historial_compras():
    print("Proximamente...")
    #Esta funcion permitira que el comprador tenga un registro de sus compras y las pueda volver a repetir
    #Para esta funcion se necesita tener un archivo de datos, algo que agregaremos para la segunda entrega
    pass
