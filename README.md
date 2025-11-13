# ⚖️ LegalTimeUY: Simulador de Plazos Procesales Civiles v.1.0.0

![Status](https://img.shields.io/badge/Status-Activo-success)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

**LegalTimeUY** es una aplicación de escritorio desarrollada en Python diseñada para asistir a estudiantes de Derecho y profesionales en Uruguay. Su objetivo es automatizar y enseñar el cálculo de vencimientos de plazos procesales (según el CGP), una tarea propensa a errores humanos debido a la necesidad de excluir días inhábiles, feriados y ferias judiciales.

---

## 📋 Tabla de Contenidos
1. [Características](#-características)
2. [Estructura del Proyecto](#-estructura-del-proyecto)
3. [Requisitos e Instalación](#-requisitos-e-instalación)
4. [Decisiones de Diseño](#-decisiones-de-diseño)
5. [Justificación de Librerías](#-justificación-de-librerías)
6. [Fundamento Didáctico](#-fundamento-didáctico)
7. [Testing](#-testing)

---

## 🚀 Características

* **Interfaz Gráfica Intuitiva:** Ventana de escritorio limpia para ingresar fechas y seleccionar tipos de plazos.
* **Cálculo de Días Hábiles:** Algoritmo que omite automáticamente sábados, domingos y feriados específicos.
* **Configuración Externa:** Los feriados se cargan desde un archivo `JSON`, permitiendo actualizar el calendario sin modificar el código fuente.
* **Validaciones:** Manejo de errores en formatos de fecha y entradas de usuario.
* **Modularidad:** Clara separación entre la interfaz (GUI), la lógica de negocio y los datos.

---

## 📂 Estructura del Proyecto

El proyecto sigue una arquitectura modular para facilitar el mantenimiento y las pruebas:

<img width="502" height="307" alt="image" src="https://github.com/user-attachments/assets/d9f94b78-97e0-4a56-927b-ad3400500eda" />

---

## 🛠 Requisitos e Instalación
Prerrequisitos
•	Python 3.8 o superior.

### Pasos de Instalación
1.	Clonar el repositorio:
Bash
Dirigirse hacia el directorio donde se desea clonar.

git clone https://github.com/MiriamCeciliaAlves/Proyecto-Final-Programacion.git

cd (directorio donde se clonó)

3.	Crear un entorno virtual (Opcional pero recomendado):
Bash
python -m venv venv
##### En Windows:
venv\Scripts\activate
##### En Mac/Linux:
source venv/bin/activate

3.	Instalar dependencias:
Bash
pip install -r requirements.txt

4.	Ejecutar la aplicación:
Bash
python main.py
________________________________________
## 💡 Decisiones de Diseño
Para el desarrollo de LegalTimeUY, se optó por una arquitectura basada en la Separación de Responsabilidades (SoC):
1.	Lógica desacoplada: La clase CalculadoraPlazos en src/logica.py no sabe nada de la interfaz gráfica. Recibe datos, calcula y devuelve resultados. Esto permite que el mismo núcleo lógico pueda ser reutilizado en una web o una API en el futuro.
2.	Persistencia Ligera: Se eligió JSON en lugar de SQLite porque la estructura de datos (listas de fechas) es jerárquica y no relacional. Además, permite que un usuario edite el archivo feriados.json con cualquier editor de texto.
3.	Inyección de Dependencias: La lógica recibe la configuración en su constructor, lo que facilita el "mocking" (simulación de datos) durante las pruebas.
________________________________________
## 📚 Justificación de Librerías
El proyecto integra dos categorías principales de librerías, priorizando la simplicidad y la robustez:
Categoría	Librería	Justificación
Interfaz Gráfica	tkinter	Librería estándar de Python. Al no requerir instalación compleja, garantiza que la aplicación sea portable y fácil de ejecutar en cualquier SO de escritorio sin dependencias pesadas.
Persistencia	json	Formato estándar para intercambio de datos. Ideal para configuraciones estáticas como feriados, legible por humanos y máquinas.
Testing	pytest	Framework de pruebas más potente y "pythonico" que unittest. Permite escribir pruebas más legibles y utilizar fixtures para configurar los entornos de prueba.
Manejo de Tiempo	datetime	Módulo nativo esencial para la aritmética de fechas y validación de formatos.
Exportar a Hojas de cálculo
________________________________________
## 🎓 Fundamento Didáctico
Este proyecto aborda una problemática de contexto abierto integrando varios aprendizajes clave:
Desafíos Superados
•	Aritmética de Fechas: Calcular plazos no es solo sumar fecha + dias. Se debió implementar un bucle while que verifique día por día si es hábil o no, simulando el paso del tiempo real vs. tiempo judicial.
•	Gestión de Rutas: Asegurar que la aplicación encuentre el archivo json independientemente de desde dónde se ejecute el script main.py.
Aprendizajes
1.	Importancia de los Tests: Al principio, los cálculos fallaban en los cambios de mes o año. Las pruebas unitarias permitieron detectar y corregir estos errores de lógica ("off-by-one errors").
2.	Experiencia de Usuario (UX): Validar que el usuario ingrese fechas correctas (DD/MM/YYYY) evita que la aplicación colapse, enseñando la importancia de la programación defensiva.
________________________________________
## 🧪 Testing
El proyecto cuenta con una suite de pruebas unitarias para garantizar la precisión de los cálculos legales.
Para ejecutar las pruebas:
Bash
pytest
Casos de prueba incluidos:
•	Suma simple de días hábiles.
•	Salto correcto de fines de semana.
•	Salto correcto de feriados fijos y específicos.
•	Manejo de errores ante formatos de fecha inválidos.
---
## Uso de herramientas de IA
En el desarrollo de la aplicación se recurrió a la utilización de herramientas IA (Gemini con motor 2.5Pro y Copilot en VSCode) como ayuda en la depuración de errores.
________________________________________
Autor: Miriam Alves
Materia: Programación 1
Año: 2025
