#PROGRAMA PRINCIAL
import os
#Aca se importaran todas las funciones del comprador y del vendedor

from comprador.func_comprador import comprar_producto, ver_productos, detalles_productos, gestionar_carrito, historial_compras, pago, iniciar_sesion, buscar_producto_similar
from vendedor.func_vendedor import Agregar_productos, Eliminar_productos, Editar_productos, Gestion_de_pedidos, estadisticas, papelera

producto = [
    ["Manzana", 10, 100],        # Comida
    ["Pera", 5, 25],             # Comida
    ["Sprite", 4, 1000],         # Bebida
    ["Camiseta Nike", 30, 50],   # Ropa
    ["Zapatos Adidas", 80, 20],  # Calzado
    ["Iphone 12", 800, 15],      # Tecnología
    ["Laptop Lenovo", 600, 10],  # Tecnología
    ["Audifonos Sony", 50, 200], # Electrónica
    ["Silla de oficina", 120, 40],  # Muebles
    ["Mesa de comedor", 250, 10],   # Muebles
    ["Libro Harry Potter", 15, 150], # Libros
    ["Perfume Chanel", 100, 35],    # Cosmética
    ["Moto Yamaha", 3000, 5],      # Vehículos
    ["Bicicleta Montaña", 500, 12], # Deportes
    ["Raqueta de tenis", 75, 30],   # Deportes
    ["Helado de vainilla", 3, 500], # Comida
    ["Juguete LEGO", 40, 100],     # Juguetes
    ["Cafetera Nespresso", 150, 25], # Electrodomésticos
    ["Colchon King Size", 400, 8],  # Muebles
    ["Guitarra Fender", 600, 7],   # Música
    ["Planta decorativa", 20, 100], # Hogar
    ["Juego de ollas", 80, 30],     # Cocina
    ["Camara Canon", 900, 12],     # Electrónica
    ["Set de toallas", 25, 60],     # Hogar
    ["Lampara de escritorio", 35, 70] # Hogar
]

contrasena = "admin"
dinero = 0
carrito = []


                      
def menu_vendedor():
    print()
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("Bienvenido al E-Commerc!!! ")
    print("")
    print('''Estas son las opciones disponibles: 
          
    1. Agregar un producto:
    2. Ver Stock       
    3. Editar Producto
    4. Eliminar Producto
    5. Estadisticas
    6. Gestionar pedidos
    7. Ver papelera
    8. Ir a Comprador''')
    print("-----------------------------------------------------------------------------------------------------------------------------")
    


def menu_comprador():
    print()
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                                                                                                                                                                                
    print("                                                     Bienvenido al kiosco Las Tias!!! ")
    print("")
    print('''Estas son las opciones disponibles: 
    1. Comprar Productos || 2. Buscar Producto || 3. Detalles de Productos || 4. Carrito || 5. Historial || Historial Compra || 6. Iniciar Session || 7. Ir a Administrador''')
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

                 
#ARRANCA EL MENU
def main(carrito, producto, dinero):
    os.system('cls')
    accion = 0


    rol = input("Ingrese quien sos: comprador o admin: ")
    rol = rol.capitalize()
    
    while rol != "Comprador" and rol != "Admin" or not (rol.isalpha):
        print("Rol Invalido! ")
        rol = input("Ingrese un rol valido: Comprador o Admin: ")
    
    while accion != -1:

        if rol == "Comprador":
            menu_comprador()
            print("")
            ver_productos(producto)

            ingreso_numero = True
            while ingreso_numero:
                try:
                    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    input("")
                    accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                    while accion != -1 and not (accion >= 1 and accion <= 7):
                        print("Ingrese una accion valida")
                        accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                    ingreso_numero = False
                except ValueError:
                    print("Ingrese un numero del 1 al 7")

            while rol != "Admin" and accion != -1: 
            
                if accion == 1:
                    carrito, producto = comprar_producto(producto)
                elif accion == 2:
                    encontrado = buscar_producto_similar(producto)
                    encontradO, nombre = encontrado

                    if encontradO == True:
                        comprar = input(f"Desea comprar el siguiente producto: {nombre}, ingrese si o no: ").lower()

                        if comprar == "si":
                            carrito, producto = comprar_producto(producto)
                        else:
                            print("Muchas Gracias")

                elif accion == 3:
                    detalles_productos()
                elif accion == 4:
                    dinero, carrito, producto = gestionar_carrito(carrito=carrito,monto_total=dinero, producto=producto)
                elif accion == 5:
                    historial_compras()
                elif accion == 6:
                    iniciar_sesion(carrito)
                elif accion ==7:
                    rol = "Admin"
                
                if accion != 7 and accion != -1:
                    input("")
                    menu_comprador()
                    print("")
                    ver_productos(producto)
                    
                    ingreso_numero = True
                    while ingreso_numero:
                        try:
                            accion = int(input("Que desea hacer? o ingrese -1 para terminar: "))
                            while (accion < 1 or accion > 7) and (accion != -1):
                                print("Ingrese una accion valida")
                                accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                            ingreso_numero = False
                        except ValueError:
                            print("Ingres una opcion del 1 al 7")
                
                

        elif rol == "Admin":

            contador = 0
            clave = input("Ingrese la clave: ")

            while clave != contrasena and contador <2:

                contador += 1
                clave = input("Ingrese la clave correcta: ")

            if clave == contrasena:  

                menu_vendedor()

                ingreso_numero = True
                while ingreso_numero:
                    try:
                        accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                        while (accion < 1 or accion > 8) and (accion != -1):
                            print("Ingrese una accion valida")
                            accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                        ingreso_numero = False
                    except ValueError:
                        print("Ingrese una opcion del 1 al 7")
                    
                while accion >= 1 and accion <= 8 and rol != "Comprador":
                    
                
                    if accion == 1:
                        Agregar_productos(producto)
                        
                    elif accion == 2:
                        ver_productos(producto)
                    
                    elif accion ==3:
                        Editar_productos(producto)
                    
                    elif accion == 4:
                        Eliminar_productos(producto)
                    elif accion == 5:
                        estadisticas(mas_vendido="Manzana", menos_vendido="Pera", lista=producto, banco=dinero)
                    elif accion == 6:
                        Gestion_de_pedidos()
                    elif accion == 7:
                        producto = papelera(producto)
                    elif accion == 8:
                        rol = "Comprador"

                    else:
                        print("accion no valida")
                
                    if accion != 8 and accion != -1:
                        menu_vendedor()
                        
                        ingreso_numero = True
                        while ingreso_numero:
                            try:
                                accion = int(input("Que desea hacer? o ingrese -1 para terminar: "))
                                while (accion < 1 or accion > 8) and (accion != -1):
                                    print("Ingrese una accion valida")
                                    accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                                ingreso_numero = False
                            except ValueError:
                                print("Ingrese una opcion valida")
                                
            else:
                print("Ladron!! ")
                accion = -1                
                

main(producto=producto, dinero=dinero, carrito=carrito)
