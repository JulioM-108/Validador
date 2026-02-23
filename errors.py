# ============================================================================
# utils/mensajes_error.py
# Mensajes de error centralizados que explican QUÉ, POR QUÉ y CÓMO resolver
# ============================================================================
from config.constants import (
    EMOJI_NO_VALIDO
)

class MensajesError:
    @staticmethod
    def archivo_corrupto(nombre_archivo, error_tecnico=""):
        """Error cuando el archivo Excel está dañado o tiene formato inválido"""
        return {
            'titulo': "Archivo corrupto o formato inválido",
            'que_paso': "El formato del archivo no es válido",
            'por_que': "El archivo no es un Excel válido (.xlsx o .xls) o está corrupto",
            'como_resolver': "1. Verifica que sea un archivo Excel real\n2. Intenta abrirlo en Excel para verificar\n3. Si está dañado, restaura desde un backup",
            'donde': f"Archivo: {nombre_archivo}",
            'tecnico': f"ValueError: {error_tecnico}" if error_tecnico else "ValueError"
        }
    
    @staticmethod
    def archivo_no_encontrado(ruta_archivo, error_tecnico=""):
        """Error cuando el archivo no existe"""
        return {
            'titulo': "Archivo no encontrado",
            'que_paso': f"El archivo no existe en la ruta especificada",
            'por_que': "El archivo fue movido, eliminado o la ruta es incorrecta",
            'como_resolver': "1. Verifica que el archivo exista\n2. Vuelve a seleccionar el archivo",
            'donde': f"Ruta: {ruta_archivo}",
            'tecnico': f"FileNotFoundError: {error_tecnico}" if error_tecnico else "FileNotFoundError"
        }
    
    @staticmethod
    def archivo_bloqueado(nombre_archivo, error_tecnico=""):
        """Error cuando el archivo está bloqueado por otro proceso (al cargar)"""
        return {
            'titulo': "Archivo bloqueado",
            'que_paso': f"El archivo '{nombre_archivo}' no se puede leer",
            'por_que': "Probablemente está abierto en Excel o siendo usado por otro programa",
            'como_resolver': "1. Cierra el archivo Excel\n2. Intenta cargarlo de nuevo",
            'donde': f"Archivo: {nombre_archivo}",
            'tecnico': f"PermissionError al cargar: {error_tecnico}" if error_tecnico else "PermissionError"
        }

    @staticmethod
    def error_guardar_resultados(nombre_archivo, error_tecnico=""):
        """Error al intentar guardar resultados en el Excel"""
        return {
            'titulo': "No se pueden guardar los resultados",
            'que_paso': f"El archivo '{nombre_archivo}' está bloqueado",
            'por_que': "Probablemente está abierto en Excel durante la validación",
            'como_resolver': "1. Cierra el archivo Excel\n2. Vuelve a ejecutar la validación COMPLETA\n3. NO abras el archivo durante la validación",
            'donde': f"Archivo: {nombre_archivo}",
            'tecnico': f"PermissionError al guardar: {error_tecnico}" if error_tecnico else "PermissionError"
        }
    
    # ========================================================================
    # ERRORES DE CONFIGURACIÓN Y DATOS
    # ========================================================================

    @staticmethod
    def rango_sin_datos(fila_ini, fila_fin):
        """Error cuando el rango seleccionado no contiene datos"""
        return {
            'titulo': "Rango sin datos",
            'que_paso': "El rango de filas seleccionado está vacío o fuera de los límites del archivo",
            'por_que': f"No se encontraron datos entre la fila {fila_ini} y la {fila_fin}",
            'como_resolver': "1. Ajusta el rango de filas para que coincida con los datos del Excel\n2. Asegúrate de que la hoja seleccionada es la correcta",
            'donde': f"Rango: {fila_ini}-{fila_fin}",
            'tecnico': "DataFrame filtrado resultó en 0 filas"
        }

    @staticmethod
    def columna_fuera_limites(columna, fila, total_cols):
        """Advertencia cuando una fila es más corta que la columna solicitada"""
        return {
            'titulo': "Columna fuera de límites para una fila",
            'que_paso': f"Se omitió la fila {fila} porque la columna '{columna}' no existe en ella",
            'por_que': f"Esa fila solo tiene {total_cols} columnas de datos",
            'como_resolver': "Revisa el archivo Excel para confirmar si la falta de datos en esa fila es correcta. La validación continuará con las demás filas.",
            'donde': f"Fila: {fila}",
            'tecnico': f"Índice de columna solicitado es mayor que la longitud de la fila"
        }

    @staticmethod
    def configuracion_invalida(detalle):
        """Error cuando la configuración de validación no es correcta o no genera resultados"""
        return {
            'titulo': "Error de Configuración",
            'que_paso': "La configuración actual no permite realizar la validación",
            'por_que': f"{detalle}",
            'como_resolver': "1. Verifica que la columna seleccionada contenga URLs\n2. Revisa que el rango de filas tenga datos",
            'donde': "Configuración de validación",
            'tecnico': "ValueError: Configuración inválida"
        }

    @staticmethod
    def error_inesperado(tipo_error, mensaje_error, contexto=""):
        """Error genérico para cualquier excepción no controlada"""
        return {
            'titulo': "Error Inesperado",
            'que_paso': "Ocurrió un error no previsto por la aplicación",
            'por_que': f"Detalle: {mensaje_error}",
            'como_resolver': "1. Revisa el archivo de logs para más detalles técnicos\n2. Si el error persiste, contacta al desarrollador",
            'donde': f"Contexto: {contexto}",
            'tecnico': f"{tipo_error}: {mensaje_error}"
        }

    # ========================================================================
    # MÉTODO PARA FORMATEAR MENSAJES
    # ========================================================================
    
    @staticmethod
    def formatear_para_log(mensaje_dict):
        lineas = [
            f"{EMOJI_NO_VALIDO} ERROR CRÍTICO: {mensaje_dict['que_paso']}",
            f"   → Causa: {mensaje_dict['por_que']}",
            f"   → Solución: {mensaje_dict['como_resolver']}",
            f"   → Ubicación: {mensaje_dict['donde']}",
            f"   → Detalle técnico: {mensaje_dict['tecnico']}"
        ]
        return "\n".join(lineas)
    
    @staticmethod
    def formatear_para_popup(mensaje_dict):
        return (
            f"{mensaje_dict['que_paso']}\n\n"
            f"Causa probable:\n{mensaje_dict['por_que']}\n\n"
            f"Solución:\n{mensaje_dict['como_resolver']}"
        )


# ============================================================================
# FUNCIONES DE AYUDA
# ============================================================================

def registrar_error(logger, mensaje_dict):
    for linea in MensajesError.formatear_para_log(mensaje_dict).split('\n'):
        logger.error(linea)


def mostrar_error(mensaje_dict, messagebox):
    messagebox.showerror(
        mensaje_dict['titulo'],
        MensajesError.formatear_para_popup(mensaje_dict)
    )