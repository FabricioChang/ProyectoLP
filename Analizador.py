import tkinter as tk
from tkinter import filedialog, messagebox
from Analizador_Lexico import analizador_lexico
from Analizador_Sintactico import analizador_sintactico
from Analizador_Semantico import analizador_semantico

file = None
# Funciones de los botones
def cargar_archivo():
    global file
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.rb"), ("Todos los archivos", "*.*")])
    file = archivo
    if archivo:
        estado_carga.set("Estado de carga: Exitoso ✓")
        messagebox.showinfo("Archivo cargado", f"Se ha cargado el archivo: {archivo}")
    else:
        estado_carga.set("Estado de carga: Fallido ✗")
    

def ejecutar_analisis():
    # Aquí iría la lógica para ejecutar los análisis léxico, sintáctico y semántico
    text_lexico.insert(tk.END, analizador_lexico(file))
    text_sintactico.insert(tk.END, analizador_sintactico(file))
    text_semantico.insert(tk.END, analizador_semantico(file))
    messagebox.showinfo("Ejecutar", "Análisis completado.")

def limpiar():
    text_lexico.delete(1.0, tk.END)
    text_sintactico.delete(1.0, tk.END)
    text_semantico.delete(1.0, tk.END)
    estado_carga.set("Estado de carga: Sin cargar")

def guardar_analisis():
    archivo = filedialog.asksaveasfilename(title="Guardar análisis", defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, "w") as file:
            file.write("=== Análisis Léxico ===\n")
            file.write(text_lexico.get(1.0, tk.END))
            file.write("\n=== Análisis Sintáctico ===\n")
            file.write(text_sintactico.get(1.0, tk.END))
            file.write("\n=== Análisis Semántico ===\n")
            file.write(text_semantico.get(1.0, tk.END))
        messagebox.showinfo("Guardar", "Análisis guardado con éxito.")

# Configuración principal de la ventana
root = tk.Tk()
root.title("Analizador de Código Ruby")
root.geometry("800x600")  # Tamaño inicial

# Configuración de expansión para filas y columnas
root.grid_columnconfigure(0, weight=1)  # Expansión para la columna 0
root.grid_columnconfigure(1, weight=1)  # Expansión para la columna 1
root.grid_columnconfigure(2, weight=1)  # Expansión para la columna 2
root.grid_rowconfigure(2, weight=3)     # Expansión para la fila 2
root.grid_rowconfigure(4, weight=3)     # Expansión para la fila 4

# Estado de carga
estado_carga = tk.StringVar()
estado_carga.set("Estado de carga: Sin cargar")

# Widgets
btn_cargar = tk.Button(root, text="Cargar archivo", command=cargar_archivo, width=15, height=2)
btn_cargar.grid(row=0, column=0, padx=10, pady=10)

label_estado = tk.Label(root, textvariable=estado_carga)
label_estado.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Cuadros de texto para los análisis
label_semantico = tk.Label(root, text="Análisis Semántico")
label_semantico.grid(row=1, column=0, columnspan=3, pady=10, sticky="w")
text_semantico = tk.Text(root, height=5, width=90)
text_semantico.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")  # Se adapta dinámicamente

label_lexico = tk.Label(root, text="Análisis Léxico")
label_lexico.grid(row=3, column=0, padx=10, sticky="w")
text_lexico = tk.Text(root, height=10, width=40)
text_lexico.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")  # Se adapta dinámicamente

label_sintactico = tk.Label(root, text="Análisis Sintáctico")
label_sintactico.grid(row=3, column=1, padx=10, sticky="w")
text_sintactico = tk.Text(root, height=10, width=40)
text_sintactico.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")  # Se adapta dinámicamente

# Botones inferiores
btn_guardar = tk.Button(root, text="Guardar Análisis", command=guardar_analisis, width=15, height=2)
btn_guardar.grid(row=5, column=0, padx=10, pady=10)

btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar, width=15, height=2)
btn_limpiar.grid(row=5, column=1, padx=10, pady=10)

btn_ejecutar = tk.Button(root, text="Ejecutar", command=ejecutar_analisis, width=15, height=2)
btn_ejecutar.grid(row=5, column=2, padx=10, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()
