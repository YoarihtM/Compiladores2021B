%option noyywrap

%{
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include "tablaSimbolos.h"
    #include "parser.tab.h"
    //extern FILE *yyin;
    //extern FILE *yyout;

    int numeroLinea = 1;
    void ret_print(char *token_type);
    void yyerror();

%}

%x ML_COMMENT

letra [a-zA-Z]
numero [0-9]
alfanum {letra}|{numero}
print [ .~]

ID {letra}+{alfanum}*
ICONST "0"|[0-9]{numero}*
FCONST "0"|{numero}*"."{numero}+
CCONST (\'{print}\')|(\'\\[nftrbv]\')
STRING \"{print}*\"

%%

"//".*                  { printf("Comentario de una sola linea %d\n", numeroLinea); }
"/*"                    { printf("Comentario de varias lineas iniciando en %d\n", numeroLinea); BEGIN(ML_COMMENT); }
<ML_COMMENT>"*/"        { printf("Comentario de varias lineas termina en %d\n", numeroLinea); BEGIN(INITIAL); }
<ML_COMMENT>[^*\n]+ 
<ML_COMMENT>"*"
<ML_COMMENT>"\N"        { numeroLinea += 1; }

"char"|"CHAR"           { return CHAR; }
"int"|"INT"             { return INT; }
"float"|"FLOAT"         { return FLOAT; }
"double"|"DOUBLE"       { return DOUBLE; }
"if"|"IF"               { return IF; }
"else"|"ELSE"           { return ELSE; }
"while"|"WHILE"         { return WHILE; }
"for"|"FOR"             { return FOR; }
"continue"|"CONTINUE"   { return CONTINUE; }
"break"|"BREAK"         { return BREAK; }
"void"|"VOID"           { return VOID; }
"return"|"RETURN"       { return RETURN; }

"+"|"-"                 { return OPSUMA; }
"*"                     { return OPMULTIP; }
"/"                     { return OPDIV; }
"++"|"--"               { return OPINCREM; }
"&&"                    { return OPAND; }
"||"                    { return OPOR; }
"!"                     { return OPNEG; }
"=="|"!="               { return OPIGUAL; }
">"|"<"|">="|"<="       { return OPDESIGUALDAD; }

"("                     { return PRNTS_IZQ; }
")"                     { return PRNTS_DER; }
"["                     { return CRCHT_IZQ; }
"]"                     { return CRCHT_DER; }
"{"                     { return LLAVE_IZQ; }
"}"                     { return LLAVE_DER; }
";"                     { return PCOMA; }
","                     { return COMA; }
"="                     { return ASIGNAR; }
"&"                     { return REFER;}

{ID}                    {

                            //insertamos el identificador en la tabla de tablaSimbolos
                            insert(yytext, strlen(yytext), UNDEF, numeroLinea);
                            return ID;

                        }
{ICONST}                { return ICONST; }
{FCONST}                { return FCONST; }
{CCONST}                { return CCONST; }
{STRING}                { return STRING; }

"\n"                    { numeroLinea += 1; }
[ \t\r\f]+              /* Comerse el espacio en blanco */

.                       { yyerror("Caracter no reconocido!"); }

%%