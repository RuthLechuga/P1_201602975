from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from Arbol.Exit import *
from Arbol.Mensaje import *
from Arbol.Etiqueta import *

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
        mensajes = g_asc.mensajes

        if len(mensajes) > 0:
            print('>>>>>Errores<<<<<')
            return

        global ts_global
        ts_global = TS.TablaDeSimbolos()

        for etiqueta in etiquetas:
            if not ts_global.addEtiqueta(etiqueta):
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La etiqueta: '+etiqueta.identificador+' ya existe.',0,0))
        
        print('-----------------------------------------------')
                
        etiqueta = ts_global.getEtiqueta('main')

        while not (etiqueta is None):

            bandera = False

            for instruccion in etiqueta.instrucciones:
                res = instruccion.ejecutar(ts_global,mensajes)
                if isinstance(res,Etiqueta) or isinstance(instruccion,Exit):
                    etiqueta = res
                    bandera = True
                    break
            
            if bandera:
                continue

            etiqueta = ts_global.getSiguiente()
             
    def ej_descendente(self):
        print('descendente')

    def reporte_errores(self):
        global mensajes
        html = ''' 
        <html>
            <head>
                <style>
                    table {
                        width:100%;
                    }
                    table, th, td {
                        border: 1px solid black;
                        border-collapse: collapse;
                    }
                    th, td {
                        padding: 15px;
                        text-align: left;
                    }
                    table#t01 th {
                        background-color: blue;
                        color: white;
                    }
                </style>
            </head>
            <body>
            <h1>Errores</h1>
            <table id="t01">
                <tr>
                    <th>Tipo</th> 
                    <th>Mensaje</th>
                    <th>Linea</th>
                    <th>Columna</th>
                </tr>
        '''

        for mensaje in mensajes:
            print(str(mensaje.mensaje))
            if True or mensaje.tipo_mensaje != TIPO_MENSAJE.LOG:
                html += '''
                <tr>
                    <td>'''+mensaje.tipo_mensaje.name+'''</td>
                    <td>'''+str(mensaje.mensaje)+'''</td>
                    <td>'''+str(mensaje.linea)+'''</td>
                    <td>'''+str(mensaje.columna)+'''</td>
                </tr>
                '''

        html += '''</table>
            </body>
            </html>
        '''
        try:
            file = open('Errores.html', 'w')
            file.write(html)
        except:
            pass
        finally:
            file.close()
    
    def reporte_ts(self):
        global ts_global
        html = ''' 
        <html>
            <head>
                <style>
                    table {
                        width:100%;
                    }
                    table, th, td {
                        border: 1px solid black;
                        border-collapse: collapse;
                    }
                    th, td {
                        padding: 15px;
                        text-align: left;
                    }
                    table#t01 th {
                        background-color: black;
                        color: white;
                    }
                    table#t02 th {
                        background-color: blue;
                        color: white;
                    }
                </style>
            </head>
            <body>
            <h1>Simbolos</h1>
            <table id="t01">
                <tr>
                    <th>Identificador</th>
                    <th>Tipo</th> 
                    <th>Dimension</th>
                    <th>Valor</th>
                    <th>Linea</th>
                    <th>Columna</th>
                    <th>Ambito</th>
                </tr>
        '''

        for simbolo in ts_global.simbolos.values():
            html += '''
                <tr>
                    <td>'''+str(simbolo.identificador)+'''</td>
                    <td>'''+str(simbolo.tipo.name)+'''</td>
                    <td>'''+str(simbolo.dimension)+'''</td>
                    <td>'''+str(simbolo.valor)+'''</td>
                    <td>'''+str(simbolo.linea)+'''</td>
                    <td>'''+str(simbolo.columna)+'''</td>
                    <td>'''+str(simbolo.ambito)+'''</td>
                </tr>
            '''
        html += '''</table> <br> <br> <br>'''
        
        html += '''<h1>Etiquetas</h1>
                <table id="t02">
                <tr>
                    <th>Identificador</th>
                    <th>Tipo</th> 
                    <th>Linea</th>
                    <th>Columna</th>
                </tr>
        '''
        for etiqueta in ts_global.etiquetas.values():
            html += '''
                <tr>
                    <td>'''+etiqueta.identificador+'''</td>
                    <td>'''+etiqueta.tipo_estructura.name+'''</td>
                    <td>'''+str(etiqueta.linea)+'''</td>
                    <td>'''+str(etiqueta.columna)+'''</td>
                </tr>
            '''
        html += '''</table>'''
        
        html += '''</body>
            </html>
        '''
        try:
            file = open('TS.html', 'w')
            file.write(html)
        except:
            pass
        finally:
            file.close()

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