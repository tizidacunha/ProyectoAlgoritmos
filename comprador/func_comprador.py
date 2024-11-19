import re
from vendedor.func_vendedor import Gestion_de_pedidos
import random 

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
    """
    Actualiza el carrito de compras agregando nuevos productos o incrementando la cantidad 
    de productos existentes basándose en una lista de compras realizadas.
    """
    # Parámetros de entrada:
    # - compras_realizadas: Lista de listas con [nombre_producto, cantidad]
    # - carrito: Lista de listas actual con [nombre_producto, cantidad] 

    # Parámetro de salida:
    # - carrito actualizado: Lista de listas con productos, 
    #   donde se han sumado cantidades de productos repetidos o agregado productos nuevos

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
    """
    Gestiona el proceso de compra de productos, permitiendo al usuario 
    seleccionar productos, verificar stock y agregar al carrito de compras.
    """
    # Parámetros de entrada:
    # - producto: Lista de listas con [nombre, stock, precio]
    # - carrito: Carrito de compras actual

    # Parámetros de salida:
    # - compras_realizadas: Lista de productos agregados al carrito 
    # - producto: Lista de productos actualizada con stock modificado

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
        
        nombre = input("Ingrese el nombre del producto que quiera comprar o -1 para terminar: ").title()

    # Actualizar el carrito con las compras realizadas
    compras_realizadas = actualizar_carrito(carrito=carrito, compras_realizadas=compras_realizadas)
    return compras_realizadas, producto

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def ver_productos(producto_aux):
   """
   Muestra los productos disponibles en stock, 
   con un formato de impresión organizado en bloques de 5 productos.
   """
   # Parámetros de entrada:
    # - producto_aux: Lista de productos con [nombre, stock, precio]

    # Parámetro de salida:
    # - Impresión en pantalla de productos con stock disponible

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
   """
   Busca productos similares basándose en una coincidencia parcial de nombre, 
   permitiendo al usuario comprar un producto sugerido.
   """
   # Parámetros de entrada:
    # - producto: Lista de productos con [nombre, stock, precio]
    # - carrito: Carrito de compras actual

    # Parámetro de salida:
    # - carrito: Carrito de compras actualizado después de una posible compra

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
               print(f'Ingrese el nombre "{j[0]}" correctamente a continuacion..')
               carrito, producto = comprar_producto(producto, carrito)
           else:
               print("Muchas Gracias")
               input("Presione Enter para continuar")

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


def categoria(producto):
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
def detalles_productos():
   """
   Busca y muestra los detalles de un producto específico 
   desde un archivo de texto con información de productos.
   """

   # Parámetros de entrada:
    # - No recibe parámetros directamente, pero solicita un nombre de producto por input()

    # Parámetro de salida:
    # - Devuelve la línea del producto encontrado si existe
    # - Imprime los detalles del producto
    # - Si no encuentra el producto, imprime un mensaje de error

   producto_buscado = input("Por favor, introduce el nombre del producto que deseas buscar: ").strip()

   try:
       # Abrir el archivo que contiene los detalles de los productos
       with open('comprador/detalles_productos.txt', 'r') as archivo:
           # Leer cada línea del archivo
           lineas = archivo.readlines()
           

           for linea in lineas:
               if linea.lower().startswith(producto_buscado.lower()):
                   print(f"Detalle del producto '{producto_buscado}': {linea}")
                   
                   input("Presione Enter para continuar")
                   return linea
           
           # Si no se encuentra el producto en el archivo
           print(f"Lo siento, no se encontró el producto '{producto_buscado}' en la lista.")
       
   except Exception:
       print("El archivo no fue encontrado.")



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def gestionar_carrito(carrito, monto_total, producto, usuario):
   """
   Gestiona las operaciones del carrito de compras, permitiendo 
   modificar cantidades, eliminar productos, vaciar el carrito y realizar pagos.
   """
   # Parámetros de entrada:
    # - carrito: Lista de productos en el carrito
    # - monto_total: Monto total de la compra
    # - producto: Lista de productos disponibles
    # - usuario: Información del usuario

    # Parámetros de salida:
    # - monto_total: Monto total actualizado
    # - carrito: Carrito de compras modificado
    # - producto: Lista de productos actualizada
    # - usuario: Información de usuario potencialmente modificada

   opcion = 1
   if not carrito:
       opcion = "5"
       print("")
       print("El carrito está vacío.")
   
   while opcion != "5":
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
                       # Buscar el stock original en 'producto'
                       for prod in producto:
                           if prod[0] == nombre_producto:
                               stock_original = prod[1]
                               cantidad_actual_carrito = carrito[numero_producto][1]
                               
                               # Verificar si la nueva cantidad supera el stock original disponible
                               if nueva_cantidad <= stock_original + cantidad_actual_carrito:
                                   nueva_cantidad_producto = carrito[numero_producto][1] + producto[numero_producto][1] - nueva_cantidad
                                   # Actualizar la cantidad en el carrito
                                   carrito[numero_producto][1] = nueva_cantidad
                                   producto[numero_producto][1] = nueva_cantidad_producto
                                   print(f"La cantidad de {nombre_producto} ha sido actualizada a {nueva_cantidad}.")
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
               monto_total, carrito, usuario = pago(carrito, usuario)
           
           elif opcion == '5':
               # Salir del carrito
               print("Saliendo del gestor del carrito.")
               
           else:
               print("Opción no válida. Intente de nuevo.")

       input("Presione Enter para continuar")

   return monto_total, carrito, producto, usuario

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


import json

def cargar_datos(archivo):
   """
   Carga datos desde un archivo JSON, retornando los usuarios 
   o una lista vacía si el archivo no existe.
   """
   # cargar_datos():
    # - Entrada: ruta del archivo JSON
    # - Salida: diccionario de datos o estructura vacía

   try:
       with open(archivo, 'r') as f:
           return json.load(f)
   except FileNotFoundError:
       return {"usuarios": []}


def guardar_datos(archivo, datos):
   """
   Guarda datos en un archivo JSON con formato indentado.
   """
   # guardar_datos():
    # - Entrada: ruta del archivo JSON, datos a guardar
    # - Salida: None (guarda los datos en el archivo)

   with open(archivo, 'w') as f:
       json.dump(datos, f, indent=4)


def validar_usuario():
   """
   Solicita y valida un nombre de usuario según criterios específicos.
   """
   # validar_usuario():
    # - Entrada: None (input interactivo)
    # - Salida: nombre de usuario validado

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
   """
   Solicita y valida una contraseña según criterios de seguridad.
   """
   # validar_contraseña():
    # - Entrada: None (input interactivo)
    # - Salida: contraseña validada

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


def iniciar_sesion(archivo_json, usuario):
    """
    Gestiona el inicio de sesión y registro de usuarios.
    """
    # iniciar_sesion():
    # - Entrada: archivo JSON de usuarios, usuario actual
    # - Salida: usuario actualizado (nuevo, cerrado sesión, o sin cambios)

    if usuario:
        print("Usted ya ha iniciado sesión!")
        accion = input("¿Desea cerrar sesión? si o no: ").capitalize()
        if accion == "Si":
            usuario = ""
            print("Se cerró sesión correctamente.")
    else:
        datos = cargar_datos(archivo_json)

        crear_iniciar = input("¿Desea crear cuenta (1) o iniciar sesión (2)? -1 para finalizar: ")

        if crear_iniciar == "1":
            usuario = validar_usuario()
            contrasena = validar_contraseña()
            
            existe = False
            for u in datos["usuarios"]:
                if u["usuario"] == usuario:
                    existe = True
                    break

            if existe:
                print("El usuario ya existe. Intente con otro nombre.")
            else:
                datos["usuarios"].append({"usuario": usuario, "contrasena": contrasena})
                guardar_datos(archivo_json, datos)
                print(f"Su cuenta ha sido creada con el usuario: {usuario}")
                
        elif crear_iniciar == "2":
            contador = 1
            ingreso = False
            
            while contador <= 3 and ingreso == False:
                usuario = input("Ingrese su nombre de usuario: ")
                contrasena = input("Ingrese su contraseña: ")

                autenticado = False
                for u in datos["usuarios"]:
                    if u["usuario"] == usuario and u["contrasena"] == contrasena:
                        autenticado = True
                        break

                if autenticado:
                    print("¡Bienvenido!")
                    ingreso = True
                else:
                    print("Usuario o contraseña incorrectos.")
                    usuario = ""
                    contador += 1
                    print(f"Le quedan {4-contador} intentos! ")
            
            if not autenticado:
                print("Se le acabaron los intentos!!")      
                
        elif crear_iniciar == "-1":
            print("Programa finalizado.")
        else:
            print("Opción no válida. Intente nuevamente.")

    input("Presione Enter para continuar")
    return usuario



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pago(carrito, usuario):
   """
   Gestiona el proceso de pago, incluyendo cálculo de monto total, 
   verificación de inicio de sesión y registro de la compra.
   """
   # Parámetros de entrada:
    # - carrito: Lista de productos en el carrito de compras
    # - usuario: Nombre de usuario actual

    # Parámetros de salida:
    # - monto_total: Monto total de la compra
    # - carrito: Carrito vaciado después de la compra
    # - usuario: Nombre de usuario (puede cambiar si inicia sesión)

   monto_total = 0
   for i in carrito:
       monto_total += i[1] * i[2]
       
   print(f"El monto total es: ${monto_total}")
   opcion = input("Desea pagar? ").lower()
   if opcion == "si":
       if usuario == "" or not usuario:
           print("Para pagar necesita iniciar sesion o registrarse")
           print("carrito: " ,carrito)
           usuario = iniciar_sesion(archivo_json='comprador/usuarios.json', usuario=usuario)
       
       historial_compras(carrito, usuario)
       Gestion_de_pedidos(carrito, usuario)

       print("Gracias por su compra!!")
       carrito.clear()
   else:
       print("Vuelva pronto!!")
   
   input("Presione Enter para continuar")
   return monto_total, carrito, usuario


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def historial_compras(historial_carrito, usuario):
    """
    Gestiona el historial de compras de un usuario, 
    permitiendo registro y visualización de compras realizadas.
    """
    # Parámetros de entrada:
    # - historial_carrito: Lista de compras actuales [producto, cantidad, precio]
    # - usuario: Nombre de usuario actual

    # Parámetros de salida:
    # - usuario: Nombre de usuario (puede cambiar si inicia sesión)

    try:
        if not usuario:
            print("Para ver tu historial de compras debes iniciar sesión.")
            accion = input("¿Desea hacerlo? Ingrese si o no: ").capitalize()
            if accion == "Si":
                usuario = iniciar_sesion(archivo_json='comprador/usuarios.json', usuario=usuario)
            else:
                print("Muchas gracias")
                input("Presione Enter para continuar")
                return usuario

        if usuario:       
            # Intentar leer el archivo existente
            try:
                with open("historial.json", "r") as archivo:
                    historial = json.load(archivo)
            except (FileNotFoundError, json.JSONDecodeError):
                historial = []
            
            # Buscar el historial del usuario
            entrada_usuario = next((entrada for entrada in historial if entrada["usuario"] == usuario), None)
            
            if entrada_usuario:
                # Obtener el último número de compra
                ultimos_numeros = [int(k) for k in entrada_usuario["compras"].keys()]
                ultimo_numero = max(ultimos_numeros) if ultimos_numeros else 0

                # Actualizar o agregar productos al historial del usuario
                for producto, cantidad, precio in historial_carrito:
                    for num_compra, detalles in entrada_usuario["compras"].items():
                        if detalles["producto"] == producto:
                            # Actualizar cantidad y precio si ya existe
                            detalles["cantidad"] += cantidad
                            detalles["precio"] = precio
                            break
                    else:
                        # Producto nuevo
                        ultimo_numero += 1
                        entrada_usuario["compras"][str(ultimo_numero)] = {
                            "producto": producto,
                            "cantidad": cantidad,
                            "precio": precio
                        }
            else:
                # Si el usuario no existe, crear una nueva entrada
                nueva_venta = {
                    "compras": {
                        str(i + 1): {
                            "producto": producto,
                            "cantidad": cantidad,
                            "precio": precio
                        }
                        for i, (producto, cantidad, precio) in enumerate(historial_carrito)
                    },
                    "usuario": usuario
                }
                historial.append(nueva_venta)
            
            # Guardar el historial actualizado
            with open("historial.json", "w") as archivo:
                json.dump(historial, archivo, indent=4)
            
            # Mostrar el historial actualizado
            print(f"\nHistorial de compras para el usuario {usuario}:")
            print("-" * 50)

            entrada_usuario = next((entrada for entrada in historial if entrada["usuario"] == usuario), None)
            if entrada_usuario:
                total_gastado = 0
                for num_compra, detalles in entrada_usuario["compras"].items():
                    subtotal = detalles["cantidad"] * detalles["precio"]
                    total_gastado += subtotal
                    print(f"Compra #{num_compra}:")
                    print(f"  Producto: {detalles['producto']}")
                    print(f"  Cantidad: {detalles['cantidad']}")
                    print(f"  Precio unitario: ${detalles['precio']:.2f}")
                    print(f"  Subtotal: ${subtotal:.2f}")
                    print("-" * 30)
                print(f"Total gastado: ${total_gastado:.2f}")

            input("Presione Enter para continuar")
        return usuario

    except IOError as e:  # Error de archivo
        print(f"Error al manejar el archivo: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
