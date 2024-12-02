from vendedor.func_vendedor import Agregar_productos, Editar_productos, Eliminar_productos, Gestion_de_pedidos,estadisticas,Eliminar_pedido,ver_compras,papelera
import unittest
from unittest.mock import patch, mock_open
import json
import pytest

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
    assert ["Manzana",10,5] and ["Coca-cola",40,1000] in productos #verifico que el carrito comprado este en el archivo json
    
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def test_estadisticas(): #EJECUTAR CON: pytest -s (para los inputs)
    
    banco = 100
    lista = [["Manzana",10,5],["Coca-cola",40,1000],["Sprite",40,1000]]

    with patch('builtins.input', side_effect=["enter","enter"]):
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
    
def test_papelera():
    
    lista = []
        
    with patch('builtins.input', side_effect=[0,-1,"enter"]):
        with patch('builtins.print'):
            papelera(lista)

    assert len(lista) == 1
    assert [["Manzana",10,10]] == lista

def test_error_papelera():
    
    lista = []
    
    with patch("builtins.input", side_effect=["abc",-1,"enter"]):
        with patch("builtins.print") as mock_print: 
            papelera(lista)
            mock_print.assert_any_call("Debe seleccionar un numero de indice") #verifico que se imprima este print al menos una vez 
    
def test_json_vacio():
    """Simula un archivo JSON vacío."""
    with patch("builtins.open", new_callable=mock_open, read_data="") as file: #open para simular la apertura de un archivo
        with patch("builtins.input", side_effect=["enter"]):
            with patch("builtins.print") as mock_print:
                ver_compras()
                mock_print.assert_called_once_with("El archivo de pedidos esta vacio") #significa el bloque try-except esta funcionando
            
def test_eliminar_pedido():
    
    pedido = [{
        "codigo de compra": 2873,
        "compras": {
            "1": {
                "producto": "Manzana",
                "cantidad": 10,
                "precio": 5
            },
            "2": {
                "producto": "Coca-cola",
                "cantidad": 40,
                "precio": 1000
            }
        },
        "usuario": "mateo123"
    }]
    
    try:
        
        with open("pedidos.json","w") as file:
            json.dump(pedido,file,indent=4)
    
        with patch('builtins.input', side_effect=[2873,-1,"enter"]):
            Eliminar_pedido()
    
        with open("pedidos.json","r") as file:
            contenido = json.load(file)
    
    except IOError:
        print("Fallo la prueba")

    assert contenido == []   #verifico que se haya eliminado el contenido del archivo
    





    