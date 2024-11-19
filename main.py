#PROGRAMA PRINCIAL
import os
#Aca se importaran todas las funciones del comprador y del vendedor

from comprador.func_comprador import comprar_producto, ver_productos, detalles_productos, gestionar_carrito, historial_compras, pago, iniciar_sesion, buscar_producto_similar
from vendedor.func_vendedor import Agregar_productos, Eliminar_productos, Editar_productos, Gestion_de_pedidos, estadisticas, papelera, ver_compras, Eliminar_pedido

producto = [
    ["Manzana", 10, 100],        # Comida
    ["Pera", 5, 25],             # Comida
    ["Sprite", 4, 1000],         # Bebida
    ["Camiseta Nike", 30, 50],   # Ropa
    ["Zapatos Adidas", 80, 20],  # Calzado
    ["Iphone 12", 800, 15],      # Tecnología
    ["Laptop Lenovo", 600, 10],  # Tecnología
    ["Audifonos Sony", 50, 200], # Electrónica
    ["Silla De Oficina", 120, 40],  # Muebles
    ["Mesa De Comedor", 250, 10],   # Muebles
    ["Libro Harry Potter", 15, 150], # Libros
    ["Perfume Chanel", 100, 35],    # Cosmética
    ["Moto Yamaha", 3000, 5],      # Vehículos
    ["Bicicleta Montaña", 500, 12], # Deportes
    ["Raqueta De Tenis", 75, 30],   # Deportes
    ["Helado De Vainilla", 3, 500], # Comida
    ["Juguete Lego", 40, 100],     # Juguetes
    ["Cafetera Nespresso", 150, 25], # Electrodomésticos
    ["Colchon King Size", 400, 8],  # Muebles
    ["Guitarra Fender", 600, 7],   # Música
    ["Planta Decorativa", 20, 100], # Hogar
    ["Juego De Ollas", 80, 30],     # Cocina
    ["Camara Canon", 900, 12],     # Electrónica
    ["Set De Toallas", 25, 60],     # Hogar
    ["Lampara De Escritorio", 35, 70] # Hogar
]

contrasena = "admin"
dinero = 0
carrito = []


def menu_vendedor():
    os.system('cls')
    print()
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                       Bienvenido al E-Commerce!!! ")
    print("")
    print('''Estas son las opciones disponibles: 
    1. Agregar un Producto || 2. Ver Stock || 3. Editar Producto || 4. Eliminar Producto || 5. Estadísticas || 6. Ver Pedidos || 7. Ver Papelera || 8. Eliminar Pedidos || 9. Ir a Comprador ''')
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



def menu_comprador():
    os.system('cls')
    print()
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                                                                                                                                                                            
    print("                                                     Bienvenido al E-Commerce!!! ")
    print("")
    print('''Estas son las opciones disponibles: 
    1. Comprar Productos || 2. Buscar Producto || 3. Detalles de Productos || 4. Carrito || 5. Historial Compra || 6. Iniciar Session || 7. Ir a Administrador''')
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def obtener_opcion_valida(min_valor, max_valor):
    """Obtiene y valida una opción numérica del usuario."""
    while True:
        try:
            accion = int(input(f"Ingrese una opción ({min_valor} a {max_valor}, -1 para salir): "))
            if accion == -1 or (min_valor <= accion <= max_valor):
                return accion
            print(f"Por favor ingrese un número entre {min_valor} y {max_valor}")
        except ValueError:
            print("Por favor ingrese un número válido")

def obtener_rol_valido():
    """Obtiene y valida el rol del usuario."""
    while True:
        rol = input("Ingrese quien sos: comprador o admin: ").capitalize()
        if rol in ["Comprador", "Admin"]:
            return rol
        print("Rol Inválido!")




#ARRANCA EL MENU
def main(carrito, producto, dinero):
    os.system('cls')
    accion = 0
    usuario = ""
      
    rol = obtener_rol_valido()
    
    while accion != -1:

        if rol == "Comprador":
            menu_comprador()
            print("")
            ver_productos(producto)

            accion = obtener_opcion_valida(1, 7)

            while rol != "Admin" and accion != -1: 
            
                if accion == 1:
                    carrito, producto = comprar_producto(producto=producto, carrito=carrito)
                elif accion == 2:
                    carrito = buscar_producto_similar(producto, carrito)
                elif accion == 3:
                    detalles_productos()
                elif accion == 4:
                    dinero, carrito, producto, usuario = gestionar_carrito(carrito=carrito,monto_total=dinero, producto=producto, usuario=usuario)
                elif accion == 5:
                    usuario = historial_compras(carrito, usuario)
                elif accion == 6:
                    usuario = iniciar_sesion(archivo_json='comprador/usuarios.json', usuario=usuario)
                elif accion ==7:
                    rol = "Admin"
                
                if accion != 7 and accion != -1:
                    
                    menu_comprador()
                    print("")
                    ver_productos(producto)
                    accion = obtener_opcion_valida(1,7)
                
            
        elif rol == "Admin":

            contador = 0
            clave = input("Ingrese la clave: ")

            while clave != contrasena and contador <2:

                contador += 1
                clave = input("Ingrese la clave correcta: ")

            if clave == contrasena:  

                menu_vendedor()
                accion = obtener_opcion_valida(1,9)
                    
                while accion >= 1 and accion <= 9 and rol != "Comprador":
                    
                
                    if accion == 1:
                        Agregar_productos(producto)
                        
                    elif accion == 2:
                        ver_productos(producto)
                    
                    elif accion ==3:
                        Editar_productos(producto)
                    
                    elif accion == 4:
                        Eliminar_productos(producto)
                    elif accion == 5:
                        estadisticas(banco=dinero, lista=producto )
                    elif accion == 6:
                        ver_compras()
                    elif accion == 7:
                        papelera(producto)
                    elif accion == 8:
                        Eliminar_pedido()
                    
                    elif accion == 9:
                        rol = "Comprador"

                    else:
                        print("accion no valida")
                
                    if accion != 9 and accion != -1:
                        menu_vendedor()
                        accion = obtener_opcion_valida(1,9)
                                
            else:
                print("Ladron!! ")
                accion = -1                
                

main(producto=producto, dinero=dinero, carrito=carrito)
