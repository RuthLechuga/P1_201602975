reservadas = {
    'print' : 'PRINT',
    'goto': 'GOTO',
    'exit': 'EXIT',
    'if': 'IF',
    'read': 'READ',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'abs': 'ABS',
    'array': 'ARRAY',
    'unset': 'UNSET',
    'xor': 'XOR'
}

tokens  = [
    'PTCOMA',
    'DPUNTOS',
    'PIZQ',
    'PDER',
    'CIZQ',
    'CDER',
    'ASIG',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MODULO',
    'BBIZQ',
    'BBDER',
    'MENOR_IGUAL_QUE',
    'MAYOR_IGUAL_QUE',
    'MENOR_QUE',
    'MAYOR_QUE',
    'IGUAL_QUE',
    'NOT',
    'AND',
    'OR',
    'BBNOT',
    'BBAND',
    'BBOR',
    'BBXOR',
    'DESIGUAL_QUE',
    'RA',
    'SP',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'TEMPORAL',
    'PARAMETRO',
    'RETORNO',
    'PILA',
    'LABEL'
] + list(reservadas.values())

# Tokens
t_PTCOMA            = r';'
t_DPUNTOS           = r':'
t_PIZQ              = r'\('
t_PDER              = r'\)'
t_CIZQ              = r'\['
t_CDER              = r']'
t_ASIG              = r'='
t_MAS               = r'\+'
t_MENOS             = r'-'
t_POR               = r'\*'
t_DIVIDIDO          = r'/'
t_MODULO            = r'%'
t_BBIZQ             = r'<<'
t_BBDER             = r'>>'
t_MENOR_IGUAL_QUE   = r'<='
t_MAYOR_IGUAL_QUE   = r'>='
t_MENOR_QUE         = r'<'
t_MAYOR_QUE         = r'>'
t_IGUAL_QUE         = r'=='
t_NOT               = r'!'
t_AND               = r'&&'
t_OR                = r'\|\|'
t_BBNOT             = r'~'
t_BBAND             = r'&'
t_BBOR              = r'\|'
t_BBXOR             = r'\^'
t_DESIGUAL_QUE      = r'!='
t_RA                = r'\$ra'
t_SP                = r'\$sp'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        global mensajes
        mensajes.append(Mensaje(TIPO_MENSAJE.LEXICO,'Valor decimal muy largo para almacenar en: '+t.value+'.',t.lexer.lineno,0))
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        global mensajes
        mensajes.append(Mensaje(TIPO_MENSAJE.LEXICO,'Valor entero muy largo para almacenar en: '+t.value+'.',t.lexer.lineno,0))
        t.value = 0
    return t

def t_LABEL(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'LABEL')
    return t

def t_CADENA(t):
    r'(\".*?\")|(\'.*?\')'
    t.value = t.value[1:-1]
    return t 

def t_COMENTARIO_MULTILINEA(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += t.value.count('\n')

def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

def t_TEMPORAL(t):
    r'\$t\d+'
    return t

def t_PARAMETRO(t):
    r'\$a\d+'
    return t

def t_RETORNO(t):
    r'\$v\d+'
    return t

def t_PILA(t):
    r'\$s\d+'
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    global mensajes
    mensajes.append(Mensaje(TIPO_MENSAJE.LEXICO,'Caracter no válido: '+t.value[0]+'.',t.lexer.lineno,0))
    t.lexer.skip(1)

import ply.lex as lex
from Arbol.Acceso import *
from Arbol.Aritmetica import *
from Arbol.Asignacion import *
from Arbol.AsignacionArray import *
from Arbol.BitToBit import *
from Arbol.Convertir import *
from Arbol.Etiqueta import *
from Arbol.Exit import *
from Arbol.Goto import *
from Arbol.If import *
from Arbol.Instruccion import *
from Arbol.Logica import *
from Arbol.Mensaje import *
from Arbol.Print import *
from Arbol.Read import *
from Arbol.Relacional import *
from Arbol.Unaria import *
from Arbol.Unset import *
lexer = lex.lex()

def p_init(t) :
    'init            : labels'
    global reporte_gramatical
    reporte_gramatical.append(['init -> labels','t[0] = t[1]']);
    t[0] = t[1]

def p_labels(t) :
    'labels    : label labels_der'
    global reporte_gramatical
    reporte_gramatical.append(['labels -> label labels_der', 't[0] = t[2]']);
    t[0] = t[2]

def p_labels_der(t):
    'labels_der : label labels_der'
    global reporte_gramatical
    reporte_gramatical.append(['labels_der -> label labels_der', 't[0] = []\nt[0].append(t[-1])\nt[0].extend(t[2])']);
    t[0] = []
    t[0].append(t[-1])
    t[0].extend(t[2])
    
def p_labels_der_epsilon(t):
    'labels_der : epsilon'
    global reporte_gramatical
    reporte_gramatical.append(['labels_der -> epsilon', 't[0] = [t[-1]]']);
    t[0] = [t[-1]]

def p_label(t):
    'label    : LABEL DPUNTOS instrucciones'
    global reporte_gramatical
    reporte_gramatical.append(['label -> LABEL DPUNTOS instrucciones','t[0] = Etiqueta(t[1],TIPO_ESTRUCTURA.CONTROL,t.lineno(2),find_column(entrada, t.slice[2]),t[3])']);
    t[0] = Etiqueta(t[1],TIPO_ESTRUCTURA.CONTROL,t.lineno(2),find_column(entrada, t.slice[2]),t[3])

def p_instrucciones(t):
    'instrucciones : instruccion instrucciones_der'
    global reporte_gramatical
    reporte_gramatical.append(['instrucciones -> instruccion instrucciones_der', 't[0] = t[2]']);
    t[0] = t[2]

def p_instrucciones_der(t):
    'instrucciones_der : instruccion instrucciones_der'
    global reporte_gramatical
    reporte_gramatical.append(['instrucciones_der -> instruccion instrucciones_der', 't[0] = []\nt[0].append(t[-1])\nt[0].extend(t[2])']);
    t[0] = []
    t[0].append(t[-1])
    t[0].extend(t[2])
    
def p_instrucciones_der_epsilon(t):
    'instrucciones_der : epsilon'
    global reporte_gramatical
    reporte_gramatical.append(['instrucciones_der -> epsilon', 't[0] = [t[-1]]']);
    t[0] = [t[-1]]

def p_instruccion_1(t):
    ''' instruccion     : print_inst'''
    global reporte_gramatical
    reporte_gramatical.append(['instruccion -> print_inst','t[0] = t[1]'])
    t[0] = t[1]

def p_instruccion_2(t):
    ''' instruccion     : goto_inst'''
    global reporte_gramatical
    reporte_gramatical.append(['instruccion -> goto_inst','t[0] = t[1]'])
    t[0] = t[1]

def p_instruccion_3(t):
    ''' instruccion     : exit_inst'''
    global reporte_gramatical
    reporte_gramatical.append(['instruccion -> exit_inst','t[0] = t[1]'])
    t[0] = t[1]

def p_instruccion_4(t):
    ''' instruccion     : unset_inst'''
    global reporte_gramatical
    reporte_gramatical.append(['instruccion -> unset_inst','t[0] = t[1]'])
    t[0] = t[1]

def p_instruccion_5(t):
    ''' instruccion     : if_inst'''
    global reporte_gramatical
    reporte_gramatical.append(['instruccion -> if_inst','t[0] = t[1]'])
    t[0] = t[1]

def p_instruccion_6(t):
    ''' instruccion : asig_inst '''
    global reporte_gramatical
    reporte_gramatical.append(['instruccion -> asig_inst','t[0] = t[1]'])
    t[0] = t[1]

def p_instruccion_print(t):
    'print_inst     : PRINT PIZQ expresion PDER PTCOMA'
    global reporte_gramatical
    reporte_gramatical.append(['print_inst -> PRINT PIZQ expresion_simple PDER PTCOMA','t[0] = Print(t[3],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Print(t[3],t.lineno(1),find_column(entrada, t.slice[1]))

def p_instruccion_goto(t):
    'goto_inst     : GOTO LABEL PTCOMA'
    global reporte_gramatical
    reporte_gramatical.append(['goto_inst -> GOTO LABEL PTCOMA','t[0] = Goto(t[2],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Goto(t[2],t.lineno(1),find_column(entrada, t.slice[1]))

def p_instruccion_exit(t):
    'exit_inst     : EXIT PTCOMA'
    global reporte_gramatical
    reporte_gramatical.append(['exit_inst -> EXIT PTCOMA','t[0] = Exit(t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Exit(t.lineno(1),find_column(entrada, t.slice[1]))

def p_instruccion_unset(t):
    'unset_inst     : UNSET PIZQ expresion_simple PDER PTCOMA'
    global reporte_gramatical
    reporte_gramatical.append(['unset_inst -> UNSET PIZQ asignable PDER PTCOMA','t[0] = Unset(t[3],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Unset(t[3],t.lineno(1),find_column(entrada, t.slice[1]))

def p_instruccion_if(t):
    'if_inst     : IF PIZQ expresion PDER instruccion'
    global reporte_gramatical
    reporte_gramatical.append(['if_inst -> IF PIZQ expresion PDER instruccion','t[0] = If(t[3],t[5],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = If(t[3],t[5],t.lineno(1),find_column(entrada, t.slice[1]))

def p_instruccion_asig(t):
    'asig_inst  : asignable accesos ASIG asig_valor PTCOMA'
    global reporte_gramatical
    reporte_gramatical.append(['asig_inst -> asignable accesos ASIG asig_valor PTCOMA','t[0] = t[4]'])
    t[0] = t[4]

def p_asig_valor(t):
    'asig_valor : expresion'
    global reporte_gramatical
    if len(t[-2])==0:
        reporte_gramatical.append(['asig_inst -> expresion','t[0] = Asignacion(t[-3],t[1],0,0)'])
        t[0] = Asignacion(t[-3],t[1],0,0)
    else:
        reporte_gramatical.append(['asig_inst -> expresion','t[0] = AsignacionArray(t[-3],t[-2],t[1],0,0)'])
        t[0] = AsignacionArray(t[-3],t[-2],t[1],0,0)

def p_asig_conversion(t):
    'asig_valor : PIZQ asig_valor_der'
    t[0] = t[2]

def p_asig_valor_conversion_der(t):
    'asig_valor_der : tipo PDER expresion'
    global reporte_gramatical
    reporte_gramatical.append(['asig_valor_der -> tipo PDER expresion','t[0] = Convertir(t[-3],t[4],t[2],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Convertir(t[-4],t[3],t[1],t.lineno(2),find_column(entrada, t.slice[2]))

def p_asig_valor_expresion_der(t):
    'asig_valor_der : expresion PDER'
    global reporte_gramatical
    reporte_gramatical.append(['asig_valor_der -> expresion PDER','t[0] = t[1]'])
    t[0] = t[1]

def p_tipo(t):
    ''' tipo : INT
            | FLOAT
            | CHAR
    '''
    global reporte_gramatical
    reporte_gramatical.append(['tipo -> '+t[1],'t[0] = t[1]'])
    t[0] = t[1]

def p_asig_read(t):
    'asig_valor : READ PIZQ PDER'
    global reporte_gramatical
    reporte_gramatical.append(['asig_valor -> READ PIZQ PDER','t[0] = Read(t[-3],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Read(t[-3],t.lineno(1),find_column(entrada, t.slice[1]))

def p_asig_array(t):
    'asig_valor : ARRAY PIZQ PDER'
    global reporte_gramatical
    reporte_gramatical.append(['asig_valor -> ARRAY PIZQ PDER','t[0] = Asignacion(t[-3],{},t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Asignacion(t[-3],{},t.lineno(1),find_column(entrada, t.slice[1]))

def p_registros_asignables_1(t):
    '''asignable     : TEMPORAL    '''
    t[0] = t[1]

def p_registros_asignables_2(t):
    '''asignable     : PARAMETRO'''
    t[0] = t[1]

def p_registros_asignables_3(t):
    '''asignable     : RETORNO'''
    t[0] = t[1]

def p_registros_asignables_4(t):
    '''asignable     : PILA'''
    t[0] = t[1]

def p_registros_asignables_5(t):
    '''asignable     : RA '''
    t[0] = t[1]

def p_registros_asignables_6(t):
    '''asignable     : SP'''
    t[0] = t[1]

def p_accesos(t):
    ' accesos   : acceso accesos'
    t[0] = [t[1]]
    t[0].extend(t[2])

def p_accesos_epsilon(t):
    ' accesos   : epsilon'
    t[0] = []

def p_acceso(t):
    ' acceso    : CIZQ expresion_simple CDER '
    t[0] = t[2]

def p_expresion(t):
    'expresion :   expresion_simple expresion_der'
    t[0] = t[2]

def p_expresion_der(t):
    '''expresion_der :  MAS expresion_simple
                        | MENOS expresion_simple
                        | POR expresion_simple
                        | DIVIDIDO expresion_simple
                        | MODULO expresion_simple
                        | AND expresion_simple
                        | OR expresion_simple
                        | XOR expresion_simple
                        | BBAND expresion_simple
                        | BBOR expresion_simple
                        | BBXOR expresion_simple
                        | BBIZQ expresion_simple
                        | BBDER expresion_simple
                        | IGUAL_QUE expresion_simple
                        | DESIGUAL_QUE expresion_simple
                        | MAYOR_QUE expresion_simple
                        | MENOR_QUE expresion_simple
                        | MAYOR_IGUAL_QUE expresion_simple
                        | MENOR_IGUAL_QUE expresion_simple
    '''
    global reporte_gramatical
    if t[1] == '+': 
        reporte_gramatical.append(['expresion -> expresion_simple MAS expresion_simple','t[0] = Aritmetica(t[-1],t[2],TIPO_ARITMETICA.SUMA,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Aritmetica(t[-1],t[2],TIPO_ARITMETICA.SUMA,t.lineno(1),find_column(entrada, t.slice[1]))

    elif t[1] == '-': 
        reporte_gramatical.append(['expresion -> expresion_simple RESTA expresion_simple','t[0] = Aritmetica(t[-1],t[2],TIPO_ARITMETICA.RESTA,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Aritmetica(t[-1],t[2],TIPO_ARITMETICA.RESTA,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '*': 
        reporte_gramatical.append(['expresion -> expresion_simple MULTIPLICACION expresion_simple','t[0] = Aritmetica(t[-1],t[2],TIPO_ARITMETICA.MULTIPLICACION,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Aritmetica(t[-1],t[2],TIPO_ARITMETICA.MULTIPLICACION,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '/': 
        reporte_gramatical.append(['expresion -> expresion_simple DIVISION expresion_simple','t[0] = Aritmetica(t[-1],t[2],TIPO_ARITMETICA.DIVISION,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Aritmetica(t[-1],t[2],TIPO_ARITMETICA.DIVISION,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '%': 
        reporte_gramatical.append(['expresion -> expresion_simple RESIDUO expresion_simple','t[0] = Aritmetica(t[-1],t[2],TIPO_ARITMETICA.RESIDUO,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Aritmetica(t[-1],t[2],TIPO_ARITMETICA.RESIDUO,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '==': 
        reporte_gramatical.append(['expresion -> expresion_simple IGUAL_QUE expresion_simple','t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.IGUAL_QUE,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.IGUAL_QUE,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '!=': 
        reporte_gramatical.append(['expresion -> expresion_simple DISTINTO_QUE expresion_simple','t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.DISTINTO_QUE,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.DISTINTO_QUE,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '>=': 
        reporte_gramatical.append(['expresion -> expresion_simple MAYOR_IGUAL_QUE expresion_simple','t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.MAYOR_IGUAL_QUE,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.MAYOR_IGUAL_QUE,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '<=': 
        reporte_gramatical.append(['expresion -> expresion_simple MENOR_IGUAL_QUE expresion_simple','t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.MENOR_IGUAL_QUE,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.MENOR_IGUAL_QUE,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '>': 
        reporte_gramatical.append(['expresion -> expresion_simple MAYOR_QUE expresion_simple','t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.MAYOR_QUE,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.MAYOR_QUE,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '<': 
        reporte_gramatical.append(['expresion -> expresion_simple MENOR_QUE expresion_simple','t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.MENOR_QUE,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Relacional(t[-1],t[2],TIPO_RELACIONAL.MENOR_QUE,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '&&': 
        reporte_gramatical.append(['expresion -> expresion_simple AND expresion_simple','t[0] = Logica(t[-1],t[2],TIPO_LOGICA.AND,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Logica(t[-1],t[2],TIPO_LOGICA.AND,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '||': 
        reporte_gramatical.append(['expresion -> expresion_simple OR expresion_simple','t[0] = Logica(t[-1],t[2],TIPO_LOGICA.OR,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Logica(t[-1],t[2],TIPO_LOGICA.OR,t.lineno(1),find_column(entrada, t.slice[1]))

    elif t[1] == 'xor': 
        reporte_gramatical.append(['expresion -> expresion_simple XOR expresion_simple','t[0] = Logica(t[-1],t[2],TIPO_LOGICA.XOR,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = Logica(t[-1],t[2],TIPO_LOGICA.XOR,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '&': 
        reporte_gramatical.append(['expresion -> expresion_simple BBAND expresion_simple','t[0] = BitToBit(t[-1],t[2],TIPO_BIT_BIT.AND,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = BitToBit(t[-1],t[2],TIPO_BIT_BIT.AND,t.lineno(1),find_column(entrada, t.slice[1]))
    
    elif t[1] == '|': 
        reporte_gramatical.append(['expresion -> expresion_simple BBOR expresion_simple','t[0] = BitToBit(t[-1],t[2],TIPO_BIT_BIT.OR,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = BitToBit(t[-1],t[2],TIPO_BIT_BIT.OR,t.lineno(1),find_column(entrada, t.slice[1]))

    elif t[1] == '^': 
        reporte_gramatical.append(['expresion -> expresion_simple BBXOR expresion_simple','t[0] = BitToBit(t[-1],t[2],TIPO_BIT_BIT.XOR,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = BitToBit(t[-1],t[2],TIPO_BIT_BIT.XOR,t.lineno(1),find_column(entrada, t.slice[1]))

    elif t[1] == '<<': 
        reporte_gramatical.append(['expresion -> expresion_simple BBIZQUIERDA expresion_simple','t[0] = BitToBit(t[-1],t[2],TIPO_BIT_BIT.IZQUIERDA,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = BitToBit(t[-1],t[2],TIPO_BIT_BIT.IZQUIERDA,t.lineno(1),find_column(entrada, t.slice[1]))

    elif t[1] == '>>': 
        reporte_gramatical.append(['expresion -> expresion_simple BBDERECHA expresion_simple','t[0] = BitToBit(t[-1],t[2],TIPO_BIT_BIT.DERECHA,t.lineno(1),find_column(entrada, t.slice[1]))'])
        t[0] = BitToBit(t[-1],t[2],TIPO_BIT_BIT.DERECHA,t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_der_epsilon(t):
    ''' expresion_der : epsilon '''
    global reporte_gramatical
    reporte_gramatical.append(['expresion_der -> epsilon','t[0] = t[-1]'])
    t[0] = t[-1]

def p_negativo(t):
    ' expresion_simple     : MENOS expresion_simple'
    global reporte_gramatical
    reporte_gramatical.append(['expresion_simple -> MENOS expresion_simple','t[0] = Unaria(t[2],TIPO_UNARIO.NEGATIVO,t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Unaria(t[2],TIPO_UNARIO.NEGATIVO,t.lineno(1),find_column(entrada, t.slice[1]))

def p_abs(t):
    ' expresion     : ABS PIZQ expresion_simple PDER '
    global reporte_gramatical
    reporte_gramatical.append(['expresion -> ABS PIZQ expresion_simple PDER','t[0] = Aritmetica(t[3],None,TIPO_ARITMETICA.ABSOLUTO,t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Aritmetica(t[3],None,TIPO_ARITMETICA.ABSOLUTO,t.lineno(1),find_column(entrada, t.slice[1]))

def p_not(t):
    ' expresion     : NOT expresion_simple'
    global reporte_gramatical
    reporte_gramatical.append(['expresion -> NOT expresion_simple','t[0] = Logica(t[2],None,TIPO_LOGICA.NOT,t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Logica(t[2],None,TIPO_LOGICA.NOT,t.lineno(1),find_column(entrada, t.slice[1]))
    
def p_bit_not(t):
    ' expresion     : BBNOT expresion_simple'
    global reporte_gramatical
    reporte_gramatical.append(['expresion -> BBNOT expresion_simple','t[0] = BitToBit(t[2],None,TIPO_BIT_BIT.NOT,t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = BitToBit(t[2],None,TIPO_BIT_BIT.NOT,t.lineno(1),find_column(entrada, t.slice[1]))

def p_acceso_arreglo(t):
    ''' expresion_simple     : asignable accesos '''
    global reporte_gramatical
    if len(t[2])==0:
        reporte_gramatical.append(['expresion_simple -> asignable accesos','t[0] = Unaria(t[1],TIPO_UNARIO.IDENTIFICADOR,0,0)'])
        t[0] = Unaria(t[1],TIPO_UNARIO.IDENTIFICADOR,0,0)
    else:
        reporte_gramatical.append(['expresion_simple -> asignable accesos','t[0] = Acceso(t[1],t[2])'])
        t[0] = Acceso(t[1],t[2])

def p_expresion_simple_entero(t):
    '''expresion_simple     : ENTERO '''
    global reporte_gramatical
    reporte_gramatical.append(['expresion_simple -> ENTERO','t[0] = Unaria(t[1],TIPO_UNARIO.ENTERO,t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Unaria(t[1],TIPO_UNARIO.ENTERO,t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_simple_decimal(t):
    '''expresion_simple     : DECIMAL '''
    global reporte_gramatical
    reporte_gramatical.append(['expresion_simple -> DECIMAL','t[0] = Unaria(t[1],TIPO_UNARIO.DECIMAL,t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Unaria(t[1],TIPO_UNARIO.DECIMAL,t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_simple_cadena(t):
    '''expresion_simple     : CADENA'''
    global reporte_gramatical
    reporte_gramatical.append(['expresion_simple -> CADENA','t[0] = Unaria(t[1],TIPO_UNARIO.CADENA,t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Unaria(t[1],TIPO_UNARIO.CADENA,t.lineno(1),find_column(entrada, t.slice[1]))

def p_epsilon(p):
    'epsilon :'
    pass

def p_error(t):
    if not t:
        mensajes.append(Mensaje(TIPO_MENSAJE.SINTACTICO,'Error sintáctico irrecuperable.',0,0))    
        return

    mensajes.append(Mensaje(TIPO_MENSAJE.SINTACTICO,'Error sintáctico en: '+str(t.value)+'.',t.lineno,find_column(entrada, t)))    
    while True:
        tok = parser.token()
        if not tok or tok.type == 'PTCOMA': 
            break
    parser.restart()

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return ((token.lexpos - line_start) + 1)

import ply.yacc as yacc
parser = yacc.yacc()

entrada = ''
mensajes = []
reporte_gramatical = []
pila = []

def parse(input) :
    global entrada
    entrada = input
    return parser.parse(input)