#FUNCIONES DEL VENDEDOR DEL E-COMMERCE
import random
import json


def Agregar_productos(lista):
    
    #Parametro de entrada: lista (matriz de productos).
    #Parametro de salida: lista (matriz de productos).
    
    """En esta funcion se podra agregar productos"""
    
    nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ").title()
    
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
        
        nombre = input("Ingresa el nombre del producto, si desea terminar ingrese -1: ").title()

    input("Presione Enter para continuar")
    return lista

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def Eliminar_productos(lista):
    """En esta funcion se podra eliminar productos"""
    
    #Parametro de entrada: lista (matriz de productos).
    #Parametro de salida: lista (matriz de productos).
    
    lista_auxiliar = []
    
    nombre = input("Ingrese el nombre del producto que quiera eliminar o -1 para terminar: ").title()
    
    while nombre != "-1":
        
        encontrado = False
        for i in lista:
                        
            if nombre == i[0]:
                lista_auxiliar.append(i)
                lista.remove(i)
                print("El producto ha sido eliminado")
                encontrado = True
        
        if encontrado == False:
            print("Producto no encontrado")
        
        nombre = input("Ingrese el nombre del producto que quiera eliminar o -1 para terminar: ").title()

    #ENTREGA DEL 80%
    try:
        Archivo_papelera = open("papelera.csv","at")
        for i in lista_auxiliar: #Agrega al archivo uno por uno los elementos eliminados de la lista
            Archivo_papelera.write(f"{i};\n")
    
    except IOError:
        print("Error de generacion de archivo")
    finally:
        Archivo_papelera.close()


    input("Presione Enter para continuar")   
    return lista

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def Editar_productos(lista):
    """En esta funcion se podra editar productos"""
    
    #Parametro de entrada: lista (matriz de productos).
    #Parametro de salida: lista (matriz de productos).
    
    nombre = input("Ingrese el nombre del producto que quiera editar o -1 para terminar: ").title()
        
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

        nombre = input("Ingrese el nombre del producto que quiera editar o -1 para terminar: ").title()
                
    input("Presione Enter para continuar")
    return lista

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def Gestion_de_pedidos(historial_carrito,usuario):
    
    #Parametro de entrada: historial_carrito(productos comprados) y el usuario q la compro (cadena de texto).
    #Parametro de salida: Escribe la informacion de la venta hecha en un archivo.json
    
    
    try:
        with open("pedidos.json","r") as archivo: #lo abro en modo lectura para ver si existe el codigo compra
            compras = json.load(archivo)
            codigo_compra = random.randint(1000,9999)
            
            for i in compras:
                for clave,valor in i.items(): #i = diccionarios dentro de la lista grande del json
                    
                    if (clave == "codigo de compra") and (valor == codigo_compra):
                        
                        while valor == codigo_compra: #hasta que el valor de esa key cambie
                            codigo_compra = random.randint(1000,9999)
                            
                        
            
    except (FileNotFoundError, json.JSONDecodeError):
        codigo_compra = random.randint(1000,9999)
    


    venta ={
        "codigo de compra": codigo_compra
        ,
        "compras": {
            
            str(i+1): {
                "producto": producto,
                "cantidad": cantidad,
                "precio": precio
            }
            for i, (producto, cantidad, precio) in enumerate(historial_carrito)
        },
        "usuario": usuario
    }
        
    try:
        
        try:
            with open("pedidos.json","r") as archivo: #primero lo abro en modo lectura
                pedidos = json.load(archivo)
        
        except (FileNotFoundError, json.JSONDecodeError):
            pedidos = []
        
        pedidos.append(venta)
        
        with open("pedidos.json","w") as archivo:
            json.dump(pedidos,archivo, indent=4)

        input("Presione Enter para continuar")       
    except IOError:
        print("Error de generacion de archivo")



#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def estadisticas(banco,lista):
    """En esta funcion se podran ver las estadisticas de gastos/ganancias, y tambien lo recaudado en el banco"""
    
    #Parametros de entrada: banco (dinero cobrado) y lista (matriz de productos).
    #Parametros de salida: diccionario de estadisticas.
    
    try:
        with open("pedidos.json","r") as archivo: #lo abro en modo lectura para ver si existe el codigo compra
            compras = json.load(archivo)
            
            productos = []
            
            for i in compras:
                for clave,valor in i.items():
                    if clave == "compras":
                        for indice,contenido in valor.items():
                             
                            existia = False
                            nombre = contenido.get("producto") 
                            cantidad = contenido.get("cantidad")
                                
                            for j in productos:
                                if nombre == j[0]: #verifico si ya existe en la lista de productos, sumo la cantidad
                                    j[1] += cantidad
                                    existia = True
                                
                            if existia == False: #si existia sigue en false significa que no esta, por ende agrego la lista con el nombre y cant.
                                productos.append([nombre,cantidad])
                        
                

            cantidad_vendidos = list(map(lambda i : i[1], productos)) #agarro solo las cantidades
            
            mas_cantidad = max(cantidad_vendidos)
            menos_cantidad = min(cantidad_vendidos)
            
            mas_vendido = []
            menos_vendido = []
            
            for item in productos:
                if item[1] == mas_cantidad:
                    mas_vendido.append(item[0])
                    
                if item[1] == menos_cantidad:
                    menos_vendido.append(item[0])
            
            mas_vendido = ", ".join(mas_vendido) #por si hay mas de uno uso join para que quede bien en el print
            menos_vendido = ", ".join(menos_vendido)
            
            
        input("Presione Enter para continuar")                      
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error archivo vacio")
    
    
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
        print(clave,":",valor)
        
    input("Presione Enter para continuar")
    return estadisticas

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def papelera(lista):
    
    #Parametros de entrada: lista (matriz de productos)
    #Parametros de salida: lista actualizada() 
    
    try:
        Papelera = open("papelera.csv","rt")
        linea = Papelera.readline()
        campos = []
        campos.append(linea.strip(";\n"))
        for linea in Papelera:
            campos.append(linea.strip(";\n"))
    
    except IOError:
        print("Error de apertura de archivo")
    finally:
        Papelera.close()
  
    print()
    print("Papelera:")
    print()

    for indice_archivo, i in enumerate(campos):
        if i == "": #Si se abre la papelera antes de que se haya eliminado algo y esta vacia, esto evita que tome las comillas vacias como un elemento
            campos.remove(i)
            print("La papelera esta vacia")
            print()
        else:
            print(f"-{indice_archivo}: {i}\n")
    bandera=True
    while bandera:
        try:
            indice = int(input("Desea recuperar alguno de los elementos? Ingrese el numero de indice si es asi o -1 para salir: "))
            while (indice > len(campos)-1) or (indice < -1):
                print("Error de seleccion de indice")
                print()
                indice = int(input("Ingrese un numero entre el rango establecido: "))
            bandera=False
        except ValueError:
            print("Debe seleccionar un numero de indice")
    print()
    
    while indice != -1:
        producto = []
        for indice_archivo,i in enumerate(campos): #Uso de enumerate para los indices por si se repite el mismo producto
            if  indice==indice_archivo:
 
                cadena = i.strip("[]")
                            
                elementos = cadena.split(",")  
                
                for x in elementos:
                    
                    x=x.strip().strip("'")
                    if x.isdigit():
                        producto.append(int(x))
                    else:
                        producto.append(x)
                    
                lista.append(producto)
                campos.remove(i)
                campos.sort()
                
        for indice_archivo, i in enumerate(campos):
            print(f"-{indice_archivo}: {i}\n")
        
        bandera=True
        while bandera:
            try:
                indice = int(input("Desea recuperar otro de los elementos? Ingrese el numero de indice si es asi o -1 para salir: "))
                while (indice > len(campos)-1) or (indice < -1):
                    print("Error de seleccion de indice")
                    print()
                    indice = int(input("Ingrese un numero entre el rango establecido: "))
                bandera=False
            except ValueError:
                print("Debe seleccionar un numero de indice")
                
        try: #Reescribe el archivo sin el elemento que se recupera
            nueva_papelera = open("papelera.csv","wt")
            for i in campos:
                nueva_papelera.write(i+";"+"\n")
                
        except IOError:
            print("Error de generacion de archivo")
        finally:
            nueva_papelera.close()
    
    input("Presione Enter para continuar")
    return lista

def ver_compras():
    
    #Lee pedidos.json, si el usuario lo desea lo redirige a eliminar_pedidos()
    
    try:
        with open("pedidos.json","r") as archivo: #lo abro en modo lectura para ver si existe el codigo compra
            compras = json.load(archivo)
            
            for i in compras:
                for clave,valor in i.items(): #i = diccionarios dentro de la lista grande del json
                    
                    if (clave == "codigo de compra"):
                        print(f"- Compra: #{valor}\n")
            
            es_numero = False
            while es_numero == False:
                
                if compras == []:
                    
                    print("No hay pedidos disponibles")
                    break
                    
                else:
                    try:
                        codigo = int(input("Ingrese el codigo del pedido que desee ver o -1 para salir: "))
                        print()
                        es_numero = True
                    except ValueError:
                        print("Ingrese un numero entero de los que se le imprimio en pantalla")
                        print()
            
            if not compras == []:
            
                while codigo != -1:
                    existe = False         
                                                    
                    for i in compras:
                        for clave,valor in i.items(): #i = diccionarios dentro de la lista grande del json
                                
                            if clave == "codigo de compra":
                                codigos = valor
                            
                            if codigos == codigo:
                                if clave == "compras":
                                    for indice,contenido in valor.items(): #itera los distintos indices por producto, luego entra a cada producto
                                        print(f"-{indice}")
                                        print()
                                        for pedido,compra in contenido.items(): #va iterando en nombre producto precio
                                            print(pedido,":",compra)
                                            print()
                                            
                                        
                                
                                else:
                                    print(f"{clave} : {valor} ")
                                    print()
                                    existe = True
                    
                    if existe == False:
                        print(f"El codigo: #{codigo} no existe")
                            
                            
                    es_numero = False
                    while es_numero == False:
                        try:
                            codigo = int(input("Ingrese el codigo del pedido que desee ver o -1 para salir: "))
                            print()
                            es_numero = True
                        except ValueError:
                            print("Ingrese un numero entero de los que se le imprimio en pantalla")
                            print()
                
                
                eliminar = input("Desea eliminar algun pedido? ingrese si o no: ").capitalize()
                if eliminar == "Si":
                    Eliminar_pedido()
                        
        
    except (FileNotFoundError, json.JSONDecodeError):
        print("El archivo de pedidos esta vacio")

    input("Presione Enter para continuar")     


def Eliminar_pedido():
    
    #Modifica pedidos.json
    
    try:
        with open("pedidos.json","r") as archivo: #lo abro en modo lectura para ver si existe el codigo compra
            compras = json.load(archivo)
            
            
            for i in compras:
                for clave,valor in i.items(): #i = diccionarios dentro de la lista grande del json
                    
                    if (clave == "codigo de compra"):
                        print(f"- Compra: #{valor}\n")
            
            es_numero = False
            while es_numero == False:
                try:
                    codigo = int(input("Ingrese el codigo del pedido que desee eliminar o -1 para salir: "))
                    print()
                    es_numero = True
                except ValueError:
                    print("Ingrese un numero entero de los que se le imprimio en pantalla")
                    print()
                    
            while codigo != -1:
                existe = False         
                                                
                for i in compras[:]: #creo copia de compras para eliminar mientras itero
                        
                    if i.get("codigo de compra") == codigo: #el valor de la key codigo de compra
                        compras.remove(i)
                        Se_elimino = True
                        print("Pedido eliminado")
                        print()
                        existe = True


                if existe == False:
                    print(f"El codigo: #{codigo} no existe")
                        
                
                
                es_numero = False
                while es_numero == False:
                    try:
                        codigo = int(input("Ingrese el codigo del pedido que desee eliminar o -1 para salir: "))
                        print()
                        es_numero = True
                    except ValueError:
                        print("Ingrese un numero entero de los que se le imprimio en pantalla")
                        print()
                    
                            

    except (FileNotFoundError, json.JSONDecodeError):
        print("El archivo de pedidos esta vacio")
        Se_elimino = False
        
    if Se_elimino == True:
            
        try:
            with open("pedidos.json","w") as archivo: #lo abro en modo lectura para ver si existe el codigo compra
                json.dump(compras,archivo,indent=4)
                
            input("Presione Enter para continuar")                   
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error")
