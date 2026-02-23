# Manual de Distribución - Validador de Enlaces

Este manual proporciona los pasos necesarios para convertir el script Python `main.py` en un ejecutable independiente (`.exe`) utilizando PyInstaller. El resultado final podrá ejecutarse en cualquier computadora con Windows sin necesidad de tener Python instalado.

## Requisitos Previos
- Python 3.x instalado.
- Terminal o Símbolo del sistema (CMD/PowerShell) abierto en la carpeta del proyecto.

## Pasos para Crear el Ejecutable

1. **Crear y Activar un Entorno Virtual (Recomendado)**:
   Esto asegura que el ejecutable sea ligero y solo contenga lo necesario.
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Instalar Dependencias del Proyecto**:
   Instala las librerías que usa tu código (pandas, requests, etc.).
   ```bash
   pip install -r requirements.txt
   ```

3. **Instalar PyInstaller**:
   La herramienta que crea el ejecutable.
   ```bash
   pip install pyinstaller
   ```

4. **Generar el Ejecutable**:
   Ejecuta el siguiente comando exacto. Es vital incluir `--collect-all tkinterdnd2` para que funcione el "Arrastrar y Soltar".

   ```bash
   pyinstaller --noconsole --onedir --name="Validador" --collect-all tkinterdnd2 main.py
   ```

   **Explicación de los parámetros:**
   - `--noconsole`: Oculta la ventana negra de comandos al abrir la app.
   - `--onedir`: Genera una carpeta con archivos (más rápido de iniciar que un solo archivo gigante).
   - `--name="Validador"`: Nombre del archivo final (`Validador.exe`).
   - `--collect-all tkinterdnd2`: **Crucial**. Copia los archivos internos necesarios para que funcione el Drag & Drop.

5. **Localizar y Probar**:
   - Ve a la carpeta `dist/Validador/`.
   - Busca el archivo `Validador.exe` y ejecútalo para probar.

6. **Distribuir**:
   - Comprime la carpeta completa `dist/Validador` en un archivo `.zip`.
   - Envía ese ZIP a los usuarios. Ellos solo deben descomprimirlo y ejecutar `Validador.exe`.

## Solución de Problemas
- **No abre**: Revisa si se creó el archivo `logs_validacion.txt` dentro de la carpeta del ejecutable para ver el error.
- **No funciona el Drag & Drop**: Asegúrate de haber usado `--collect-all tkinterdnd2` en el paso 4.
