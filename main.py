#PROGRAMA PRINCIAL

#Aca se importaran todas las funciones del comprador y del vendedor

from comprador.func_comprador import comprar_producto, ver_productos, detalles_productos, gestionar_carrito, historial_compras, pago
from vendedor.func_vendedor import Agregar_productos, Eliminar_productos, Editar_productos, Gestion_de_pedidos, estadisticas
producto = [["Manzana", 10, 100], ["Pera", 5, 25], ["Sprite", 4, 1000]]
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
    7. Ir a Comprador''')
    print("-----------------------------------------------------------------------------------------------------------------------------")
    


def menu_comprador():
    print()
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("Bienvenido al kiosco Las Tias!!! ")
    print("")
    print('''Estas son las opciones disponibles: 
    1. Comprar Productos      
    2. Ver Productos
    3. Detalles de Productos
    4. Carrito / inciar sesion / Pago
    5. Historial Compra
    6. Ir a Administrador''')
    print("-----------------------------------------------------------------------------------------------------------------------------")
   
                 
#ARRANCA EL MENU
def main():
    global carrito
    global dinero
    accion = 0


    rol = input("Ingrese quien sos: comprador o admin: ")
    rol = rol.capitalize()
    
    while rol != "Comprador" and rol != "Admin" or not (rol.isalpha):
        print("Rol Invalido! ")
        rol = input("Ingrese un rol valido: Comprador o Admin: ")
        
    while accion != -1:

        if rol == "Comprador":
            menu_comprador()
            
            ingreso_numero = True
            while ingreso_numero:
                try:
                    accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                    while accion != -1 and not (accion >= 1 and accion <= 6):
                        print("Ingrese una accion valida")
                        accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                    ingreso_numero = False
                except ValueError:
                    print("Ingrese un numero del 1 al 6")

            while rol != "Admin" and accion != -1: 
            
                if accion == 1:
                    carrito, dinero = comprar_producto(dinero, producto)
                elif accion == 2:
                    ver_productos(producto)
                elif accion == 3:
                    detalles_productos()
                elif accion == 4:
                    gestionar_carrito(carrito=carrito,monto_total=dinero)
                elif accion == 5:
                    historial_compras()
                elif accion == 6:
                    rol = "Admin"
                
                if accion != 6 and accion != -1:
                    menu_comprador()
                    
                    ingreso_numero = True
                    while ingreso_numero:
                        try:
                            accion = int(input("Que desea hacer? o ingrese -1 para terminar: "))
                            while (accion < 1 or accion > 6) and (accion != -1):
                                print("Ingrese una accion valida")
                                accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                            ingreso_numero = False
                        except ValueError:
                            print("Ingres una opcion del 1 al 6")
                
                
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
                        while (accion < 1 or accion > 7) and (accion != -1):
                            print("Ingrese una accion valida")
                            accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                        ingreso_numero = False
                    except ValueError:
                        print("Ingrese una opcion del 1 al 7")
                    
                while accion >= 1 and accion <= 7 and rol != "Comprador":
                    
                
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
                        rol = "Comprador"

                    else:
                        print("accion no valida")
                
                    if accion != 7 and accion != -1:
                        menu_vendedor()
                        
                        ingreso_numero = True
                        while ingreso_numero:
                            try:
                                accion = int(input("Que desea hacer? o ingrese -1 para terminar: "))
                                while (accion < 1 or accion > 7) and (accion != -1):
                                    print("Ingrese una accion valida")
                                    accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                                ingreso_numero = False
                            except ValueError:
                                print("Ingrese una opcion valida")
                                
            else:
                print("Ladron!! ")
                accion = -1                
                

main()
