%{
    /* vamos a necesitar declarar la funcion math.h
    para posteriormente llamar a la funcion atof()*/
    #include <math.h>
%}

DIGIT [0-9]
ID    [a-z][a-z0-0]*

%%

{DIGIT}+ {printf("Un entero: %s (%d)\n", yytext, atoi( yytext) );}

{DIGIT}"."{DIGIT}* {printf("Un flotante: %s (%g)\n", yytext, atof( yytext ));}

if|then|begin|end|procedure|function {printf("Una palabra clave: %s\n", yytext);}

{ID} printf("Un identificador: %s\n", yytext);

"+"|"-"|"*"|"/" printf("Un operador: %s\n", yytext);

"{"[^{}\n]*"}" /*eat up one-line comments*/

[\t\n]+ /*eat up whitespace*/

. printf("Caracter no reconocido: %s\n", yytext);

%%

int main( int argc, char **argv){
  ++argv, --argc; /*skip over program name*/
  if (argc > 0)
    yyin = fopen(argv[0], "r");
  else  
  
  yyin = stdin;
  yylex();
}