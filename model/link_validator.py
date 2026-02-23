# ============================================================================
# models/link_validator.py
# MODELO - Lógica de negocio de validación de enlaces (MODIFICADO)
# ============================================================================

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from urllib.parse import urlparse
import warnings

from config.constants import (
    HEADERS_HTTP,
    CODIGOS_HTTP_EXITOSOS,
    TIMEOUT_HTTP,
    MAX_REINTENTOS,
    DELAY_DEFAULT,
    KEYWORDS_ERROR_CRITICO,
    KEYWORDS_AD_BLOCKER,
    KEYWORDS_LOGIN,
    MENSAJE_CELDA_VACIA,
    MENSAJE_NO_ES_URL,
    MENSAJE_ERROR_NORMALIZACION,
    MENSAJE_SIN_SSL,
    MENSAJE_ERROR_SSL,
    MENSAJE_TIMEOUT,
    MENSAJE_ERROR_CONEXION,
    MENSAJE_DEMASIADAS_REDIRECCIONES,
    MENSAJE_ERROR_REINTENTOS,
    MENSAJE_PAGINA_PROBLEMATICA,
    MENSAJE_REQUIERE_LOGIN,
    EMOJI_NO_VALIDO,
)
from logger import get_logger

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

class LinkValidator:
    
    def __init__(self):
        self.headers = HEADERS_HTTP
        self.codigos_exitosos = CODIGOS_HTTP_EXITOSOS
        self.logger = get_logger()

    # ========================================================================
    # UTILIDADES
    # ========================================================================
    
    @staticmethod
    def letra_a_indice(letra):
        letra = str(letra).upper().strip()
        indice = 0
        for i, char in enumerate(reversed(letra)):
            indice += (ord(char) - ord('A') + 1) * (26 ** i)
        return indice - 1
    
    @staticmethod
    def normalizar_url(url):
        if pd.isna(url) or not url:
            return None
            
        url = str(url).strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url
    
    @staticmethod
    def es_url_valida(url):
        if pd.isna(url) or not url:
            return False
        
        url_str = str(url).strip()
        
        try:
            result = urlparse(url_str)
            return bool(result.scheme) and bool(result.netloc) and '.' in result.netloc
        except ValueError:
            return False
    
    # ========================================================================
    # VERIFICACIÓN HTTP
    # ========================================================================
    
    def hacer_request(self, url, timeout=TIMEOUT_HTTP, max_retries=MAX_REINTENTOS):
        for intento in range(max_retries + 1):
            try:
                response = requests.get(
                    url, 
                    headers=self.headers, 
                    timeout=timeout,
                    allow_redirects=True,
                    verify=False
                )
                return response, None, False
                
            except requests.exceptions.SSLError:
                return None, MENSAJE_ERROR_SSL, True
                
            except requests.exceptions.Timeout:
                if intento < max_retries:
                    time.sleep(1)
                    continue
                return None, MENSAJE_TIMEOUT, False
                
            except requests.exceptions.ConnectionError:
                if intento < max_retries:
                    time.sleep(1)
                    continue
                return None, MENSAJE_ERROR_CONEXION, False
                
            except requests.exceptions.TooManyRedirects:
                return None, MENSAJE_DEMASIADAS_REDIRECCIONES, False
                
            except requests.exceptions.RequestException as e:
                return None, f"Error: {str(e)[:50]}", False
        
        return None, MENSAJE_ERROR_REINTENTOS, False
    
    # ========================================================================
    # ANÁLISIS DE CONTENIDO HTML
    # ========================================================================
    
    def analizar_contenido_html(self, response):
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('title')
            title_text = title.get_text().lower() if title else ""
            body = soup.find('body')
            body_text = body.get_text().lower() if body else ""
            
            contenido_completo = title_text + " " + body_text
            
            # Verificar errores críticos y dominios en venta
            if any(err in contenido_completo for err in KEYWORDS_ERROR_CRITICO):
                return 'error'
            
            # Detectar bloqueadores de anuncios
            if any(keyword in contenido_completo for keyword in KEYWORDS_AD_BLOCKER):
                return 'validar'
            
            # Detección de login/contraseña
            if any(keyword in contenido_completo for keyword in KEYWORDS_LOGIN):
                return 'validar'
            
            return 'ok'
            
        except Exception as e:
            self.logger.warning(f"{EMOJI_NO_VALIDO} No se pudo analizar el contenido HTML de {response.url}: {e}")
            return 'ok'
    
    # ========================================================================
    # VALIDACIÓN PRINCIPAL
    # ========================================================================
    
    def validar_url(self, url, delay=DELAY_DEFAULT):
        resultado = {
            'url_original': url,
            'estado': None,
            'detalles': '',
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # PASO 1: Verificar si está vacío
        if pd.isna(url) or not str(url).strip():
            resultado['detalles'] = MENSAJE_CELDA_VACIA
            return resultado
            
        # PASO 2: Normalizar URL (Agregar https:// si falta)
        url_norm = self.normalizar_url(url)
        if not url_norm:
            resultado['detalles'] = MENSAJE_ERROR_NORMALIZACION
            return resultado
            
        # PASO 3: Verificar si es una URL válida (usando la URL ya normalizada)
        if not self.es_url_valida(url_norm):
            resultado['detalles'] = MENSAJE_NO_ES_URL
            return resultado
        
        # PASO 3.5: Verificar si tiene HTTPS (certificado SSL)
        if url_norm.startswith('http://'):
            resultado['estado'] = 'validar'
            resultado['detalles'] = MENSAJE_SIN_SSL
            time.sleep(delay)
            return resultado
        
        # PASO 4: Hacer request HTTP
        response, error, requiere_validacion = self.hacer_request(url_norm)
        
        # Si requiere validación (ej: SSL Error)
        if requiere_validacion:
            resultado['estado'] = 'validar'
            resultado['detalles'] = error
            time.sleep(delay)
            return resultado
        
        # Si hay error definitivo
        if error:
            resultado['estado'] = 'no_valido'
            resultado['detalles'] = error
            time.sleep(delay)
            return resultado
        
        # PASO 5: Verificar código HTTP
        if response.status_code not in self.codigos_exitosos and response.status_code != 403:
            resultado['estado'] = 'no_valido'
            resultado['detalles'] = f"HTTP {response.status_code}"
            time.sleep(delay)
            return resultado
        
        # PASO 6: Análisis HTML
        content_type = response.headers.get('Content-Type', '').lower()
        if 'text/html' in content_type or 'application/xhtml' in content_type:
            analisis = self.analizar_contenido_html(response)
            if analisis == 'error':
                resultado['estado'] = 'no_valido'
                resultado['detalles'] = MENSAJE_PAGINA_PROBLEMATICA
                time.sleep(delay)
                return resultado
            elif analisis == 'validar':
                resultado['estado'] = 'validar'
                resultado['detalles'] = MENSAJE_REQUIERE_LOGIN
                time.sleep(delay)
                return resultado
        
        # PASO 7: Todo está bien
        resultado['estado'] = 'valido'
        resultado['detalles'] = f"OK - HTTP {response.status_code}"
        time.sleep(delay)
        return resultado
    
    # ========================================================================
    # VALIDACIÓN EN LOTE
    # ========================================================================
    
    def validar_lote_con_filas(self, urls_con_filas, delay=DELAY_DEFAULT, callback=None):
        resultados = []
        total = len(urls_con_filas)
        
        for idx, (fila_excel, url) in enumerate(urls_con_filas, 1):
            resultado = self.validar_url(url, delay)
            resultado['fila_excel'] = fila_excel
            resultados.append(resultado)
            
            # Llamar al callback si existe (para actualizar UI)
            if callback:
                callback(url, idx, total, resultado, fila_excel)
        
        return resultados