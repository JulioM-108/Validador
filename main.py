
import tkinter as tk
from controller.validator_Controller import ValidadorController
from utils.logger import get_logger


def main(): 
    # Inicializar el logger para capturar el arranque
    logger = get_logger(guardar_en_archivo=True, ruta_archivo="logs_validacion.txt")
    
    # Intentar usar TkinterDnD para drag & drop
    try:
        from tkinterdnd2 import TkinterDnD
        root = TkinterDnD.Tk()
        logger.success("TkinterDnD inicializado - Drag & Drop disponible")
    except ImportError:
        root = tk.Tk()
        logger.warning("TkinterDnD no instalado - Drag & Drop no disponible")
        logger.info("Para habilitar: pip install tkinterdnd2")
    except Exception as e:
        root = tk.Tk()
        logger.error(f"Error al inicializar TkinterDnD: {e}")
    
    # Inicializar el controlador (que a su vez crea modelo y vista)
    controller = ValidadorController(root)
    
    # Iniciar el loop principal de Tkinter
    root.mainloop()


if __name__ == "__main__":
    main()