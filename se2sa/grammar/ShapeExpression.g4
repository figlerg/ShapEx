grammar ShapeExpression;
// TODO import anyHR grammar here?

shape_expression:
     (param_declaration | duration_declaration | relation | relation_string) + expression ';'
     ;

param_declaration:
//    PARAM ID  (interval | '=' Number)? ';' // TODO might be worth implementing to support 'param a = 3;'
    PARAM ID  interval? ';'
    ;

duration_declaration:
    DURATION ID discrete_interval? ';'
    ;

// TODO relations are cumbersome, should support "<" ">" and "=="
relation:
    summand+ COMP_OP number ';'
    ; // this addition has been made for the relational parameter definitions (-Felix)
    // TODO create checks for missing number; should I also make two signs (e.g. '--' illegal for clarity?)

relation_string:
    // TODO this should be harmonised with anyHR grammar
    CONSTRAINT scalar (COMP_OP scalar)+ ';'
//    NONLIN STRING ';'
    ;

//  for user specified non-linear relations we need different relations (simply strings) to be evalued via eval
scalar:
    scalar (( '+' | '-' | '*' | '^' | '**') scalar)+
    | ID
    | number
    | '(' scalar ')'
    | 'abs(' scalar ')' // added for usability. No visitor necessary if I use eval
    | EXPONENTIAL '(' scalar ')'
;

expression:
    atomic                                  #AtomicExp
    |   expression CONCAT expression        #ConcatExp
    |   expression UNION expression         #UnionExp
    |   expression '*'                      #KleeneExp
    |   LEFTPAREN expression RIGHTPAREN     #ParenExp
    ;

atomic:
    atomic_constant                         #AtomicConstExp
    | atomic_line                           #AtomicLineExp
    | atomic_exponential                    #AtomicExponentialExp
    | atomic_sine                           #AtomicSineExp
    | atomic_sinc                           #AtomicSincExp
    ;


atomic_constant:
    CONSTANT LEFTPAREN ID (',' ID)? RIGHTPAREN
    ;

atomic_line:
    LINE LEFTPAREN ID ',' ID (',' ID)? RIGHTPAREN
    ;

atomic_exponential:
    EXPONENTIAL LEFTPAREN ID ',' ID ',' ID (',' ID)? RIGHTPAREN
    ;

atomic_sine:
    SINE LEFTPAREN ID ',' ID ',' ID ',' ID (',' ID)? RIGHTPAREN
    ;

atomic_sinc:
    SINC LEFTPAREN ID ',' ID ',' ID ',' ID (',' ID)? RIGHTPAREN
    ;

summand:
    (SIGN? number? '*'? ID)
    ;

interval:
    'in' '[' number ',' number ']'
    ;

discrete_interval:
    'in' '[' (INT|DOUBLE) ',' (INT|DOUBLE) ']'
    ;

number:
    SIGN? (DOUBLE | INT)
    ;

DOUBLE:
    SIGN? [0-9]+ '.' [0-9]+
    ;

INT: SIGN? [0-9]+;

SIGN: ('-' | '+');

//INEQ: '<=' | '>=';
// TODO think about equality as well, this would definitely extend useability.
//  This might be difficult but possible with some linear algebra (eg transforming to the subspace that is the slice where equality holds?)

COMP_OP: '<' | '>' | '==' | '>=' | '<=' | '!=';

CONCAT: '.';
UNION: 'join';
//KLEENE: '*'; // using * elsewhere... KLEENE would shadow this

LEFTPAREN: '(';
RIGHTPAREN: ')';

CONSTANT: 'const';
LINE: 'line';
EXPONENTIAL: 'exp';
SINE: 'sine';
SINC: 'sinc';
PARAM: 'param';
DURATION: 'duration';
CONSTRAINT: 'constraint';

STRING : '"' .*? '"' ;
ID: [a-zA-Z]+[0-9]*; // for relations it is necessary to enforce that no ID starts with a number
WS: [ \t\r] -> skip;
LINE_TERMINATOR: [\n] -> skip;

LINE_COMMENT
    : '#' ~[\r\n]* -> skip
;