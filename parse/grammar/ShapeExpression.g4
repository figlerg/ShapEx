grammar ShapeExpression;


// full __expression
shape_expression:
//     (param_declaration | duration_declaration | relation | relation_string) + regular_expression ';'
     regular_expression ':' constraints
     ;

// constraints and subrules
constraints:
    (param_declaration | duration_declaration | constraint) +
    ;

param_declaration:
//    PARAM ID  (interval | '=' Number)? ';' // TODO might be worth implementing to support 'param a = 3;'
//    PARAM Identifier  interval? ';'
    PARAM Identifier  interval ';'
    ;

duration_declaration:
//    DURATION Identifier discrete_interval? ';'
    DURATION Identifier discrete_interval ';'
    ;

//TODO should I add keyword?
constraint:
    expression LEQ expression                                           #LRA_LEQ
    | expression GEQ expression                                         #LRA_GEQ
    | expression LESS expression                                        #LRA_Less
    | expression GREATER expression                                     #LRA_Greater
    | expression EQ expression                                          #LRA_Eq
    | expression NEQ expression                                         #LRA_Neq
    | expression IN LEFTPAREN expression COMMA expression RIGHTPAREN    #LRA_In
    ;

expression
	:
	Identifier                                                          #ExpressionVariable
	| literal                                                           #ExpressionConstant
	| LEFTPAREN expression RIGHTPAREN                                   #ExpressionParanthesis
	| EULER EXP expression                                              #ExpressionExponential
    | expression '*' expression                                         #ExpressionMultiplication
	| expression PLUS expression                                        #ExpressionAddition
	| expression MINUS expression                                       #ExpressionSubtraction
    ;


// regular __expression and subrules

regular_expression:
    atomic                                                  #AtomicExp
    |   regular_expression CONCAT regular_expression        #ConcatExp
    |   regular_expression UNION regular_expression         #UnionExp
    |   regular_expression '*'                              #KleeneExp
    |   LEFTPAREN regular_expression RIGHTPAREN             #ParenExp
    ;

atomic:
    atomic_constant                         #AtomicConstExp
    | atomic_line                           #AtomicLineExp
    | atomic_exponential                    #AtomicExponentialExp
    | atomic_sine                           #AtomicSineExp
    | atomic_sinc                           #AtomicSincExp
    ;


atomic_constant:
    CONSTANT LEFTPAREN Identifier (COMMA Identifier)? RIGHTPAREN
    ;

atomic_line:
    LINE LEFTPAREN Identifier COMMA Identifier (COMMA Identifier)? RIGHTPAREN
    ;

atomic_exponential:
    EXPONENTIAL LEFTPAREN Identifier COMMA Identifier COMMA Identifier (COMMA Identifier)? RIGHTPAREN
    ;

atomic_sine:
    SINE LEFTPAREN Identifier COMMA Identifier COMMA Identifier COMMA Identifier (COMMA Identifier)? RIGHTPAREN
    ;

atomic_sinc:
    SINC LEFTPAREN Identifier COMMA Identifier COMMA Identifier COMMA Identifier (COMMA Identifier)? RIGHTPAREN
    ;


interval:
    IN '(' literal COMMA literal ')'
    ;

discrete_interval:
    IN '(' literal COMMA literal ')'
    ;


literal
	: IntegerLiteral
	| RealLiteral
	| MINUS literal
	;


// basic building blocks

// for regular __expression phi (from original shapex grammar)
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
CONSTRAINT: '__constraint';






// for constraints, numbers etc
EULER
    : 'e' ;

EXP
    : '**' ;

MINUS
    : '-' ;

PLUS
    : '+' ;

//TIMES
//    : '*' ;

//LPAREN
//	: '(' ;
//
//RPAREN
//	: ')' ;

LSQBRACKET
    : '[' ;

RSQBRACKET
    : ']' ;

LEQ
    : '<=' ;

GEQ
    : '>=' ;

LESS
    : '<' ;

GREATER
    : '>' ;

EQ
    : '==' ;

NEQ
    : '!=' ;


COMMA
    : ',' ;

IN
    : 'in' ;



IntegerLiteral
	: DecimalNumeral
	| HexNumeral
	| BinaryNumeral ;

fragment DecimalNumeral
	: '0'
	| NonZeroDigit (Digits? | Underscores Digits) ;

fragment Digits
	: Digit (DigitsAndUnderscores? Digit)? ;

fragment Digit
	: '0'
	| NonZeroDigit ;

fragment NonZeroDigit
	: [1-9] ;

fragment DigitsAndUnderscores
	: DigitOrUnderscore+ ;

fragment DigitOrUnderscore
	: Digit
	| '_' ;

fragment Underscores
	: '_'+ ;

fragment HexNumeral
	: '0' [xX] HexDigits ;

fragment HexDigits
	: HexDigit (HexDigitsAndUnderscores? HexDigit)? ;

fragment HexDigit
	: [0-9a-fA-F] ;

fragment HexDigitsAndUnderscores
	: HexDigitOrUnderscore+ ;

fragment HexDigitOrUnderscore
	: HexDigit
	| '_' ;

fragment BinaryNumeral
	: '0' [bB] BinaryDigits ;

fragment BinaryDigits
	: BinaryDigit (BinaryDigitsAndUnderscores? BinaryDigit)? ;

fragment BinaryDigit
	: [01] ;

fragment BinaryDigitsAndUnderscores
	: BinaryDigitOrUnderscore+ ;


fragment BinaryDigitOrUnderscore
	: BinaryDigit
	| '_' ;

RealLiteral
	: DecimalRealLiteral ;

fragment DecimalRealLiteral
	: Digits '.' Digits? ExponentPart?
	| '.' Digits ExponentPart?
	| Digits ExponentPart
	;

fragment ExponentPart
	: ExponentIndicator SignedInteger ;

fragment ExponentIndicator
	: [eE] ;

fragment SignedInteger
	: Sign? Digit+ ;

fragment Sign
	: [+-] ;


Identifier
	: ((IdentifierStart)(IdentifierPart)*) ;


fragment IdentifierStart
	: (LetterOrUnderscore | '$') ;

fragment IdentifierPart
	: ( IdentifierStart | Digit | '.' | '/' ) ;

fragment LetterOrUnderscore
	: (Letter | '_') ;

fragment Letter
	: [A-Za-z] ;


// Whitespace and comments
//
LINE_TERMINATOR
	: [\n] -> skip ;

WHITESPACE
	: [ \t\r\u000C]+ -> skip ;

COMMENT
	: '/*' .*? '*/' -> skip ;

LINE_COMMENT
    : '#' ~[\r\n]* -> skip
;
