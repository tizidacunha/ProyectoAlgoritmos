#PROGRAMA PRINCIAL

#Aca se importaran todas las funciones del comprador y del vendedor

from comprador.func_comprador import comprar_producto, ver_productos, detalles_productos, gestionar_carrito, historial_compras
from vendedor.func_vendedor import Agregar_productos, Eliminar_productos, Editar_productos, Gestion_de_pedidos, estadisticas


contrasena = "admin"






                      
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
    6. Ir a Comprador''')
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
    3. Ir a Administrador''')
    print("-----------------------------------------------------------------------------------------------------------------------------")
   
                 
#ARRANCA EL MENU
def main():
    accion = 0


    rol = input("Ingrese quien sos: comprador o admin: ")
    while rol != "comprador" and rol != "Comprador" and rol != "Admin" and rol != "admin":
        print("Rol Invalido! ")
        rol = input("Ingrese un rol valido: comprador o admin: ")
        
    while accion != -1:

        if rol == "comprador" or rol == "Comprador":
            menu_comprador()
            
            accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
            while accion != -1 and not (accion >= 1 and accion <= 5):
                print("Ingrese una accion valida")
                accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))

            while rol != "admin" and rol != "Admin" and accion != -1: 
            
                if accion == 1:
                    comprar_producto()
                elif accion == 2:
                    ver_productos()
                elif accion == 2:
                    detalles_productos()
                elif accion == 3:
                    gestionar_carrito()
                elif accion == 4:
                    historial_compras()
                elif accion == 5:
                    rol = "admin"
                
                if accion != 5 and accion != -1:
                    menu_comprador()
                    accion = int(input("Que desea hacer? o ingrese -1 para terminar: "))
                    while (accion < 1 or accion > 6) and (accion != -1):
                        print("Ingrese una accion valida")
                        accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                    
                
                
        elif rol == "admin" or rol == "Admin":

            contador = 0
            clave = input("Ingrese la clave: ")

            while clave != contrasena and contador <2:

                contador += 1
                clave = input("Ingrese la clave correcta: ")

            if clave == contrasena:  

                menu_vendedor()

                accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
                while (accion < 1 or accion > 7) and (accion != -1):
                    print("Ingrese una accion valida")
                    accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))

                while accion >= 1 and accion <= 7 and rol != "comprador" and rol != "Comprador":
                    
                
                    if accion == 1:
                        Agregar_productos()
                        
                    elif accion == 2:
                        ver_productos()
                    
                    elif accion ==3:
                        Editar_productos()
                    
                    elif accion == 4:
                        Eliminar_productos()
                    elif accion == 5:
                        estadisticas()
                    elif accion == 6:
                        Gestion_de_pedidos()
                    elif accion == 7:
                        rol = "Comprador"

                    else:
                        print("accion no valida")
                
                    if accion != 7 and accion != -1:
                        menu_vendedor()
                        accion = int(input("Que desea hacer? o ingrese -1 para terminar: "))
                        while (accion < 1 or accion > 7) and (accion != -1):
                            print("Ingrese una accion valida")
                            accion = int(input("Que desea hacer ? o ingrese -1 para terminar: "))
            else:
                print("Ladron!! ")
                accion = -1                
                

main()



