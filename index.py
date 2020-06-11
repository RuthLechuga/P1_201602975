from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from Arbol.Mensaje import *

import gramatica_asc as g_asc
import Arbol.TablaDeSimbolos as TS

mensajes = []
ts_global = None

class EditorTexto:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Augus IDE")

        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=RIGHT, fill=Y)

        menubar = Menu(self.root)
        
        mArchivo = Menu(menubar)
        mArchivo.add_command(label="Nuevo", command=self.nuevo)
        mArchivo.add_command(label="Abrir", command=self.abrir)
        mArchivo.add_command(label="Guardar", command=self.guardar)
        mArchivo.add_command(label="Guardar Como", command=self.guardarComo)
        mArchivo.add_command(label="Cerrar", command=self.cerrar)
        mArchivo.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Archivo", menu=mArchivo)

        mEditar = Menu(menubar)
        mEditar.add_command(label="Buscar", command=self.buscar)
        mEditar.add_command(label="Reemplazar", command=self.reemplazar)
        menubar.add_cascade(label="Editar", menu=mEditar)

        mEjecutar = Menu(menubar)
        mEjecutar.add_command(label="Ejecutar ascendente", command=self.ej_ascendente)
        mEjecutar.add_command(label="Ejecutar descendente", command=self.ej_descendente)
        mEjecutar.add_command(label="Reporte errores", command=self.reporte_errores)
        mEjecutar.add_command(label="Reporte Tabla Simbolos",command=self.reporte_ts)
        mEjecutar.add_command(label="Reporte AST",command=self.reporte_ast)
        mEjecutar.add_command(label="Reporte gramatical",command=self.reporte_gramatical)
        menubar.add_cascade(label="Ejecutar", menu=mEjecutar)

        mOpciones = Menu(menubar)
        mOpciones.add_command(label="Color fondo",command=self.cambiar_color)
        mOpciones.add_command(label="Activar lineas",command=self.activar_linas)
        menubar.add_cascade(label="Opciones", menu=mOpciones)

        mAyuda = Menu(menubar)
        mAyuda.add_command(label="Acerca de", command=self.acerca)
        menubar.add_cascade(label="Ayuda", menu=mAyuda)
        self.root.config(menu=menubar)

        self.text = Text(self.root)
        self.text.pack(expand=YES, fill=BOTH)

        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

        self.root.mainloop()
        
    def nuevo(self):
        print('nuevo')
    
    def abrir(self):
        fileName = askopenfilename()
        try:
            file = open(fileName, 'r')
            contents = file.read()

            self.text.delete(0.0, END)
            self.text.insert(0.0, contents)
        except:
            pass

    def guardar(self):
        fileName = asksaveasfilename()
        try:
            file = open(fileName, 'w')
            textoutput = self.text.get(0.0, END)
            file.write(textoutput)
        except:
            pass
        finally:
            file.close()

    def guardarComo(self):
        print('Guardar Como')

    def salir(self):
        print('salir')
    
    def cerrar(self):
        print('cerrar')
    
    def buscar(self):
        print('buscar')
    
    def reemplazar(self):
        print('reemplazar')
    
    def ej_ascendente(self):
        global mensajes
        mensajes = []
        etiquetas = g_asc.parse(self.text.get(0.0, END))

        global ts_global
        ts_global = TS.TablaDeSimbolos()

        for etiqueta in etiquetas:
            if not ts_global.addEtiqueta(etiqueta):
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La etiqueta: '+etiqueta.identificador+' ya existe.',0,0))
        
        main = ts_global.getEtiqueta('main')
        print('-----------------------------------------------')

        for instruccion in main.instrucciones:
            res = instruccion.ejecutar(ts_global,mensajes)
            if res:
                break
    
    def ej_descendente(self):
        print('descendente')

    def reporte_errores(self):
        global mensajes
        for mensaje in mensajes:
            print(mensaje.mensaje,"en:",mensaje.linea,",",mensaje.columna)
    
    def reporte_ts(self):
        print('reporte tabla')
    
    def reporte_ast(self):
        print('reporte ast')

    def reporte_gramatical(self):
        print('reporte gramatical')
    
    def cambiar_color(self):
        print('cambiar color')
    
    def activar_linas(self):
        print('lineas')

    def acerca(self):
        root = Tk()
        root.wm_title("Acerca De")
        texto=("Augus es un lenguaje de programación, basado en PHP y en MIPS. Su principal funcionalidad es ser un lenguaje intermedio, ni de alto nivel como PHP ni de bajo nivel como el lenguaje ensamblador de MIPS. \n Elaborado por Ruth Lechuga, 201602975")
        textONlabel = Label(root, text=texto)
        textONlabel.pack()

EditorTexto()