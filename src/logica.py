from datetime import datetime, timedelta

class CalculadoraPlazos:
    def __init__(self, config):
        self.config = config

    def es_dia_habil(self, fecha: datetime) -> bool:
        # 1. Chequear fin de semana (Sábado=5, Domingo=6)
        if fecha.weekday() >= 5:
            return False

        dia_mes = fecha.strftime("%d-%m")
        fecha_str = fecha.strftime("%Y-%m-%d")

        # 2. Chequear feriados fijos
        if dia_mes in self.config.get("feriados_fijos", []):
            return False
            
        # 3. Chequear feriados específicos (por año)
        if fecha_str in self.config.get("feriados_especificos_2025", []):
            return False

        # 4. Chequear Ferias Judiciales (Simplificado para el ejemplo)
        # Aquí se podría expandir la lógica para rangos de fechas complejos
        
        return True

    def calcular_vencimiento(self, fecha_notificacion: str, dias_plazo: int) -> str:
        """
        Calcula la fecha de vencimiento sumando solo días hábiles.
        Formato fecha: DD/MM/YYYY
        """
        try:
            fecha_actual = datetime.strptime(fecha_notificacion, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Formato de fecha incorrecto. Use DD/MM/YYYY")

        dias_sumados = 0
        
        # El plazo comienza a contar al día siguiente de la notificación
        fecha_actual += timedelta(days=1)

        while dias_sumados < dias_plazo:
            if self.es_dia_habil(fecha_actual):
                dias_sumados += 1
            
            # Si ya sumamos todos los días, no avanzamos más al siguiente día
            if dias_sumados < dias_plazo:
                fecha_actual += timedelta(days=1)
        
        # Si el vencimiento cae en inhábil, se extiende al siguiente hábil (regla general)
        while not self.es_dia_habil(fecha_actual):
             fecha_actual += timedelta(days=1)

        return fecha_actual.strftime("%d/%m/%Y")