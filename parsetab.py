
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND AND_BLOCK ASIGNACION BEGIN_BLOCK BREAK CADENA CASE CLASS COMA COMENTARIO CORCHETE_DER CORCHETE_IZQ DEF DEFINED DIFERENTE DIVIDIR DO DOSPUNTOS DOSPUNTOS_IGUAL ELSE ELSIF END END_BLOCK ENSURE EXPONENCIACION FALSE FLECHA_HASH FLOTANTE GETS IF IGUAL_IGUAL IN INTERROGACION LENGTH LLAVE_DER LLAVE_IZQ MAS MAYOR_IGUAL MAYOR_QUE MENOR_IGUAL MENOR_QUE MENOS MODULE MODULO MULTIPLICAR NEXT NOT NOT_BLOCK NUMERO OR PARENTESIS_DER PARENTESIS_IZQ PUNTO PUNTO_Y_COMA PUTS REDO RESERVADA RETRY RETURN SELF SIMBOLO SUPER THEN TRUE UNLESS UNTIL VARIABLE_CLASE VARIABLE_GLOBAL VARIABLE_INSTANCIA VARIABLE_LOCAL WHEN WHILEprograma : sentencia\n                | sentencia programasentencia : asignacion\n                | impresion\n                | array\n                | condicion\n                | funcion\n                | comentarioasignacion : variable ASIGNACION valoressolicitud_datos : VARIABLE_LOCAL ASIGNACION GETS PARENTESIS_IZQ PARENTESIS_DERimpresion : PUTS PARENTESIS_IZQ argumentos PARENTESIS_DERimpresion : PUTScomentario : COMENTARIO argumentoarray : CORCHETE_IZQ argumentos CORCHETE_DERcondicion : if\n                | if_else\n                | if_elsif_elseif : IF expresion instrucciones END_BLOCK\n            | IF expresion THEN instrucciones END_BLOCKif_else : IF expresion instrucciones ELSE instrucciones END_BLOCK\n               | IF expresion THEN instrucciones ELSE instrucciones END_BLOCKif_elsif_else : IF expresion instrucciones elsif_clauses END_BLOCK\n                     | IF expresion THEN instrucciones elsif_clauses END_BLOCK\n                     | IF expresion instrucciones elsif_clauses ELSE instrucciones END_BLOCK\n                     | IF expresion THEN instrucciones elsif_clauses ELSE instrucciones END_BLOCKelsif_clauses : ELSIF expresion instrucciones\n                     | ELSIF expresion THEN instrucciones\n                     | ELSIF expresion instrucciones elsif_clauses\n                     | ELSIF expresion THEN instrucciones elsif_clausesfuncion : DEF VARIABLE_LOCAL PARENTESIS_IZQ parametros PARENTESIS_DER instrucciones END_BLOCKparametros : parametro\n                  | parametro COMA parametrosparametro : VARIABLE_LOCAL\n                | emptyexpresion : var_expresion\n                | var_expresion comparadores var_expresion\n                | expresion comparadores expresion\n                | PARENTESIS_IZQ expresion PARENTESIS_DER\n                | NOT_BLOCK expresion\n                | expresion operador_logico expresioncomparadores : MAYOR_QUE\n                    | MENOR_QUE\n                    | IGUAL_IGUAL\n                    | DIFERENTE\n                    | MAYOR_IGUAL\n                    | MENOR_IGUALoperador_logico : AND\n                        | OR\n                        | NOTvar_expresion : valor\n                    | booleanoinstrucciones : instruccion\n                    | instruccion instrucciones\n                    | instruccion PUNTO_Y_COMA instruccionesinstruccion : asignacion\n                    | impresion\n                    | condicion\n                    | llamada_funcion\n                    | funcionllamada_funcion : VARIABLE_LOCAL PARENTESIS_IZQ argumentos PARENTESIS_DER\n                       |  VARIABLE_LOCAL PARENTESIS_IZQ PARENTESIS_DERvariable : VARIABLE_LOCAL\n                | VARIABLE_GLOBAL\n                | VARIABLE_INSTANCIA\n                | VARIABLE_CLASEbooleano : FALSE\n                | TRUE argumentos : argumento\n                    | argumento COMA argumentosargumento : booleano\n                | operacionAritmetica\n                | array\n                | empty empty :valores : operacionAritmetica\n                | SIMBOLO\n                | booleano\n                | arrayvalor : NUMERO\n            | FLOTANTE\n            | CADENA\n            | variableoperacionAritmetica : valor \n                         | valor operador operacionAritmeticaoperador : MAS\n                | MENOS\n                | MULTIPLICAR\n                | DIVIDIR\n                | MODULO\n                | EXPONENCIACIONhash : LLAVE_IZQ pares LLAVE_DERpares : par\n             | par COMA parespar : valor FLECHA_HASH valoruntil : UNTIL expresion DO instrucciones END_BLOCK\n             | UNTIL expresion instrucciones END_BLOCKfuncion : DEF VARIABLE_LOCAL PARENTESIS_IZQ parametros_defecto PARENTESIS_DER instrucciones END_BLOCKparametros_defecto : parametro_defecto\n                          | parametro_defecto COMA parametros_defectoparametro_defecto : VARIABLE_LOCAL\n                         | VARIABLE_LOCAL ASIGNACION valorcadena_interpolacion : CADENA LLAVE_IZQ variable LLAVE_DERincremento : VARIABLE_LOCAL MAS ASIGNACION expresion'
    
_lr_action_items = {'PUTS':([0,2,3,4,5,6,7,8,10,12,13,14,16,17,18,19,20,27,28,29,30,31,32,33,34,35,36,37,39,40,41,44,45,46,47,48,49,50,52,63,66,76,77,78,79,80,84,85,87,94,95,99,100,102,104,105,107,108,112,113,114,115,116,120,128,131,133,134,135,136,137,138,141,144,],[10,10,-3,-4,-5,-6,-7,-8,-12,-15,-16,-17,-62,-74,-63,-64,-65,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-13,10,-35,-50,-51,-9,-75,-76,-77,-78,-14,10,10,-55,-56,-57,-58,-59,-39,-11,-84,-18,10,-37,-40,10,-36,-38,10,10,-22,10,10,-19,10,-61,-20,10,-23,10,-60,-30,-97,-24,-21,-25,]),'CORCHETE_IZQ':([0,2,3,4,5,6,7,8,10,11,12,13,14,16,17,18,19,20,23,24,27,28,29,30,31,32,33,34,35,36,37,39,46,47,48,49,50,52,53,85,87,94,103,112,115,128,133,136,137,138,141,144,],[11,11,-3,-4,-5,-6,-7,-8,-12,11,-15,-16,-17,-62,11,-63,-64,-65,11,11,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-13,-9,-75,-76,-77,-78,-14,11,-11,-84,-18,11,-22,-19,-20,-23,-30,-97,-24,-21,-25,]),'DEF':([0,2,3,4,5,6,7,8,10,12,13,14,16,17,18,19,20,27,28,29,30,31,32,33,34,35,36,37,39,40,41,44,45,46,47,48,49,50,52,63,66,76,77,78,79,80,84,85,87,94,95,99,100,102,104,105,107,108,112,113,114,115,116,120,128,131,133,134,135,136,137,138,141,144,],[15,15,-3,-4,-5,-6,-7,-8,-12,-15,-16,-17,-62,-74,-63,-64,-65,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-13,15,-35,-50,-51,-9,-75,-76,-77,-78,-14,15,15,-55,-56,-57,-58,-59,-39,-11,-84,-18,15,-37,-40,15,-36,-38,15,15,-22,15,15,-19,15,-61,-20,15,-23,15,-60,-30,-97,-24,-21,-25,]),'COMENTARIO':([0,2,3,4,5,6,7,8,10,12,13,14,16,17,18,19,20,27,28,29,30,31,32,33,34,35,36,37,39,46,47,48,49,50,52,85,87,94,112,115,128,133,136,137,138,141,144,],[17,17,-3,-4,-5,-6,-7,-8,-12,-15,-16,-17,-62,-74,-63,-64,-65,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-13,-9,-75,-76,-77,-78,-14,-11,-84,-18,-22,-19,-20,-23,-30,-97,-24,-21,-25,]),'VARIABLE_LOCAL':([0,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,84,85,87,94,95,97,99,100,102,103,104,105,106,107,108,109,110,112,113,114,115,116,120,128,131,133,134,135,136,137,138,141,144,],[16,16,-3,-4,-5,-6,-7,-8,-12,16,-15,-16,-17,38,-62,16,-63,-64,-65,16,16,16,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-13,81,-35,16,16,-50,-51,-9,-75,-76,-77,-78,-14,16,16,-85,-86,-87,-88,-89,-90,88,81,16,16,81,-41,-42,-43,-44,-45,-46,-47,-48,-49,-55,-56,-57,-58,-59,16,-39,-11,-84,-18,81,16,-37,-40,81,16,-36,-38,16,81,81,125,127,-22,81,81,-19,81,-61,-20,81,-23,81,-60,-30,-97,-24,-21,-25,]),'VARIABLE_GLOBAL':([0,2,3,4,5,6,7,8,10,11,12,13,14,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,84,85,87,94,95,97,99,100,102,103,104,105,106,107,108,112,113,114,115,116,120,128,131,133,134,135,136,137,138,141,144,],[18,18,-3,-4,-5,-6,-7,-8,-12,18,-15,-16,-17,-62,18,-63,-64,-65,18,18,18,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-13,18,-35,18,18,-50,-51,-9,-75,-76,-77,-78,-14,18,18,-85,-86,-87,-88,-89,-90,18,18,18,18,-41,-42,-43,-44,-45,-46,-47,-48,-49,-55,-56,-57,-58,-59,18,-39,-11,-84,-18,18,18,-37,-40,18,18,-36,-38,18,18,18,-22,18,18,-19,18,-61,-20,18,-23,18,-60,-30,-97,-24,-21,-25,]),'VARIABLE_INSTANCIA':([0,2,3,4,5,6,7,8,10,11,12,13,14,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,84,85,87,94,95,97,99,100,102,103,104,105,106,107,108,112,113,114,115,116,120,128,131,133,134,135,136,137,138,141,144,],[19,19,-3,-4,-5,-6,-7,-8,-12,19,-15,-16,-17,-62,19,-63,-64,-65,19,19,19,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-13,19,-35,19,19,-50,-51,-9,-75,-76,-77,-78,-14,19,19,-85,-86,-87,-88,-89,-90,19,19,19,19,-41,-42,-43,-44,-45,-46,-47,-48,-49,-55,-56,-57,-58,-59,19,-39,-11,-84,-18,19,19,-37,-40,19,19,-36,-38,19,19,19,-22,19,19,-19,19,-61,-20,19,-23,19,-60,-30,-97,-24,-21,-25,]),'VARIABLE_CLASE':([0,2,3,4,5,6,7,8,10,11,12,13,14,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,84,85,87,94,95,97,99,100,102,103,104,105,106,107,108,112,113,114,115,116,120,128,131,133,134,135,136,137,138,141,144,],[20,20,-3,-4,-5,-6,-7,-8,-12,20,-15,-16,-17,-62,20,-63,-64,-65,20,20,20,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-13,20,-35,20,20,-50,-51,-9,-75,-76,-77,-78,-14,20,20,-85,-86,-87,-88,-89,-90,20,20,20,20,-41,-42,-43,-44,-45,-46,-47,-48,-49,-55,-56,-57,-58,-59,20,-39,-11,-84,-18,20,20,-37,-40,20,20,-36,-38,20,20,20,-22,20,20,-19,20,-61,-20,20,-23,20,-60,-30,-97,-24,-21,-25,]),'IF':([0,2,3,4,5,6,7,8,10,12,13,14,16,17,18,19,20,27,28,29,30,31,32,33,34,35,36,37,39,40,41,44,45,46,47,48,49,50,52,63,66,76,77,78,79,80,84,85,87,94,95,99,100,102,104,105,107,108,112,113,114,115,116,120,128,131,133,134,135,136,137,138,141,144,],[21,21,-3,-4,-5,-6,-7,-8,-12,-15,-16,-17,-62,-74,-63,-64,-65,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-13,21,-35,-50,-51,-9,-75,-76,-77,-78,-14,21,21,-55,-56,-57,-58,-59,-39,-11,-84,-18,21,-37,-40,21,-36,-38,21,21,-22,21,21,-19,21,-61,-20,21,-23,21,-60,-30,-97,-24,-21,-25,]),'$end':([1,2,3,4,5,6,7,8,10,12,13,14,16,17,18,19,20,22,27,28,29,30,31,32,33,34,35,36,37,39,46,47,48,49,50,52,85,87,94,112,115,128,133,136,137,138,141,144,],[0,-1,-3,-4,-5,-6,-7,-8,-12,-15,-16,-17,-62,-74,-63,-64,-65,-2,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-13,-9,-75,-76,-77,-78,-14,-11,-84,-18,-22,-19,-20,-23,-30,-97,-24,-21,-25,]),'ASIGNACION':([9,16,18,19,20,81,88,127,],[23,-62,-63,-64,-65,-62,106,106,]),'PARENTESIS_IZQ':([10,21,38,42,43,64,65,67,68,69,70,71,72,73,74,75,81,97,],[24,42,61,42,42,42,42,-41,-42,-43,-44,-45,-46,-47,-48,-49,103,42,]),'PUNTO_Y_COMA':([10,12,13,14,16,18,19,20,31,32,33,34,35,36,37,46,47,48,49,50,52,66,76,77,78,79,80,85,87,94,112,115,120,128,133,135,136,137,138,141,144,],[-12,-15,-16,-17,-62,-63,-64,-65,-66,-67,-83,-79,-80,-81,-82,-9,-75,-76,-77,-78,-14,102,-55,-56,-57,-58,-59,-11,-84,-18,-22,-19,-61,-20,-23,-60,-30,-97,-24,-21,-25,]),'END_BLOCK':([10,12,13,14,16,18,19,20,31,32,33,34,35,36,37,46,47,48,49,50,52,62,66,76,77,78,79,80,85,87,94,96,98,101,111,112,115,117,118,120,122,123,128,129,130,132,133,135,136,137,138,139,140,141,142,143,144,],[-12,-15,-16,-17,-62,-63,-64,-65,-66,-67,-83,-79,-80,-81,-82,-9,-75,-76,-77,-78,-14,94,-52,-55,-56,-57,-58,-59,-11,-84,-18,112,115,-53,128,-22,-19,133,-54,-61,136,137,-20,138,-26,141,-23,-60,-30,-97,-24,-28,-27,-21,144,-29,-25,]),'ELSE':([10,12,13,14,16,18,19,20,31,32,33,34,35,36,37,46,47,48,49,50,52,62,66,76,77,78,79,80,85,87,94,96,98,101,112,115,117,118,120,128,130,133,135,136,137,138,139,140,141,143,144,],[-12,-15,-16,-17,-62,-63,-64,-65,-66,-67,-83,-79,-80,-81,-82,-9,-75,-76,-77,-78,-14,95,-52,-55,-56,-57,-58,-59,-11,-84,-18,113,116,-53,-22,-19,134,-54,-61,-20,-26,-23,-60,-30,-97,-24,-28,-27,-21,-29,-25,]),'ELSIF':([10,12,13,14,16,18,19,20,31,32,33,34,35,36,37,46,47,48,49,50,52,62,66,76,77,78,79,80,85,87,94,98,101,112,115,118,120,128,130,133,135,136,137,138,140,141,144,],[-12,-15,-16,-17,-62,-63,-64,-65,-66,-67,-83,-79,-80,-81,-82,-9,-75,-76,-77,-78,-14,97,-52,-55,-56,-57,-58,-59,-11,-84,-18,97,-53,-22,-19,-54,-61,-20,97,-23,-60,-30,-97,-24,97,-21,-25,]),'FALSE':([11,17,21,23,24,42,43,53,64,65,67,68,69,70,71,72,73,74,75,82,97,103,],[31,31,31,31,31,31,31,31,31,31,-41,-42,-43,-44,-45,-46,-47,-48,-49,31,31,31,]),'TRUE':([11,17,21,23,24,42,43,53,64,65,67,68,69,70,71,72,73,74,75,82,97,103,],[32,32,32,32,32,32,32,32,32,32,-41,-42,-43,-44,-45,-46,-47,-48,-49,32,32,32,]),'COMA':([11,16,18,19,20,24,26,27,28,29,30,31,32,33,34,35,36,37,52,53,61,87,88,91,92,93,103,109,121,125,127,],[-74,-62,-63,-64,-65,-74,53,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-14,-74,-74,-84,-33,109,110,-34,-74,-74,-101,-33,-100,]),'CORCHETE_DER':([11,16,18,19,20,25,26,27,28,29,30,31,32,33,34,35,36,37,52,53,86,87,],[-74,-62,-63,-64,-65,52,-68,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-14,-74,-69,-84,]),'NUMERO':([11,17,21,23,24,42,43,53,54,55,56,57,58,59,60,64,65,67,68,69,70,71,72,73,74,75,82,97,103,106,],[34,34,34,34,34,34,34,34,34,-85,-86,-87,-88,-89,-90,34,34,-41,-42,-43,-44,-45,-46,-47,-48,-49,34,34,34,34,]),'FLOTANTE':([11,17,21,23,24,42,43,53,54,55,56,57,58,59,60,64,65,67,68,69,70,71,72,73,74,75,82,97,103,106,],[35,35,35,35,35,35,35,35,35,-85,-86,-87,-88,-89,-90,35,35,-41,-42,-43,-44,-45,-46,-47,-48,-49,35,35,35,35,]),'CADENA':([11,17,21,23,24,42,43,53,54,55,56,57,58,59,60,64,65,67,68,69,70,71,72,73,74,75,82,97,103,106,],[36,36,36,36,36,36,36,36,36,-85,-86,-87,-88,-89,-90,36,36,-41,-42,-43,-44,-45,-46,-47,-48,-49,36,36,36,36,]),'MAS':([16,18,19,20,33,34,35,36,37,],[-62,-63,-64,-65,55,-79,-80,-81,-82,]),'MENOS':([16,18,19,20,33,34,35,36,37,],[-62,-63,-64,-65,56,-79,-80,-81,-82,]),'MULTIPLICAR':([16,18,19,20,33,34,35,36,37,],[-62,-63,-64,-65,57,-79,-80,-81,-82,]),'DIVIDIR':([16,18,19,20,33,34,35,36,37,],[-62,-63,-64,-65,58,-79,-80,-81,-82,]),'MODULO':([16,18,19,20,33,34,35,36,37,],[-62,-63,-64,-65,59,-79,-80,-81,-82,]),'EXPONENCIACION':([16,18,19,20,33,34,35,36,37,],[-62,-63,-64,-65,60,-79,-80,-81,-82,]),'MAYOR_QUE':([16,18,19,20,31,32,34,35,36,37,40,41,44,45,83,84,99,100,104,105,114,],[-62,-63,-64,-65,-66,-67,-79,-80,-81,-82,67,67,-50,-51,67,67,67,67,-36,-38,67,]),'MENOR_QUE':([16,18,19,20,31,32,34,35,36,37,40,41,44,45,83,84,99,100,104,105,114,],[-62,-63,-64,-65,-66,-67,-79,-80,-81,-82,68,68,-50,-51,68,68,68,68,-36,-38,68,]),'IGUAL_IGUAL':([16,18,19,20,31,32,34,35,36,37,40,41,44,45,83,84,99,100,104,105,114,],[-62,-63,-64,-65,-66,-67,-79,-80,-81,-82,69,69,-50,-51,69,69,69,69,-36,-38,69,]),'DIFERENTE':([16,18,19,20,31,32,34,35,36,37,40,41,44,45,83,84,99,100,104,105,114,],[-62,-63,-64,-65,-66,-67,-79,-80,-81,-82,70,70,-50,-51,70,70,70,70,-36,-38,70,]),'MAYOR_IGUAL':([16,18,19,20,31,32,34,35,36,37,40,41,44,45,83,84,99,100,104,105,114,],[-62,-63,-64,-65,-66,-67,-79,-80,-81,-82,71,71,-50,-51,71,71,71,71,-36,-38,71,]),'MENOR_IGUAL':([16,18,19,20,31,32,34,35,36,37,40,41,44,45,83,84,99,100,104,105,114,],[-62,-63,-64,-65,-66,-67,-79,-80,-81,-82,72,72,-50,-51,72,72,72,72,-36,-38,72,]),'THEN':([16,18,19,20,31,32,34,35,36,37,40,41,44,45,84,99,100,104,105,114,],[-62,-63,-64,-65,-66,-67,-79,-80,-81,-82,63,-35,-50,-51,-39,-37,-40,-36,-38,131,]),'AND':([16,18,19,20,31,32,34,35,36,37,40,41,44,45,83,84,99,100,104,105,114,],[-62,-63,-64,-65,-66,-67,-79,-80,-81,-82,73,-35,-50,-51,73,73,73,73,-36,-38,73,]),'OR':([16,18,19,20,31,32,34,35,36,37,40,41,44,45,83,84,99,100,104,105,114,],[-62,-63,-64,-65,-66,-67,-79,-80,-81,-82,74,-35,-50,-51,74,74,74,74,-36,-38,74,]),'NOT':([16,18,19,20,31,32,34,35,36,37,40,41,44,45,83,84,99,100,104,105,114,],[-62,-63,-64,-65,-66,-67,-79,-80,-81,-82,75,-35,-50,-51,75,75,75,75,-36,-38,75,]),'PARENTESIS_DER':([16,18,19,20,24,26,27,28,29,30,31,32,33,34,35,36,37,41,44,45,51,52,53,61,83,84,86,87,88,89,90,91,92,93,99,100,103,104,105,109,119,121,124,125,126,127,],[-62,-63,-64,-65,-74,-68,-70,-71,-72,-73,-66,-67,-83,-79,-80,-81,-82,-35,-50,-51,85,-14,-74,-74,105,-39,-69,-84,-33,107,108,-31,-98,-34,-37,-40,120,-36,-38,-74,135,-101,-32,-33,-99,-100,]),'NOT_BLOCK':([21,42,43,64,65,67,68,69,70,71,72,73,74,75,97,],[43,43,43,43,43,-41,-42,-43,-44,-45,-46,-47,-48,-49,43,]),'SIMBOLO':([23,],[48,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,],[1,22,]),'sentencia':([0,2,],[2,2,]),'asignacion':([0,2,40,63,66,95,102,107,108,113,114,116,131,134,],[3,3,76,76,76,76,76,76,76,76,76,76,76,76,]),'impresion':([0,2,40,63,66,95,102,107,108,113,114,116,131,134,],[4,4,77,77,77,77,77,77,77,77,77,77,77,77,]),'array':([0,2,11,17,23,24,53,103,],[5,5,29,29,50,29,29,29,]),'condicion':([0,2,40,63,66,95,102,107,108,113,114,116,131,134,],[6,6,78,78,78,78,78,78,78,78,78,78,78,78,]),'funcion':([0,2,40,63,66,95,102,107,108,113,114,116,131,134,],[7,7,80,80,80,80,80,80,80,80,80,80,80,80,]),'comentario':([0,2,],[8,8,]),'variable':([0,2,11,17,21,23,24,40,42,43,53,54,63,64,65,66,82,95,97,102,103,106,107,108,113,114,116,131,134,],[9,9,37,37,37,37,37,9,37,37,37,37,9,37,37,9,37,9,37,9,37,37,9,9,9,9,9,9,9,]),'if':([0,2,40,63,66,95,102,107,108,113,114,116,131,134,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'if_else':([0,2,40,63,66,95,102,107,108,113,114,116,131,134,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'if_elsif_else':([0,2,40,63,66,95,102,107,108,113,114,116,131,134,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'argumentos':([11,24,53,103,],[25,51,86,119,]),'argumento':([11,17,24,53,103,],[26,39,26,26,26,]),'booleano':([11,17,21,23,24,42,43,53,64,65,82,97,103,],[27,27,45,49,27,45,45,27,45,45,45,45,27,]),'operacionAritmetica':([11,17,23,24,53,54,103,],[28,28,47,28,28,87,28,]),'empty':([11,17,24,53,61,103,109,],[30,30,30,30,93,30,93,]),'valor':([11,17,21,23,24,42,43,53,54,64,65,82,97,103,106,],[33,33,44,33,33,44,44,33,33,44,44,44,44,33,121,]),'expresion':([21,42,43,64,65,97,],[40,83,84,99,100,114,]),'var_expresion':([21,42,43,64,65,82,97,],[41,41,41,41,41,104,41,]),'valores':([23,],[46,]),'operador':([33,],[54,]),'instrucciones':([40,63,66,95,102,107,108,113,114,116,131,134,],[62,98,101,111,118,122,123,129,130,132,140,142,]),'comparadores':([40,41,83,84,99,100,114,],[64,82,64,64,64,64,64,]),'operador_logico':([40,83,84,99,100,114,],[65,65,65,65,65,65,]),'instruccion':([40,63,66,95,102,107,108,113,114,116,131,134,],[66,66,66,66,66,66,66,66,66,66,66,66,]),'llamada_funcion':([40,63,66,95,102,107,108,113,114,116,131,134,],[79,79,79,79,79,79,79,79,79,79,79,79,]),'parametros':([61,109,],[89,124,]),'parametros_defecto':([61,110,],[90,126,]),'parametro':([61,109,],[91,91,]),'parametro_defecto':([61,110,],[92,92,]),'elsif_clauses':([62,98,130,140,],[96,117,139,143,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> sentencia','programa',1,'p_programa','Analizador_Sintactico.py',8),
  ('programa -> sentencia programa','programa',2,'p_programa','Analizador_Sintactico.py',9),
  ('sentencia -> asignacion','sentencia',1,'p_sentencia','Analizador_Sintactico.py',12),
  ('sentencia -> impresion','sentencia',1,'p_sentencia','Analizador_Sintactico.py',13),
  ('sentencia -> array','sentencia',1,'p_sentencia','Analizador_Sintactico.py',14),
  ('sentencia -> condicion','sentencia',1,'p_sentencia','Analizador_Sintactico.py',15),
  ('sentencia -> funcion','sentencia',1,'p_sentencia','Analizador_Sintactico.py',16),
  ('sentencia -> comentario','sentencia',1,'p_sentencia','Analizador_Sintactico.py',17),
  ('asignacion -> variable ASIGNACION valores','asignacion',3,'p_asignacion','Analizador_Sintactico.py',20),
  ('solicitud_datos -> VARIABLE_LOCAL ASIGNACION GETS PARENTESIS_IZQ PARENTESIS_DER','solicitud_datos',5,'p_solicitud_datos','Analizador_Sintactico.py',23),
  ('impresion -> PUTS PARENTESIS_IZQ argumentos PARENTESIS_DER','impresion',4,'p_impresion','Analizador_Sintactico.py',26),
  ('impresion -> PUTS','impresion',1,'p_impresion_sin_argumentos','Analizador_Sintactico.py',29),
  ('comentario -> COMENTARIO argumento','comentario',2,'p_comentario','Analizador_Sintactico.py',32),
  ('array -> CORCHETE_IZQ argumentos CORCHETE_DER','array',3,'p_array','Analizador_Sintactico.py',37),
  ('condicion -> if','condicion',1,'p_condicion','Analizador_Sintactico.py',41),
  ('condicion -> if_else','condicion',1,'p_condicion','Analizador_Sintactico.py',42),
  ('condicion -> if_elsif_else','condicion',1,'p_condicion','Analizador_Sintactico.py',43),
  ('if -> IF expresion instrucciones END_BLOCK','if',4,'p_if','Analizador_Sintactico.py',46),
  ('if -> IF expresion THEN instrucciones END_BLOCK','if',5,'p_if','Analizador_Sintactico.py',47),
  ('if_else -> IF expresion instrucciones ELSE instrucciones END_BLOCK','if_else',6,'p_if_else','Analizador_Sintactico.py',50),
  ('if_else -> IF expresion THEN instrucciones ELSE instrucciones END_BLOCK','if_else',7,'p_if_else','Analizador_Sintactico.py',51),
  ('if_elsif_else -> IF expresion instrucciones elsif_clauses END_BLOCK','if_elsif_else',5,'p_if_elsif_else','Analizador_Sintactico.py',54),
  ('if_elsif_else -> IF expresion THEN instrucciones elsif_clauses END_BLOCK','if_elsif_else',6,'p_if_elsif_else','Analizador_Sintactico.py',55),
  ('if_elsif_else -> IF expresion instrucciones elsif_clauses ELSE instrucciones END_BLOCK','if_elsif_else',7,'p_if_elsif_else','Analizador_Sintactico.py',56),
  ('if_elsif_else -> IF expresion THEN instrucciones elsif_clauses ELSE instrucciones END_BLOCK','if_elsif_else',8,'p_if_elsif_else','Analizador_Sintactico.py',57),
  ('elsif_clauses -> ELSIF expresion instrucciones','elsif_clauses',3,'p_elsif_clauses','Analizador_Sintactico.py',60),
  ('elsif_clauses -> ELSIF expresion THEN instrucciones','elsif_clauses',4,'p_elsif_clauses','Analizador_Sintactico.py',61),
  ('elsif_clauses -> ELSIF expresion instrucciones elsif_clauses','elsif_clauses',4,'p_elsif_clauses','Analizador_Sintactico.py',62),
  ('elsif_clauses -> ELSIF expresion THEN instrucciones elsif_clauses','elsif_clauses',5,'p_elsif_clauses','Analizador_Sintactico.py',63),
  ('funcion -> DEF VARIABLE_LOCAL PARENTESIS_IZQ parametros PARENTESIS_DER instrucciones END_BLOCK','funcion',7,'p_funcion','Analizador_Sintactico.py',67),
  ('parametros -> parametro','parametros',1,'p_parametros','Analizador_Sintactico.py',70),
  ('parametros -> parametro COMA parametros','parametros',3,'p_parametros','Analizador_Sintactico.py',71),
  ('parametro -> VARIABLE_LOCAL','parametro',1,'p_parametro','Analizador_Sintactico.py',74),
  ('parametro -> empty','parametro',1,'p_parametro','Analizador_Sintactico.py',75),
  ('expresion -> var_expresion','expresion',1,'p_expresion','Analizador_Sintactico.py',79),
  ('expresion -> var_expresion comparadores var_expresion','expresion',3,'p_expresion','Analizador_Sintactico.py',80),
  ('expresion -> expresion comparadores expresion','expresion',3,'p_expresion','Analizador_Sintactico.py',81),
  ('expresion -> PARENTESIS_IZQ expresion PARENTESIS_DER','expresion',3,'p_expresion','Analizador_Sintactico.py',82),
  ('expresion -> NOT_BLOCK expresion','expresion',2,'p_expresion','Analizador_Sintactico.py',83),
  ('expresion -> expresion operador_logico expresion','expresion',3,'p_expresion','Analizador_Sintactico.py',84),
  ('comparadores -> MAYOR_QUE','comparadores',1,'p_comparadores','Analizador_Sintactico.py',87),
  ('comparadores -> MENOR_QUE','comparadores',1,'p_comparadores','Analizador_Sintactico.py',88),
  ('comparadores -> IGUAL_IGUAL','comparadores',1,'p_comparadores','Analizador_Sintactico.py',89),
  ('comparadores -> DIFERENTE','comparadores',1,'p_comparadores','Analizador_Sintactico.py',90),
  ('comparadores -> MAYOR_IGUAL','comparadores',1,'p_comparadores','Analizador_Sintactico.py',91),
  ('comparadores -> MENOR_IGUAL','comparadores',1,'p_comparadores','Analizador_Sintactico.py',92),
  ('operador_logico -> AND','operador_logico',1,'p_operador_logico','Analizador_Sintactico.py',95),
  ('operador_logico -> OR','operador_logico',1,'p_operador_logico','Analizador_Sintactico.py',96),
  ('operador_logico -> NOT','operador_logico',1,'p_operador_logico','Analizador_Sintactico.py',97),
  ('var_expresion -> valor','var_expresion',1,'p_var_expresion','Analizador_Sintactico.py',100),
  ('var_expresion -> booleano','var_expresion',1,'p_var_expresion','Analizador_Sintactico.py',101),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','Analizador_Sintactico.py',104),
  ('instrucciones -> instruccion instrucciones','instrucciones',2,'p_instrucciones','Analizador_Sintactico.py',105),
  ('instrucciones -> instruccion PUNTO_Y_COMA instrucciones','instrucciones',3,'p_instrucciones','Analizador_Sintactico.py',106),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion','Analizador_Sintactico.py',109),
  ('instruccion -> impresion','instruccion',1,'p_instruccion','Analizador_Sintactico.py',110),
  ('instruccion -> condicion','instruccion',1,'p_instruccion','Analizador_Sintactico.py',111),
  ('instruccion -> llamada_funcion','instruccion',1,'p_instruccion','Analizador_Sintactico.py',112),
  ('instruccion -> funcion','instruccion',1,'p_instruccion','Analizador_Sintactico.py',113),
  ('llamada_funcion -> VARIABLE_LOCAL PARENTESIS_IZQ argumentos PARENTESIS_DER','llamada_funcion',4,'p_llamada_funcion','Analizador_Sintactico.py',116),
  ('llamada_funcion -> VARIABLE_LOCAL PARENTESIS_IZQ PARENTESIS_DER','llamada_funcion',3,'p_llamada_funcion','Analizador_Sintactico.py',117),
  ('variable -> VARIABLE_LOCAL','variable',1,'p_variable','Analizador_Sintactico.py',121),
  ('variable -> VARIABLE_GLOBAL','variable',1,'p_variable','Analizador_Sintactico.py',122),
  ('variable -> VARIABLE_INSTANCIA','variable',1,'p_variable','Analizador_Sintactico.py',123),
  ('variable -> VARIABLE_CLASE','variable',1,'p_variable','Analizador_Sintactico.py',124),
  ('booleano -> FALSE','booleano',1,'p_booleano','Analizador_Sintactico.py',127),
  ('booleano -> TRUE','booleano',1,'p_booleano','Analizador_Sintactico.py',128),
  ('argumentos -> argumento','argumentos',1,'p_argumentos','Analizador_Sintactico.py',131),
  ('argumentos -> argumento COMA argumentos','argumentos',3,'p_argumentos','Analizador_Sintactico.py',132),
  ('argumento -> booleano','argumento',1,'p_argumento','Analizador_Sintactico.py',135),
  ('argumento -> operacionAritmetica','argumento',1,'p_argumento','Analizador_Sintactico.py',136),
  ('argumento -> array','argumento',1,'p_argumento','Analizador_Sintactico.py',137),
  ('argumento -> empty','argumento',1,'p_argumento','Analizador_Sintactico.py',138),
  ('empty -> <empty>','empty',0,'p_empty','Analizador_Sintactico.py',141),
  ('valores -> operacionAritmetica','valores',1,'p_valores','Analizador_Sintactico.py',144),
  ('valores -> SIMBOLO','valores',1,'p_valores','Analizador_Sintactico.py',145),
  ('valores -> booleano','valores',1,'p_valores','Analizador_Sintactico.py',146),
  ('valores -> array','valores',1,'p_valores','Analizador_Sintactico.py',147),
  ('valor -> NUMERO','valor',1,'p_valor','Analizador_Sintactico.py',150),
  ('valor -> FLOTANTE','valor',1,'p_valor','Analizador_Sintactico.py',151),
  ('valor -> CADENA','valor',1,'p_valor','Analizador_Sintactico.py',152),
  ('valor -> variable','valor',1,'p_valor','Analizador_Sintactico.py',153),
  ('operacionAritmetica -> valor','operacionAritmetica',1,'p_operacionAritmetica','Analizador_Sintactico.py',157),
  ('operacionAritmetica -> valor operador operacionAritmetica','operacionAritmetica',3,'p_operacionAritmetica','Analizador_Sintactico.py',158),
  ('operador -> MAS','operador',1,'p_operador','Analizador_Sintactico.py',162),
  ('operador -> MENOS','operador',1,'p_operador','Analizador_Sintactico.py',163),
  ('operador -> MULTIPLICAR','operador',1,'p_operador','Analizador_Sintactico.py',164),
  ('operador -> DIVIDIR','operador',1,'p_operador','Analizador_Sintactico.py',165),
  ('operador -> MODULO','operador',1,'p_operador','Analizador_Sintactico.py',166),
  ('operador -> EXPONENCIACION','operador',1,'p_operador','Analizador_Sintactico.py',167),
  ('hash -> LLAVE_IZQ pares LLAVE_DER','hash',3,'p_hash','Analizador_Sintactico.py',172),
  ('pares -> par','pares',1,'p_pares','Analizador_Sintactico.py',175),
  ('pares -> par COMA pares','pares',3,'p_pares','Analizador_Sintactico.py',176),
  ('par -> valor FLECHA_HASH valor','par',3,'p_par','Analizador_Sintactico.py',179),
  ('until -> UNTIL expresion DO instrucciones END_BLOCK','until',5,'p_until','Analizador_Sintactico.py',183),
  ('until -> UNTIL expresion instrucciones END_BLOCK','until',4,'p_until','Analizador_Sintactico.py',184),
  ('funcion -> DEF VARIABLE_LOCAL PARENTESIS_IZQ parametros_defecto PARENTESIS_DER instrucciones END_BLOCK','funcion',7,'p_funcion_parametros_defecto','Analizador_Sintactico.py',188),
  ('parametros_defecto -> parametro_defecto','parametros_defecto',1,'p_parametros_defecto','Analizador_Sintactico.py',191),
  ('parametros_defecto -> parametro_defecto COMA parametros_defecto','parametros_defecto',3,'p_parametros_defecto','Analizador_Sintactico.py',192),
  ('parametro_defecto -> VARIABLE_LOCAL','parametro_defecto',1,'p_parametro_defecto','Analizador_Sintactico.py',195),
  ('parametro_defecto -> VARIABLE_LOCAL ASIGNACION valor','parametro_defecto',3,'p_parametro_defecto','Analizador_Sintactico.py',196),
  ('cadena_interpolacion -> CADENA LLAVE_IZQ variable LLAVE_DER','cadena_interpolacion',4,'p_cadena_interpolacion','Analizador_Sintactico.py',200),
  ('incremento -> VARIABLE_LOCAL MAS ASIGNACION expresion','incremento',4,'p_incremento','Analizador_Sintactico.py',203),
]
