
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABS AND ARRAY ASIG BBAND BBDER BBIZQ BBNOT BBOR BBXOR CADENA CDER CHAR CIZQ DECIMAL DESIGUAL_QUE DIVIDIDO DPUNTOS ENTERO EXIT FLOAT GOTO IF IGUAL_QUE INT LABEL MAS MAYOR_IGUAL_QUE MAYOR_QUE MENOR_IGUAL_QUE MENOR_QUE MENOS MODULO NOT OR PARAMETRO PDER PILA PIZQ POR PRINT PTCOMA RA READ RETORNO SP TEMPORAL UNSET XORinit            : labelslabels    : label labels_derlabels_der : label labels_derlabels_der : epsilonlabel    : LABEL DPUNTOS instruccionesinstrucciones : instruccion instrucciones_derinstrucciones_der : instruccion instrucciones_derinstrucciones_der : epsilon instruccion     : print_inst instruccion     : goto_inst instruccion     : exit_inst instruccion     : unset_inst instruccion     : if_inst instruccion : asig_inst print_inst     : PRINT PIZQ expresion PDER PTCOMAgoto_inst     : GOTO LABEL PTCOMAexit_inst     : EXIT PTCOMAunset_inst     : UNSET PIZQ expresion_simple PDER PTCOMAif_inst     : IF PIZQ expresion PDER instruccionasig_inst  : asignable accesos ASIG asig_valor PTCOMAasig_valor : expresionasig_valor : PIZQ asig_valor_derasig_valor_der : tipo PDER expresionasig_valor_der : expresion PDER tipo : INT\n            | FLOAT\n            | CHAR\n    asig_valor : READ PIZQ PDERasig_valor : ARRAY PIZQ PDERasignable     : TEMPORAL    asignable     : PARAMETROasignable     : RETORNOasignable     : PILAasignable     : RA asignable     : SP accesos   : acceso accesos accesos   : epsilon acceso    : CIZQ expresion_simple CDER expresion :   expresion_simple expresion_derexpresion_der :  MAS expresion_simple\n                        | MENOS expresion_simple\n                        | POR expresion_simple\n                        | DIVIDIDO expresion_simple\n                        | MODULO expresion_simple\n                        | AND expresion_simple\n                        | OR expresion_simple\n                        | XOR expresion_simple\n                        | BBAND expresion_simple\n                        | BBOR expresion_simple\n                        | BBXOR expresion_simple\n                        | BBIZQ expresion_simple\n                        | BBDER expresion_simple\n                        | IGUAL_QUE expresion_simple\n                        | DESIGUAL_QUE expresion_simple\n                        | MAYOR_QUE expresion_simple\n                        | MENOR_QUE expresion_simple\n                        | MAYOR_IGUAL_QUE expresion_simple\n                        | MENOR_IGUAL_QUE expresion_simple\n     expresion_der : epsilon  expresion_simple     : MENOS expresion_simple expresion     : ABS PIZQ expresion_simple PDER  expresion     : NOT expresion_simple expresion     : BBNOT expresion_simple expresion_simple     : asignable accesos expresion_simple     : ENTERO expresion_simple     : DECIMAL expresion_simple     : CADENAepsilon :'
    
_lr_action_items = {'LABEL':([0,3,5,10,11,12,13,14,15,16,17,19,30,31,32,35,42,53,94,115,116,117,],[4,4,4,-5,-68,-9,-10,-11,-12,-13,-14,34,-68,-6,-8,-17,-7,-16,-15,-18,-19,-20,]),'$end':([1,2,3,5,6,7,9,10,11,12,13,14,15,16,17,30,31,32,35,42,53,94,115,116,117,],[0,-1,-68,-68,-2,-4,-3,-5,-68,-9,-10,-11,-12,-13,-14,-68,-6,-8,-17,-7,-16,-15,-18,-19,-20,]),'DPUNTOS':([4,],[8,]),'PRINT':([8,11,12,13,14,15,16,17,30,35,53,87,94,115,116,117,],[18,18,-9,-10,-11,-12,-13,-14,18,-17,-16,18,-15,-18,-19,-20,]),'GOTO':([8,11,12,13,14,15,16,17,30,35,53,87,94,115,116,117,],[19,19,-9,-10,-11,-12,-13,-14,19,-17,-16,19,-15,-18,-19,-20,]),'EXIT':([8,11,12,13,14,15,16,17,30,35,53,87,94,115,116,117,],[20,20,-9,-10,-11,-12,-13,-14,20,-17,-16,20,-15,-18,-19,-20,]),'UNSET':([8,11,12,13,14,15,16,17,30,35,53,87,94,115,116,117,],[21,21,-9,-10,-11,-12,-13,-14,21,-17,-16,21,-15,-18,-19,-20,]),'IF':([8,11,12,13,14,15,16,17,30,35,53,87,94,115,116,117,],[22,22,-9,-10,-11,-12,-13,-14,22,-17,-16,22,-15,-18,-19,-20,]),'TEMPORAL':([8,11,12,13,14,15,16,17,30,33,35,36,37,41,46,47,48,53,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,87,90,94,115,116,117,127,],[24,24,-9,-10,-11,-12,-13,-14,24,24,-17,24,24,24,24,24,24,-16,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-15,-18,-19,-20,24,]),'PARAMETRO':([8,11,12,13,14,15,16,17,30,33,35,36,37,41,46,47,48,53,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,87,90,94,115,116,117,127,],[25,25,-9,-10,-11,-12,-13,-14,25,25,-17,25,25,25,25,25,25,-16,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-15,-18,-19,-20,25,]),'RETORNO':([8,11,12,13,14,15,16,17,30,33,35,36,37,41,46,47,48,53,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,87,90,94,115,116,117,127,],[26,26,-9,-10,-11,-12,-13,-14,26,26,-17,26,26,26,26,26,26,-16,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-15,-18,-19,-20,26,]),'PILA':([8,11,12,13,14,15,16,17,30,33,35,36,37,41,46,47,48,53,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,87,90,94,115,116,117,127,],[27,27,-9,-10,-11,-12,-13,-14,27,27,-17,27,27,27,27,27,27,-16,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-15,-18,-19,-20,27,]),'RA':([8,11,12,13,14,15,16,17,30,33,35,36,37,41,46,47,48,53,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,87,90,94,115,116,117,127,],[28,28,-9,-10,-11,-12,-13,-14,28,28,-17,28,28,28,28,28,28,-16,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-15,-18,-19,-20,28,]),'SP':([8,11,12,13,14,15,16,17,30,33,35,36,37,41,46,47,48,53,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,87,90,94,115,116,117,127,],[29,29,-9,-10,-11,-12,-13,-14,29,29,-17,29,29,29,29,29,29,-16,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-15,-18,-19,-20,29,]),'PIZQ':([18,21,22,45,56,91,92,],[33,36,37,81,90,124,125,]),'PTCOMA':([20,24,25,26,27,28,29,34,39,40,44,49,50,51,52,57,59,60,80,82,83,84,85,86,88,89,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,118,126,128,129,130,131,],[35,-30,-31,-32,-33,-34,-35,53,-68,-37,-68,-68,-65,-66,-67,-36,94,-39,-59,-62,-63,-60,-64,115,117,-21,-38,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-22,-61,-24,-28,-29,-23,]),'CIZQ':([23,24,25,26,27,28,29,39,49,93,],[41,-30,-31,-32,-33,-34,-35,41,41,-38,]),'ASIG':([23,24,25,26,27,28,29,38,39,40,57,93,],[-68,-30,-31,-32,-33,-34,-35,56,-68,-37,-36,-38,]),'MAS':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,61,-68,-65,-66,-67,-36,-60,-64,-38,]),'MENOS':([24,25,26,27,28,29,33,36,37,39,40,41,44,46,47,48,49,50,51,52,56,57,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,84,85,90,93,127,],[-30,-31,-32,-33,-34,-35,48,48,48,-68,-37,48,62,48,48,48,-68,-65,-66,-67,48,-36,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-60,-64,48,-38,48,]),'POR':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,63,-68,-65,-66,-67,-36,-60,-64,-38,]),'DIVIDIDO':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,64,-68,-65,-66,-67,-36,-60,-64,-38,]),'MODULO':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,65,-68,-65,-66,-67,-36,-60,-64,-38,]),'AND':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,66,-68,-65,-66,-67,-36,-60,-64,-38,]),'OR':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,67,-68,-65,-66,-67,-36,-60,-64,-38,]),'XOR':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,68,-68,-65,-66,-67,-36,-60,-64,-38,]),'BBAND':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,69,-68,-65,-66,-67,-36,-60,-64,-38,]),'BBOR':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,70,-68,-65,-66,-67,-36,-60,-64,-38,]),'BBXOR':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,71,-68,-65,-66,-67,-36,-60,-64,-38,]),'BBIZQ':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,72,-68,-65,-66,-67,-36,-60,-64,-38,]),'BBDER':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,73,-68,-65,-66,-67,-36,-60,-64,-38,]),'IGUAL_QUE':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,74,-68,-65,-66,-67,-36,-60,-64,-38,]),'DESIGUAL_QUE':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,75,-68,-65,-66,-67,-36,-60,-64,-38,]),'MAYOR_QUE':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,76,-68,-65,-66,-67,-36,-60,-64,-38,]),'MENOR_QUE':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,77,-68,-65,-66,-67,-36,-60,-64,-38,]),'MAYOR_IGUAL_QUE':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,78,-68,-65,-66,-67,-36,-60,-64,-38,]),'MENOR_IGUAL_QUE':([24,25,26,27,28,29,39,40,44,49,50,51,52,57,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,79,-68,-65,-66,-67,-36,-60,-64,-38,]),'PDER':([24,25,26,27,28,29,39,40,43,44,49,50,51,52,54,55,57,60,80,82,83,84,85,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,119,120,121,122,123,124,125,126,],[-30,-31,-32,-33,-34,-35,-68,-37,59,-68,-68,-65,-66,-67,86,87,-36,-39,-59,-62,-63,-60,-64,-38,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,126,127,128,-25,-26,-27,129,130,-61,]),'CDER':([24,25,26,27,28,29,39,40,49,50,51,52,57,58,84,85,93,],[-30,-31,-32,-33,-34,-35,-68,-37,-68,-65,-66,-67,-36,93,-60,-64,-38,]),'ABS':([33,37,56,90,127,],[45,45,45,45,45,]),'NOT':([33,37,56,90,127,],[46,46,46,46,46,]),'BBNOT':([33,37,56,90,127,],[47,47,47,47,47,]),'ENTERO':([33,36,37,41,46,47,48,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,90,127,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'DECIMAL':([33,36,37,41,46,47,48,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,90,127,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'CADENA':([33,36,37,41,46,47,48,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,90,127,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'READ':([56,],[91,]),'ARRAY':([56,],[92,]),'INT':([90,],[121,]),'FLOAT':([90,],[122,]),'CHAR':([90,],[123,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'labels':([0,],[2,]),'label':([0,3,5,],[3,5,5,]),'labels_der':([3,5,],[6,9,]),'epsilon':([3,5,11,23,30,39,44,49,],[7,7,32,40,32,40,80,40,]),'instrucciones':([8,],[10,]),'instruccion':([8,11,30,87,],[11,30,30,116,]),'print_inst':([8,11,30,87,],[12,12,12,12,]),'goto_inst':([8,11,30,87,],[13,13,13,13,]),'exit_inst':([8,11,30,87,],[14,14,14,14,]),'unset_inst':([8,11,30,87,],[15,15,15,15,]),'if_inst':([8,11,30,87,],[16,16,16,16,]),'asig_inst':([8,11,30,87,],[17,17,17,17,]),'asignable':([8,11,30,33,36,37,41,46,47,48,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,87,90,127,],[23,23,23,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,23,49,49,]),'instrucciones_der':([11,30,],[31,42,]),'accesos':([23,39,49,],[38,57,85,]),'acceso':([23,39,49,],[39,39,39,]),'expresion':([33,37,56,90,127,],[43,55,89,120,131,]),'expresion_simple':([33,36,37,41,46,47,48,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,90,127,],[44,54,44,58,82,83,84,44,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,44,44,]),'expresion_der':([44,],[60,]),'asig_valor':([56,],[88,]),'asig_valor_der':([90,],[118,]),'tipo':([90,],[119,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> labels','init',1,'p_init','gramatica_desc.py',174),
  ('labels -> label labels_der','labels',2,'p_labels','gramatica_desc.py',180),
  ('labels_der -> label labels_der','labels_der',2,'p_labels_der','gramatica_desc.py',186),
  ('labels_der -> epsilon','labels_der',1,'p_labels_der_epsilon','gramatica_desc.py',194),
  ('label -> LABEL DPUNTOS instrucciones','label',3,'p_label','gramatica_desc.py',200),
  ('instrucciones -> instruccion instrucciones_der','instrucciones',2,'p_instrucciones','gramatica_desc.py',206),
  ('instrucciones_der -> instruccion instrucciones_der','instrucciones_der',2,'p_instrucciones_der','gramatica_desc.py',212),
  ('instrucciones_der -> epsilon','instrucciones_der',1,'p_instrucciones_der_epsilon','gramatica_desc.py',220),
  ('instruccion -> print_inst','instruccion',1,'p_instruccion_1','gramatica_desc.py',226),
  ('instruccion -> goto_inst','instruccion',1,'p_instruccion_2','gramatica_desc.py',232),
  ('instruccion -> exit_inst','instruccion',1,'p_instruccion_3','gramatica_desc.py',238),
  ('instruccion -> unset_inst','instruccion',1,'p_instruccion_4','gramatica_desc.py',244),
  ('instruccion -> if_inst','instruccion',1,'p_instruccion_5','gramatica_desc.py',250),
  ('instruccion -> asig_inst','instruccion',1,'p_instruccion_6','gramatica_desc.py',256),
  ('print_inst -> PRINT PIZQ expresion PDER PTCOMA','print_inst',5,'p_instruccion_print','gramatica_desc.py',262),
  ('goto_inst -> GOTO LABEL PTCOMA','goto_inst',3,'p_instruccion_goto','gramatica_desc.py',268),
  ('exit_inst -> EXIT PTCOMA','exit_inst',2,'p_instruccion_exit','gramatica_desc.py',274),
  ('unset_inst -> UNSET PIZQ expresion_simple PDER PTCOMA','unset_inst',5,'p_instruccion_unset','gramatica_desc.py',280),
  ('if_inst -> IF PIZQ expresion PDER instruccion','if_inst',5,'p_instruccion_if','gramatica_desc.py',286),
  ('asig_inst -> asignable accesos ASIG asig_valor PTCOMA','asig_inst',5,'p_instruccion_asig','gramatica_desc.py',292),
  ('asig_valor -> expresion','asig_valor',1,'p_asig_valor','gramatica_desc.py',298),
  ('asig_valor -> PIZQ asig_valor_der','asig_valor',2,'p_asig_conversion','gramatica_desc.py',308),
  ('asig_valor_der -> tipo PDER expresion','asig_valor_der',3,'p_asig_valor_conversion_der','gramatica_desc.py',312),
  ('asig_valor_der -> expresion PDER','asig_valor_der',2,'p_asig_valor_expresion_der','gramatica_desc.py',318),
  ('tipo -> INT','tipo',1,'p_tipo','gramatica_desc.py',324),
  ('tipo -> FLOAT','tipo',1,'p_tipo','gramatica_desc.py',325),
  ('tipo -> CHAR','tipo',1,'p_tipo','gramatica_desc.py',326),
  ('asig_valor -> READ PIZQ PDER','asig_valor',3,'p_asig_read','gramatica_desc.py',333),
  ('asig_valor -> ARRAY PIZQ PDER','asig_valor',3,'p_asig_array','gramatica_desc.py',339),
  ('asignable -> TEMPORAL','asignable',1,'p_registros_asignables_1','gramatica_desc.py',345),
  ('asignable -> PARAMETRO','asignable',1,'p_registros_asignables_2','gramatica_desc.py',349),
  ('asignable -> RETORNO','asignable',1,'p_registros_asignables_3','gramatica_desc.py',353),
  ('asignable -> PILA','asignable',1,'p_registros_asignables_4','gramatica_desc.py',357),
  ('asignable -> RA','asignable',1,'p_registros_asignables_5','gramatica_desc.py',361),
  ('asignable -> SP','asignable',1,'p_registros_asignables_6','gramatica_desc.py',365),
  ('accesos -> acceso accesos','accesos',2,'p_accesos','gramatica_desc.py',369),
  ('accesos -> epsilon','accesos',1,'p_accesos_epsilon','gramatica_desc.py',374),
  ('acceso -> CIZQ expresion_simple CDER','acceso',3,'p_acceso','gramatica_desc.py',378),
  ('expresion -> expresion_simple expresion_der','expresion',2,'p_expresion','gramatica_desc.py',382),
  ('expresion_der -> MAS expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',386),
  ('expresion_der -> MENOS expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',387),
  ('expresion_der -> POR expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',388),
  ('expresion_der -> DIVIDIDO expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',389),
  ('expresion_der -> MODULO expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',390),
  ('expresion_der -> AND expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',391),
  ('expresion_der -> OR expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',392),
  ('expresion_der -> XOR expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',393),
  ('expresion_der -> BBAND expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',394),
  ('expresion_der -> BBOR expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',395),
  ('expresion_der -> BBXOR expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',396),
  ('expresion_der -> BBIZQ expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',397),
  ('expresion_der -> BBDER expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',398),
  ('expresion_der -> IGUAL_QUE expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',399),
  ('expresion_der -> DESIGUAL_QUE expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',400),
  ('expresion_der -> MAYOR_QUE expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',401),
  ('expresion_der -> MENOR_QUE expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',402),
  ('expresion_der -> MAYOR_IGUAL_QUE expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',403),
  ('expresion_der -> MENOR_IGUAL_QUE expresion_simple','expresion_der',2,'p_expresion_der','gramatica_desc.py',404),
  ('expresion_der -> epsilon','expresion_der',1,'p_expresion_der_epsilon','gramatica_desc.py',484),
  ('expresion_simple -> MENOS expresion_simple','expresion_simple',2,'p_negativo','gramatica_desc.py',490),
  ('expresion -> ABS PIZQ expresion_simple PDER','expresion',4,'p_abs','gramatica_desc.py',496),
  ('expresion -> NOT expresion_simple','expresion',2,'p_not','gramatica_desc.py',502),
  ('expresion -> BBNOT expresion_simple','expresion',2,'p_bit_not','gramatica_desc.py',508),
  ('expresion_simple -> asignable accesos','expresion_simple',2,'p_acceso_arreglo','gramatica_desc.py',514),
  ('expresion_simple -> ENTERO','expresion_simple',1,'p_expresion_simple_entero','gramatica_desc.py',524),
  ('expresion_simple -> DECIMAL','expresion_simple',1,'p_expresion_simple_decimal','gramatica_desc.py',530),
  ('expresion_simple -> CADENA','expresion_simple',1,'p_expresion_simple_cadena','gramatica_desc.py',536),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','gramatica_desc.py',542),
]
