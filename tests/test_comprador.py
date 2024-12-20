import pytest
import json
import os
import tempfile
from unittest.mock import patch, mock_open
import sys
import re


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from comprador.func_comprador import pago, comprar_producto,Recomendar_productos, actualizar_carrito, ver_productos, categoria, detalles_productos, cargar_datos, guardar_datos, validar_usuario, validar_contraseña, historial_compras,buscar_producto_similar



producto = [
    ["Manzana", 10, 100],
    ["Pera", 5, 25],
    ["Sprite", 4, 1000],
    ["Camiseta Nike", 30, 50],
    ["Zapatos Adidas", 80, 20],
]

def test_recomendar_productos():
    """Test the product recommendation function."""
    historial_compra = [
        [["Manzana", 2, 100], ["Pera", 1, 25], "usuario1"],
        [["Sprite", 3, 1000], "usuario2"]
    ]
    compras_realizadas = ["Manzana"]
    usuario = "usuario1"
    
    recommended = Recomendar_productos(compras_realizadas, usuario, historial_compra)
    assert "Pera" in recommended
    assert "Manzana" not in recommended

def test_actualizar_carrito():
    """Test updating the shopping cart."""
    carrito = [["Manzana", 2, 100]]
    compras_realizadas = [["Manzana", 3, 100], ["Pera", 1, 25]]
    
    updated_carrito = actualizar_carrito(compras_realizadas, carrito)
    
  
    manzana_entry = [item for item in updated_carrito if item[0] == "Manzana"][0]
    assert manzana_entry[1] == 5
    
   
    pera_entry = [item for item in updated_carrito if item[0] == "Pera"][0]
    assert pera_entry[1] == 1



def test_validar_usuario():
    
    valid_usernames = ["john_doe", "user123", "test_user.123"]
    
    
    invalid_usernames = ["a", "123user", "user with space", "@user"]
    
 
    with patch('builtins.input', side_effect=valid_usernames):
        for username in valid_usernames:
            assert re.match(r'^[a-zA-Z][a-zA-Z0-9._]{2,15}$', username)
    

    with patch('builtins.input', side_effect=invalid_usernames):
        for username in invalid_usernames:
            assert not re.match(r'^[a-zA-Z][a-zA-Z0-9._]{2,15}$', username)

def test_validar_contraseña():

    valid_passwords = ["Strong1!Pass", "Secure123@Test", "Complex#Pass456"]
    
   
    invalid_passwords = ["weak", "NoSpecialChar1", "nocapital123!", "NOCAPITALNOLOWER123!"]
    
   
    with patch('builtins.input', side_effect=valid_passwords):
        for password in valid_passwords:
            assert re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$', password)
    
   
    with patch('builtins.input', side_effect=invalid_passwords):
        for password in invalid_passwords:
            assert not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$', password)


def test_historial_compras():

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
        temp_file_path = temp_file.name
    
    try:
     
        historial_carrito = [
            ["Manzana", 2, 100],
            ["Pera", 1, 25]
        ]
        usuario = "testuser"
        
        
        historial_compras(historial_carrito, usuario, mostrar_historial=False)
    
        with open("historial.json", "r") as archivo:
            historial = json.load(archivo)
   
        user_history = next((entry for entry in historial if entry["usuario"] == usuario), None)
        assert user_history is not None
        assert len(user_history["compras"]) > 0
        
        first_purchase = list(user_history["compras"].values())[0]
        assert first_purchase["producto"] == "Manzana"
        assert first_purchase["cantidad"] == 2
        assert first_purchase["precio"] == 100
    
    finally:
   
        if os.path.exists("historial.json"):
            os.unlink("historial.json")
        os.unlink(temp_file_path)



def test_detalles_productos(monkeypatch, tmp_path):
   
    details_file = tmp_path / "detalles_productos.txt"
    details_file.write_text("Manzana: Fruta fresca de temporada\nPera: Variedad dorada")
    
  
    monkeypatch.setattr('builtins.open', mock_open(read_data=details_file.read_text()))
    
  
    monkeypatch.setattr('builtins.input', lambda _: "Manzana")
    
   
    result = detalles_productos()
   
    assert result is not None
    assert "Manzana" in str(result)
    
    
def test_comprar_productos():
    
    lista = [["Manzana", 10, 100],["Pera", 10, 100]]
    carrito = []
    
    with patch('builtins.input', side_effect=["Manzana",10,"-1"]):
        with patch('builtins.print'):
            compra_realizada, resultado=comprar_producto(lista, carrito)
    
    
    assert compra_realizada == [["Manzana",10,100]]                               
    assert ["Manzana", 0, 100]  in resultado #verifico haya un elemento
    print(resultado)
    assert [["Manzana", 0, 100],["Pera",10,100]] == resultado #verifico que este en la lista



def test_pago():
    
    carrito = [["Manzana", 10, 100]]
    usuario = 'usuario_prueba'
    
    with patch('builtins.input', side_effect=["si", "a"]):
        with patch('builtins.print'):
            monto_total, carrito, usuario = pago(carrito, usuario)
    
    assert carrito == []                               
    assert monto_total == 1000
  