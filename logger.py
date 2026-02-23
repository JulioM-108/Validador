# ============================================================================
# utils/logger.py
# Sistema de logging centralizado con timestamps
# ============================================================================

from datetime import datetime
from config.constants import (
    EMOJI_VALIDO,
    EMOJI_NO_VALIDO,
    EMOJI_VALIDAR,
    EMOJI_VACIO,
    EMOJI_ARCHIVO,
    EMOJI_HOJA,
    EMOJI_INICIO,
    EMOJI_VALIDO,
    EMOJI_TIEMPO,
    EMOJI_ESTADO
)

class Logger:    
    def __init__(self, guardar_en_archivo=True, ruta_archivo=None):
        self.guardar_en_archivo = guardar_en_archivo
        self.ruta_archivo = ruta_archivo or "logs_validacion.txt"
        
        # Si se va a guardar en archivo, crear/limpiar el archivo
        if self.guardar_en_archivo:
            self._inicializar_archivo()
    
    def _inicializar_archivo(self):
        try:
            with open(self.ruta_archivo, 'w', encoding='utf-8') as f:
                f.write(f"=== LOGS DE VALIDACIÓN - {self._get_timestamp()} ===\n\n")
        except Exception as e:
            print(f"{EMOJI_VALIDAR} No se pudo crear archivo de logs: {e}")
            self.guardar_en_archivo = False
    
    def _get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _escribir_en_archivo(self, mensaje):
        if not self.guardar_en_archivo:
            return
        
        try:
            with open(self.ruta_archivo, 'a', encoding='utf-8') as f:
                f.write(mensaje + '\n')
        except Exception as e:
            print(f"{EMOJI_VALIDAR} Error escribiendo en archivo de logs: {e}")
    
    
    def _log(self, mensaje, prefijo=""):
        timestamp = self._get_timestamp()
        
        # Mensaje para consola
        mensaje_consola = f"[{timestamp}]{prefijo} {mensaje}"
        
        print(mensaje_consola)
        
        # Mensaje para archivo (sin colores)
        mensaje_archivo = f"[{timestamp}]{prefijo} {mensaje}"
        self._escribir_en_archivo(mensaje_archivo)
    
    # ========================================================================
    # Diferentes niveles de log
    # ========================================================================
    
    def info(self, mensaje):
        self._log(mensaje, " [INFO]")
    
    def success(self, mensaje):
        self._log(mensaje, " [OK]")
    
    def warning(self, mensaje):
        self._log(mensaje, " [WARN]")
    
    def error(self, mensaje):
        self._log(mensaje, " [ERROR]")
    
    def debug(self, mensaje):
        self._log(mensaje, " [DEBUG]")
    
    def header(self, mensaje):
        timestamp = self._get_timestamp()
        mensaje_consola = f"[{timestamp}] {mensaje}"
        print(mensaje_consola)
        self._escribir_en_archivo(f"[{timestamp}] {mensaje}")
    
    def separador(self, caracter="=", longitud=80):
        linea = caracter * longitud
        print(linea)
        self._escribir_en_archivo(linea)
    
    def log_simple(self, mensaje):
        print(mensaje)
        self._escribir_en_archivo(mensaje)
    
    # ========================================================================
    # MÉTODOS ESPECIALES PARA LA APLICACIÓN
    # ========================================================================
    
    def log_validacion(self, estado, fila, url, idx=None, total=None):
        # Acortar URL si es muy larga
        url_corta = url[:50] + "..." if len(url) > 50 else url
        
        # Determinar emoji y color según estado
        if estado == 'valido':
            emoji = EMOJI_VALIDO
        elif estado == 'validar':
            emoji = EMOJI_VALIDAR
        elif estado == 'no_valido':
            emoji = EMOJI_NO_VALIDO
        else:
            emoji = EMOJI_VACIO
        
        # Construir mensaje
        if idx and total:
            mensaje = f"{emoji} [{idx}/{total}] Fila {fila}: {url_corta}"
        else:
            mensaje = f"{emoji} Fila {fila}: {url_corta}"
        
        self._log(mensaje, "")
    
    def log_inicio_validacion(self, hoja, columna, fila_ini, fila_fin, total, delay):
        self.separador()
        self.header(f"{EMOJI_INICIO} INICIANDO VALIDACIÓN")
        self.separador()
        self.info(f"{EMOJI_HOJA} Hoja: {hoja}")
        self.info(f"{EMOJI_ESTADO} Columna: {columna} | Filas: {fila_ini} a {fila_fin}")
        self.info(f"{EMOJI_TIEMPO}  Total URLs: {total} | Delay: {delay} seg")
        self.separador()
    
    def log_fin_validacion(self, tiempo_total, validos, no_validos, validar):
        self.separador()
        self.success(f"{EMOJI_VALIDO} VALIDACIÓN COMPLETADA")
        self.separador()
        self.info(f"{EMOJI_TIEMPO}  Tiempo total: {tiempo_total:.2f} segundos")
        self.success(f"{EMOJI_VALIDO} Válidas: {validos}")
        self.warning(f"{EMOJI_VALIDAR}  Validar: {validar}")
        self.error(f"{EMOJI_NO_VALIDO} No válidas: {no_validos}")
        self.separador()
    
    def log_carga_archivo(self, nombre_archivo, num_filas, num_columnas, hojas):
        self.info(f"{EMOJI_ARCHIVO} Cargando archivo: {nombre_archivo}")
        self.success(f"{EMOJI_VALIDO} Archivo cargado: {num_filas} filas × {num_columnas} columnas")
        if len(hojas) > 1:
            self.info(f"{EMOJI_HOJA} Hojas disponibles: {', '.join(hojas)}")


# ============================================================================
# INSTANCIA GLOBAL DEL LOGGER (Singleton pattern)
# ============================================================================
_logger_instance = None

def get_logger(guardar_en_archivo=False, ruta_archivo=None):
    global _logger_instance
    if _logger_instance is None:
        _logger_instance = Logger(guardar_en_archivo, ruta_archivo)
    return _logger_instance