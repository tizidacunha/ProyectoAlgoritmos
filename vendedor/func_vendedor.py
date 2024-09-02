#FUNCIONES DEL VENDEDOR DEL E-COMMERCE

def Agregar_productos(lista):
    """En esta funcion se podra agregar productos"""
    
    nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")
    
    while nombre != "-1":
        producto_existente = False
        for i in lista:
            if nombre == i[0]:
                print("El producto ya existe")
                producto_existente = True

        if producto_existente == False:
                
            cantidad = int(input("Ingresa la cantidad del producto: "))
            while cantidad < 1:
                print("Ingrese una cantidad valida")
            precio = float(input("Ingresa el precio del producto: "))
            while precio <= 0:
                print("Ingrese un precio valido")
            lista.append([nombre, cantidad, precio])
        
        nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ")
    return lista

def Eliminar_productos():
    """En esta funcion se podra eliminar productos"""
    pass

def Editar_productos():
    """En esta funcion se podra editar productos"""
    pass
    
def Gestion_de_pedidos():
    """En esta funcion se podra gestionar los pedidos que lleguen del comprador"""
    pass



def estadisticas():
    """En esta funcion se podran ver las estadisticas de gastos/ganancias, y tambien lo recaudado en el banco"""
    pass
 