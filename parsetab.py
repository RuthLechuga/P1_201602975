
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABS AND ARRAY ASIG BBAND BBDER BBIZQ BBNOT BBOR BBXOR CADENA CDER CHAR CIZQ DECIMAL DESIGUAL_QUE DIVIDIDO DPUNTOS ENTERO EXIT FLOAT GOTO IF IGUAL_QUE INT LABEL MAS MAYOR_IGUAL_QUE MAYOR_QUE MENOR_IGUAL_QUE MENOR_QUE MENOS MODULO NOT OR PARAMETRO PDER PILA PIZQ POR PRINT PTCOMA RA READ RETORNO SP TEMPORAL UNSET XORinit            : labelslabels    : labels labellabels    : labellabel    : LABEL DPUNTOS instruccionesinstrucciones     : instrucciones instruccioninstrucciones     : instruccion instruccion     : print_inst\n                        | goto_inst\n                        | exit_inst\n                        | unset_inst\n                        | if_inst\n                        | asig_inst\n    print_inst     : PRINT PIZQ asignable PDER PTCOMAgoto_inst     : GOTO LABEL PTCOMAexit_inst     : EXIT PTCOMAunset_inst     : UNSET PIZQ asignable PDER PTCOMAif_inst     : IF PIZQ expresion_simple PDER instruccionasig_inst      : asignable ASIG expresion PTCOMAasig_inst      : asignable ASIG PIZQ INT PDER expresion_simple PTCOMA\n                    | asignable ASIG PIZQ FLOAT PDER expresion_simple PTCOMA\n                    | asignable ASIG PIZQ CHAR PDER expresion_simple PTCOMA\n     asig_inst     : asignable ASIG READ PIZQ PDER PTCOMA  asig_inst     : asignable ASIG ARRAY PIZQ PDER PTCOMA asignable     : TEMPORAL\n                     | PARAMETRO\n                     | RETORNO\n                     | PILA\n                     | RA\n                     | SP\n    asignable     : TEMPORAL CIZQ expresion_simple CDER\n                     | PARAMETRO CIZQ expresion_simple CDER\n                     | RETORNO CIZQ expresion_simple CDER\n                     | PILA CIZQ expresion_simple CDER\n     expresion     : expresion_simple MAS expresion_simple\n                      | expresion_simple MENOS expresion_simple\n                      | expresion_simple POR expresion_simple\n                      | expresion_simple DIVIDIDO expresion_simple\n                      | expresion_simple MODULO expresion_simple\n                      | expresion_simple AND expresion_simple\n                      | expresion_simple OR expresion_simple\n                      | expresion_simple XOR expresion_simple\n                      | expresion_simple BBAND expresion_simple\n                      | expresion_simple BBOR expresion_simple\n                      | expresion_simple BBXOR expresion_simple\n                      | expresion_simple BBIZQ expresion_simple\n                      | expresion_simple BBDER expresion_simple\n                      | expresion_simple IGUAL_QUE expresion_simple\n                      | expresion_simple DESIGUAL_QUE expresion_simple\n                      | expresion_simple MAYOR_QUE expresion_simple\n                      | expresion_simple MENOR_QUE expresion_simple\n                      | expresion_simple MAYOR_IGUAL_QUE expresion_simple\n                      | expresion_simple MENOR_IGUAL_QUE expresion_simple                     \n     expresion     : expresion_simple  expresion_simple     : MENOS expresion_simple expresion     : ABS PIZQ expresion_simple PDER  expresion     : NOT expresion_simple expresion     : BBNOT expresion_simple expresion     : TEMPORAL CIZQ expresion_simple CDER\n                      | PARAMETRO CIZQ expresion_simple CDER\n                      | RETORNO CIZQ expresion_simple CDER\n                      | PILA CIZQ expresion_simple CDER\n    expresion_simple     : TEMPORAL\n                            | PARAMETRO\n                            | RETORNO\n                            | PILA\n                            | RA\n                            | SP\n    expresion_simple     : ENTERO\n    expresion_simple     : DECIMAL\n    expresion_simple     : CADENA\n    '
    
_lr_action_items = {'LABEL':([0,2,3,5,7,8,9,10,11,12,13,14,17,27,31,57,69,108,138,139,143,144,150,151,152,],[4,4,-3,-2,-4,-6,-7,-8,-9,-10,-11,-12,30,-5,-15,-14,-18,-13,-16,-17,-22,-23,-19,-20,-21,]),'$end':([1,2,3,5,7,8,9,10,11,12,13,14,27,31,57,69,108,138,139,143,144,150,151,152,],[0,-1,-3,-2,-4,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,-18,-13,-16,-17,-22,-23,-19,-20,-21,]),'DPUNTOS':([4,],[6,]),'PRINT':([6,7,8,9,10,11,12,13,14,27,31,57,69,103,108,138,139,143,144,150,151,152,],[15,15,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,-18,15,-13,-16,-17,-22,-23,-19,-20,-21,]),'GOTO':([6,7,8,9,10,11,12,13,14,27,31,57,69,103,108,138,139,143,144,150,151,152,],[17,17,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,-18,17,-13,-16,-17,-22,-23,-19,-20,-21,]),'EXIT':([6,7,8,9,10,11,12,13,14,27,31,57,69,103,108,138,139,143,144,150,151,152,],[18,18,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,-18,18,-13,-16,-17,-22,-23,-19,-20,-21,]),'UNSET':([6,7,8,9,10,11,12,13,14,27,31,57,69,103,108,138,139,143,144,150,151,152,],[19,19,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,-18,19,-13,-16,-17,-22,-23,-19,-20,-21,]),'IF':([6,7,8,9,10,11,12,13,14,27,31,57,69,103,108,138,139,143,144,150,151,152,],[20,20,-6,-7,-8,-9,-10,-11,-12,-5,-15,-14,-18,20,-13,-16,-17,-22,-23,-19,-20,-21,]),'TEMPORAL':([6,7,8,9,10,11,12,13,14,27,28,29,31,32,33,34,35,36,37,44,46,47,57,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,95,98,99,100,101,103,108,109,110,111,138,139,143,144,150,151,152,],[21,21,-6,-7,-8,-9,-10,-11,-12,-5,21,48,-15,21,60,60,60,60,60,60,60,60,-14,-18,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,21,-13,60,60,60,-16,-17,-22,-23,-19,-20,-21,]),'PARAMETRO':([6,7,8,9,10,11,12,13,14,27,28,29,31,32,33,34,35,36,37,44,46,47,57,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,95,98,99,100,101,103,108,109,110,111,138,139,143,144,150,151,152,],[22,22,-6,-7,-8,-9,-10,-11,-12,-5,22,49,-15,22,61,61,61,61,61,61,61,61,-14,-18,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,22,-13,61,61,61,-16,-17,-22,-23,-19,-20,-21,]),'RETORNO':([6,7,8,9,10,11,12,13,14,27,28,29,31,32,33,34,35,36,37,44,46,47,57,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,95,98,99,100,101,103,108,109,110,111,138,139,143,144,150,151,152,],[23,23,-6,-7,-8,-9,-10,-11,-12,-5,23,50,-15,23,62,62,62,62,62,62,62,62,-14,-18,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,23,-13,62,62,62,-16,-17,-22,-23,-19,-20,-21,]),'PILA':([6,7,8,9,10,11,12,13,14,27,28,29,31,32,33,34,35,36,37,44,46,47,57,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,95,98,99,100,101,103,108,109,110,111,138,139,143,144,150,151,152,],[24,24,-6,-7,-8,-9,-10,-11,-12,-5,24,51,-15,24,63,63,63,63,63,63,63,63,-14,-18,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,24,-13,63,63,63,-16,-17,-22,-23,-19,-20,-21,]),'RA':([6,7,8,9,10,11,12,13,14,27,28,29,31,32,33,34,35,36,37,44,46,47,57,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,95,98,99,100,101,103,108,109,110,111,138,139,143,144,150,151,152,],[25,25,-6,-7,-8,-9,-10,-11,-12,-5,25,52,-15,25,52,52,52,52,52,52,52,52,-14,-18,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,25,-13,52,52,52,-16,-17,-22,-23,-19,-20,-21,]),'SP':([6,7,8,9,10,11,12,13,14,27,28,29,31,32,33,34,35,36,37,44,46,47,57,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,95,98,99,100,101,103,108,109,110,111,138,139,143,144,150,151,152,],[26,26,-6,-7,-8,-9,-10,-11,-12,-5,26,53,-15,26,53,53,53,53,53,53,53,53,-14,-18,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,26,-13,53,53,53,-16,-17,-22,-23,-19,-20,-21,]),'PIZQ':([15,19,20,29,42,43,45,],[28,32,33,40,92,93,95,]),'ASIG':([16,21,22,23,24,25,26,104,105,106,107,],[29,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,]),'PTCOMA':([18,30,39,41,48,49,50,51,52,53,54,55,56,60,61,62,63,68,94,96,97,102,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,140,141,142,145,146,147,148,149,],[31,57,69,-53,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,108,-54,-56,-57,138,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,143,144,150,151,152,-55,-58,-59,-60,-61,]),'PDER':([21,22,23,24,25,26,38,52,53,54,55,56,58,59,60,61,62,63,70,71,72,92,93,94,104,105,106,107,133,],[-24,-25,-26,-27,-28,-29,68,-66,-67,-68,-69,-70,102,103,-62,-63,-64,-65,109,110,111,131,132,-54,-30,-31,-32,-33,145,]),'CIZQ':([21,22,23,24,48,49,50,51,],[34,35,36,37,98,99,100,101,]),'READ':([29,],[42,]),'ARRAY':([29,],[43,]),'ABS':([29,],[45,]),'NOT':([29,],[46,]),'BBNOT':([29,],[47,]),'MENOS':([29,33,34,35,36,37,41,44,46,47,48,49,50,51,52,53,54,55,56,60,61,62,63,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,95,98,99,100,101,109,110,111,],[44,44,44,44,44,44,74,44,44,44,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-54,44,44,44,44,44,44,44,44,]),'ENTERO':([29,33,34,35,36,37,44,46,47,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,95,98,99,100,101,109,110,111,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'DECIMAL':([29,33,34,35,36,37,44,46,47,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,95,98,99,100,101,109,110,111,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'CADENA':([29,33,34,35,36,37,44,46,47,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,95,98,99,100,101,109,110,111,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'INT':([40,],[70,]),'FLOAT':([40,],[71,]),'CHAR':([40,],[72,]),'MAS':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[73,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'POR':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[75,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'DIVIDIDO':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[76,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'MODULO':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[77,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'AND':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[78,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'OR':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[79,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'XOR':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[80,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'BBAND':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[81,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'BBOR':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[82,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'BBXOR':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[83,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'BBIZQ':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[84,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'BBDER':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[85,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'IGUAL_QUE':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[86,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'DESIGUAL_QUE':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[87,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'MAYOR_QUE':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[88,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'MENOR_QUE':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[89,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'MAYOR_IGUAL_QUE':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[90,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'MENOR_IGUAL_QUE':([41,48,49,50,51,52,53,54,55,56,60,61,62,63,94,],[91,-62,-63,-64,-65,-66,-67,-68,-69,-70,-62,-63,-64,-65,-54,]),'CDER':([52,53,54,55,56,60,61,62,63,64,65,66,67,94,134,135,136,137,],[-66,-67,-68,-69,-70,-62,-63,-64,-65,104,105,106,107,-54,146,147,148,149,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'labels':([0,],[2,]),'label':([0,2,],[3,5,]),'instrucciones':([6,],[7,]),'instruccion':([6,7,103,],[8,27,139,]),'print_inst':([6,7,103,],[9,9,9,]),'goto_inst':([6,7,103,],[10,10,10,]),'exit_inst':([6,7,103,],[11,11,11,]),'unset_inst':([6,7,103,],[12,12,12,]),'if_inst':([6,7,103,],[13,13,13,]),'asig_inst':([6,7,103,],[14,14,14,]),'asignable':([6,7,28,32,103,],[16,16,38,58,16,]),'expresion':([29,],[39,]),'expresion_simple':([29,33,34,35,36,37,44,46,47,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,95,98,99,100,101,109,110,111,],[41,59,64,65,66,67,94,96,97,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,133,134,135,136,137,140,141,142,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> labels','init',1,'p_init','gramatica_asc.py',160),
  ('labels -> labels label','labels',2,'p_labels_lista','gramatica_asc.py',164),
  ('labels -> label','labels',1,'p_labels_label','gramatica_asc.py',169),
  ('label -> LABEL DPUNTOS instrucciones','label',3,'p_label','gramatica_asc.py',173),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica_asc.py',177),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica_asc.py',182),
  ('instruccion -> print_inst','instruccion',1,'p_instruccion','gramatica_asc.py',186),
  ('instruccion -> goto_inst','instruccion',1,'p_instruccion','gramatica_asc.py',187),
  ('instruccion -> exit_inst','instruccion',1,'p_instruccion','gramatica_asc.py',188),
  ('instruccion -> unset_inst','instruccion',1,'p_instruccion','gramatica_asc.py',189),
  ('instruccion -> if_inst','instruccion',1,'p_instruccion','gramatica_asc.py',190),
  ('instruccion -> asig_inst','instruccion',1,'p_instruccion','gramatica_asc.py',191),
  ('print_inst -> PRINT PIZQ asignable PDER PTCOMA','print_inst',5,'p_instruccion_print','gramatica_asc.py',196),
  ('goto_inst -> GOTO LABEL PTCOMA','goto_inst',3,'p_instruccion_goto','gramatica_asc.py',200),
  ('exit_inst -> EXIT PTCOMA','exit_inst',2,'p_instruccion_exit','gramatica_asc.py',204),
  ('unset_inst -> UNSET PIZQ asignable PDER PTCOMA','unset_inst',5,'p_instruccion_unset','gramatica_asc.py',208),
  ('if_inst -> IF PIZQ expresion_simple PDER instruccion','if_inst',5,'p_instruccion_if','gramatica_asc.py',212),
  ('asig_inst -> asignable ASIG expresion PTCOMA','asig_inst',4,'p_instruccion_asignacion_expresion','gramatica_asc.py',216),
  ('asig_inst -> asignable ASIG PIZQ INT PDER expresion_simple PTCOMA','asig_inst',7,'p_instruccion_asignacion_conversion','gramatica_asc.py',220),
  ('asig_inst -> asignable ASIG PIZQ FLOAT PDER expresion_simple PTCOMA','asig_inst',7,'p_instruccion_asignacion_conversion','gramatica_asc.py',221),
  ('asig_inst -> asignable ASIG PIZQ CHAR PDER expresion_simple PTCOMA','asig_inst',7,'p_instruccion_asignacion_conversion','gramatica_asc.py',222),
  ('asig_inst -> asignable ASIG READ PIZQ PDER PTCOMA','asig_inst',6,'p_instruccion_asignacion_read','gramatica_asc.py',227),
  ('asig_inst -> asignable ASIG ARRAY PIZQ PDER PTCOMA','asig_inst',6,'p_instruccion_asignacion_array','gramatica_asc.py',231),
  ('asignable -> TEMPORAL','asignable',1,'p_registros_asignables','gramatica_asc.py',235),
  ('asignable -> PARAMETRO','asignable',1,'p_registros_asignables','gramatica_asc.py',236),
  ('asignable -> RETORNO','asignable',1,'p_registros_asignables','gramatica_asc.py',237),
  ('asignable -> PILA','asignable',1,'p_registros_asignables','gramatica_asc.py',238),
  ('asignable -> RA','asignable',1,'p_registros_asignables','gramatica_asc.py',239),
  ('asignable -> SP','asignable',1,'p_registros_asignables','gramatica_asc.py',240),
  ('asignable -> TEMPORAL CIZQ expresion_simple CDER','asignable',4,'p_registros_asignables_array','gramatica_asc.py',245),
  ('asignable -> PARAMETRO CIZQ expresion_simple CDER','asignable',4,'p_registros_asignables_array','gramatica_asc.py',246),
  ('asignable -> RETORNO CIZQ expresion_simple CDER','asignable',4,'p_registros_asignables_array','gramatica_asc.py',247),
  ('asignable -> PILA CIZQ expresion_simple CDER','asignable',4,'p_registros_asignables_array','gramatica_asc.py',248),
  ('expresion -> expresion_simple MAS expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',252),
  ('expresion -> expresion_simple MENOS expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',253),
  ('expresion -> expresion_simple POR expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',254),
  ('expresion -> expresion_simple DIVIDIDO expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',255),
  ('expresion -> expresion_simple MODULO expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',256),
  ('expresion -> expresion_simple AND expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',257),
  ('expresion -> expresion_simple OR expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',258),
  ('expresion -> expresion_simple XOR expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',259),
  ('expresion -> expresion_simple BBAND expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',260),
  ('expresion -> expresion_simple BBOR expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',261),
  ('expresion -> expresion_simple BBXOR expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',262),
  ('expresion -> expresion_simple BBIZQ expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',263),
  ('expresion -> expresion_simple BBDER expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',264),
  ('expresion -> expresion_simple IGUAL_QUE expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',265),
  ('expresion -> expresion_simple DESIGUAL_QUE expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',266),
  ('expresion -> expresion_simple MAYOR_QUE expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',267),
  ('expresion -> expresion_simple MENOR_QUE expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',268),
  ('expresion -> expresion_simple MAYOR_IGUAL_QUE expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',269),
  ('expresion -> expresion_simple MENOR_IGUAL_QUE expresion_simple','expresion',3,'p_expresion','gramatica_asc.py',270),
  ('expresion -> expresion_simple','expresion',1,'p_der_expresion','gramatica_asc.py',279),
  ('expresion_simple -> MENOS expresion_simple','expresion_simple',2,'p_negativo','gramatica_asc.py',283),
  ('expresion -> ABS PIZQ expresion_simple PDER','expresion',4,'p_abs','gramatica_asc.py',287),
  ('expresion -> NOT expresion_simple','expresion',2,'p_not','gramatica_asc.py',291),
  ('expresion -> BBNOT expresion_simple','expresion',2,'p_bit_not','gramatica_asc.py',295),
  ('expresion -> TEMPORAL CIZQ expresion_simple CDER','expresion',4,'p_acceso_arreglo','gramatica_asc.py',299),
  ('expresion -> PARAMETRO CIZQ expresion_simple CDER','expresion',4,'p_acceso_arreglo','gramatica_asc.py',300),
  ('expresion -> RETORNO CIZQ expresion_simple CDER','expresion',4,'p_acceso_arreglo','gramatica_asc.py',301),
  ('expresion -> PILA CIZQ expresion_simple CDER','expresion',4,'p_acceso_arreglo','gramatica_asc.py',302),
  ('expresion_simple -> TEMPORAL','expresion_simple',1,'p_expresion_simple_identificador','gramatica_asc.py',307),
  ('expresion_simple -> PARAMETRO','expresion_simple',1,'p_expresion_simple_identificador','gramatica_asc.py',308),
  ('expresion_simple -> RETORNO','expresion_simple',1,'p_expresion_simple_identificador','gramatica_asc.py',309),
  ('expresion_simple -> PILA','expresion_simple',1,'p_expresion_simple_identificador','gramatica_asc.py',310),
  ('expresion_simple -> RA','expresion_simple',1,'p_expresion_simple_identificador','gramatica_asc.py',311),
  ('expresion_simple -> SP','expresion_simple',1,'p_expresion_simple_identificador','gramatica_asc.py',312),
  ('expresion_simple -> ENTERO','expresion_simple',1,'p_expresion_simple_entero','gramatica_asc.py',317),
  ('expresion_simple -> DECIMAL','expresion_simple',1,'p_expresion_simple_decimal','gramatica_asc.py',322),
  ('expresion_simple -> CADENA','expresion_simple',1,'p_expresion_simple_cadena','gramatica_asc.py',327),
]
