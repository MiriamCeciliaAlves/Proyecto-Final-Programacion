import pytest
from src.logica import CalculadoraPlazos

# Mock de configuración para pruebas
config_test = {
    "feriados_fijos": ["01-01", "25-12"],
    "feriados_especificos_2025": []
}

@pytest.fixture
def calc():
    return CalculadoraPlazos(config_test)

def test_suma_simple_dias_habiles(calc):
    # Si notifican lunes 09/06/2025 (sin feriados), plazo 3 días.
    # Martes(1), Miércoles(2), Jueves(3). Vence Jueves 12.
    assert calc.calcular_vencimiento("09/06/2025", 3) == "12/06/2025"

def test_salto_fin_de_semana(calc):
    # Notifican Jueves 05/06/2025, plazo 2 días.
    # Viernes(1), Sábado(x), Domingo(x), Lunes(2). Vence Lunes 09.
    assert calc.calcular_vencimiento("05/06/2025", 2) == "09/06/2025"

def test_salto_feriado_fijo(calc):
    # Notifican 23/12/2025 (Martes), plazo 2 días.
    # Miércoles 24 (1), Jueves 25 (Feriado), Viernes 26 (2). Vence 26.
    assert calc.calcular_vencimiento("23/12/2025", 2) == "26/12/2025"

def test_fecha_formato_invalido(calc):
    with pytest.raises(ValueError):
        calc.calcular_vencimiento("2025-01-01", 5) # Formato incorrecto

def test_plazo_largo(calc):
    # Prueba de consistencia para plazos más largos
    # Notificación Lunes 02/06/2025, 5 días hábiles -> Lunes 09/06/2025
    assert calc.calcular_vencimiento("02/06/2025", 5) == "09/06/2025"