from vendedor.func_vendedor import Agregar_productos, Editar_productos, Eliminar_productos
import unittest
from unittest.mock import patch

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
    
    assert resultado == []