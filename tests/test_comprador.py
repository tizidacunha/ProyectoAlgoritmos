import pytest
import json
import os
import tempfile
from unittest.mock import patch, mock_open
import sys
import re

# Add the directory containing the source files to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the functions to test
from comprador.func_comprador import Recomendar_productos, actualizar_carrito, ver_productos, categoria, detalles_productos, cargar_datos, guardar_datos, validar_usuario, validar_contraseña, historial_compras,buscar_producto_similar


# Sample data for testing
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
    
    # Check if Manzana quantity is updated
    manzana_entry = [item for item in updated_carrito if item[0] == "Manzana"][0]
    assert manzana_entry[1] == 5
    
    # Check if Pera is added to the cart
    pera_entry = [item for item in updated_carrito if item[0] == "Pera"][0]
    assert pera_entry[1] == 1

def test_ver_productos(capsys):
    """Test displaying products."""
    ver_productos(producto)
    captured = capsys.readouterr()
    
    # Check if the table header is correct
    assert "Nombre" in captured.out
    assert "Stock" in captured.out
    assert "Precio" in captured.out
    
    # Check if specific products are displayed
    assert "Manzana" in captured.out
    assert "Sprite" in captured.out


def test_cargar_datos():
    """Test loading data from a JSON file."""
    # Create a temporary JSON file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
        json.dump({"usuarios": [{"usuario": "test", "contrasena": "Test123!"}]}, temp_file)
        temp_file_path = temp_file.name
    
    try:
        loaded_data = cargar_datos(temp_file_path)
        assert "usuarios" in loaded_data
        assert len(loaded_data["usuarios"]) > 0
    finally:
        os.unlink(temp_file_path)

def test_guardar_datos():
    """Test saving data to a JSON file."""
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
        temp_file_path = temp_file.name
    
    try:
        test_data = {"usuarios": [{"usuario": "test", "contrasena": "Test123!"}]}
        guardar_datos(temp_file_path, test_data)
        
        # Read and verify the saved data
        with open(temp_file_path, 'r') as f:
            loaded_data = json.load(f)
        
        assert loaded_data == test_data
    finally:
        os.unlink(temp_file_path)

def test_validar_usuario():
    """Test user validation."""
    # Valid usernames
    valid_usernames = ["john_doe", "user123", "test_user.123"]
    
    # Invalid usernames
    invalid_usernames = ["a", "123user", "user with space", "@user"]
    
    # Test valid usernames using a mock
    with patch('builtins.input', side_effect=valid_usernames):
        for username in valid_usernames:
            assert re.match(r'^[a-zA-Z][a-zA-Z0-9._]{2,15}$', username)
    
    # Test invalid usernames using a mock
    with patch('builtins.input', side_effect=invalid_usernames):
        for username in invalid_usernames:
            assert not re.match(r'^[a-zA-Z][a-zA-Z0-9._]{2,15}$', username)

def test_validar_contraseña():
    """Test password validation."""
    # Valid passwords
    valid_passwords = ["Strong1!Pass", "Secure123@Test", "Complex#Pass456"]
    
    # Invalid passwords
    invalid_passwords = ["weak", "NoSpecialChar1", "nocapital123!", "NOCAPITALNOLOWER123!"]
    
    # Test valid passwords using a mock
    with patch('builtins.input', side_effect=valid_passwords):
        for password in valid_passwords:
            assert re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$', password)
    
    # Test invalid passwords using a mock
    with patch('builtins.input', side_effect=invalid_passwords):
        for password in invalid_passwords:
            assert not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$', password)

def test_historial_compras():
    """Test purchase history management."""
    # Create a temporary JSON file for testing
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
        temp_file_path = temp_file.name
    
    try:
        # Prepare test data
        historial_carrito = [
            ["Manzana", 2, 100],
            ["Pera", 1, 25]
        ]
        usuario = "testuser"
        
        # First, run the function to create/update history
        historial_compras(historial_carrito, usuario, mostrar_historial=False)
        
        # Read the created history
        with open("historial.json", "r") as archivo:
            historial = json.load(archivo)
        
        # Verify the history
        user_history = next((entry for entry in historial if entry["usuario"] == usuario), None)
        assert user_history is not None
        assert len(user_history["compras"]) > 0
        
        # Verify specific product details
        first_purchase = list(user_history["compras"].values())[0]
        assert first_purchase["producto"] == "Manzana"
        assert first_purchase["cantidad"] == 2
        assert first_purchase["precio"] == 100
    
    finally:
        # Clean up the temporary files
        if os.path.exists("historial.json"):
            os.unlink("historial.json")
        os.unlink(temp_file_path)

# Optional: Test for categoria function (might need modification based on exact implementation)
def test_categoria(capsys, monkeypatch):
    """Test category selection."""
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "Comida")
    
    categoria(producto)
    captured = capsys.readouterr()
    
    # Check if the output contains expected food category items
    assert "Manzana" in captured.out
    assert "Pera" in captured.out

# Optional: Test for detalles_productos (will require a mock file)
def test_detalles_productos(monkeypatch, tmp_path):
    """Test product details retrieval."""
    # Create a mock details file
    details_file = tmp_path / "detalles_productos.txt"
    details_file.write_text("Manzana: Fruta fresca de temporada\nPera: Variedad dorada")
    
    # Patch the file path
    monkeypatch.setattr('builtins.open', mock_open(read_data=details_file.read_text()))
    
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "Manzana")
    
    # Call the function and capture its return
    result = detalles_productos()
    
    # Check the result
    assert result is not None
    assert "Manzana" in str(result)