import json
import os

class GestorDatos:
    def __init__(self, ruta_archivo='data/feriados.json'):
        self.ruta_archivo = ruta_archivo

    def cargar_configuracion(self):
        """Carga la configuración de feriados desde el JSON."""
        if not os.path.exists(self.ruta_archivo):
            # Retorna una estructura vacía si no existe el archivo
            return {"feriados_fijos": [], "feriados_especificos_2025": []}
        
        with open(self.ruta_archivo, 'r', encoding='utf-8') as f:
            return json.load(f)