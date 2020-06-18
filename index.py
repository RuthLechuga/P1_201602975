from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from Arbol.Exit import *
from Arbol.Mensaje import *
from Arbol.Etiqueta import *
from Arbol.Read import *
from graphviz import Source
import Arbol.TablaDeSimbolos as TS
import gramatica_asc as g_asc
import gramatica_desc as g_desc
import webbrowser
import easygui as eg

#bibliotecas para interfaz gráfica
from magicsticklibs.TextPad import TextPad
from magicsticklibs.Graphics import Tkinter as tk, tkFileDialog, tkMessageBox 
from magicsticklibs.FontChooser import FontChooser, Font_wm

mensajes = []
ts_global = None
is_ascendente = False;
reporte_gramatical = []
path_archivo = ''
new = 2
head_html = '''
<head> 
    <style>
        table {
            width:100%;
            white-space: pre-line;
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
'''

class EditorTexto:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1000x600')
        self.root.wm_title("Augus IDE")
        self.root.resizable(False,False)
        
        self.text = TextPad(self.root, bg="#81BEF7")
        
        menubar = Menu(self.root)
        mArchivo = Menu(menubar, background='#FFFFFF',foreground='blue')
        mArchivo.add_command(label="Abrir", command=self.abrir)
        mArchivo.add_command(label="Guardar", command=self.guardar)
        mArchivo.add_command(label="Guardar Como", command=self.guardarComo)
        mArchivo.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Archivo", menu=mArchivo)

        """mEditar = Menu(menubar, background='#FFFFFF',foreground='blue')
        mEditar.add_command(label="Buscar", command=self.buscar)
        mEditar.add_command(label="Reemplazar", command=self.reemplazar)
        menubar.add_cascade(label="Editar", menu=mEditar)"""

        mEjecutar = Menu(menubar, background='#FFFFFF',foreground='blue')
        mEjecutar.add_command(label="Ejecutar ascendente", command=self.ej_ascendente)
        mEjecutar.add_command(label="Ejecutar descendente", command=self.ej_descendente)
        mEjecutar.add_command(label="Reporte errores", command=self.reporte_errores)
        mEjecutar.add_command(label="Reporte Tabla Simbolos",command=self.reporte_ts)
        mEjecutar.add_command(label="Reporte AST",command=self.reporte_ast)
        mEjecutar.add_command(label="Reporte gramatical",command=self.reporte_gramatical)
        menubar.add_cascade(label="Ejecutar", menu=mEjecutar)

        mOpciones = Menu(menubar, background='#FFFFFF',foreground='blue')
        mOpciones.add_command(label="Font",command=self.font)

        mColores = Menu(menubar, background='#FFFFFF',foreground='blue')
        mColores.add_command(label="Celeste",command=self.celeste)
        mColores.add_command(label="Verde",command=self.verde)
        mColores.add_command(label="Blanco",command=self.blanco)
        mColores.add_command(label="Gris",command=self.gris)
        mColores.add_command(label="Rosa",command=self.rosa)
        mColores.add_command(label="Lila",command=self.lila)
        mOpciones.add_cascade(label="Color fondo", menu=mColores)
        menubar.add_cascade(label="Opciones", menu=mOpciones)

        mDebugger = Menu(menubar, background='#FFFFFF',foreground='blue')
        mDebugger.add_command(label="Debuggear",command=self.debuggear)
        menubar.add_cascade(label="Debuggear", menu=mDebugger)
       
        mAyuda = Menu(menubar, background='#FFFFFF',foreground='blue')
        mAyuda.add_command(label="Acerca de", command=self.acerca)
        menubar.add_cascade(label="Ayuda", menu=mAyuda)
        self.root.config(menu=menubar)

        tab_control = ttk.Notebook(self.root)
        tab_consola = ttk.Frame(tab_control)
        self.tab_errores = ttk.Frame(tab_control)
        self.tab_ts = ttk.Frame(tab_control)
        tab_control.add(tab_consola,text='CONSOLA')
        tab_control.add(self.tab_errores,text='ERRORES')
        tab_control.add(self.tab_ts,text='TABLA SIMBOLOS')
        tab_control.pack(expand=1, fill='both')

        self.consola = Text(tab_consola,bg="#000000",fg="#FFFFFF")
        self.consola.pack(expand=True, fill='both')
        
        self.tipo = Entry(self.tab_errores, borderwidth=1, width=15, bg="black", fg='white', font=('Arial',11,'bold')) 
        self.tipo.grid(row=0, column=0) 
        self.tipo.insert(END, 'Tipo') 

        self.linea = Entry(self.tab_errores, borderwidth=1, width=10, bg="black", fg='white', font=('Arial',11,'bold'))
        self.linea.grid(row=0, column=1) 
        self.linea.insert(END, 'Linea') 

        self.columna = Entry(self.tab_errores, borderwidth=1, width=10, bg="black", fg='white', font=('Arial',11,'bold'))
        self.columna.grid(row=0, column=2) 
        self.columna.insert(END, 'Columna') 

        self.error = Entry(self.tab_errores, borderwidth=1, width=95, bg="black", fg='white', font=('Arial',11,'bold'))
        self.error.grid(row=0, column=3) 
        self.error.insert(END, 'Error') 

        self.id = Entry(self.tab_ts, borderwidth=1, width=15, bg="black", fg='white', font=('Arial',11,'bold')) 
        self.id.grid(row=0, column=0) 
        self.id.insert(END, 'ID') 

        self.tipo = Entry(self.tab_ts, borderwidth=1, width=15, bg="black", fg='white', font=('Arial',11,'bold')) 
        self.tipo.grid(row=0, column=1) 
        self.tipo.insert(END, 'Tipo') 

        self.dimension = Entry(self.tab_ts, borderwidth=1, width=15, bg="black", fg='white', font=('Arial',11,'bold')) 
        self.dimension.grid(row=0, column=2) 
        self.dimension.insert(END, 'Dimension') 

        self.valor = Entry(self.tab_ts, borderwidth=1, width=15, bg="black", fg='white', font=('Arial',11,'bold')) 
        self.valor.grid(row=0, column=3) 
        self.valor.insert(END, 'Valor') 
        
        self.linea = Entry(self.tab_ts, borderwidth=1, width=15, bg="black", fg='white', font=('Arial',11,'bold')) 
        self.linea.grid(row=0, column=4) 
        self.linea.insert(END, 'Linea') 

        self.columna = Entry(self.tab_ts, borderwidth=1, width=15, bg="black", fg='white', font=('Arial',11,'bold')) 
        self.columna.grid(row=0, column=5) 
        self.columna.insert(END, 'Columna')     

        self.ambito = Entry(self.tab_ts, borderwidth=1, width=15, bg="black", fg='white', font=('Arial',11,'bold')) 
        self.ambito.grid(row=0, column=6) 
        self.ambito.insert(END, 'ambito') 

        self.root.mainloop()
    
    def celeste(self):
        self.text.change_color("#81BEF7")
    
    def verde(self):
        self.text.change_color("#81F79F")

    def blanco(self):
        self.text.change_color("#FFFFFF")
    
    def gris(self):
        self.text.change_color("#D8D8D8")

    def rosa(self):
        self.text.change_color("#F5A9F2")

    def lila(self):
        self.text.change_color("#E2A9F3")
    
    def font(self):
        Font_wm(self.text)
        
    def abrir(self):
        path = tkFileDialog.askopenfilename()
        if path:
            data=open(path,"rb").read()
            self.text.delete_text()
            self.text.insert_text(data)
            self.path_archivo = path
        return

    def guardar(self):
        if self.path_archivo == '':
            path = tkFileDialog.asksaveasfilename()
        else:
            path = self.path_archivo
        if path:
            data = self.text.get_text()
            f_=open(path,"w")
            f_.write(data)
            f_.close()
            print('guardado')
        return

    def guardarComo(self):
        path = tkFileDialog.asksaveasfilename()
        if path:
            data = self.text.get_text()
            f_=open(path,"w")
            f_.write(data)
            f_.close()
            self.path_archivo = path
        return

    def salir(self):
        import sys
        sys.exit(0)
        return

    def ej_ascendente(self):
        global is_ascendente
        global mensajes
        global reporte_gramatical

        self.cleanTable()
        self.cleanTS()
        is_ascendente = True
        del mensajes[:]
        etiquetas = g_asc.parse(self.text.get_text())
        mensajes = g_asc.mensajes
        reporte_gramatical = g_asc.reporte_gramatical
        self.ejecutar(etiquetas)
    
    def imprimir_errores(self):
        fila = 1
        for mensaje in mensajes:
            print(mensaje.mensaje)
            if mensaje.tipo_mensaje != TIPO_MENSAJE.LOG:
                tipo = Entry(self.tab_errores, borderwidth=1, width=15, fg='black', font=('Arial',11)) 
                tipo.grid(row=fila, column=0) 
                tipo.insert(END, mensaje.tipo_mensaje.name)
                linea = Entry(self.tab_errores, borderwidth=1, width=10, fg='black', font=('Arial',11))
                linea.grid(row=fila, column=1) 
                linea.insert(END, mensaje.linea)
                columna = Entry(self.tab_errores, borderwidth=1, width=10, fg='black', font=('Arial',11))
                columna.grid(row=fila, column=2) 
                columna.insert(END, mensaje.columna)
                error = Entry(self.tab_errores, borderwidth=1, width=95, fg='black', font=('Arial',11))
                error.grid(row=fila, column=3) 
                error.insert(END, mensaje.mensaje) 
                fila+=1
             
    def ej_descendente(self):
        global is_ascendente
        global mensajes
        global reporte_gramatical
        
        self.cleanTable()
        self.cleanTS()
        is_ascendente = False
        del mensajes[:]
        etiquetas = g_desc.parse(self.text.get_text())
        mensajes = g_desc.mensajes
        reporte_gramatical = g_desc.reporte_gramatical
        self.ejecutar(etiquetas)

    def ejecutar(self,etiquetas):
        global mensajes
        global ts_global
        
        if len(mensajes) > 0:
            self.consola.delete('1.0',END)
            self.consola.insert('1.0','>>>>>Errores<<<<<')
            self.imprimir_errores()
            return

        ts_global = TS.TablaDeSimbolos()
        ts_global.reiniciar()

        for etiqueta in etiquetas:
            if not ts_global.addEtiqueta(etiqueta):
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La etiqueta: '+etiqueta.identificador+' ya existe.',0,0))
                        
        etiqueta = ts_global.getEtiqueta('main')

        while not (etiqueta is None):

            bandera = False

            for instruccion in etiqueta.instrucciones:
                if isinstance(instruccion,Read):
                    salida = ""
                    for mensaje in mensajes:
                        if mensaje.tipo_mensaje == TIPO_MENSAJE.LOG:
                            salida += str(mensaje.mensaje).replace('\\n','\n')
                    
                    self.consola.delete('1.0',END)
                    self.consola.insert('1.0',salida)
                
                res = instruccion.ejecutar(ts_global,mensajes)
                if isinstance(res,Etiqueta) or isinstance(instruccion,Exit):
                    etiqueta = res
                    bandera = True
                    break
         
            if bandera:
                continue

            etiqueta = ts_global.getSiguiente()
        
        salida = ""
        for mensaje in mensajes:
            if mensaje.tipo_mensaje == TIPO_MENSAJE.LOG:
                salida += str(mensaje.mensaje).replace('\\n','\n')
        
        self.consola.delete('1.0',END)
        self.consola.insert('1.0',salida)
        self.imprimir_errores()
        self.imprimir_TS()

    def reporte_errores(self):
        global mensajes
        global head_html
        html = ''' 
        <html>'''+head_html+'''
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
            if mensaje.tipo_mensaje != TIPO_MENSAJE.LOG:
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
            global new
            webbrowser.open('Errores.html',new=new)
    
    def reporte_ts(self):
        global ts_global
        global head_html
        html = ''' 
        <html>'''+head_html+'''
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
            global new
            webbrowser.open('TS.html',new=new)

    def reporte_ast(self):
        global is_ascendente
        global ts_global

        arbol = 'digraph ast_ascendente {\n init -> labels\n '

        if is_ascendente:
        
            for etiqueta in ts_global.etiquetas.values():
                arbol+= 'labels -> et_'+etiqueta.identificador+'\n'
                arbol += 'et_'+etiqueta.identificador+' -> et_'+etiqueta.identificador+'_instrucciones\n'

                for instruccion in etiqueta.instrucciones:
                    arbol += 'et_'+etiqueta.identificador+'_instrucciones -> '+'\"'+str(instruccion)+'\"'+'\n'
                    arbol += instruccion.getAST_Ascendente()
        
        else:
            temporal = ''
            cont_label = 0
            for etiqueta in ts_global.etiquetas.values():

                if cont_label==0:
                    arbol+= 'labels -> et_'+etiqueta.identificador+'\n'
                    arbol+= 'labels -> labels_'+str(cont_label+1)+'\n'
                else:
                    arbol +=  'labels_'+str(cont_label)+ '[label=\"labels\'\"] ;\n'
                    arbol+= 'labels_'+str(cont_label)+' -> et_'+etiqueta.identificador+'\n'
                    arbol+= 'labels_'+str(cont_label)+' -> labels_'+str(cont_label+1)+'\n'

                cont_instruccion = 0
                for instruccion in etiqueta.instrucciones:
                    if cont_instruccion==0:
                        arbol += 'et_'+etiqueta.identificador+' -> et_'+etiqueta.identificador+'_instrucciones\n'
                        arbol += 'et_'+etiqueta.identificador+'_instrucciones [label=\"instrucciones\"] ;\n'
                        
                        arbol += ' et_'+etiqueta.identificador+'_instrucciones -> et_'+etiqueta.identificador+'_instruccion\n'
                        arbol += 'et_'+etiqueta.identificador+'_instruccion [label=\"instruccion\"] ;\n'
                        arbol += 'et_'+etiqueta.identificador+'_instruccion -> '+'\"'+str(instruccion)+'\"'+'\n'
                        
                        arbol += 'et_'+etiqueta.identificador+'_instrucciones -> et_'+etiqueta.identificador+'_instrucciones_'+str(cont_instruccion+1)+'\n'
                        arbol += 'et_'+etiqueta.identificador+'_instrucciones_'+str(cont_instruccion+1)+' [label=\"instrucciones\'\"] ;\n'
                    else:
                        arbol += 'et_'+etiqueta.identificador+'_instrucciones_'+str(cont_instruccion)+' -> ''et_'+etiqueta.identificador+'_instruccion_'+str(cont_instruccion)+'\n'
                        arbol += 'et_'+etiqueta.identificador+'_instruccion_'+str(cont_instruccion)+' [label=\"instruccion\"] ;\n'
                        arbol += 'et_'+etiqueta.identificador+'_instruccion_'+str(cont_instruccion)+' -> \"'+str(instruccion)+'\"'+'\n'
                        
                        arbol += 'et_'+etiqueta.identificador+'_instrucciones_'+str(cont_instruccion)+' -> et_'+etiqueta.identificador+'_instrucciones_'+str(cont_instruccion+1)+'\n'
                        arbol += 'et_'+etiqueta.identificador+'_instrucciones_'+str(cont_instruccion+1)+' [label=\"instrucciones\'\"] ;\n'
                                   
                    cont_instruccion+=1
                    arbol += instruccion.getAST_Descendente()
                
                cont_label+=1

        arbol += "\n}"
        #print(arbol)

        s = Source(arbol, filename="AST", format="svg")
        s.view()

    def reporte_gramatical(self):
        global reporte_gramatical
        global head_html
        html = ''' 
        <html>'''+head_html+'''
            <body>
            <h1>Reporte Gramatical</h1>
            <table id="t02">
                <tr>
                    <th>Produccion</th>
                    <th>Regla Semántica</th> 
                </tr>
        '''
        for r in reporte_gramatical:
            html += '''
            <tr>
                <td>'''+r[0]+'''</td>
                <td>'''+r[1]+'''</td>
            </tr>
            '''
        html += '''</table>'''
        
        html += '''</body>
            </html>
        '''
        try:
            file = open('Gramatical.html', 'w')
            file.write(html)
        except:
            pass
        finally:
            file.close()
            global new
            webbrowser.open('Gramatical.html',new=new)
    
    def debuggear(self):
        global is_ascendente
        global mensajes
        global reporte_gramatical

        self.cleanTable()
        is_ascendente = True
        del mensajes[:]
        etiquetas = g_asc.parse(self.text.get_text())
        mensajes = g_asc.mensajes
        reporte_gramatical = g_asc.reporte_gramatical

        global ts_global
        if len(mensajes) > 0:
            self.consola.delete('1.0',END)
            self.consola.insert('1.0','>>>>>Errores<<<<<')
            self.imprimir_errores()
            return

        ts_global = TS.TablaDeSimbolos()
        ts_global.reiniciar()

        for etiqueta in etiquetas:
            if not ts_global.addEtiqueta(etiqueta):
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La etiqueta: '+etiqueta.identificador+' ya existe.',0,0))
                        
        etiqueta = ts_global.getEtiqueta('main')

        debugueando = True;
        while (not (etiqueta is None)) and debugueando:

            bandera = False

            for instruccion in etiqueta.instrucciones:
                self.text.resaltar(instruccion.linea)
                res = instruccion.ejecutar(ts_global,mensajes)
                if isinstance(res,Etiqueta) or isinstance(instruccion,Exit):
                    etiqueta = res
                    bandera = True
                    debugueando = eg.ccbox(msg='Desea continuar debugueando',title='Debug')
                    self.text.deleteResaltar()
                    break
                
                salida = ""
                for mensaje in mensajes:
                    if mensaje.tipo_mensaje == TIPO_MENSAJE.LOG:
                        salida += str(mensaje.mensaje).replace('\\n','\n')
                
                self.consola.delete('1.0',END)
                self.consola.insert('1.0',salida)
                self.imprimir_errores() 
                self.imprimir_TS()

                debugueando = eg.ccbox(msg='Desea continuar debugueando',title='Debug')

                if not debugueando:
                    break
                self.text.deleteResaltar()

            if bandera:
                continue

            etiqueta = ts_global.getSiguiente()

        self.text.deleteResaltar()
        salida = ""
        for mensaje in mensajes:
            if mensaje.tipo_mensaje == TIPO_MENSAJE.LOG:
                salida += str(mensaje.mensaje).replace('\\n','\n')
        
        self.consola.delete('1.0',END)
        self.consola.insert('1.0',salida)
        self.imprimir_errores()
    
    def imprimir_TS(self):
        global ts_global
        fila = 1
        for simbolo in ts_global.simbolos.values():
            identificador = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11)) 
            identificador.grid(row=fila, column=0) 
            identificador.insert(END, simbolo.identificador)
            tipo = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            tipo.grid(row=fila, column=1) 
            tipo.insert(END, simbolo.tipo.name)
            dimension = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            dimension.grid(row=fila, column=2) 
            dimension.insert(END, str(simbolo.dimension))
            valor = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            valor.grid(row=fila, column=3) 
            valor.insert(END, str(simbolo.valor))
            linea = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            linea.grid(row=fila, column=4) 
            linea.insert(END, str(simbolo.linea))
            columna = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            columna.grid(row=fila, column=5) 
            columna.insert(END, str(simbolo.columna))
            ambito = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            ambito.grid(row=fila, column=6) 
            ambito.insert(END, simbolo.ambito)
            fila+=1

    def acerca(self):
        root = Tk()
        root.geometry('300x100')
        root.wm_title("Augus IDE")
        root.configure(bg="#81BEF7")
        root.resizable(False,False)

        textAugust = Label(root, text='August IDE', bg="#81BEF7")
        textAugust.pack()

        textName = Label(root,text='Ruth Nohemy Ardón Lechuga', bg="#81BEF7")
        textName.pack()

        textCarnet = Label(root,text='201602975',bg="#81BEF7")
        textCarnet.pack()

    def cleanTable(self):
        for fila in range(1,25):
            tipo = Entry(self.tab_errores, borderwidth=1, width=15, fg='black', font=('Arial',11)) 
            tipo.grid(row=fila, column=0) 
            tipo.insert(END, "")
            linea = Entry(self.tab_errores, borderwidth=1, width=10, fg='black', font=('Arial',11))
            linea.grid(row=fila, column=1) 
            linea.insert(END, "")
            columna = Entry(self.tab_errores, borderwidth=1, width=10, fg='black', font=('Arial',11))
            columna.grid(row=fila, column=2) 
            columna.insert(END, "")
            error = Entry(self.tab_errores, borderwidth=1, width=95, fg='black', font=('Arial',11))
            error.grid(row=fila, column=3) 
            error.insert(END, "")
    
    def cleanTS(self):
        for fila in range(1,25):
            identificador = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11)) 
            identificador.grid(row=fila, column=0) 
            identificador.insert(END, "")

            tipo = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            tipo.grid(row=fila, column=1) 
            tipo.insert(END, "")

            dimension = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            dimension.grid(row=fila, column=2) 
            dimension.insert(END, "")

            valor = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            valor.grid(row=fila, column=3) 
            valor.insert(END, "")

            linea = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            linea.grid(row=fila, column=4) 
            linea.insert(END, "")

            columna = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            columna.grid(row=fila, column=5) 
            columna.insert(END, "")

            ambito = Entry(self.tab_ts, borderwidth=1, width=15, fg='black', font=('Arial',11))
            ambito.grid(row=fila, column=6) 
            ambito.insert(END, "")
            
EditorTexto()