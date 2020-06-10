
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABS AND ARRAY ASIG BBAND BBDER BBIZQ BBNOT BBOR BBXOR CADENA CDER CHAR CIZQ DECIMAL DESIGUAL_QUE DIVIDIDO DPUNTOS ENTERO EXIT FLOAT GOTO IF IGUAL_QUE INT LABEL MAS MAYOR_IGUAL_QUE MAYOR_QUE MENOR_IGUAL_QUE MENOR_QUE MENOS MODULO NOT OR PARAMETRO PDER PILA PIZQ POR PRINT PTCOMA RA READ RETORNO SP TEMPORAL UNSET XORinit            : labelslabels    : labels labellabels    : labellabel    : LABEL DPUNTOS instruccionesinstrucciones     : instrucciones instruccioninstrucciones     : instruccion instruccion     : print_inst\n                        | goto_inst\n                        | exit_inst\n                        | unset_inst\n                        | if_inst\n                        | asig_inst\n    print_inst     : PRINT PIZQ TEMPORAL PDER PTCOMAgoto_inst     : GOTO LABEL PTCOMAexit_inst     : EXIT PTCOMAunset_inst     : UNSET PIZQ TEMPORAL PDER PTCOMAif_inst     : IF PIZQ expresion_simple PDER instruccionasig_inst      : asignable ASIG expresion PTCOMAasig_inst      : asignable ASIG PIZQ INT PDER expresion_simple PTCOMA\n                    | asignable ASIG PIZQ FLOAT PDER expresion_simple PTCOMA\n                    | asignable ASIG PIZQ CHAR PDER expresion_simple PTCOMA\n     asig_inst     : asignable ASIG READ PIZQ PDER PTCOMA  asig_inst     : asignable ASIG ARRAY PIZQ PDER PTCOMA asignable     : TEMPORAL\n                     | PARAMETRO\n                     | RETORNO\n                     | PILA\n                     | RA\n                     | SP\n                     | TEMPORAL CIZQ expresion_simple CDER\n                     | PARAMETRO CIZQ expresion_simple CDER\n                     | RETORNO CIZQ expresion_simple CDER\n                     | PILA CIZQ expresion_simple CDER\n     expresion     : expresion_simple MAS expresion_simple\n                      | expresion_simple MENOS expresion_simple\n                      | expresion_simple POR expresion_simple\n                      | expresion_simple DIVIDIDO expresion_simple\n                      | expresion_simple MODULO expresion_simple\n                      | expresion_simple AND expresion_simple\n                      | expresion_simple OR expresion_simple\n                      | expresion_simple XOR expresion_simple\n                      | expresion_simple BBAND expresion_simple\n                      | expresion_simple BBOR expresion_simple\n                      | expresion_simple BBXOR expresion_simple\n                      | expresion_simple BBIZQ expresion_simple\n                      | expresion_simple BBDER expresion_simple\n                      | expresion_simple IGUAL_QUE expresion_simple\n                      | expresion_simple DESIGUAL_QUE expresion_simple\n                      | expresion_simple MAYOR_QUE expresion_simple\n                      | expresion_simple MENOR_QUE expresion_simple\n                      | expresion_simple MAYOR_IGUAL_QUE expresion_simple\n                      | expresion_simple MENOR_IGUAL_QUE expresion_simple                     \n     expresion     : expresion_simple  expresion     : ABS PIZQ expresion_simple PDER  expresion     : NOT expresion_simple expresion     : BBNOT expresion_simple expresion     : TEMPORAL CIZQ expresion_simple CDER\n                      | PARAMETRO CIZQ expresion_simple CDER\n                      | RETORNO CIZQ expresion_simple CDER\n                      | PILA CIZQ expresion_simple CDER\n    expresion_simple     : TEMPORAL\n                            | PARAMETRO\n                            | RETORNO\n                            | PILA\n                            | RA\n                            | SP\n                            | ENTERO\n                            | DECIMAL\n                            | CADENA\n    '
    
_lr_action_items = {'LABEL':([0,2,3,5,7,8,9,10,11,12,13,14,17,27,31,49,71,106,107,108,141,142,148,149,150,],[4,4,-3,-2,-4,-6,-7,-8,-9,-10,-11,-12,30,-5,-15,-14,-18,-13,-16,-17,-22,-23,-19,-20,-21,]),'$end':([1,2,3,5,7,8,9,10,11,12,13,14,27,31,49,71,106,107,108,141,142,148,149,150,],[0,-1,-3,-2,-4,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,-18,-13,-16,-17,-22,-23,-19,-20,-21,]),'DPUNTOS':([4,],[6,]),'PRINT':([6,7,8,9,10,11,12,13,14,27,31,49,70,71,106,107,108,141,142,148,149,150,],[15,15,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,15,-18,-13,-16,-17,-22,-23,-19,-20,-21,]),'GOTO':([6,7,8,9,10,11,12,13,14,27,31,49,70,71,106,107,108,141,142,148,149,150,],[17,17,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,17,-18,-13,-16,-17,-22,-23,-19,-20,-21,]),'EXIT':([6,7,8,9,10,11,12,13,14,27,31,49,70,71,106,107,108,141,142,148,149,150,],[18,18,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,18,-18,-13,-16,-17,-22,-23,-19,-20,-21,]),'UNSET':([6,7,8,9,10,11,12,13,14,27,31,49,70,71,106,107,108,141,142,148,149,150,],[19,19,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,19,-18,-13,-16,-17,-22,-23,-19,-20,-21,]),'IF':([6,7,8,9,10,11,12,13,14,27,31,49,70,71,106,107,108,141,142,148,149,150,],[20,20,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,20,-18,-13,-16,-17,-22,-23,-19,-20,-21,]),'TEMPORAL':([6,7,8,9,10,11,12,13,14,27,28,29,31,32,33,34,35,36,37,49,58,59,70,71,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,99,100,101,102,106,107,108,109,110,111,141,142,148,149,150,],[16,16,-6,-7,-8,-9,-10,-11,-12,-5,38,39,-15,50,39,60,39,39,39,-14,39,39,16,-18,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-13,-16,-17,39,39,39,-22,-23,-19,-20,-21,]),'PARAMETRO':([6,7,8,9,10,11,12,13,14,27,29,31,33,34,35,36,37,49,58,59,70,71,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,99,100,101,102,106,107,108,109,110,111,141,142,148,149,150,],[22,22,-6,-7,-8,-9,-10,-11,-12,-5,41,-15,41,61,41,41,41,-14,41,41,22,-18,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-13,-16,-17,41,41,41,-22,-23,-19,-20,-21,]),'RETORNO':([6,7,8,9,10,11,12,13,14,27,29,31,33,34,35,36,37,49,58,59,70,71,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,99,100,101,102,106,107,108,109,110,111,141,142,148,149,150,],[23,23,-6,-7,-8,-9,-10,-11,-12,-5,42,-15,42,62,42,42,42,-14,42,42,23,-18,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-13,-16,-17,42,42,42,-22,-23,-19,-20,-21,]),'PILA':([6,7,8,9,10,11,12,13,14,27,29,31,33,34,35,36,37,49,58,59,70,71,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,99,100,101,102,106,107,108,109,110,111,141,142,148,149,150,],[24,24,-6,-7,-8,-9,-10,-11,-12,-5,43,-15,43,63,43,43,43,-14,43,43,24,-18,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-13,-16,-17,43,43,43,-22,-23,-19,-20,-21,]),'RA':([6,7,8,9,10,11,12,13,14,27,29,31,33,34,35,36,37,49,58,59,70,71,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,99,100,101,102,106,107,108,109,110,111,141,142,148,149,150,],[25,25,-6,-7,-8,-9,-10,-11,-12,-5,44,-15,44,44,44,44,44,-14,44,44,25,-18,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-13,-16,-17,44,44,44,-22,-23,-19,-20,-21,]),'SP':([6,7,8,9,10,11,12,13,14,27,29,31,33,34,35,36,37,49,58,59,70,71,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,99,100,101,102,106,107,108,109,110,111,141,142,148,149,150,],[26,26,-6,-7,-8,-9,-10,-11,-12,-5,45,-15,45,45,45,45,45,-14,45,45,26,-18,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-13,-16,-17,45,45,45,-22,-23,-19,-20,-21,]),'PIZQ':([15,19,20,34,55,56,57,],[28,32,33,53,94,95,96,]),'ASIG':([16,21,22,23,24,25,26,68,103,104,105,],[-24,34,-25,-26,-27,-28,-29,-30,-31,-32,-33,]),'CIZQ':([16,22,23,24,60,61,62,63,],[29,35,36,37,99,100,101,102,]),'PTCOMA':([18,30,39,41,42,43,44,45,46,47,48,52,54,60,61,62,63,67,69,97,98,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,138,139,140,143,144,145,146,147,],[31,49,-61,-62,-63,-64,-65,-66,-67,-68,-69,71,-53,-61,-62,-63,-64,106,107,-55,-56,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,141,142,148,149,150,-54,-57,-58,-59,-60,]),'ENTERO':([29,33,34,35,36,37,58,59,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,99,100,101,102,109,110,111,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'DECIMAL':([29,33,34,35,36,37,58,59,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,99,100,101,102,109,110,111,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'CADENA':([29,33,34,35,36,37,58,59,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,99,100,101,102,109,110,111,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'READ':([34,],[55,]),'ARRAY':([34,],[56,]),'ABS':([34,],[57,]),'NOT':([34,],[58,]),'BBNOT':([34,],[59,]),'PDER':([38,39,41,42,43,44,45,46,47,48,50,51,72,73,74,94,95,133,],[67,-61,-62,-63,-64,-65,-66,-67,-68,-69,69,70,109,110,111,131,132,143,]),'CDER':([39,40,41,42,43,44,45,46,47,48,64,65,66,134,135,136,137,],[-61,68,-62,-63,-64,-65,-66,-67,-68,-69,103,104,105,144,145,146,147,]),'MAS':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,75,-61,-62,-63,-64,]),'MENOS':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,76,-61,-62,-63,-64,]),'POR':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,77,-61,-62,-63,-64,]),'DIVIDIDO':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,78,-61,-62,-63,-64,]),'MODULO':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,79,-61,-62,-63,-64,]),'AND':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,80,-61,-62,-63,-64,]),'OR':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,81,-61,-62,-63,-64,]),'XOR':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,82,-61,-62,-63,-64,]),'BBAND':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,83,-61,-62,-63,-64,]),'BBOR':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,84,-61,-62,-63,-64,]),'BBXOR':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,85,-61,-62,-63,-64,]),'BBIZQ':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,86,-61,-62,-63,-64,]),'BBDER':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,87,-61,-62,-63,-64,]),'IGUAL_QUE':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,88,-61,-62,-63,-64,]),'DESIGUAL_QUE':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,89,-61,-62,-63,-64,]),'MAYOR_QUE':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,90,-61,-62,-63,-64,]),'MENOR_QUE':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,91,-61,-62,-63,-64,]),'MAYOR_IGUAL_QUE':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,92,-61,-62,-63,-64,]),'MENOR_IGUAL_QUE':([44,45,46,47,48,54,60,61,62,63,],[-65,-66,-67,-68,-69,93,-61,-62,-63,-64,]),'INT':([53,],[72,]),'FLOAT':([53,],[73,]),'CHAR':([53,],[74,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'labels':([0,],[2,]),'label':([0,2,],[3,5,]),'instrucciones':([6,],[7,]),'instruccion':([6,7,70,],[8,27,108,]),'print_inst':([6,7,70,],[9,9,9,]),'goto_inst':([6,7,70,],[10,10,10,]),'exit_inst':([6,7,70,],[11,11,11,]),'unset_inst':([6,7,70,],[12,12,12,]),'if_inst':([6,7,70,],[13,13,13,]),'asig_inst':([6,7,70,],[14,14,14,]),'asignable':([6,7,70,],[21,21,21,]),'expresion_simple':([29,33,34,35,36,37,58,59,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,99,100,101,102,109,110,111,],[40,51,54,64,65,66,97,98,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,133,134,135,136,137,138,139,140,]),'expresion':([34,],[52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> labels','init',1,'p_init','gramatica.py',161),
  ('labels -> labels label','labels',2,'p_labels_lista','gramatica.py',165),
  ('labels -> label','labels',1,'p_labels_label','gramatica.py',170),
  ('label -> LABEL DPUNTOS instrucciones','label',3,'p_label','gramatica.py',174),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',178),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',183),
  ('instruccion -> print_inst','instruccion',1,'p_instruccion','gramatica.py',187),
  ('instruccion -> goto_inst','instruccion',1,'p_instruccion','gramatica.py',188),
  ('instruccion -> exit_inst','instruccion',1,'p_instruccion','gramatica.py',189),
  ('instruccion -> unset_inst','instruccion',1,'p_instruccion','gramatica.py',190),
  ('instruccion -> if_inst','instruccion',1,'p_instruccion','gramatica.py',191),
  ('instruccion -> asig_inst','instruccion',1,'p_instruccion','gramatica.py',192),
  ('print_inst -> PRINT PIZQ TEMPORAL PDER PTCOMA','print_inst',5,'p_instruccion_print','gramatica.py',198),
  ('goto_inst -> GOTO LABEL PTCOMA','goto_inst',3,'p_instruccion_goto','gramatica.py',202),
  ('exit_inst -> EXIT PTCOMA','exit_inst',2,'p_instruccion_exit','gramatica.py',206),
  ('unset_inst -> UNSET PIZQ TEMPORAL PDER PTCOMA','unset_inst',5,'p_instruccion_unset','gramatica.py',210),
  ('if_inst -> IF PIZQ expresion_simple PDER instruccion','if_inst',5,'p_instruccion_if','gramatica.py',214),
  ('asig_inst -> asignable ASIG expresion PTCOMA','asig_inst',4,'p_instruccion_asignacion_expresion','gramatica.py',218),
  ('asig_inst -> asignable ASIG PIZQ INT PDER expresion_simple PTCOMA','asig_inst',7,'p_instruccion_asignacion_conversion','gramatica.py',222),
  ('asig_inst -> asignable ASIG PIZQ FLOAT PDER expresion_simple PTCOMA','asig_inst',7,'p_instruccion_asignacion_conversion','gramatica.py',223),
  ('asig_inst -> asignable ASIG PIZQ CHAR PDER expresion_simple PTCOMA','asig_inst',7,'p_instruccion_asignacion_conversion','gramatica.py',224),
  ('asig_inst -> asignable ASIG READ PIZQ PDER PTCOMA','asig_inst',6,'p_instruccion_asignacion_read','gramatica.py',229),
  ('asig_inst -> asignable ASIG ARRAY PIZQ PDER PTCOMA','asig_inst',6,'p_instruccion_asignacion_array','gramatica.py',233),
  ('asignable -> TEMPORAL','asignable',1,'p_registros_asignables','gramatica.py',237),
  ('asignable -> PARAMETRO','asignable',1,'p_registros_asignables','gramatica.py',238),
  ('asignable -> RETORNO','asignable',1,'p_registros_asignables','gramatica.py',239),
  ('asignable -> PILA','asignable',1,'p_registros_asignables','gramatica.py',240),
  ('asignable -> RA','asignable',1,'p_registros_asignables','gramatica.py',241),
  ('asignable -> SP','asignable',1,'p_registros_asignables','gramatica.py',242),
  ('asignable -> TEMPORAL CIZQ expresion_simple CDER','asignable',4,'p_registros_asignables','gramatica.py',243),
  ('asignable -> PARAMETRO CIZQ expresion_simple CDER','asignable',4,'p_registros_asignables','gramatica.py',244),
  ('asignable -> RETORNO CIZQ expresion_simple CDER','asignable',4,'p_registros_asignables','gramatica.py',245),
  ('asignable -> PILA CIZQ expresion_simple CDER','asignable',4,'p_registros_asignables','gramatica.py',246),
  ('expresion -> expresion_simple MAS expresion_simple','expresion',3,'p_expresion','gramatica.py',250),
  ('expresion -> expresion_simple MENOS expresion_simple','expresion',3,'p_expresion','gramatica.py',251),
  ('expresion -> expresion_simple POR expresion_simple','expresion',3,'p_expresion','gramatica.py',252),
  ('expresion -> expresion_simple DIVIDIDO expresion_simple','expresion',3,'p_expresion','gramatica.py',253),
  ('expresion -> expresion_simple MODULO expresion_simple','expresion',3,'p_expresion','gramatica.py',254),
  ('expresion -> expresion_simple AND expresion_simple','expresion',3,'p_expresion','gramatica.py',255),
  ('expresion -> expresion_simple OR expresion_simple','expresion',3,'p_expresion','gramatica.py',256),
  ('expresion -> expresion_simple XOR expresion_simple','expresion',3,'p_expresion','gramatica.py',257),
  ('expresion -> expresion_simple BBAND expresion_simple','expresion',3,'p_expresion','gramatica.py',258),
  ('expresion -> expresion_simple BBOR expresion_simple','expresion',3,'p_expresion','gramatica.py',259),
  ('expresion -> expresion_simple BBXOR expresion_simple','expresion',3,'p_expresion','gramatica.py',260),
  ('expresion -> expresion_simple BBIZQ expresion_simple','expresion',3,'p_expresion','gramatica.py',261),
  ('expresion -> expresion_simple BBDER expresion_simple','expresion',3,'p_expresion','gramatica.py',262),
  ('expresion -> expresion_simple IGUAL_QUE expresion_simple','expresion',3,'p_expresion','gramatica.py',263),
  ('expresion -> expresion_simple DESIGUAL_QUE expresion_simple','expresion',3,'p_expresion','gramatica.py',264),
  ('expresion -> expresion_simple MAYOR_QUE expresion_simple','expresion',3,'p_expresion','gramatica.py',265),
  ('expresion -> expresion_simple MENOR_QUE expresion_simple','expresion',3,'p_expresion','gramatica.py',266),
  ('expresion -> expresion_simple MAYOR_IGUAL_QUE expresion_simple','expresion',3,'p_expresion','gramatica.py',267),
  ('expresion -> expresion_simple MENOR_IGUAL_QUE expresion_simple','expresion',3,'p_expresion','gramatica.py',268),
  ('expresion -> expresion_simple','expresion',1,'p_der_expresion','gramatica.py',273),
  ('expresion -> ABS PIZQ expresion_simple PDER','expresion',4,'p_abs','gramatica.py',276),
  ('expresion -> NOT expresion_simple','expresion',2,'p_not','gramatica.py',280),
  ('expresion -> BBNOT expresion_simple','expresion',2,'p_bit_not','gramatica.py',284),
  ('expresion -> TEMPORAL CIZQ expresion_simple CDER','expresion',4,'p_acceso_arreglo','gramatica.py',288),
  ('expresion -> PARAMETRO CIZQ expresion_simple CDER','expresion',4,'p_acceso_arreglo','gramatica.py',289),
  ('expresion -> RETORNO CIZQ expresion_simple CDER','expresion',4,'p_acceso_arreglo','gramatica.py',290),
  ('expresion -> PILA CIZQ expresion_simple CDER','expresion',4,'p_acceso_arreglo','gramatica.py',291),
  ('expresion_simple -> TEMPORAL','expresion_simple',1,'p_expresion_simple','gramatica.py',296),
  ('expresion_simple -> PARAMETRO','expresion_simple',1,'p_expresion_simple','gramatica.py',297),
  ('expresion_simple -> RETORNO','expresion_simple',1,'p_expresion_simple','gramatica.py',298),
  ('expresion_simple -> PILA','expresion_simple',1,'p_expresion_simple','gramatica.py',299),
  ('expresion_simple -> RA','expresion_simple',1,'p_expresion_simple','gramatica.py',300),
  ('expresion_simple -> SP','expresion_simple',1,'p_expresion_simple','gramatica.py',301),
  ('expresion_simple -> ENTERO','expresion_simple',1,'p_expresion_simple','gramatica.py',302),
  ('expresion_simple -> DECIMAL','expresion_simple',1,'p_expresion_simple','gramatica.py',303),
  ('expresion_simple -> CADENA','expresion_simple',1,'p_expresion_simple','gramatica.py',304),
]
