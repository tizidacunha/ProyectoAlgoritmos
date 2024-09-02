#FUNCIONES DEL COMPRADOR

producto = [["Manzana", 10, 100], ["Pera", 5, 25], ["Sprite", 4, 1000]]
banco = 0
#Actualmente se utiliza una lista en lista, luego se usara diccionarios y finalmente se usaran archivos!!!



def comprar_producto(banco):
    nombre = input("Ingrese el nombre del producto que quiera comprar o -1 para terminar: ")
    while nombre != "-1":
        encontrado = False #Variable bandera para saber si el producto esta o no en la lista
        for i in producto:
            if i[0] == nombre:
                
                encontrado = True  #Si se encontro el producto ya se le cambia el valor a la variable
                
                cantidad_compra = int(input("Cuanto desea comprar? "))
                while cantidad_compra < 1: #por si la cantidad de productos es negativa
                    print("Ingrese un valor valido ")
                    cantidad_compra = int(input("Cuanto desea comprar? "))
                
                if cantidad_compra < i[1]: #Compra menos del stock dispo
                    i[1] = i[1] - cantidad_compra #Se actualiza la cantidad de stock (i[1]) ya que el stock era mayor
                    banco = i[2] * cantidad_compra  #Se suma el dinero cobrado en el banco
                    
                elif cantidad_compra == i[1]: #Si compra justo la cantidad que habia en stock
                    contador = 0  #variable contador para borrar el producto
                    for i in producto:
                        if i[0] == nombre:  #Busca el producto pedido
                            banco += i[2] * i[1]  #Suma al banco el dinero cobrado
                            del producto[contador]  #Borra el producto de la lista ya que se agoto el stock
                            
                        contador += 1  #el contador seguira sumando hasta que i[0] sea igual al nombre
                    
                    
                else: #si solicita mas cantidad que el stock maximo
                    
                    print("Solo tenemos disponible en stock", i[1]) 
                    accion = input("Desea comprar lo disponible, ingrese si o no: ")
                    
                    if accion == "si" or accion == "Si":
                        contador = 0
                        for i in producto:  #funciona de la misma forma que el elif anterior
                            if i[0] == nombre: 
                                banco += i[2] * i[1]
                                del producto[contador]
                                
                            contador += 1
                        
                    else:
                        print("Gracias, Vuelva pronto!! ")

        
        if encontrado == False:  #Si se ingreso un producto que no estaba en la lista
            print("Producto no encontrado ingrese otro")

        nombre = input("Ingrese el nombre del producto que quiera comprar o -1 para terminar: ")
    
    return banco  #devuelve el valor que se ha cobrado en el banco
   

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

def iniciar_sesion():
    #Esta funcion permitira que el comprador inicie sesion para que guarden los productos en el carrito, haya una recomendacion de productos ya comprados
    pass

def pago():
    #Esta funcion permitira que el comprador pague al finalizar la compra (efectivo o otro metodo de pago)
    pass


def historial_compras():
    #Esta funcion permitira que el comprador tenga un registro de sus compras y las pueda volver a repetir
    pass