from vendedor.func_vendedor import Agregar_productos, Editar_productos, Eliminar_productos, Gestion_de_pedidos,estadisticas,Eliminar_pedido,ver_compras
import unittest
from unittest.mock import patch
import json

#VALIDO AGREGAR PRODUCTOS

def test_agregar_productos():
    
    lista = []
    
    with patch('builtins.input', side_effect=["sprite",10,1000,"-1","a"]):
        with patch('builtins.print'):
            resultado=Agregar_productos(lista)
                                    
    assert len(resultado) == 1 #verifico haya un elemento
    assert ["Sprite",10,1000] in resultado #verifico que este en la lista

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

#VALIDO EDICIONES DEL PRODUCTO

def test_editar_nombre():
    
    lista = [["Manzana",10,100]]
    
    with patch('builtins.input', side_effect=["Manzana",1,"Pera","-1","a"]):
        with patch('builtins.print'):
            resultado=Editar_productos(lista)
    
    assert resultado == [["Pera",10,100]] #Verifico que se le cambie el nombre
    
def test_editar_cantidad():
    
    lista = [["Manzana",10,100]]
    
    with patch('builtins.input', side_effect=["Manzana",2,20,"-1","a"]):
        with patch('builtins.print'):
            resultado=Editar_productos(lista)
    
    assert resultado == [["Manzana",20,100]]
    
def test_editar_precio():
    
    lista = [["Manzana",10,100]]
    
    with patch('builtins.input', side_effect=["Manzana",3,2000,"-1","a"]):
        with patch('builtins.print'):
            resultado=Editar_productos(lista)
    
    assert resultado == [["Manzana",10,2000]]
    
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

#VALIDO ELIMINACION DEL PRODUCTO

def test_eliminar_producto():
    lista = [["Manzana",10,10]]
    
    with patch('builtins.input', side_effect=["Manzana","-1","enter"]):
        with patch('builtins.print'):
            resultado = Eliminar_productos(lista)
    
    assert resultado == [] #Confirma que se elimine el producto
    assert "papelera.csv" #Confirma que exista la papelera
    
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def test_pedidos():
    
    historial_compra = [["Manzana",10,5],["Coca-cola",40,1000]]
    usuario = "mateo123"
        
    Gestion_de_pedidos(historial_compra,usuario)
    
    try:
        with open("pedidos.json","r") as archivo: #lo abro en modo lectura para ver si existe el codigo compra
            compras = json.load(archivo)
            
            productos = []
            
            for i in compras:
                for clave,valor in i.items():
                    if clave == "compras":
                        for indice,contenido in valor.items():
                            
                            nombre = contenido.get("producto") 
                            cantidad = contenido.get("cantidad")
                            precio = contenido.get("precio")
                            productos.append([nombre,cantidad,precio])

                    if clave == "usuario":
                        user = "mateo123"
                        
                    
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error archivo vacio")
    
    assert user == "mateo123" #verifico que el usuario sea el que se envia como parametro
    assert "pedidos.json" #verifico que exista el archivo
    assert ["Manzana",10,5] and ["Coca-cola"] in productos #verifico que el carrito comprado este en el archivo json
    
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def test_estadisticas(): #EJECUTAR CON: pytest -s (para los inputs)
    
    banco = 100
    lista = [["Manzana",10,5],["Coca-cola",40,1000],["Sprite",40,1000]]

    diccionario = estadisticas(banco,lista)
    
    for clave,valor in diccionario.items():
        plata = diccionario.get("dinero") 
        mayor_stock = diccionario.get("Mayor stock")
        menor_stock = diccionario.get("Menor stock") 
    
    assert plata == 100
    assert mayor_stock == 40
    assert menor_stock == 10 
    
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------    
    

    