# ============================================================================
# views/validador_view.py
# VISTA - Solo interfaz visual, sin lógica de negocio
# ============================================================================

import tkinter as tk
from tkinter import ttk

from config.constants import (
    EMOJI_CADENA,
    EMOJI_ARCHIVO,
    EMOJI_CONFIGURACION,
    EMOJI_ESTADO,
    EMOJI_CONTINUAR,
    EMOJI_HOJA,
    EMOJI_VALIDO,
    EMOJI_NO_VALIDO,
    EMOJI_DETENER,
    EMOJI_PAUSAR,
    UI_COLOR_FONDO,
    UI_COLOR_TEXTO_PRINCIPAL,
    UI_COLOR_TEXTO_SECUNDARIO,
    UI_COLOR_ERROR,
    UI_COLOR_EXITO,
    UI_COLOR_WARNING,
    UI_COLOR_PROCESANDO,
    UI_COLOR_BLANCO,
    UI_COLOR_DROP_AREA,
    UI_COLOR_INFO,
    UI_FONT_TITULO_APP,
    UI_FONT_TITULO_SECCION,
    UI_FONT_TEXTO_NORMAL,
    UI_FONT_TEXTO_INFO,
    UI_FONT_LABEL_RESALTADO,
    UI_FONT_INPUT,
    UI_FONT_AYUDA,
    UI_FONT_BOTON_PRINCIPAL,
    UI_FONT_BOTON_SECUNDARIO,
    UI_FONT_BOTON_TERCIARIO
)


class ValidadorView:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{EMOJI_CADENA} Validador de Enlaces - Excel")
        self.root.geometry("900x500")
        self.root.configure(bg=UI_COLOR_FONDO)
        
        # Referencias a widgets
        self.drop_label = None
        self.archivo_label = None
        self.hoja_combo = None
        self.columna_entrada = None
        self.fila_inicio = None
        self.fila_fin = None
        self.resultado_entrada = None
        self.ejecutar_btn = None
        self.ver_logs_btn = None
        self.progreso_label = None
        self.progreso_bar = None
        
        self.crear_interfaz()
    
    # ========================================================================
    # CREACIÓN DE INTERFAZ
    # ========================================================================
    
    def crear_interfaz(self):
        titulo = tk.Label(
            self.root, 
            text=f"{EMOJI_CADENA} Validador de Enlaces en Excel", 
            font=UI_FONT_TITULO_APP, 
            bg=UI_COLOR_FONDO, 
            fg=UI_COLOR_TEXTO_PRINCIPAL
        )
        titulo.pack(pady=15)
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=UI_COLOR_FONDO)
        main_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Crear secciones
        self.crear_seccion_archivo(main_frame)
        self.crear_seccion_configuracion(main_frame)
        self.crear_seccion_resultados(main_frame)
        self.crear_seccion_ejecucion(main_frame)
    
    def crear_seccion_archivo(self, parent):
        archivo_frame = tk.LabelFrame(
            parent, 
            text=f"{EMOJI_ARCHIVO} 1. Cargar Archivo Excel", 
            font=UI_FONT_TITULO_SECCION, 
            bg=UI_COLOR_BLANCO, 
            padx=15, 
            pady=15
        )
        archivo_frame.pack(fill='x', pady=10)
        
        # Zona de arrastrar y soltar
        self.drop_label = tk.Label(
            archivo_frame, 
            text=f"{EMOJI_ARCHIVO} Arrastra el archivo Excel aquí\no haz clic para seleccionar",
            font=UI_FONT_TEXTO_NORMAL, 
            bg=UI_COLOR_DROP_AREA, 
            fg=UI_COLOR_TEXTO_SECUNDARIO,
            relief='solid', 
            borderwidth=2, 
            height=4,
            cursor='hand2'
        )
        self.drop_label.pack(fill='x', pady=5)
        
        # Label de estado del archivo
        self.archivo_label = tk.Label(
            archivo_frame, 
            text="No se ha cargado ningún archivo", 
            font=UI_FONT_TEXTO_INFO, 
            bg=UI_COLOR_BLANCO, 
            fg=UI_COLOR_ERROR
        )
        self.archivo_label.pack(pady=5)
    
    def crear_seccion_configuracion(self, parent):
        config_frame = tk.LabelFrame(
            parent, 
            text=f"{EMOJI_CONFIGURACION} 2. Configuración de Análisis", 
            font=UI_FONT_TITULO_SECCION, 
            bg=UI_COLOR_BLANCO, 
            padx=15, 
            pady=15
        )
        config_frame.pack(fill='x', pady=10)
        
        # Selección de hoja
        hoja_frame = tk.Frame(config_frame, bg=UI_COLOR_BLANCO)
        hoja_frame.pack(fill='x', pady=5)
        
        tk.Label(
            hoja_frame, 
            text="Hoja de Excel:", 
            font=UI_FONT_LABEL_RESALTADO, 
            bg=UI_COLOR_BLANCO, 
            width=20, 
            anchor='w'
        ).pack(side='left')
        
        self.hoja_combo = ttk.Combobox(hoja_frame, state='disabled', width=25)
        self.hoja_combo.pack(side='left', padx=10)
        
        # Columna de URLs
        col_frame = tk.Frame(config_frame, bg=UI_COLOR_BLANCO)
        col_frame.pack(fill='x', pady=5)
        
        tk.Label(
            col_frame, 
            text="Columna de URLs (letra):", 
            font=UI_FONT_LABEL_RESALTADO, 
            bg=UI_COLOR_BLANCO, 
            width=20, 
            anchor='w'
        ).pack(side='left')
        
        self.columna_entrada = tk.Entry(col_frame, width=10, font=UI_FONT_INPUT)
        self.columna_entrada.pack(side='left', padx=10)
        self.columna_entrada.insert(0, 'C')
        
        tk.Label(
            col_frame,
            text="Ejemplo: A, B, C, AA, AB...",
            font=UI_FONT_AYUDA,
            bg=UI_COLOR_BLANCO,
            fg=UI_COLOR_TEXTO_SECUNDARIO
        ).pack(side='left', padx=5)
        
        # Rango de filas
        rango_frame = tk.Frame(config_frame, bg=UI_COLOR_BLANCO)
        rango_frame.pack(fill='x', pady=10)
        
        tk.Label(
            rango_frame, 
            text="Fila inicial:", 
            font=UI_FONT_LABEL_RESALTADO, 
            bg=UI_COLOR_BLANCO, 
            width=20, 
            anchor='w'
        ).pack(side='left')
        
        self.fila_inicio = tk.Spinbox(
            rango_frame, 
            from_=1, 
            to=999999, 
            width=10, 
            font=UI_FONT_INPUT
        )
        self.fila_inicio.pack(side='left', padx=10)
        self.fila_inicio.delete(0, 'end')
        self.fila_inicio.insert(0, '2')
        
        tk.Label(
            rango_frame, 
            text="Fila final:", 
            font=UI_FONT_LABEL_RESALTADO, 
            bg=UI_COLOR_BLANCO
        ).pack(side='left', padx=(20, 0))
        
        self.fila_fin = tk.Spinbox(
            rango_frame, 
            from_=1, 
            to=999999, 
            width=10, 
            font=UI_FONT_INPUT
        )
        self.fila_fin.pack(side='left', padx=10)
        self.fila_fin.delete(0, 'end')
        self.fila_fin.insert(0, '100')
    
    def crear_seccion_resultados(self, parent):
        result_frame = tk.LabelFrame(
            parent, 
            text=f"{EMOJI_ESTADO} 3. Configuración de Resultados", 
            font=UI_FONT_TITULO_SECCION, 
            bg=UI_COLOR_BLANCO, 
            padx=15, 
            pady=15
        )
        result_frame.pack(fill='x', pady=10)
        
        # Columna para resultados
        res_col_frame = tk.Frame(result_frame, bg=UI_COLOR_BLANCO)
        res_col_frame.pack(fill='x', pady=5)
        
        tk.Label(
            res_col_frame, 
            text="Columna resultado (letra):", 
            font=UI_FONT_LABEL_RESALTADO, 
            bg=UI_COLOR_BLANCO, 
            width=22, 
            anchor='w'
        ).pack(side='left')
        
        self.resultado_entrada = tk.Entry(res_col_frame, width=10, font=UI_FONT_INPUT)
        self.resultado_entrada.pack(side='left', padx=10)
        self.resultado_entrada.insert(0, 'Z')
        
        tk.Label(
            res_col_frame,
            text="Ejemplo: Z, AA, AB... | Delay: 2 seg (fijo)",
            font=UI_FONT_AYUDA,
            bg=UI_COLOR_BLANCO,
            fg=UI_COLOR_TEXTO_SECUNDARIO
        ).pack(side='left', padx=5)
    
    def crear_seccion_ejecucion(self, parent):
        exec_frame = tk.Frame(parent, bg=UI_COLOR_FONDO)
        exec_frame.pack(fill='x', pady=15)
        
        # Frame para botones (ejecutar, pausar, detener y ver logs)
        botones_frame = tk.Frame(exec_frame, bg=UI_COLOR_FONDO)
        botones_frame.pack()
        
        # Botón de iniciar
        self.ejecutar_btn = tk.Button(
            botones_frame, 
            text=f"{EMOJI_CONTINUAR} INICIAR VALIDACIÓN", 
            font=UI_FONT_BOTON_PRINCIPAL, 
            bg=UI_COLOR_EXITO, 
            fg=UI_COLOR_BLANCO,
            state='disabled',
            relief='raised', 
            borderwidth=3, 
            padx=20, 
            pady=10,
            cursor='hand2'
        )
        self.ejecutar_btn.pack(side='left', padx=5)
        
        # Botón de pausar/reanudar
        self.pausar_btn = tk.Button(
            botones_frame,
            text=f"{EMOJI_PAUSAR} PAUSAR",
            font=UI_FONT_BOTON_SECUNDARIO,
            bg=UI_COLOR_WARNING,
            fg=UI_COLOR_BLANCO,
            state='disabled',
            relief='raised',
            borderwidth=3,
            padx=15,
            pady=10,
            cursor='hand2'
        )
        self.pausar_btn.pack(side='left', padx=5)
        
        # Botón de detener
        self.detener_btn = tk.Button(
            botones_frame,
            text=f"{EMOJI_DETENER} DETENER",
            font=UI_FONT_BOTON_SECUNDARIO,
            bg=UI_COLOR_ERROR,
            fg=UI_COLOR_BLANCO,
            state='disabled',
            relief='raised',
            borderwidth=3,
            padx=15,
            pady=10,
            cursor='hand2'
        )
        self.detener_btn.pack(side='left', padx=5)
        
        # Botón de ver logs
        self.ver_logs_btn = tk.Button(
            botones_frame,
            text=f"{EMOJI_HOJA} Ver Logs",
            font=UI_FONT_BOTON_TERCIARIO,
            bg=UI_COLOR_INFO,
            fg=UI_COLOR_BLANCO,
            relief='raised',
            borderwidth=2,
            padx=15,
            pady=10,
            cursor='hand2'
        )
        self.ver_logs_btn.pack(side='left', padx=5)
        
        # Label de progreso
        self.progreso_label = tk.Label(
            parent, 
            text="", 
            font=UI_FONT_INPUT, 
            bg=UI_COLOR_FONDO, 
            fg=UI_COLOR_TEXTO_PRINCIPAL
        )
        self.progreso_label.pack(pady=5)
        
        # Barra de progreso
        self.progreso_bar = ttk.Progressbar(parent, length=900, mode='determinate')
        self.progreso_bar.pack(pady=5)
    
    # ========================================================================
    # Para que el Controlador actualice la vista
    # ========================================================================
    
    def mostrar_archivo_cargado(self, nombre_archivo, num_filas, num_columnas, hojas):
        self.drop_label.config(
            bg=UI_COLOR_EXITO, 
            fg=UI_COLOR_BLANCO, 
            text=f"{EMOJI_VALIDO} Archivo cargado\n{nombre_archivo}"
        )
        self.archivo_label.config(
            text=f"{EMOJI_VALIDO} {num_filas} filas × {num_columnas} columnas | {len(hojas)} hoja(s)", 
            fg=UI_COLOR_EXITO
        )
        self.hoja_combo.config(state='readonly', values=hojas)
        if hojas:
            self.hoja_combo.current(0)
        self.ejecutar_btn.config(state='normal')
    
    def mostrar_error_carga(self):
        self.drop_label.config(
            bg=UI_COLOR_ERROR, 
            fg=UI_COLOR_BLANCO, 
            text=f"{EMOJI_NO_VALIDO} Error al cargar archivo\nIntenta nuevamente"
        )
    
    def actualizar_progreso(self, texto, valor):
        self.progreso_label.config(text=texto)
        self.progreso_bar['value'] = valor
        self.root.update()
    
    def configurar_progreso_maximo(self, maximo):
        self.progreso_bar['maximum'] = maximo
    
    def resetear_progreso(self):
        self.progreso_label.config(text="")
        self.progreso_bar['value'] = 0
    
    def habilitar_boton_ejecutar(self):
        self.ejecutar_btn.config(
            state='normal', 
            bg=UI_COLOR_EXITO, 
            text=f"{EMOJI_CONTINUAR} INICIAR VALIDACIÓN"
        )
    
    def deshabilitar_boton_ejecutar(self):
        self.ejecutar_btn.config(
            state='disabled', 
            bg=UI_COLOR_PROCESANDO, 
            text=f"{EMOJI_PAUSAR} VALIDANDO..."
        )
        # Habilitar botones durante validación
        self.pausar_btn.config(state='normal', bg=UI_COLOR_WARNING, text=f"{EMOJI_PAUSAR} PAUSAR")
        self.detener_btn.config(state='normal', bg=UI_COLOR_ERROR)
    
    def cambiar_boton_pausar_a_reanudar(self):
        self.pausar_btn.config(text=f"{EMOJI_CONTINUAR} REANUDAR", bg=UI_COLOR_EXITO)
    
    def cambiar_boton_reanudar_a_pausar(self):
        self.pausar_btn.config(text=f"{EMOJI_PAUSAR} PAUSAR", bg=UI_COLOR_WARNING)
    
    def deshabilitar_boton_pausar(self):
        self.pausar_btn.config(state='disabled', bg=UI_COLOR_PROCESANDO)
    
    def deshabilitar_boton_detener(self):
        self.detener_btn.config(state='disabled', bg=UI_COLOR_PROCESANDO)
    
    # ========================================================================
    # GETTERS - Para que el Controlador obtenga valores ingresados
    # ========================================================================
    
    def obtener_columna(self):
        return self.columna_entrada.get().strip().upper()
    
    def obtener_fila_inicio(self):
        return int(self.fila_inicio.get())
    
    def obtener_fila_fin(self):
        return int(self.fila_fin.get())
    
    def obtener_hoja(self):
        return self.hoja_combo.get()
    
    def obtener_columna_resultado(self):
        return self.resultado_entrada.get().strip().upper()
    
    # ========================================================================
    # MÉTODOS PARA BINDING DE EVENTOS (el Controlador los conectará)
    # ========================================================================
    
    def vincular_click_archivo(self, callback):
        self.drop_label.bind('<Button-1>', callback)
    
    def vincular_boton_ejecutar(self, callback):
        self.ejecutar_btn.config(command=callback)
    
    def vincular_boton_ver_logs(self, callback):
        self.ver_logs_btn.config(command=callback)
    
    def vincular_boton_detener(self, callback):
        self.detener_btn.config(command=callback)
    
    def vincular_boton_pausar(self, callback):
        self.pausar_btn.config(command=callback)
    
    def vincular_drag_drop(self, callback):
        try:
            from tkinterdnd2 import DND_FILES
            self.drop_label.drop_target_register(DND_FILES)
            self.drop_label.dnd_bind('<<Drop>>', callback)
        except ImportError:
            pass  