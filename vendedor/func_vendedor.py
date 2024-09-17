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

def Eliminar_productos(lista):
    """En esta funcion se podra eliminar productos"""
    
    nombre = input("Ingrese el nombre del producto que quiera eliminar o -1 para terminar: ")
    while (not (nombre.isalpha())) and nombre != "-1": #para revisar que el nombre del producto ingresado no sea un numero
        print("Ingrese un nombre de producto en letras: ")
        nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")
    
    while nombre != "-1":
        
        encontrado = True
        for i in lista:
            if nombre == i[0]:
                lista.remove(i)
                print("El producto ha sido eliminado")

            else:
                encontrado = False
        
        if encontrado == False:
            print("Producto no encontrado")
        
        nombre = input("Ingrese el nombre del producto que quiera eliminar o -1 para terminar: ") 
        while (not (nombre.isalpha())) and nombre != "-1": #para revisar que el nombre del producto ingresado no sea un numero
            print("Ingrese un nombre de producto en letras: ")
            nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")      
    

def Editar_productos():
    """En esta funcion se podra editar productos"""
    pass
    
def Gestion_de_pedidos():
    """En esta funcion se podra gestionar los pedidos que lleguen del comprador"""
    pass



def estadisticas():
    """En esta funcion se podran ver las estadisticas de gastos/ganancias, y tambien lo recaudado en el banco"""
    pass
