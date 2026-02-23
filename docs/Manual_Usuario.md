# Manual de Usuario - Validador de Enlaces en Excel

Esta aplicación permite validar masivamente la disponibilidad y el estado de enlaces (URLs) contenidos en archivos Excel, automatizando la verificación de cientos de registros de manera eficiente.

### Instalación y Requisitos

- **Requisitos del sistema**: Windows 10/11.
- **Ejecución**:
  - Si tienes el código fuente: Ejecuta `python main.py`.
  - Si tienes el ejecutable: Descomprime la carpeta y abre `Validador.exe`.
- **Conexión**: Se requiere conexión a internet estable para verificar los enlaces.

### Uso de la Aplicación

1. **Inicio**:
   Al abrir la aplicación, verás una interfaz dividida en secciones para facilitar el flujo de trabajo.

2. **Cargar Archivo**:
   - **Arrastrar y Soltar**: Puedes arrastrar tu archivo Excel (`.xlsx` o `.xls`) directamente sobre el recuadro gris que dice "Arrastra el archivo Excel aquí".
   - **Selección Manual**: También puedes hacer clic en el mismo recuadro para abrir el explorador de archivos y buscar tu documento.
   - *Indicador*: Una vez cargado, verás un mensaje confirmando el nombre del archivo, número de filas y columnas detectadas.

3. **Configuración de Análisis**:
   - **Hoja de Excel**: Selecciona en el menú desplegable la hoja que contiene los datos.
   - **Columna de URLs**: Ingresa la letra de la columna donde están los enlaces (ej. `C`, `AA`).
   - **Fila inicial**: Indica en qué fila comenzar (por defecto `2` para saltar encabezados).
   - **Fila final**: Indica hasta qué fila procesar.

4. **Configuración de Resultados**:
   - **Columna resultado**: Ingresa la letra de la columna donde quieres que se escriba el estado del enlace (ej. `D`, `Z`).
   - *Nota*: La aplicación escribirá "VÁLIDO", "NO VÁLIDO" o "VALIDAR" en esta columna. Asegúrate de elegir una columna vacía para no sobrescribir datos importantes.

5. **Ejecución del Proceso**:
   - Haz clic en el botón **"INICIAR VALIDACIÓN"**.
   - La barra de progreso te mostrará el avance en tiempo real, indicando qué URL se está analizando y en qué fila.

6. **Controles durante la Validación**:
   - **Pausar**: Si necesitas liberar ancho de banda momentáneamente, usa el botón "PAUSAR". Puedes reanudar cuando quieras.
   - **Detener**: El botón "DETENER" cancela el proceso. *Advertencia: Si detienes el proceso, los resultados obtenidos hasta ese momento no se guardarán en el Excel.*

7. **Resultados y Logs**:
   - Al finalizar, aparecerá una ventana emergente con el resumen (Total procesados, Válidos, No válidos).
   - Los resultados se guardan automáticamente en tu archivo Excel original.
   - **Ver Logs**: El botón "Ver Logs" abre un archivo de texto detallado con el historial de todas las validaciones, útil para auditar errores específicos.

### Notas Importantes

- **Guardado Automático**: No abras el archivo Excel mientras la validación está en curso, ya que esto podría bloquear el guardado de los resultados.
- **Criterios de Validación**:
  - **VÁLIDO**: La página carga correctamente (Código 200).
  - **NO VÁLIDO**: La página no existe (404), el dominio está en venta o hay errores de servidor.
  - **VALIDAR**: Casos ambiguos que requieren revisión manual (ej. bloqueos de seguridad, login requerido o tiempos de espera agotados).
- **Velocidad**: El proceso tiene un pequeño retraso intencional entre cada enlace para evitar bloqueos por parte de los servidores.
