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
    'unset': 'UNSET'
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
    'XOR',
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
t_XOR               = r'xor'
t_BBNOT             = r'~'
t_BBAND             = r'&'
t_BBOR              = r'\|'
t_BBXOR             = r'\^'
t_DESIGUAL_QUE      = r'!='
t_RA                = r'$ra'
t_SP                = r'$sp'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
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
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
from Arbol.Aritmetica import *
from Arbol.Asignacion import *
from Arbol.Instruccion import *
from Arbol.Etiqueta import *
from Arbol.Print import *
from Arbol.Relacional import *
from Arbol.Unaria import *
lexer = lex.lex()

def p_init(t) :
    'init            : labels'
    t[0] = t[1]

def p_labels_lista(t) :
    'labels    : labels label'
    t[1].append(t[2])
    t[0] = t[1]

def p_labels_label(t):
    'labels    : label'
    t[0] = [t[1]]

def p_label(t):
    'label    : LABEL DPUNTOS instrucciones'
    t[0] = Etiqueta(t[1],TIPO_ESTRUCTURA.CONTROL,0,0,t[3])

def p_instrucciones_lista(t):
    'instrucciones     : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    'instrucciones     : instruccion'
    t[0] = [t[1]]

def p_instruccion(t):
    ''' instruccion     : print_inst
                        | goto_inst
                        | exit_inst
                        | unset_inst
                        | if_inst
                        | asig_inst
    '''
    t[0] = t[1]

def p_instruccion_print(t):
    'print_inst     : PRINT PIZQ asignable PDER PTCOMA'
    t[0] = Print(t[3],t.lineno(1),find_column(entrada, t.slice[1]))

def p_instruccion_goto(t):
    'goto_inst     : GOTO LABEL PTCOMA'
    print('instruccion goto')

def p_instruccion_exit(t):
    'exit_inst     : EXIT PTCOMA'
    print('instruccion exit')

def p_instruccion_unset(t):
    'unset_inst     : UNSET PIZQ asignable PDER PTCOMA'
    print('instruccion unset')

def p_instruccion_if(t):
    'if_inst     : IF PIZQ expresion_simple PDER instruccion'
    print('instruccion if')

def p_instruccion_asignacion_expresion(t):
    'asig_inst      : asignable ASIG expresion PTCOMA'
    t[0] = Asignacion(t[1],t[3],t.lineno(2),find_column(entrada, t.slice[2]))

def p_instruccion_asignacion_conversion(t):
    '''asig_inst      : asignable ASIG PIZQ INT PDER expresion_simple PTCOMA
                    | asignable ASIG PIZQ FLOAT PDER expresion_simple PTCOMA
                    | asignable ASIG PIZQ CHAR PDER expresion_simple PTCOMA
    '''
    print('asignacion conversion')

def p_instruccion_asignacion_read(t):
    ' asig_inst     : asignable ASIG READ PIZQ PDER PTCOMA '
    print('asignacion read')

def p_instruccion_asignacion_array(t):
    ' asig_inst     : asignable ASIG ARRAY PIZQ PDER PTCOMA '
    print('asignacion array')

def p_registros_asignables(t):
    '''asignable     : TEMPORAL
                     | PARAMETRO
                     | RETORNO
                     | PILA
                     | RA
                     | SP
    '''
    t[0] = t[1]

def p_registros_asignables_array(t):
    '''asignable     : TEMPORAL CIZQ expresion_simple CDER
                     | PARAMETRO CIZQ expresion_simple CDER
                     | RETORNO CIZQ expresion_simple CDER
                     | PILA CIZQ expresion_simple CDER
    '''

def p_expresion(t):
    ''' expresion     : expresion_simple MAS expresion_simple
                      | expresion_simple MENOS expresion_simple
                      | expresion_simple POR expresion_simple
                      | expresion_simple DIVIDIDO expresion_simple
                      | expresion_simple MODULO expresion_simple
                      | expresion_simple AND expresion_simple
                      | expresion_simple OR expresion_simple
                      | expresion_simple XOR expresion_simple
                      | expresion_simple BBAND expresion_simple
                      | expresion_simple BBOR expresion_simple
                      | expresion_simple BBXOR expresion_simple
                      | expresion_simple BBIZQ expresion_simple
                      | expresion_simple BBDER expresion_simple
                      | expresion_simple IGUAL_QUE expresion_simple
                      | expresion_simple DESIGUAL_QUE expresion_simple
                      | expresion_simple MAYOR_QUE expresion_simple
                      | expresion_simple MENOR_QUE expresion_simple
                      | expresion_simple MAYOR_IGUAL_QUE expresion_simple
                      | expresion_simple MENOR_IGUAL_QUE expresion_simple                     
    '''
    if t[2] == '+': t[0] = Aritmetica(t[1],t[3],TIPO_ARITMETICA.SUMA,t.lineno(2),find_column(entrada, t.slice[2]))
    if t[2] == '-': t[0] = Aritmetica(t[1],t[3],TIPO_ARITMETICA.RESTA,t.lineno(2),find_column(entrada, t.slice[2]))
    if t[2] == '*': t[0] = Aritmetica(t[1],t[3],TIPO_ARITMETICA.MULTIPLICACION,t.lineno(2),find_column(entrada, t.slice[2]))
    if t[2] == '/': t[0] = Aritmetica(t[1],t[3],TIPO_ARITMETICA.DIVISION,t.lineno(2),find_column(entrada, t.slice[2]))
    if t[2] == '%': t[0] = Aritmetica(t[1],t[3],TIPO_ARITMETICA.RESIDUO,t.lineno(2),find_column(entrada, t.slice[2]))
    if t[2] == '==': t[0] = Relacional(t[1],t[3],TIPO_RELACIONAL.IGUAL_QUE,t.lineno(2),find_column(entrada, t.slice[2]))
    if t[2] == '!=': t[0] = Relacional(t[1],t[3],TIPO_RELACIONAL.DISTINTO_QUE,t.lineno(2),find_column(entrada, t.slice[2]))
    if t[2] == '>=': t[0] = Relacional(t[1],t[3],TIPO_RELACIONAL.MAYOR_IGUAL_QUE,t.lineno(2),find_column(entrada, t.slice[2]))
    if t[2] == '<=': t[0] = Relacional(t[1],t[3],TIPO_RELACIONAL.MENOR_IGUAL_QUE,t.lineno(2),find_column(entrada, t.slice[2]))
    if t[2] == '>': t[0] = Relacional(t[1],t[3],TIPO_RELACIONAL.MAYOR_QUE,t.lineno(2),find_column(entrada, t.slice[2]))
    if t[2] == '<': t[0] = Relacional(t[1],t[3],TIPO_RELACIONAL.MENOR_QUE,t.lineno(2),find_column(entrada, t.slice[2]))

def p_der_expresion(t):
    ' expresion     : expresion_simple '
    t[0] = t[1]

def p_negativo(t):
    ' expresion_simple     : MENOS expresion_simple'
    t[0] = Unaria(t[2],TIPO_UNARIO.NEGATIVO,t.lineno(1),find_column(entrada, t.slice[1]))

def p_abs(t):
    ' expresion     : ABS PIZQ expresion_simple PDER '
    t[0] = Aritmetica(t[3],None,TIPO_ARITMETICA.ABSOLUTO,t.lineno(1),find_column(entrada, t.slice[1]))

def p_not(t):
    ' expresion     : NOT expresion_simple'
    print('not')

def p_bit_not(t):
    ' expresion     : BBNOT expresion_simple'
    print('bit not')

def p_acceso_arreglo(t):
    ''' expresion     : TEMPORAL CIZQ expresion_simple CDER
                      | PARAMETRO CIZQ expresion_simple CDER
                      | RETORNO CIZQ expresion_simple CDER
                      | PILA CIZQ expresion_simple CDER
    '''
    print('acceso arreglo');

def p_expresion_simple_identificador(t):
    '''expresion_simple     : TEMPORAL
                            | PARAMETRO
                            | RETORNO
                            | PILA
                            | RA
                            | SP
    '''
    t[0] = Unaria(t[1],TIPO_UNARIO.IDENTIFICADOR,t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_simple_entero(t):
    '''expresion_simple     : ENTERO
    '''
    t[0] = Unaria(t[1],TIPO_UNARIO.ENTERO,t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_simple_decimal(t):
    '''expresion_simple     : DECIMAL
    '''
    t[0] = Unaria(t[1],TIPO_UNARIO.DECIMAL,t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_simple_cadena(t):
    '''expresion_simple     : CADENA
    '''
    t[0] = Unaria(t[1],TIPO_UNARIO.CADENA,t.lineno(1),find_column(entrada, t.slice[1]))

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return ((token.lexpos - line_start) + 1)

import ply.yacc as yacc
parser = yacc.yacc()

entrada = ''

def parse(input) :
    global entrada
    entrada = input
    return parser.parse(input)