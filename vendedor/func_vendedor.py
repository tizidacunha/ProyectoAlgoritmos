#FUNCIONES DEL VENDEDOR DEL E-COMMERCE

def Agregar_productos(lista):
    """En esta funcion se podra agregar productos"""
    
    nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")
    while (not (nombre.isalpha())) and nombre != "-1": #para revisar que el nombre del producto ingresado no sea un numero
        print("Ingrese un nombre de producto en letras: ")
        nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")
        
    nombre = nombre.capitalize()   #Para que el nombre quede registrado solo con la primer letra mayuscula
    
    while nombre != "-1":
        producto_existente = False
        for i in lista:
            if nombre == i[0]:
                print("El producto ya existe")
                producto_existente = True

        if producto_existente == False:
            
            son_numeros = True
            while son_numeros:
                try:
                    cantidad = int(input("Ingresa la cantidad del producto: "))
                    while cantidad < 1:
                        print("Ingrese una cantidad valida")
                        cantidad = int(input("Ingresa la cantidad del producto: "))
                    son_numeros = False
                except ValueError:
                        print("Ingrese la cantidad en numeros")
                    
                    
            son_numeros = True
            while son_numeros:
                try:
                    precio = float(input("Ingresa el precio del producto: "))
                    while precio <= 0:
                        print("Ingrese un precio valido")
                        precio = float(input("Ingresa el precio del producto: "))
                    son_numeros = False
                except ValueError:
                    print("Ingrese el precio en numeros")                    
                
            
            lista.append([nombre, cantidad, precio])
        
        nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")
        while not (nombre.isalpha()) and nombre != "-1": #para revisar que el nombre del producto ingresado no sea un numero
            print("Ingrese un nombre de producto en letras: ")
            nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")
    return lista

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def Eliminar_productos(lista):
    """En esta funcion se podra eliminar productos"""
    
    nombre = input("Ingrese el nombre del producto que quiera eliminar o -1 para terminar: ")
    while (not (nombre.isalpha())) and nombre != "-1": #para revisar que el nombre del producto ingresado no sea un numero
        print("Ingrese un nombre de producto en letras: ")
        nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")
    
    while nombre != "-1":
        
        encontrado = False
        for i in lista:
            if nombre == i[0]:
                lista.remove(i)
                print("El producto ha sido eliminado")
                encontrado = True
        
        if encontrado == False:
            print("Producto no encontrado")
        
        nombre = input("Ingrese el nombre del producto que quiera eliminar o -1 para terminar: ") 
        while (not (nombre.isalpha())) and nombre != "-1": #para revisar que el nombre del producto ingresado no sea un numero
            print("Ingrese un nombre de producto en letras: ")
            nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")      
    
    return lista

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def Editar_productos(lista):
    """En esta funcion se podra editar productos"""
    
    nombre = input("Ingrese el nombre del producto que quiera editar o -1 para terminar: ")
    while (not (nombre.isalpha())) and nombre != "-1": #para revisar que el nombre del producto ingresado no sea un numero
        print("Ingrese un nombre de producto en letras: ")
        nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")
        
    while nombre != "-1":
        encontrado = False
        for i in lista:
            if i[0] == nombre: #Selecciona el producto que quiere editar
                encontrado = True
                
                ingreso_numeros = True
                while ingreso_numeros: #Bucle while para que elija una opcion del 1 al 3, y no una letra
                    try:
                        editar = int(input("Que desea editar? Nombre(1), cantidad(2) o precio(3): ")) #que cosa quiere editar
                        while editar < 1 or editar > 3:
                            print("Ingrese un valor valido ")
                            editar = int(input("Que desea editar? Nombre(1), cantidad(2) o precio(3): "))
                        ingreso_numeros = False
                        
                    except ValueError:
                        print("Ingrese 1 para nombre, 2 para cantidad o 3 para precio como se indico antes")
                    
                if editar == 1:
                                
                    nombre_nuevo = input("Ingrese el nombre nuevo: ")
                    while (nombre_nuevo == i[0]) or (not(nombre_nuevo.isalpha())):
                        print("No puede ingresar el mismo nombre y debe ingresarlo en letras")
                        nombre_nuevo = input("Ingrese el nombre nuevo: ")
                    i[0] = nombre_nuevo #cambia el nombre
                    
                    
                elif editar == 2:
                    
                    ingreso_numeros = True
                    while ingreso_numeros:
                        try:
                            cantidad_nueva= int(input("Ingrese el nuevo stock: "))
                            while cantidad_nueva < 1 or cantidad_nueva == i[1]: #por si el stock es negativo
                                print("Ingrese una cantidad valida ")
                                cantidad_nueva= int(input("Ingrese el nuevo stock: ")) #cambia el stock
                            i[1] = cantidad_nueva #reemplaza la cantidad
                            ingreso_numeros = False
                        except ValueError:
                            print("Ingrese la cantidad en numeros")
                    
                else:
                    
                    ingreso_numeros = True
                    while ingreso_numeros:
                        try:
                            precio_nuevo= int(input("Ingrese el precio nuevo: "))
                            while precio_nuevo < 1 or precio_nuevo == i[2]:
                                print("Ingrese un precio valido ") #por si el precio es negativo
                                precio_nuevo= int(input("Ingrese el precio nuevo: "))
                            i[2] = precio_nuevo #cambia el precio
                            ingreso_numeros = False
                        except ValueError:
                            print("Ingrese la cantidad en numeros")

        if not encontrado:
            print("Producto no encontrado ingrese otro")

        nombre = input("Ingrese el nombre del producto que quiera editar o -1 para terminar: ")
            
        while (not (nombre.isalpha())) and nombre != "-1": #para revisar que el nombre del producto ingresado no sea un numero
            print("Ingrese un nombre de producto en letras: ")
            nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")
    
    return lista

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
    
def Gestion_de_pedidos():
    """En esta funcion se podra gestionar los pedidos que lleguen del comprador"""
    pass

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------



def estadisticas(mas_vendido,menos_vendido,banco,lista):
    """En esta funcion se podran ver las estadisticas de gastos/ganancias, y tambien lo recaudado en el banco"""
    
    estadisticas = {

        "dinero" : banco,
        "producto mas vendido": mas_vendido,
        "producto menos vendido": menos_vendido,
    }
    
    try:
        cantidades = list(map(lambda i : i[1], lista))
        precios = list(map(lambda i : i[2], lista))
        
        mayor_stock = max(cantidades)
        menor_stock = min(cantidades)
        mayor_precio = max(precios)
        menor_precio = min(precios)
        
        precios_y_stocks = {            
            "Mayor Precio": mayor_precio,
            "Menor Precio": menor_precio,
            "Mayor stock":mayor_stock,
            "Menor stock":menor_stock
        }
        
        print("")
        estadisticas.update(precios_y_stocks)
        
    except IndexError:
        print("No hay productos en el almacen")
    
    for clave,valor in estadisticas.items():
        print(clave,";",valor)
    
    return estadisticas

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------