grammar MiniLang;

program : (statement NEWLINE)* EOF ;

statement : assign | print | fromStmt ;

assign : ID '=' expr ;

print : 'print' '(' expr ')' ;

fromStmt : 'from' ID 'import' ID ;

expr : expr op=('*'|'/') expr
     | expr op=('+'|'-') expr
     | INT | ID
     | '(' expr ')' ;

ID : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
NEWLINE : [\r\n]+ ;
WS : [ \t]+ -> skip ;
