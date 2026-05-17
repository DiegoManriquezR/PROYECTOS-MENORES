import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading
from funciones import inicio_sesion, registrar_usuario, guardar_indicadores

class Aplicacion(tk.Tk):

    def consultar_indicadores(self, indicadores, fecha):
        indicadores = ["uf", "ivp", "ipc", "utm", "dolar", "euro"] 
        resultado_str = ""
        self.resultados_consultados = {}
        
        with requests.Session() as session:
            for indicador in indicadores:
                url = f"https://mindicador.cl/api/{indicador}/{fecha}"
                try:
                    respuesta = session.get(url)
                    respuesta.raise_for_status()
                    datos = respuesta.json()
                    
                    if datos.get("serie"):
                        valor = datos["serie"][0]["valor"]
                        unidad = datos["unidad_medida"]
                        self.resultados_consultados[indicador] = {"valor": valor, "unidad": unidad}
                        resultado_str += f"{indicador}: {valor} {unidad}\n"
                    else:
                        self.resultados_consultados[indicador] = {"mensaje": "No se encontraron datos"}
                        resultado_str += f"{indicador}: No se encontraron datos\n"
                except requests.exceptions.HTTPError as http_err:
                    self.resultados_consultados[indicador] = {"mensaje": f"Error HTTP: {http_err}"}
                    resultado_str += f"{indicador}: Error HTTP\n"
                except requests.exceptions.RequestException as req_err:
                    self.resultados_consultados[indicador] = {"mensaje": f"Error al consultar: {req_err}"}
                    resultado_str += f"{indicador}: Error al consultar\n"
            self.resultados_consultados['fecha'] = fecha

        return resultado_str

    def __init__(self):
        super().__init__()
        self.title("Sistema de Autenticación")
        self.geometry("450x350")
        self.configure(bg="#81C784")  # Color de fondo de la ventana principal

        self.frame = tk.Frame(self, bg="#A5D6A7", padx=20, pady=20)  # Fondo del marco
        self.frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        tk.Label(self.frame, text="Bienvenido al Sistema", font=("Helvetica", 18, "bold"), bg="#A5D6A7", fg="#388E3C").pack(pady=20)  # Color del texto

        self.crear_botones()

        self.resultados_frame = None

    def crear_botones(self):
        estilo_boton = {'bg': '#388E3C', 'fg': 'white', 'font': ('Helvetica', 12, 'bold'), 'width': 20}

        self.boton_iniciar_sesion = tk.Button(self.frame, text="Iniciar Sesión", command=self.inicio_sesion, **estilo_boton)
        self.boton_iniciar_sesion.pack(pady=15)

        self.boton_registrar_usuario = tk.Button(self.frame, text="Registrar Usuario", command=self.registrar_usuario, **estilo_boton)
        self.boton_registrar_usuario.pack(pady=15)

    def inicio_sesion(self):
        ventana_sesion = tk.Toplevel(self)
        ventana_sesion.title("Iniciar Sesión")
        ventana_sesion.geometry("400x300")
        ventana_sesion.configure(bg="#C8E6C9")  # Fondo de la ventana secundaria

        tk.Label(ventana_sesion, text="Iniciar Sesión", font=("Helvetica", 16, "bold"), bg="#C8E6C9", fg="#388E3C").pack(pady=10)  # Color del texto

        tk.Label(ventana_sesion, text="RUT (con punto y guión):", bg="#C8E6C9", fg="#388E3C").pack(pady=5)
        entry_rut = tk.Entry(ventana_sesion)
        entry_rut.pack(pady=5)

        tk.Label(ventana_sesion, text="Contraseña:", bg="#C8E6C9", fg="#388E3C").pack(pady=5)
        entry_contraseña = tk.Entry(ventana_sesion, show="*")
        entry_contraseña.pack(pady=5)
        
        def manejar_inicio_sesion():
            rut = entry_rut.get()
            contraseña = entry_contraseña.get()

            nombre_usuario = inicio_sesion(rut, contraseña)
            if nombre_usuario:
                messagebox.showinfo("Éxito", f"Hola, {nombre_usuario}, has iniciado sesión correctamente.")
                ventana_sesion.destroy()  # Cerrar la ventana de inicio de sesión
                self.ventana_consulta_indicadores()
            else:
                messagebox.showerror("Error", "RUT o contraseña incorrectos.")
        tk.Button(ventana_sesion, text ="Aceptar", command=manejar_inicio_sesion, bg='#388E3C', fg='white', font=('Helvetica', 12, 'bold')).pack(pady=10)

    def ventana_consulta_indicadores(self):
        ventana_consulta = tk.Toplevel(self)
        ventana_consulta.title("Consulta de Indicadores")
        ventana_consulta.geometry("400x600")
        ventana_consulta.configure(bg="#C8E6C9")  # Fondo de la ventana secundaria

        tk.Label(ventana_consulta, text="Consulta de Indicadores", font=("Helvetica", 16, "bold"), bg="#C8E6C9", fg="#388E3C").pack(pady=10)

        tk.Label(ventana_consulta, text="Fecha (DD-MM-YYYY):", bg="#C8E6C9", fg="#388E3C").pack(pady=5)
        entrada_fecha = tk.Entry(ventana_consulta)
        entrada_fecha.pack(pady=5)

        self.progress = ttk.Progressbar(ventana_consulta, mode='indeterminate')
        self.progress.pack(pady=10)

        self.resultados_frame = tk.Frame(ventana_consulta, bg="#C8E6C9")
        self.resultados_frame.pack(pady=10)

        def consultar_indicadores_button():
            fecha = entrada_fecha.get()
            indicadores = ["uf", "ivp", "ipc", "utm", "dolar", "euro"]

            self.progress.start()

            threading.Thread(target=self.realizar_consulta, args=(indicadores, fecha)).start()

        tk.Button(ventana_consulta, text="Consultar", command=consultar_indicadores_button, bg='#388E3C', fg='white', font=('Helvetica', 12, 'bold')).pack(pady=10)
        tk.Button(ventana_consulta, text="Guardar Indicadores", command=self.msg_ind, bg='#388E3C', fg='white', font=('Helvetica', 12, 'bold')).pack(pady=10)

        def volver_al_inicio():
            ventana_consulta.destroy()

        tk.Button(ventana_consulta, text="Volver", command=volver_al_inicio, bg='#388E3C', fg='white', font=('Helvetica', 12, 'bold')).pack(pady=10)

    def realizar_consulta(self, indicadores, fecha):
        resultado = self.consultar_indicadores(indicadores, fecha)
        self.progress.stop()  

        self.after(0, lambda: self.mostrar_resultados(resultado))

    def mostrar_resultados(self, resultado):
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()

        tk.Label(self.resultados_frame, text="Resultados de Indicadores:", bg="#C8E6C9", fg="#388E3C").pack(pady=5)

        label_resultado = tk.Label(self.resultados_frame, text=resultado, bg="#C8E6C9", fg="#388E3C")
        label_resultado.pack(pady=5)

    def msg_ind(self):
        try:
            guardar_indicadores(self.resultados_consultados)
            messagebox.showinfo("Éxito", "Indicadores guardados exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar indicadores: {e}")

    def registrar_usuario(self):
        ventana_registro = tk.Toplevel(self)
        ventana_registro.title("Registrar Usuario")
        ventana_registro.geometry("400x400")
        ventana_registro.configure(bg="#C8E6C9")  # Fondo de la ventana secundaria

        tk.Label(ventana_registro, text="Registrar Usuario", font=("Helvetica", 16, "bold"), bg="#C8E6C9", fg="#388E3C").pack(pady=10)

        tk.Label(ventana_registro, text="RUT(con punto y guión):", bg="#C8E6C9", fg="#388E3C").pack(pady=5)
        entry_rut = tk.Entry(ventana_registro)
        entry_rut.pack(pady=5)

        tk.Label(ventana_registro, text="Nombre:", bg="#C8E6C9", fg="#388E3C").pack(pady=5)
        entry_nombre = tk.Entry(ventana_registro)
        entry_nombre.pack(pady=5)

        tk.Label(ventana_registro, text="Apellido:", bg="#C8E6C9", fg="#388E3C").pack(pady=5)
        entry_apellido = tk.Entry(ventana_registro)
        entry_apellido.pack(pady=5)

        tk.Label(ventana_registro, text="Contraseña:", bg="#C8E6C9", fg="#388E3C").pack(pady=5)
        entry_contraseña = tk.Entry(ventana_registro, show="*")
        entry_contraseña.pack(pady=5)

        tk.Button(ventana_registro, text="Registrar", command=lambda: registrar_usuario(
            entry_rut.get(),
            entry_nombre.get(),
            entry_apellido.get(),
            entry_contraseña.get(),
        ), bg='#388E3C', fg='white', font=('Helvetica', 12, 'bold')).pack(pady=10)

        tk.Button(ventana_registro, text="Volver", command=ventana_registro.destroy, bg='#388E3C', fg='white', font=('Helvetica', 12, 'bold')).pack(pady=10)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
