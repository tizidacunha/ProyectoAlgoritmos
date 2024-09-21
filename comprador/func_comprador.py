producto = [["Manzana", 10, 100], ["Pera", 5, 25], ["Sprite", 4, 1000]]
historial_compra = [[("Manzana", 2), ("Pera", 2), "tizidac2004"]]
usuario_contrasena = [{"usuario": "tizidac2004", "contrasena": "admin"}]


def Recomendar_productos(compras_realizadas, usuario):
    recomendar_productos = []
    for compra in historial_compra:
        if compra[-1] == usuario:
            for item in compra[:-1]:
                producto = item[0] 
                if producto not in compras_realizadas and producto not in recomendar_productos:  
                    recomendar_productos.append(producto)

    return recomendar_productos




def comprar_producto(banco ,producto):
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
                    banco += i[2] * cantidad_compra
                    compras_realizadas.append((i[0], cantidad_compra))
                
                elif cantidad_compra == i[1]:
                    banco += i[2] * i[1]
                    compras_realizadas.append((i[0], i[1]))
                    del producto[producto.index(i)]
                    
                else:
                    print(f"Solo tenemos disponible en stock {i[1]}.")
                    accion = input("¿Desea comprar lo disponible? Ingrese 'si' o 'no': ")
                    
                    if accion.lower() == "si":
                        banco += i[2] * i[1]
                        compras_realizadas.append((i[0], i[1]))
                        del producto[producto.index(i)]
                    else:
                        print("Gracias, ¡Vuelva pronto!")
        
        if not encontrado:
            print("Producto no encontrado, ingrese otro.")

        nombre = input("Ingrese el nombre del producto que quiera comprar o -1 para terminar: ")
    


def ver_productos():
    print()
    print("Productos: ")
    if producto == []:
        print("No hay productos en stock")
    else:
        for i in producto:
            print("Nombre:", i[0]," , Cantidad: ", i[1]," y Precio: $", i[2])


def detalles_productos():
    #Esta funcion permitira que el comprador vea unos detalles breves del producto que seleccione
    pass

def agregar_producto_carrito():
    #Esta funcion permitira que el comprador agregue productos al carrito
    #Estos pueden ser modificados dentro de este
    pass

def iniciar_sesion(compras_realizadas, usuario):
    crear_iniciar = input("Desea crear cuenta (1) o iniciar sesion (2). -1 para finalizar ? ")

    if crear_iniciar == "1":
        usuario = validar_usuario()
        contrasena = input("Ingrese su contrasena: ")
        
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

def validar_usuario():
    valido = False
    while valido == False:
        valido = True 
        usuario = input("Ingrese su nombre de usuario: ")

        for i in usuario_contrasena:
                if i["usuario"] == usuario :
                    print("Este usuario ya se encuentra")
                    valido = False

        if len(usuario) > 20:
            print("tiene que tener menos caracteres ")
            valido = False

        if len(usuario) < 5:
            print("tiene que tener mas caracteres ")
            valido = False

        caracteres_especiales = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/"]

        for i in usuario:
            if i in caracteres_especiales:
                print("no puede contener caracteres especiales el usuario ")
                valido = False

    return usuario


def pago():
    #Esta funcion permitira que el comprador pague al finalizar la compra (efectivo o otro metodo de pago)
    pass


def historial_compras():
    #Esta funcion permitira que el comprador tenga un registro de sus compras y las pueda volver a repetir
    pass



comprar_producto(banco=0, producto=producto)
# iniciar_sesion(compras_realizadas=["Manzana"], usuario="tizidac2004")