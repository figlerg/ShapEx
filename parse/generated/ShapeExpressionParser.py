# Generated from C:/Users/giglerf/Documents/dev/ShapEx/parse/grammar\ShapeExpression.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3&")
        buf.write("\u00e3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\6\3*\n\3\r\3\16\3+\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6X\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7d\n\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\7\7o\n\7\f\7\16\7r\13\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\bz\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\7\b\u0084\n\b\f\b\16\b\u0087\13\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u008e\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u0095\n\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a0")
        buf.write("\n\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00ad\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\r\u00bc\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00cb\n\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u00e1\n")
        buf.write("\21\3\21\2\4\f\16\22\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \2\2\2\u00f0\2\"\3\2\2\2\4)\3\2\2\2\6-\3\2\2\2")
        buf.write("\b\62\3\2\2\2\nW\3\2\2\2\fc\3\2\2\2\16y\3\2\2\2\20\u008d")
        buf.write("\3\2\2\2\22\u008f\3\2\2\2\24\u0098\3\2\2\2\26\u00a3\3")
        buf.write("\2\2\2\30\u00b0\3\2\2\2\32\u00bf\3\2\2\2\34\u00ce\3\2")
        buf.write("\2\2\36\u00d5\3\2\2\2 \u00e0\3\2\2\2\"#\5\16\b\2#$\7\3")
        buf.write("\2\2$%\5\4\3\2%\3\3\2\2\2&*\5\6\4\2\'*\5\b\5\2(*\5\n\6")
        buf.write("\2)&\3\2\2\2)\'\3\2\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2")
        buf.write("+,\3\2\2\2,\5\3\2\2\2-.\7\17\2\2./\7\"\2\2/\60\5\34\17")
        buf.write("\2\60\61\7\4\2\2\61\7\3\2\2\2\62\63\7\20\2\2\63\64\7\"")
        buf.write("\2\2\64\65\5\36\20\2\65\66\7\4\2\2\66\t\3\2\2\2\678\5")
        buf.write("\f\7\289\7\30\2\29:\5\f\7\2:X\3\2\2\2;<\5\f\7\2<=\7\31")
        buf.write("\2\2=>\5\f\7\2>X\3\2\2\2?@\5\f\7\2@A\7\32\2\2AB\5\f\7")
        buf.write("\2BX\3\2\2\2CD\5\f\7\2DE\7\33\2\2EF\5\f\7\2FX\3\2\2\2")
        buf.write("GH\5\f\7\2HI\7\34\2\2IJ\5\f\7\2JX\3\2\2\2KL\5\f\7\2LM")
        buf.write("\7\35\2\2MN\5\f\7\2NX\3\2\2\2OP\5\f\7\2PQ\7\37\2\2QR\7")
        buf.write("\b\2\2RS\5\f\7\2ST\7\36\2\2TU\5\f\7\2UV\7\t\2\2VX\3\2")
        buf.write("\2\2W\67\3\2\2\2W;\3\2\2\2W?\3\2\2\2WC\3\2\2\2WG\3\2\2")
        buf.write("\2WK\3\2\2\2WO\3\2\2\2X\13\3\2\2\2YZ\b\7\1\2Zd\7\"\2\2")
        buf.write("[d\5 \21\2\\]\7\b\2\2]^\5\f\7\2^_\7\t\2\2_d\3\2\2\2`a")
        buf.write("\7\22\2\2ab\7\23\2\2bd\5\f\7\6cY\3\2\2\2c[\3\2\2\2c\\")
        buf.write("\3\2\2\2c`\3\2\2\2dp\3\2\2\2ef\f\5\2\2fg\7\5\2\2go\5\f")
        buf.write("\7\6hi\f\4\2\2ij\7\25\2\2jo\5\f\7\5kl\f\3\2\2lm\7\24\2")
        buf.write("\2mo\5\f\7\4ne\3\2\2\2nh\3\2\2\2nk\3\2\2\2or\3\2\2\2p")
        buf.write("n\3\2\2\2pq\3\2\2\2q\r\3\2\2\2rp\3\2\2\2st\b\b\1\2tz\5")
        buf.write("\20\t\2uv\7\b\2\2vw\5\16\b\2wx\7\t\2\2xz\3\2\2\2ys\3\2")
        buf.write("\2\2yu\3\2\2\2z\u0085\3\2\2\2{|\f\6\2\2|}\7\6\2\2}\u0084")
        buf.write("\5\16\b\7~\177\f\5\2\2\177\u0080\7\7\2\2\u0080\u0084\5")
        buf.write("\16\b\6\u0081\u0082\f\4\2\2\u0082\u0084\7\5\2\2\u0083")
        buf.write("{\3\2\2\2\u0083~\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0087")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\17\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u008e\5\22\n\2\u0089")
        buf.write("\u008e\5\24\13\2\u008a\u008e\5\26\f\2\u008b\u008e\5\30")
        buf.write("\r\2\u008c\u008e\5\32\16\2\u008d\u0088\3\2\2\2\u008d\u0089")
        buf.write("\3\2\2\2\u008d\u008a\3\2\2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\21\3\2\2\2\u008f\u0090\7\n\2\2\u0090")
        buf.write("\u0091\7\b\2\2\u0091\u0094\7\"\2\2\u0092\u0093\7\36\2")
        buf.write("\2\u0093\u0095\7\"\2\2\u0094\u0092\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\7\t\2\2\u0097")
        buf.write("\23\3\2\2\2\u0098\u0099\7\13\2\2\u0099\u009a\7\b\2\2\u009a")
        buf.write("\u009b\7\"\2\2\u009b\u009c\7\36\2\2\u009c\u009f\7\"\2")
        buf.write("\2\u009d\u009e\7\36\2\2\u009e\u00a0\7\"\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\u00a2\7\t\2\2\u00a2\25\3\2\2\2\u00a3\u00a4\7\f\2\2\u00a4")
        buf.write("\u00a5\7\b\2\2\u00a5\u00a6\7\"\2\2\u00a6\u00a7\7\36\2")
        buf.write("\2\u00a7\u00a8\7\"\2\2\u00a8\u00a9\7\36\2\2\u00a9\u00ac")
        buf.write("\7\"\2\2\u00aa\u00ab\7\36\2\2\u00ab\u00ad\7\"\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2")
        buf.write("\u00ae\u00af\7\t\2\2\u00af\27\3\2\2\2\u00b0\u00b1\7\r")
        buf.write("\2\2\u00b1\u00b2\7\b\2\2\u00b2\u00b3\7\"\2\2\u00b3\u00b4")
        buf.write("\7\36\2\2\u00b4\u00b5\7\"\2\2\u00b5\u00b6\7\36\2\2\u00b6")
        buf.write("\u00b7\7\"\2\2\u00b7\u00b8\7\36\2\2\u00b8\u00bb\7\"\2")
        buf.write("\2\u00b9\u00ba\7\36\2\2\u00ba\u00bc\7\"\2\2\u00bb\u00b9")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00be\7\t\2\2\u00be\31\3\2\2\2\u00bf\u00c0\7\16\2\2\u00c0")
        buf.write("\u00c1\7\b\2\2\u00c1\u00c2\7\"\2\2\u00c2\u00c3\7\36\2")
        buf.write("\2\u00c3\u00c4\7\"\2\2\u00c4\u00c5\7\36\2\2\u00c5\u00c6")
        buf.write("\7\"\2\2\u00c6\u00c7\7\36\2\2\u00c7\u00ca\7\"\2\2\u00c8")
        buf.write("\u00c9\7\36\2\2\u00c9\u00cb\7\"\2\2\u00ca\u00c8\3\2\2")
        buf.write("\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd")
        buf.write("\7\t\2\2\u00cd\33\3\2\2\2\u00ce\u00cf\7\37\2\2\u00cf\u00d0")
        buf.write("\7\b\2\2\u00d0\u00d1\5 \21\2\u00d1\u00d2\7\36\2\2\u00d2")
        buf.write("\u00d3\5 \21\2\u00d3\u00d4\7\t\2\2\u00d4\35\3\2\2\2\u00d5")
        buf.write("\u00d6\7\37\2\2\u00d6\u00d7\7\b\2\2\u00d7\u00d8\5 \21")
        buf.write("\2\u00d8\u00d9\7\36\2\2\u00d9\u00da\5 \21\2\u00da\u00db")
        buf.write("\7\t\2\2\u00db\37\3\2\2\2\u00dc\u00e1\7 \2\2\u00dd\u00e1")
        buf.write("\7!\2\2\u00de\u00df\7\24\2\2\u00df\u00e1\5 \21\2\u00e0")
        buf.write("\u00dc\3\2\2\2\u00e0\u00dd\3\2\2\2\u00e0\u00de\3\2\2\2")
        buf.write("\u00e1!\3\2\2\2\22)+Wcnpy\u0083\u0085\u008d\u0094\u009f")
        buf.write("\u00ac\u00bb\u00ca\u00e0")
        return buf.getvalue()


class ShapeExpressionParser ( Parser ):

    grammarFileName = "ShapeExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "';'", "'*'", "'.'", "'join'", 
                     "'('", "')'", "'const'", "'line'", "'exp'", "'sine'", 
                     "'sinc'", "'param'", "'duration'", "'__constraint'", 
                     "'e'", "'**'", "'-'", "'+'", "'['", "']'", "'<='", 
                     "'>='", "'<'", "'>'", "'=='", "'!='", "','", "'in'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CONCAT", "UNION", "LEFTPAREN", "RIGHTPAREN", "CONSTANT", 
                      "LINE", "EXPONENTIAL", "SINE", "SINC", "PARAM", "DURATION", 
                      "CONSTRAINT", "EULER", "EXP", "MINUS", "PLUS", "LSQBRACKET", 
                      "RSQBRACKET", "LEQ", "GEQ", "LESS", "GREATER", "EQ", 
                      "NEQ", "COMMA", "IN", "IntegerLiteral", "RealLiteral", 
                      "Identifier", "LINE_TERMINATOR", "WHITESPACE", "COMMENT", 
                      "LINE_COMMENT" ]

    RULE_shape_expression = 0
    RULE_constraints = 1
    RULE_param_declaration = 2
    RULE_duration_declaration = 3
    RULE_constraint = 4
    RULE_expression = 5
    RULE_regular_expression = 6
    RULE_atomic = 7
    RULE_atomic_constant = 8
    RULE_atomic_line = 9
    RULE_atomic_exponential = 10
    RULE_atomic_sine = 11
    RULE_atomic_sinc = 12
    RULE_interval = 13
    RULE_discrete_interval = 14
    RULE_literal = 15

    ruleNames =  [ "shape_expression", "constraints", "param_declaration", 
                   "duration_declaration", "constraint", "expression", "regular_expression", 
                   "atomic", "atomic_constant", "atomic_line", "atomic_exponential", 
                   "atomic_sine", "atomic_sinc", "interval", "discrete_interval", 
                   "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    CONCAT=4
    UNION=5
    LEFTPAREN=6
    RIGHTPAREN=7
    CONSTANT=8
    LINE=9
    EXPONENTIAL=10
    SINE=11
    SINC=12
    PARAM=13
    DURATION=14
    CONSTRAINT=15
    EULER=16
    EXP=17
    MINUS=18
    PLUS=19
    LSQBRACKET=20
    RSQBRACKET=21
    LEQ=22
    GEQ=23
    LESS=24
    GREATER=25
    EQ=26
    NEQ=27
    COMMA=28
    IN=29
    IntegerLiteral=30
    RealLiteral=31
    Identifier=32
    LINE_TERMINATOR=33
    WHITESPACE=34
    COMMENT=35
    LINE_COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Shape_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def regular_expression(self):
            return self.getTypedRuleContext(ShapeExpressionParser.Regular_expressionContext,0)


        def constraints(self):
            return self.getTypedRuleContext(ShapeExpressionParser.ConstraintsContext,0)


        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_shape_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShape_expression" ):
                return visitor.visitShape_expression(self)
            else:
                return visitor.visitChildren(self)




    def shape_expression(self):

        localctx = ShapeExpressionParser.Shape_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_shape_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.regular_expression(0)
            self.state = 33
            self.match(ShapeExpressionParser.T__0)
            self.state = 34
            self.constraints()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.Param_declarationContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.Param_declarationContext,i)


        def duration_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.Duration_declarationContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.Duration_declarationContext,i)


        def constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.ConstraintContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.ConstraintContext,i)


        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_constraints

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraints" ):
                return visitor.visitConstraints(self)
            else:
                return visitor.visitChildren(self)




    def constraints(self):

        localctx = ShapeExpressionParser.ConstraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_constraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ShapeExpressionParser.PARAM]:
                    self.state = 36
                    self.param_declaration()
                    pass
                elif token in [ShapeExpressionParser.DURATION]:
                    self.state = 37
                    self.duration_declaration()
                    pass
                elif token in [ShapeExpressionParser.LEFTPAREN, ShapeExpressionParser.EULER, ShapeExpressionParser.MINUS, ShapeExpressionParser.IntegerLiteral, ShapeExpressionParser.RealLiteral, ShapeExpressionParser.Identifier]:
                    self.state = 38
                    self.constraint()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ShapeExpressionParser.LEFTPAREN) | (1 << ShapeExpressionParser.PARAM) | (1 << ShapeExpressionParser.DURATION) | (1 << ShapeExpressionParser.EULER) | (1 << ShapeExpressionParser.MINUS) | (1 << ShapeExpressionParser.IntegerLiteral) | (1 << ShapeExpressionParser.RealLiteral) | (1 << ShapeExpressionParser.Identifier))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAM(self):
            return self.getToken(ShapeExpressionParser.PARAM, 0)

        def Identifier(self):
            return self.getToken(ShapeExpressionParser.Identifier, 0)

        def interval(self):
            return self.getTypedRuleContext(ShapeExpressionParser.IntervalContext,0)


        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_param_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_declaration" ):
                return visitor.visitParam_declaration(self)
            else:
                return visitor.visitChildren(self)




    def param_declaration(self):

        localctx = ShapeExpressionParser.Param_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_param_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ShapeExpressionParser.PARAM)
            self.state = 44
            self.match(ShapeExpressionParser.Identifier)
            self.state = 45
            self.interval()
            self.state = 46
            self.match(ShapeExpressionParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Duration_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DURATION(self):
            return self.getToken(ShapeExpressionParser.DURATION, 0)

        def Identifier(self):
            return self.getToken(ShapeExpressionParser.Identifier, 0)

        def discrete_interval(self):
            return self.getTypedRuleContext(ShapeExpressionParser.Discrete_intervalContext,0)


        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_duration_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDuration_declaration" ):
                return visitor.visitDuration_declaration(self)
            else:
                return visitor.visitChildren(self)




    def duration_declaration(self):

        localctx = ShapeExpressionParser.Duration_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_duration_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ShapeExpressionParser.DURATION)
            self.state = 49
            self.match(ShapeExpressionParser.Identifier)
            self.state = 50
            self.discrete_interval()
            self.state = 51
            self.match(ShapeExpressionParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_constraint

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LRA_NeqContext(ConstraintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ConstraintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,i)

        def NEQ(self):
            return self.getToken(ShapeExpressionParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_Neq" ):
                return visitor.visitLRA_Neq(self)
            else:
                return visitor.visitChildren(self)


    class LRA_EqContext(ConstraintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ConstraintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(ShapeExpressionParser.EQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_Eq" ):
                return visitor.visitLRA_Eq(self)
            else:
                return visitor.visitChildren(self)


    class LRA_LEQContext(ConstraintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ConstraintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,i)

        def LEQ(self):
            return self.getToken(ShapeExpressionParser.LEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_LEQ" ):
                return visitor.visitLRA_LEQ(self)
            else:
                return visitor.visitChildren(self)


    class LRA_GEQContext(ConstraintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ConstraintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,i)

        def GEQ(self):
            return self.getToken(ShapeExpressionParser.GEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_GEQ" ):
                return visitor.visitLRA_GEQ(self)
            else:
                return visitor.visitChildren(self)


    class LRA_InContext(ConstraintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ConstraintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,i)

        def IN(self):
            return self.getToken(ShapeExpressionParser.IN, 0)
        def LEFTPAREN(self):
            return self.getToken(ShapeExpressionParser.LEFTPAREN, 0)
        def COMMA(self):
            return self.getToken(ShapeExpressionParser.COMMA, 0)
        def RIGHTPAREN(self):
            return self.getToken(ShapeExpressionParser.RIGHTPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_In" ):
                return visitor.visitLRA_In(self)
            else:
                return visitor.visitChildren(self)


    class LRA_GreaterContext(ConstraintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ConstraintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,i)

        def GREATER(self):
            return self.getToken(ShapeExpressionParser.GREATER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_Greater" ):
                return visitor.visitLRA_Greater(self)
            else:
                return visitor.visitChildren(self)


    class LRA_LessContext(ConstraintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ConstraintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,i)

        def LESS(self):
            return self.getToken(ShapeExpressionParser.LESS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLRA_Less" ):
                return visitor.visitLRA_Less(self)
            else:
                return visitor.visitChildren(self)



    def constraint(self):

        localctx = ShapeExpressionParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constraint)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ShapeExpressionParser.LRA_LEQContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.expression(0)
                self.state = 54
                self.match(ShapeExpressionParser.LEQ)
                self.state = 55
                self.expression(0)
                pass

            elif la_ == 2:
                localctx = ShapeExpressionParser.LRA_GEQContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.expression(0)
                self.state = 58
                self.match(ShapeExpressionParser.GEQ)
                self.state = 59
                self.expression(0)
                pass

            elif la_ == 3:
                localctx = ShapeExpressionParser.LRA_LessContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.expression(0)
                self.state = 62
                self.match(ShapeExpressionParser.LESS)
                self.state = 63
                self.expression(0)
                pass

            elif la_ == 4:
                localctx = ShapeExpressionParser.LRA_GreaterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.expression(0)
                self.state = 66
                self.match(ShapeExpressionParser.GREATER)
                self.state = 67
                self.expression(0)
                pass

            elif la_ == 5:
                localctx = ShapeExpressionParser.LRA_EqContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.expression(0)
                self.state = 70
                self.match(ShapeExpressionParser.EQ)
                self.state = 71
                self.expression(0)
                pass

            elif la_ == 6:
                localctx = ShapeExpressionParser.LRA_NeqContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.expression(0)
                self.state = 74
                self.match(ShapeExpressionParser.NEQ)
                self.state = 75
                self.expression(0)
                pass

            elif la_ == 7:
                localctx = ShapeExpressionParser.LRA_InContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.expression(0)
                self.state = 78
                self.match(ShapeExpressionParser.IN)
                self.state = 79
                self.match(ShapeExpressionParser.LEFTPAREN)
                self.state = 80
                self.expression(0)
                self.state = 81
                self.match(ShapeExpressionParser.COMMA)
                self.state = 82
                self.expression(0)
                self.state = 83
                self.match(ShapeExpressionParser.RIGHTPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExpressionParanthesisContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFTPAREN(self):
            return self.getToken(ShapeExpressionParser.LEFTPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,0)

        def RIGHTPAREN(self):
            return self.getToken(ShapeExpressionParser.RIGHTPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionParanthesis" ):
                return visitor.visitExpressionParanthesis(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionMultiplicationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionMultiplication" ):
                return visitor.visitExpressionMultiplication(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionSubtractionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,i)

        def MINUS(self):
            return self.getToken(ShapeExpressionParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionSubtraction" ):
                return visitor.visitExpressionSubtraction(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionAdditionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(ShapeExpressionParser.PLUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionAddition" ):
                return visitor.visitExpressionAddition(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionVariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ShapeExpressionParser.Identifier, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionVariable" ):
                return visitor.visitExpressionVariable(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionConstantContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(ShapeExpressionParser.LiteralContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionConstant" ):
                return visitor.visitExpressionConstant(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionExponentialContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EULER(self):
            return self.getToken(ShapeExpressionParser.EULER, 0)
        def EXP(self):
            return self.getToken(ShapeExpressionParser.EXP, 0)
        def expression(self):
            return self.getTypedRuleContext(ShapeExpressionParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionExponential" ):
                return visitor.visitExpressionExponential(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ShapeExpressionParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ShapeExpressionParser.Identifier]:
                localctx = ShapeExpressionParser.ExpressionVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 88
                self.match(ShapeExpressionParser.Identifier)
                pass
            elif token in [ShapeExpressionParser.MINUS, ShapeExpressionParser.IntegerLiteral, ShapeExpressionParser.RealLiteral]:
                localctx = ShapeExpressionParser.ExpressionConstantContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                self.literal()
                pass
            elif token in [ShapeExpressionParser.LEFTPAREN]:
                localctx = ShapeExpressionParser.ExpressionParanthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                self.match(ShapeExpressionParser.LEFTPAREN)
                self.state = 91
                self.expression(0)
                self.state = 92
                self.match(ShapeExpressionParser.RIGHTPAREN)
                pass
            elif token in [ShapeExpressionParser.EULER]:
                localctx = ShapeExpressionParser.ExpressionExponentialContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 94
                self.match(ShapeExpressionParser.EULER)
                self.state = 95
                self.match(ShapeExpressionParser.EXP)
                self.state = 96
                self.expression(4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 108
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ShapeExpressionParser.ExpressionMultiplicationContext(self, ShapeExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 99
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 100
                        self.match(ShapeExpressionParser.T__2)
                        self.state = 101
                        self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = ShapeExpressionParser.ExpressionAdditionContext(self, ShapeExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 102
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 103
                        self.match(ShapeExpressionParser.PLUS)
                        self.state = 104
                        self.expression(3)
                        pass

                    elif la_ == 3:
                        localctx = ShapeExpressionParser.ExpressionSubtractionContext(self, ShapeExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 105
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 106
                        self.match(ShapeExpressionParser.MINUS)
                        self.state = 107
                        self.expression(2)
                        pass

             
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Regular_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_regular_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AtomicExpContext(Regular_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.Regular_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomic(self):
            return self.getTypedRuleContext(ShapeExpressionParser.AtomicContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicExp" ):
                return visitor.visitAtomicExp(self)
            else:
                return visitor.visitChildren(self)


    class KleeneExpContext(Regular_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.Regular_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regular_expression(self):
            return self.getTypedRuleContext(ShapeExpressionParser.Regular_expressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKleeneExp" ):
                return visitor.visitKleeneExp(self)
            else:
                return visitor.visitChildren(self)


    class UnionExpContext(Regular_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.Regular_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regular_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.Regular_expressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.Regular_expressionContext,i)

        def UNION(self):
            return self.getToken(ShapeExpressionParser.UNION, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnionExp" ):
                return visitor.visitUnionExp(self)
            else:
                return visitor.visitChildren(self)


    class ParenExpContext(Regular_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.Regular_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFTPAREN(self):
            return self.getToken(ShapeExpressionParser.LEFTPAREN, 0)
        def regular_expression(self):
            return self.getTypedRuleContext(ShapeExpressionParser.Regular_expressionContext,0)

        def RIGHTPAREN(self):
            return self.getToken(ShapeExpressionParser.RIGHTPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExp" ):
                return visitor.visitParenExp(self)
            else:
                return visitor.visitChildren(self)


    class ConcatExpContext(Regular_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.Regular_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def regular_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.Regular_expressionContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.Regular_expressionContext,i)

        def CONCAT(self):
            return self.getToken(ShapeExpressionParser.CONCAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatExp" ):
                return visitor.visitConcatExp(self)
            else:
                return visitor.visitChildren(self)



    def regular_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ShapeExpressionParser.Regular_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_regular_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ShapeExpressionParser.CONSTANT, ShapeExpressionParser.LINE, ShapeExpressionParser.EXPONENTIAL, ShapeExpressionParser.SINE, ShapeExpressionParser.SINC]:
                localctx = ShapeExpressionParser.AtomicExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 114
                self.atomic()
                pass
            elif token in [ShapeExpressionParser.LEFTPAREN]:
                localctx = ShapeExpressionParser.ParenExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(ShapeExpressionParser.LEFTPAREN)
                self.state = 116
                self.regular_expression(0)
                self.state = 117
                self.match(ShapeExpressionParser.RIGHTPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 129
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = ShapeExpressionParser.ConcatExpContext(self, ShapeExpressionParser.Regular_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regular_expression)
                        self.state = 121
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 122
                        self.match(ShapeExpressionParser.CONCAT)
                        self.state = 123
                        self.regular_expression(5)
                        pass

                    elif la_ == 2:
                        localctx = ShapeExpressionParser.UnionExpContext(self, ShapeExpressionParser.Regular_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regular_expression)
                        self.state = 124
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 125
                        self.match(ShapeExpressionParser.UNION)
                        self.state = 126
                        self.regular_expression(4)
                        pass

                    elif la_ == 3:
                        localctx = ShapeExpressionParser.KleeneExpContext(self, ShapeExpressionParser.Regular_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regular_expression)
                        self.state = 127
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 128
                        self.match(ShapeExpressionParser.T__2)
                        pass

             
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_atomic

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AtomicSincExpContext(AtomicContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.AtomicContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomic_sinc(self):
            return self.getTypedRuleContext(ShapeExpressionParser.Atomic_sincContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicSincExp" ):
                return visitor.visitAtomicSincExp(self)
            else:
                return visitor.visitChildren(self)


    class AtomicSineExpContext(AtomicContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.AtomicContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomic_sine(self):
            return self.getTypedRuleContext(ShapeExpressionParser.Atomic_sineContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicSineExp" ):
                return visitor.visitAtomicSineExp(self)
            else:
                return visitor.visitChildren(self)


    class AtomicLineExpContext(AtomicContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.AtomicContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomic_line(self):
            return self.getTypedRuleContext(ShapeExpressionParser.Atomic_lineContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicLineExp" ):
                return visitor.visitAtomicLineExp(self)
            else:
                return visitor.visitChildren(self)


    class AtomicExponentialExpContext(AtomicContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.AtomicContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomic_exponential(self):
            return self.getTypedRuleContext(ShapeExpressionParser.Atomic_exponentialContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicExponentialExp" ):
                return visitor.visitAtomicExponentialExp(self)
            else:
                return visitor.visitChildren(self)


    class AtomicConstExpContext(AtomicContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShapeExpressionParser.AtomicContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomic_constant(self):
            return self.getTypedRuleContext(ShapeExpressionParser.Atomic_constantContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicConstExp" ):
                return visitor.visitAtomicConstExp(self)
            else:
                return visitor.visitChildren(self)



    def atomic(self):

        localctx = ShapeExpressionParser.AtomicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_atomic)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ShapeExpressionParser.CONSTANT]:
                localctx = ShapeExpressionParser.AtomicConstExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.atomic_constant()
                pass
            elif token in [ShapeExpressionParser.LINE]:
                localctx = ShapeExpressionParser.AtomicLineExpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.atomic_line()
                pass
            elif token in [ShapeExpressionParser.EXPONENTIAL]:
                localctx = ShapeExpressionParser.AtomicExponentialExpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.atomic_exponential()
                pass
            elif token in [ShapeExpressionParser.SINE]:
                localctx = ShapeExpressionParser.AtomicSineExpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 137
                self.atomic_sine()
                pass
            elif token in [ShapeExpressionParser.SINC]:
                localctx = ShapeExpressionParser.AtomicSincExpContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 138
                self.atomic_sinc()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_constantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTANT(self):
            return self.getToken(ShapeExpressionParser.CONSTANT, 0)

        def LEFTPAREN(self):
            return self.getToken(ShapeExpressionParser.LEFTPAREN, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(ShapeExpressionParser.Identifier)
            else:
                return self.getToken(ShapeExpressionParser.Identifier, i)

        def RIGHTPAREN(self):
            return self.getToken(ShapeExpressionParser.RIGHTPAREN, 0)

        def COMMA(self):
            return self.getToken(ShapeExpressionParser.COMMA, 0)

        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_atomic_constant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_constant" ):
                return visitor.visitAtomic_constant(self)
            else:
                return visitor.visitChildren(self)




    def atomic_constant(self):

        localctx = ShapeExpressionParser.Atomic_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atomic_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ShapeExpressionParser.CONSTANT)
            self.state = 142
            self.match(ShapeExpressionParser.LEFTPAREN)
            self.state = 143
            self.match(ShapeExpressionParser.Identifier)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ShapeExpressionParser.COMMA:
                self.state = 144
                self.match(ShapeExpressionParser.COMMA)
                self.state = 145
                self.match(ShapeExpressionParser.Identifier)


            self.state = 148
            self.match(ShapeExpressionParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE(self):
            return self.getToken(ShapeExpressionParser.LINE, 0)

        def LEFTPAREN(self):
            return self.getToken(ShapeExpressionParser.LEFTPAREN, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(ShapeExpressionParser.Identifier)
            else:
                return self.getToken(ShapeExpressionParser.Identifier, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ShapeExpressionParser.COMMA)
            else:
                return self.getToken(ShapeExpressionParser.COMMA, i)

        def RIGHTPAREN(self):
            return self.getToken(ShapeExpressionParser.RIGHTPAREN, 0)

        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_atomic_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_line" ):
                return visitor.visitAtomic_line(self)
            else:
                return visitor.visitChildren(self)




    def atomic_line(self):

        localctx = ShapeExpressionParser.Atomic_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atomic_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(ShapeExpressionParser.LINE)
            self.state = 151
            self.match(ShapeExpressionParser.LEFTPAREN)
            self.state = 152
            self.match(ShapeExpressionParser.Identifier)
            self.state = 153
            self.match(ShapeExpressionParser.COMMA)
            self.state = 154
            self.match(ShapeExpressionParser.Identifier)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ShapeExpressionParser.COMMA:
                self.state = 155
                self.match(ShapeExpressionParser.COMMA)
                self.state = 156
                self.match(ShapeExpressionParser.Identifier)


            self.state = 159
            self.match(ShapeExpressionParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_exponentialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPONENTIAL(self):
            return self.getToken(ShapeExpressionParser.EXPONENTIAL, 0)

        def LEFTPAREN(self):
            return self.getToken(ShapeExpressionParser.LEFTPAREN, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(ShapeExpressionParser.Identifier)
            else:
                return self.getToken(ShapeExpressionParser.Identifier, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ShapeExpressionParser.COMMA)
            else:
                return self.getToken(ShapeExpressionParser.COMMA, i)

        def RIGHTPAREN(self):
            return self.getToken(ShapeExpressionParser.RIGHTPAREN, 0)

        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_atomic_exponential

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_exponential" ):
                return visitor.visitAtomic_exponential(self)
            else:
                return visitor.visitChildren(self)




    def atomic_exponential(self):

        localctx = ShapeExpressionParser.Atomic_exponentialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atomic_exponential)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ShapeExpressionParser.EXPONENTIAL)
            self.state = 162
            self.match(ShapeExpressionParser.LEFTPAREN)
            self.state = 163
            self.match(ShapeExpressionParser.Identifier)
            self.state = 164
            self.match(ShapeExpressionParser.COMMA)
            self.state = 165
            self.match(ShapeExpressionParser.Identifier)
            self.state = 166
            self.match(ShapeExpressionParser.COMMA)
            self.state = 167
            self.match(ShapeExpressionParser.Identifier)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ShapeExpressionParser.COMMA:
                self.state = 168
                self.match(ShapeExpressionParser.COMMA)
                self.state = 169
                self.match(ShapeExpressionParser.Identifier)


            self.state = 172
            self.match(ShapeExpressionParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_sineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINE(self):
            return self.getToken(ShapeExpressionParser.SINE, 0)

        def LEFTPAREN(self):
            return self.getToken(ShapeExpressionParser.LEFTPAREN, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(ShapeExpressionParser.Identifier)
            else:
                return self.getToken(ShapeExpressionParser.Identifier, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ShapeExpressionParser.COMMA)
            else:
                return self.getToken(ShapeExpressionParser.COMMA, i)

        def RIGHTPAREN(self):
            return self.getToken(ShapeExpressionParser.RIGHTPAREN, 0)

        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_atomic_sine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_sine" ):
                return visitor.visitAtomic_sine(self)
            else:
                return visitor.visitChildren(self)




    def atomic_sine(self):

        localctx = ShapeExpressionParser.Atomic_sineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_atomic_sine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(ShapeExpressionParser.SINE)
            self.state = 175
            self.match(ShapeExpressionParser.LEFTPAREN)
            self.state = 176
            self.match(ShapeExpressionParser.Identifier)
            self.state = 177
            self.match(ShapeExpressionParser.COMMA)
            self.state = 178
            self.match(ShapeExpressionParser.Identifier)
            self.state = 179
            self.match(ShapeExpressionParser.COMMA)
            self.state = 180
            self.match(ShapeExpressionParser.Identifier)
            self.state = 181
            self.match(ShapeExpressionParser.COMMA)
            self.state = 182
            self.match(ShapeExpressionParser.Identifier)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ShapeExpressionParser.COMMA:
                self.state = 183
                self.match(ShapeExpressionParser.COMMA)
                self.state = 184
                self.match(ShapeExpressionParser.Identifier)


            self.state = 187
            self.match(ShapeExpressionParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_sincContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINC(self):
            return self.getToken(ShapeExpressionParser.SINC, 0)

        def LEFTPAREN(self):
            return self.getToken(ShapeExpressionParser.LEFTPAREN, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(ShapeExpressionParser.Identifier)
            else:
                return self.getToken(ShapeExpressionParser.Identifier, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ShapeExpressionParser.COMMA)
            else:
                return self.getToken(ShapeExpressionParser.COMMA, i)

        def RIGHTPAREN(self):
            return self.getToken(ShapeExpressionParser.RIGHTPAREN, 0)

        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_atomic_sinc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_sinc" ):
                return visitor.visitAtomic_sinc(self)
            else:
                return visitor.visitChildren(self)




    def atomic_sinc(self):

        localctx = ShapeExpressionParser.Atomic_sincContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_atomic_sinc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(ShapeExpressionParser.SINC)
            self.state = 190
            self.match(ShapeExpressionParser.LEFTPAREN)
            self.state = 191
            self.match(ShapeExpressionParser.Identifier)
            self.state = 192
            self.match(ShapeExpressionParser.COMMA)
            self.state = 193
            self.match(ShapeExpressionParser.Identifier)
            self.state = 194
            self.match(ShapeExpressionParser.COMMA)
            self.state = 195
            self.match(ShapeExpressionParser.Identifier)
            self.state = 196
            self.match(ShapeExpressionParser.COMMA)
            self.state = 197
            self.match(ShapeExpressionParser.Identifier)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ShapeExpressionParser.COMMA:
                self.state = 198
                self.match(ShapeExpressionParser.COMMA)
                self.state = 199
                self.match(ShapeExpressionParser.Identifier)


            self.state = 202
            self.match(ShapeExpressionParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(ShapeExpressionParser.IN, 0)

        def LEFTPAREN(self):
            return self.getToken(ShapeExpressionParser.LEFTPAREN, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.LiteralContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.LiteralContext,i)


        def COMMA(self):
            return self.getToken(ShapeExpressionParser.COMMA, 0)

        def RIGHTPAREN(self):
            return self.getToken(ShapeExpressionParser.RIGHTPAREN, 0)

        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_interval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterval" ):
                return visitor.visitInterval(self)
            else:
                return visitor.visitChildren(self)




    def interval(self):

        localctx = ShapeExpressionParser.IntervalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_interval)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ShapeExpressionParser.IN)
            self.state = 205
            self.match(ShapeExpressionParser.LEFTPAREN)
            self.state = 206
            self.literal()
            self.state = 207
            self.match(ShapeExpressionParser.COMMA)
            self.state = 208
            self.literal()
            self.state = 209
            self.match(ShapeExpressionParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Discrete_intervalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(ShapeExpressionParser.IN, 0)

        def LEFTPAREN(self):
            return self.getToken(ShapeExpressionParser.LEFTPAREN, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShapeExpressionParser.LiteralContext)
            else:
                return self.getTypedRuleContext(ShapeExpressionParser.LiteralContext,i)


        def COMMA(self):
            return self.getToken(ShapeExpressionParser.COMMA, 0)

        def RIGHTPAREN(self):
            return self.getToken(ShapeExpressionParser.RIGHTPAREN, 0)

        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_discrete_interval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiscrete_interval" ):
                return visitor.visitDiscrete_interval(self)
            else:
                return visitor.visitChildren(self)




    def discrete_interval(self):

        localctx = ShapeExpressionParser.Discrete_intervalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_discrete_interval)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(ShapeExpressionParser.IN)
            self.state = 212
            self.match(ShapeExpressionParser.LEFTPAREN)
            self.state = 213
            self.literal()
            self.state = 214
            self.match(ShapeExpressionParser.COMMA)
            self.state = 215
            self.literal()
            self.state = 216
            self.match(ShapeExpressionParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(ShapeExpressionParser.IntegerLiteral, 0)

        def RealLiteral(self):
            return self.getToken(ShapeExpressionParser.RealLiteral, 0)

        def MINUS(self):
            return self.getToken(ShapeExpressionParser.MINUS, 0)

        def literal(self):
            return self.getTypedRuleContext(ShapeExpressionParser.LiteralContext,0)


        def getRuleIndex(self):
            return ShapeExpressionParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ShapeExpressionParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_literal)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ShapeExpressionParser.IntegerLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(ShapeExpressionParser.IntegerLiteral)
                pass
            elif token in [ShapeExpressionParser.RealLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(ShapeExpressionParser.RealLiteral)
                pass
            elif token in [ShapeExpressionParser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(ShapeExpressionParser.MINUS)
                self.state = 221
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expression_sempred
        self._predicates[6] = self.regular_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def regular_expression_sempred(self, localctx:Regular_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




