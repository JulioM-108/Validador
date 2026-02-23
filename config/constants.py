# ============================================================================
# Constantes y configuraciones fijas de la aplicación
# ============================================================================

# Headers para las peticiones HTTP
HEADERS_HTTP = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
}

# Códigos HTTP considerados exitosos
CODIGOS_HTTP_EXITOSOS = {
    100, 101, 102, 103,                     
    200, 201, 202, 203, 204, 205, 206, 207, 208, 226,  
    300, 301, 302, 303, 304, 307, 308,      
    403                                       
}

# Timeout para requests HTTP (segundos)
TIMEOUT_HTTP = 13

# Número máximo de reintentos
MAX_REINTENTOS = 1 

# Delay por defecto entre validaciones (segundos)
DELAY_DEFAULT = 2.0


# ============================================================================
# PALABRAS CLAVE PARA DETECCIÓN DE CONTENIDO
# ============================================================================

# Keywords que indican errores críticos o dominios en venta
KEYWORDS_ERROR_CRITICO = [
    '404 not found',
    '404 - not found',
    'page not found',
    'página no encontrada',
    'error 404',
    '500 internal server error',
    'site not found',
    'domain for sale',
    'dominio en venta',
    'the domain',
    'is for sale',
    'click here to learn more',
    'buy this domain',
    'comprar este dominio',
    'this domain is for sale',
    'este dominio está en venta'
]

# Keywords que indican bloqueadores de anuncios
KEYWORDS_AD_BLOCKER = [
    'ad blocker detected',
    'please disable ad blocker',
    'adblocker detected',
    'disable your ad blocker',
    'turn off ad blocker',
    'bloqueador de anuncios detectado',
    'desactiva el bloqueador',
    'desactive su bloqueador',
    'please disable ad blockers to view this domain'
]

# Keywords que indican login/autenticación requerida
KEYWORDS_LOGIN = [
    'find your institution',
    'your university, organization or library',
    'choose your institution',
    'select your institution',
    'institutional login',
    'login institucional',
    'sign in',
    'password required',
    'contraseña requerida',
    'ingrese su contraseña',
    'enter your password',
    'ingresa tu contraseña',
    'introduce tu contraseña'
]


# ============================================================================
# MENSAJES DE LA APLICACIÓN
# ============================================================================

# Mensajes de estado
MENSAJE_CELDA_VACIA = "Celda vacía"
MENSAJE_NO_ES_URL = "Texto no es una URL (falta protocolo)"
MENSAJE_ERROR_NORMALIZACION = "Error de normalización"
MENSAJE_SIN_SSL = "Sin certificado SSL (HTTP)"
MENSAJE_ERROR_SSL = "Error SSL/Certificado"
MENSAJE_TIMEOUT = "Timeout"
MENSAJE_ERROR_CONEXION = "Error de conexión"
MENSAJE_DEMASIADAS_REDIRECCIONES = "Demasiadas redirecciones"
MENSAJE_ERROR_REINTENTOS = "Error después de reintentos"
MENSAJE_PAGINA_PROBLEMATICA = "Página de error/bloqueada/dominio en venta"
MENSAJE_REQUIERE_LOGIN = "Requiere login"

# Valores que se escriben en Excel
VALOR_EXCEL_VALIDO = "VÁLIDO"
VALOR_EXCEL_NO_VALIDO = "NO VÁLIDO"
VALOR_EXCEL_VALIDAR = "VALIDAR"


# ============================================================================
# CONFIGURACIÓN DE LA INTERFAZ
# ============================================================================

# Valores por defecto de la UI
UI_COLUMNA_URLS_DEFAULT = 'C'
UI_FILA_INICIO_DEFAULT = 2
UI_FILA_FIN_DEFAULT = 100
UI_COLUMNA_RESULTADO_DEFAULT = 'Z'

# Geometría de la ventana
UI_VENTANA_ANCHO = 900
UI_VENTANA_ALTO = 500

# Colores de la interfaz
UI_COLOR_FONDO = '#f0f0f0'
UI_COLOR_EXITO = '#27ae60'
UI_COLOR_ERROR = '#e74c3c'
UI_COLOR_WARNING = '#f39c12'
UI_COLOR_PROCESANDO = '#95a5a6'
UI_COLOR_TEXTO_PRINCIPAL = '#2c3e50'
UI_COLOR_TEXTO_SECUNDARIO = '#7f8c8d'
UI_COLOR_BLANCO = '#ffffff'
UI_COLOR_DROP_AREA = '#ecf0f1'
UI_COLOR_INFO = '#3498db'

# Fuentes
UI_FUENTE_PRINCIPAL = 'Arial'

# Estilos de Fuentes (Agrupados por uso)
UI_FONT_TITULO_APP = (UI_FUENTE_PRINCIPAL, 18, "bold")
UI_FONT_TITULO_SECCION = (UI_FUENTE_PRINCIPAL, 11, "bold")
UI_FONT_TEXTO_NORMAL = (UI_FUENTE_PRINCIPAL, 11)
UI_FONT_TEXTO_INFO = (UI_FUENTE_PRINCIPAL, 9)
UI_FONT_LABEL_RESALTADO = (UI_FUENTE_PRINCIPAL, 10, "bold")
UI_FONT_INPUT = (UI_FUENTE_PRINCIPAL, 10)
UI_FONT_AYUDA = (UI_FUENTE_PRINCIPAL, 8)
UI_FONT_BOTON_PRINCIPAL = (UI_FUENTE_PRINCIPAL, 12, "bold")
UI_FONT_BOTON_SECUNDARIO = (UI_FUENTE_PRINCIPAL, 11, "bold")
UI_FONT_BOTON_TERCIARIO = (UI_FUENTE_PRINCIPAL, 10)


# ============================================================================
# EMOJIS PARA LOGS
# ============================================================================
EMOJI_VALIDO = "✅"
EMOJI_NO_VALIDO = "❌"
EMOJI_VALIDAR = "⚠️"
EMOJI_VACIO = "📘"
EMOJI_ARCHIVO = "📂"
EMOJI_HOJA = "📋"
EMOJI_INICIO = "🚀"
EMOJI_GUARDADO = "💾"
EMOJI_TIEMPO = "⏱️"
EMOJI_ESTADO = "📊"
EMOJI_CUIDADO = "🛑"
EMOJI_CONTINUAR = "▶️"
EMOJI_CONFIGURACION = "⚙️"
EMOJI_INICIO = "🔄"
EMOJI_CADENA = "🔗"
EMOJI_DETENER = "⏹"
EMOJI_PAUSAR = "⏸"