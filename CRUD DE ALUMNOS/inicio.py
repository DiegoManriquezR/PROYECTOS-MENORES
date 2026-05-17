import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from funciones import insertar_producto,mostrar_producto,actualizar_producto,eliminar_producto

class AplicacionCRUD(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('CRUD SECCION LUNES POR LA TARDE') #TITULO DE VENTANA
        self.geometry('600x400') #esto es el tamaño de la ventana
        self.crear_widgets()
        self.mostrar_producto()
        
    def crear_widgets(self):
        #creamos el titulo
        tk.Label(self,text='CRUD SECCION LUNES POR LA TARDE', font=('Arial', 20)).pack(pady=10)
        
        #contenedor para 4 botones
        frame_botones=tk.Frame(self)
        frame_botones.pack(pady=5)
        
        #crear lista de botones (texto,comando,color de fondo, color de texto)
        botones=[
            ("Agregar Producto",self.agregar_producto,"#4CAF50","Black"),
            ('Mostrar Producto',self.mostrar_producto,'#2196F3','Black'),
            ('Actualizar Producto',self.actualizar_producto,'#FF9800','Black'),
            ('Eliminar Producto',self.eliminar_producto,'#F44336','Black'),
        ]
        for texto, comando,fg,bg in botones:
            tk.Button(frame_botones,text=texto,command=comando, bg=bg,fg=fg, width=20).pack(side=tk.LEFT,padx=5)
        #crear n treeview -> tabla de datos
        columnas=('ID','CODIGO','NOMBRE','MODELO','PRECIO','CANTIDAD')
        self.tree=ttk.Treeview(self,columns=columnas,show='headings')
        
        #configuramos encabezados
        for col, ancho in zip(columnas,[30,100,150,100,80,70]):
            self.tree.heading(col,text=col)
            self.tree.column(col, width=ancho)
            
        #mostrar tabla
        self.tree.pack(pady=10,padx=10,fill=tk.BOTH,expand=True)
    def solicitar_dato(self,campo,tipo):
        if tipo=='string':
            return simpledialog.askstring(campo, f'ingrese el {campo} del producto', parent=self)
        elif tipo=='float':
            return simpledialog.askfloat(campo, f'ingrese el {campo} del producto', parent=self)
        elif tipo=='int':
            return simpledialog.askinteger(campo,f'ingrese el {campo} del producto', parent=self)
        
        
    def agregar_producto(self):
        
        datos={
            "codigo": self.solicitar_dato('CODIGO','string'),
            "nombre": self.solicitar_dato('NOMBRE','string'),
            "modelo": self.solicitar_dato('MODELO','string'),
            "precio": self.solicitar_dato('PRECIO','float'),
            "cantidad": self.solicitar_dato('CANTIDAD','int'),
        }
        if None not in datos.values():
            insertar_producto(**datos)
            messagebox.showinfo('exito','producto agregado correctamente.', parent=self)
            self.mostrar_producto()
            
    def mostrar_producto(self):
           for item in self.tree.get_children():
               self.tree.delete(item) 
               
           for producto in mostrar_producto():
               self.tree.insert('','end',values=producto)
               
    def actualizar_producto(self):
            id=self.solicitar_dato('ID','int')
            
            datos={
                'id':id,
                "codigo": self.solicitar_dato('CODIGO','string'),
                'nombre': self.solicitar_dato('NOMBRE','string'),
                'modelo': self.solicitar_dato('MODELO','string'),
                'precio': self.solicitar_dato('PRECIO','float'),
                'cantidad': self.solicitar_dato('CANTIDAD','int'),
            }
            
            if None not in datos.values():
                actualizar_producto(**datos)
                messagebox.showinfo('Exito','Producto actualizado correctamente.',parent=self)
                self.mostrar_producto()
                
    def eliminar_producto(self):
        id=self.solicitar_dato('ID','int')
        
        eliminar_producto(id)
        messagebox.showinfo('Exito', 'Producto eliminado correctamente.',parent=self)
        self.mostrar_producto()
        
        
app = AplicacionCRUD()
app.mainloop()