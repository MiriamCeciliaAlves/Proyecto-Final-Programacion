import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# Importación clave para el selector de fecha
from tkcalendar import DateEntry 

from src.logica import CalculadoraPlazos
from src.persistencia import GestorDatos

class AplicacionLegal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Plazos Procesales - Uruguay")
        self.geometry("500x350")
        
        # Cargar datos y lógica
        gestor = GestorDatos()
        config = gestor.cargar_configuracion()
        self.calculadora = CalculadoraPlazos(config)

        self.crear_widgets()

    def crear_widgets(self):
        # Título
        lbl_titulo = tk.Label(self, text="Calculadora de Vencimientos (CGP)", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=10)

        # Frame para el formulario
        frame = tk.Frame(self)
        frame.pack(pady=10)

        # 📅 Fecha de Notificación (Usando DateEntry)
        tk.Label(frame, text="Fecha de Notificación:").grid(row=0, column=0, padx=5, pady=5)
        
        # El widget DateEntry reemplaza al tk.Entry
        self.entry_fecha = DateEntry(
            frame, 
            width=12, 
            background='darkblue',
            foreground='white', 
            borderwidth=2,
            # Importante: Asegura el formato DD/MM/YYYY requerido por logica.py
            date_pattern='dd/mm/yyyy' 
        )
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        # Tipo de Plazo (Ejemplos didácticos)
        tk.Label(frame, text="Tipo de Acto:").grid(row=1, column=0, padx=5, pady=5)
        self.combo_tipo = ttk.Combobox(frame, values=[
            "Contestar Demanda (30 días)", 
            "Apelación Interlocutoria (6 días)", 
            "Apelación Sentencia (15 días)",
            "Evacuar Traslado (6 días)"
        ])
        self.combo_tipo.grid(row=1, column=1, padx=5, pady=5)
        self.combo_tipo.current(0)

        # Botón Calcular
        btn_calcular = tk.Button(self, text="CALCULAR VENCIMIENTO", command=self.procesar_calculo, bg="#4CAF50", fg="white")
        btn_calcular.pack(pady=20)

        # Resultado
        self.lbl_resultado = tk.Label(self, text="---", font=("Arial", 12), fg="blue")
        self.lbl_resultado.pack(pady=10)

    def procesar_calculo(self):
        # El método .get() en DateEntry ahora devuelve la fecha en el formato 'dd/mm/yyyy'
        fecha_txt = self.entry_fecha.get()
        seleccion = self.combo_tipo.get()
        
        # Extraer el número de días del string 
        import re
        try:
            dias = int(re.search(r'(\d+)', seleccion).group(1))
            
            resultado = self.calculadora.calcular_vencimiento(fecha_txt, dias)
            self.lbl_resultado.config(text=f"El plazo vence el: {resultado}")
            
        except ValueError as e:
            # Captura errores de formato si se hubiera modificado el date_pattern o la entrada
            messagebox.showerror("Error de Formato", f"Asegúrese de que la fecha seleccionada sea válida.\n{e}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado al calcular: {e}")