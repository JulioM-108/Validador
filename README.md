# Validador de Enlaces en Excel 🔗

Una aplicación de escritorio robusta desarrollada en Python para validar masivamente la disponibilidad y el estado de enlaces (URLs) contenidos en archivos Excel.

## 📋 Características Principales

- **Validación Masiva**: Procesa cientos de enlaces automáticamente sin congelar la interfaz.
- **Análisis Inteligente**:
  - Detecta códigos de estado HTTP (200, 404, 500, etc.).
  - Verifica certificados SSL (HTTP vs HTTPS).
  - Analiza el contenido HTML para detectar "falsos positivos" (páginas de parking, login requerido, soft 404).
- **Interfaz Gráfica Moderna**:
  - Soporte para **Arrastrar y Soltar** archivos (Drag & Drop).
  - Barra de progreso en tiempo real.
  - Configuración flexible de columnas y filas.
- **Resultados en Excel**: Escribe el estado ("VÁLIDO", "NO VÁLIDO", "VALIDAR") directamente en el archivo original.
- **Logs Detallados**: Sistema de registro completo para auditoría y depuración.

## 🛠️ Requisitos

- Python 3.x
- Librerías listadas en `requirements.txt`

## 🚀 Instalación Rápida

1.  **Clonar o descargar** este repositorio.
2.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Ejecutar la aplicación**:
    ```bash
    python main.py
    ```

## 📚 Documentación

Para más detalles, consulta los manuales en la carpeta `docs/`:

- [Manual de Usuario](docs/Manual_Usuario.md): Guía paso a paso para utilizar la herramienta.
- [Manual Técnico](docs/Manual_Tecnico.md): Detalles sobre la arquitectura MVC, clases y flujo de datos.
- [Manual de Distribución](docs/Manual_Distribuccion.md): Instrucciones para compilar el proyecto en un ejecutable `.exe`.

## 🏗️ Estructura del Proyecto

El proyecto sigue el patrón de arquitectura **MVC (Modelo-Vista-Controlador)** para asegurar un código limpio y mantenible.

---
Desarrollado para automatizar procesos de verificación de calidad de datos.
