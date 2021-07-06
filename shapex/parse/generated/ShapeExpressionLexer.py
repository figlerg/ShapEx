# Generated from C:/Users/giglerf/Documents/dev/dev_code/ShapEx/shapex/parse/grammar\ShapeExpression.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2&")
        buf.write("\u019c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\5\37\u00ed")
        buf.write("\n\37\3 \3 \3 \5 \u00f2\n \3 \3 \3 \5 \u00f7\n \5 \u00f9")
        buf.write("\n \3!\3!\5!\u00fd\n!\3!\5!\u0100\n!\3\"\3\"\5\"\u0104")
        buf.write("\n\"\3#\3#\3$\6$\u0109\n$\r$\16$\u010a\3%\3%\5%\u010f")
        buf.write("\n%\3&\6&\u0112\n&\r&\16&\u0113\3\'\3\'\3\'\3\'\3(\3(")
        buf.write("\5(\u011c\n(\3(\5(\u011f\n(\3)\3)\3*\6*\u0124\n*\r*\16")
        buf.write("*\u0125\3+\3+\5+\u012a\n+\3,\3,\3,\3,\3-\3-\5-\u0132\n")
        buf.write("-\3-\5-\u0135\n-\3.\3.\3/\6/\u013a\n/\r/\16/\u013b\3\60")
        buf.write("\3\60\5\60\u0140\n\60\3\61\3\61\3\62\3\62\3\62\5\62\u0147")
        buf.write("\n\62\3\62\5\62\u014a\n\62\3\62\3\62\3\62\5\62\u014f\n")
        buf.write("\62\3\62\3\62\3\62\5\62\u0154\n\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\65\5\65\u015c\n\65\3\65\6\65\u015f\n\65\r\65\16")
        buf.write("\65\u0160\3\66\3\66\3\67\3\67\7\67\u0167\n\67\f\67\16")
        buf.write("\67\u016a\13\67\38\38\58\u016e\n8\39\39\39\59\u0173\n")
        buf.write("9\3:\3:\5:\u0177\n:\3;\3;\3<\3<\3<\3<\3=\6=\u0180\n=\r")
        buf.write("=\16=\u0181\3=\3=\3>\3>\3>\3>\7>\u018a\n>\f>\16>\u018d")
        buf.write("\13>\3>\3>\3>\3>\3>\3?\3?\7?\u0196\n?\f?\16?\u0199\13")
        buf.write("?\3?\3?\3\u018b\2@\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?\2A\2C\2E\2G\2I\2K\2M\2O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a!")
        buf.write("c\2e\2g\2i\2k\2m\"o\2q\2s\2u\2w#y${%}&\3\2\r\3\2\63;\4")
        buf.write("\2ZZzz\5\2\62;CHch\4\2DDdd\3\2\62\63\4\2GGgg\4\2--//\4")
        buf.write("\2C\\c|\3\2\f\f\5\2\13\13\16\17\"\"\4\2\f\f\17\17\2\u01a3")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2a\3\2\2\2\2")
        buf.write("m\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\3\177\3\2\2\2\5\u0081\3\2\2\2\7\u0083\3\2\2\2\t\u0085")
        buf.write("\3\2\2\2\13\u0087\3\2\2\2\r\u008c\3\2\2\2\17\u008e\3\2")
        buf.write("\2\2\21\u0090\3\2\2\2\23\u0096\3\2\2\2\25\u009b\3\2\2")
        buf.write("\2\27\u009f\3\2\2\2\31\u00a4\3\2\2\2\33\u00a9\3\2\2\2")
        buf.write("\35\u00af\3\2\2\2\37\u00b8\3\2\2\2!\u00c3\3\2\2\2#\u00c9")
        buf.write("\3\2\2\2%\u00cc\3\2\2\2\'\u00ce\3\2\2\2)\u00d0\3\2\2\2")
        buf.write("+\u00d2\3\2\2\2-\u00d4\3\2\2\2/\u00d7\3\2\2\2\61\u00da")
        buf.write("\3\2\2\2\63\u00dc\3\2\2\2\65\u00de\3\2\2\2\67\u00e1\3")
        buf.write("\2\2\29\u00e4\3\2\2\2;\u00e6\3\2\2\2=\u00ec\3\2\2\2?\u00f8")
        buf.write("\3\2\2\2A\u00fa\3\2\2\2C\u0103\3\2\2\2E\u0105\3\2\2\2")
        buf.write("G\u0108\3\2\2\2I\u010e\3\2\2\2K\u0111\3\2\2\2M\u0115\3")
        buf.write("\2\2\2O\u0119\3\2\2\2Q\u0120\3\2\2\2S\u0123\3\2\2\2U\u0129")
        buf.write("\3\2\2\2W\u012b\3\2\2\2Y\u012f\3\2\2\2[\u0136\3\2\2\2")
        buf.write("]\u0139\3\2\2\2_\u013f\3\2\2\2a\u0141\3\2\2\2c\u0153\3")
        buf.write("\2\2\2e\u0155\3\2\2\2g\u0158\3\2\2\2i\u015b\3\2\2\2k\u0162")
        buf.write("\3\2\2\2m\u0164\3\2\2\2o\u016d\3\2\2\2q\u0172\3\2\2\2")
        buf.write("s\u0176\3\2\2\2u\u0178\3\2\2\2w\u017a\3\2\2\2y\u017f\3")
        buf.write("\2\2\2{\u0185\3\2\2\2}\u0193\3\2\2\2\177\u0080\7<\2\2")
        buf.write("\u0080\4\3\2\2\2\u0081\u0082\7=\2\2\u0082\6\3\2\2\2\u0083")
        buf.write("\u0084\7,\2\2\u0084\b\3\2\2\2\u0085\u0086\7\60\2\2\u0086")
        buf.write("\n\3\2\2\2\u0087\u0088\7l\2\2\u0088\u0089\7q\2\2\u0089")
        buf.write("\u008a\7k\2\2\u008a\u008b\7p\2\2\u008b\f\3\2\2\2\u008c")
        buf.write("\u008d\7*\2\2\u008d\16\3\2\2\2\u008e\u008f\7+\2\2\u008f")
        buf.write("\20\3\2\2\2\u0090\u0091\7e\2\2\u0091\u0092\7q\2\2\u0092")
        buf.write("\u0093\7p\2\2\u0093\u0094\7u\2\2\u0094\u0095\7v\2\2\u0095")
        buf.write("\22\3\2\2\2\u0096\u0097\7n\2\2\u0097\u0098\7k\2\2\u0098")
        buf.write("\u0099\7p\2\2\u0099\u009a\7g\2\2\u009a\24\3\2\2\2\u009b")
        buf.write("\u009c\7g\2\2\u009c\u009d\7z\2\2\u009d\u009e\7r\2\2\u009e")
        buf.write("\26\3\2\2\2\u009f\u00a0\7u\2\2\u00a0\u00a1\7k\2\2\u00a1")
        buf.write("\u00a2\7p\2\2\u00a2\u00a3\7g\2\2\u00a3\30\3\2\2\2\u00a4")
        buf.write("\u00a5\7u\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7p\2\2\u00a7")
        buf.write("\u00a8\7e\2\2\u00a8\32\3\2\2\2\u00a9\u00aa\7r\2\2\u00aa")
        buf.write("\u00ab\7c\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7c\2\2\u00ad")
        buf.write("\u00ae\7o\2\2\u00ae\34\3\2\2\2\u00af\u00b0\7f\2\2\u00b0")
        buf.write("\u00b1\7w\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3\7c\2\2\u00b3")
        buf.write("\u00b4\7v\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7q\2\2\u00b6")
        buf.write("\u00b7\7p\2\2\u00b7\36\3\2\2\2\u00b8\u00b9\7e\2\2\u00b9")
        buf.write("\u00ba\7q\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc\7u\2\2\u00bc")
        buf.write("\u00bd\7v\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7c\2\2\u00bf")
        buf.write("\u00c0\7k\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7v\2\2\u00c2")
        buf.write(" \3\2\2\2\u00c3\u00c4\7G\2\2\u00c4\u00c5\7W\2\2\u00c5")
        buf.write("\u00c6\7N\2\2\u00c6\u00c7\7G\2\2\u00c7\u00c8\7T\2\2\u00c8")
        buf.write("\"\3\2\2\2\u00c9\u00ca\7,\2\2\u00ca\u00cb\7,\2\2\u00cb")
        buf.write("$\3\2\2\2\u00cc\u00cd\7/\2\2\u00cd&\3\2\2\2\u00ce\u00cf")
        buf.write("\7-\2\2\u00cf(\3\2\2\2\u00d0\u00d1\7]\2\2\u00d1*\3\2\2")
        buf.write("\2\u00d2\u00d3\7_\2\2\u00d3,\3\2\2\2\u00d4\u00d5\7>\2")
        buf.write("\2\u00d5\u00d6\7?\2\2\u00d6.\3\2\2\2\u00d7\u00d8\7@\2")
        buf.write("\2\u00d8\u00d9\7?\2\2\u00d9\60\3\2\2\2\u00da\u00db\7>")
        buf.write("\2\2\u00db\62\3\2\2\2\u00dc\u00dd\7@\2\2\u00dd\64\3\2")
        buf.write("\2\2\u00de\u00df\7?\2\2\u00df\u00e0\7?\2\2\u00e0\66\3")
        buf.write("\2\2\2\u00e1\u00e2\7#\2\2\u00e2\u00e3\7?\2\2\u00e38\3")
        buf.write("\2\2\2\u00e4\u00e5\7.\2\2\u00e5:\3\2\2\2\u00e6\u00e7\7")
        buf.write("k\2\2\u00e7\u00e8\7p\2\2\u00e8<\3\2\2\2\u00e9\u00ed\5")
        buf.write("? \2\u00ea\u00ed\5M\'\2\u00eb\u00ed\5W,\2\u00ec\u00e9")
        buf.write("\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed")
        buf.write(">\3\2\2\2\u00ee\u00f9\7\62\2\2\u00ef\u00f6\5E#\2\u00f0")
        buf.write("\u00f2\5A!\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2")
        buf.write("\u00f7\3\2\2\2\u00f3\u00f4\5K&\2\u00f4\u00f5\5A!\2\u00f5")
        buf.write("\u00f7\3\2\2\2\u00f6\u00f1\3\2\2\2\u00f6\u00f3\3\2\2\2")
        buf.write("\u00f7\u00f9\3\2\2\2\u00f8\u00ee\3\2\2\2\u00f8\u00ef\3")
        buf.write("\2\2\2\u00f9@\3\2\2\2\u00fa\u00ff\5C\"\2\u00fb\u00fd\5")
        buf.write("G$\2\u00fc\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe")
        buf.write("\3\2\2\2\u00fe\u0100\5C\"\2\u00ff\u00fc\3\2\2\2\u00ff")
        buf.write("\u0100\3\2\2\2\u0100B\3\2\2\2\u0101\u0104\7\62\2\2\u0102")
        buf.write("\u0104\5E#\2\u0103\u0101\3\2\2\2\u0103\u0102\3\2\2\2\u0104")
        buf.write("D\3\2\2\2\u0105\u0106\t\2\2\2\u0106F\3\2\2\2\u0107\u0109")
        buf.write("\5I%\2\u0108\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0108")
        buf.write("\3\2\2\2\u010a\u010b\3\2\2\2\u010bH\3\2\2\2\u010c\u010f")
        buf.write("\5C\"\2\u010d\u010f\7a\2\2\u010e\u010c\3\2\2\2\u010e\u010d")
        buf.write("\3\2\2\2\u010fJ\3\2\2\2\u0110\u0112\7a\2\2\u0111\u0110")
        buf.write("\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0111\3\2\2\2\u0113")
        buf.write("\u0114\3\2\2\2\u0114L\3\2\2\2\u0115\u0116\7\62\2\2\u0116")
        buf.write("\u0117\t\3\2\2\u0117\u0118\5O(\2\u0118N\3\2\2\2\u0119")
        buf.write("\u011e\5Q)\2\u011a\u011c\5S*\2\u011b\u011a\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011f\5Q)\2\u011e")
        buf.write("\u011b\3\2\2\2\u011e\u011f\3\2\2\2\u011fP\3\2\2\2\u0120")
        buf.write("\u0121\t\4\2\2\u0121R\3\2\2\2\u0122\u0124\5U+\2\u0123")
        buf.write("\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0123\3\2\2\2")
        buf.write("\u0125\u0126\3\2\2\2\u0126T\3\2\2\2\u0127\u012a\5Q)\2")
        buf.write("\u0128\u012a\7a\2\2\u0129\u0127\3\2\2\2\u0129\u0128\3")
        buf.write("\2\2\2\u012aV\3\2\2\2\u012b\u012c\7\62\2\2\u012c\u012d")
        buf.write("\t\5\2\2\u012d\u012e\5Y-\2\u012eX\3\2\2\2\u012f\u0134")
        buf.write("\5[.\2\u0130\u0132\5]/\2\u0131\u0130\3\2\2\2\u0131\u0132")
        buf.write("\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0135\5[.\2\u0134\u0131")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135Z\3\2\2\2\u0136\u0137")
        buf.write("\t\6\2\2\u0137\\\3\2\2\2\u0138\u013a\5_\60\2\u0139\u0138")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0139\3\2\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013c^\3\2\2\2\u013d\u0140\5[.\2\u013e")
        buf.write("\u0140\7a\2\2\u013f\u013d\3\2\2\2\u013f\u013e\3\2\2\2")
        buf.write("\u0140`\3\2\2\2\u0141\u0142\5c\62\2\u0142b\3\2\2\2\u0143")
        buf.write("\u0144\5A!\2\u0144\u0146\7\60\2\2\u0145\u0147\5A!\2\u0146")
        buf.write("\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149\3\2\2\2")
        buf.write("\u0148\u014a\5e\63\2\u0149\u0148\3\2\2\2\u0149\u014a\3")
        buf.write("\2\2\2\u014a\u0154\3\2\2\2\u014b\u014c\7\60\2\2\u014c")
        buf.write("\u014e\5A!\2\u014d\u014f\5e\63\2\u014e\u014d\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0154\3\2\2\2\u0150\u0151\5A!\2\u0151")
        buf.write("\u0152\5e\63\2\u0152\u0154\3\2\2\2\u0153\u0143\3\2\2\2")
        buf.write("\u0153\u014b\3\2\2\2\u0153\u0150\3\2\2\2\u0154d\3\2\2")
        buf.write("\2\u0155\u0156\5g\64\2\u0156\u0157\5i\65\2\u0157f\3\2")
        buf.write("\2\2\u0158\u0159\t\7\2\2\u0159h\3\2\2\2\u015a\u015c\5")
        buf.write("k\66\2\u015b\u015a\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e")
        buf.write("\3\2\2\2\u015d\u015f\5C\"\2\u015e\u015d\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2")
        buf.write("\u0161j\3\2\2\2\u0162\u0163\t\b\2\2\u0163l\3\2\2\2\u0164")
        buf.write("\u0168\5o8\2\u0165\u0167\5q9\2\u0166\u0165\3\2\2\2\u0167")
        buf.write("\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2")
        buf.write("\u0169n\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016e\5s:\2")
        buf.write("\u016c\u016e\7&\2\2\u016d\u016b\3\2\2\2\u016d\u016c\3")
        buf.write("\2\2\2\u016ep\3\2\2\2\u016f\u0173\5o8\2\u0170\u0173\5")
        buf.write("C\"\2\u0171\u0173\4\60\61\2\u0172\u016f\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0172\u0171\3\2\2\2\u0173r\3\2\2\2\u0174")
        buf.write("\u0177\5u;\2\u0175\u0177\7a\2\2\u0176\u0174\3\2\2\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177t\3\2\2\2\u0178\u0179\t\t\2\2\u0179")
        buf.write("v\3\2\2\2\u017a\u017b\t\n\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017d\b<\2\2\u017dx\3\2\2\2\u017e\u0180\t\13\2\2\u017f")
        buf.write("\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u017f\3\2\2\2")
        buf.write("\u0181\u0182\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\b")
        buf.write("=\2\2\u0184z\3\2\2\2\u0185\u0186\7\61\2\2\u0186\u0187")
        buf.write("\7,\2\2\u0187\u018b\3\2\2\2\u0188\u018a\13\2\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018c\u018e\3\2\2\2\u018d\u018b\3")
        buf.write("\2\2\2\u018e\u018f\7,\2\2\u018f\u0190\7\61\2\2\u0190\u0191")
        buf.write("\3\2\2\2\u0191\u0192\b>\2\2\u0192|\3\2\2\2\u0193\u0197")
        buf.write("\7%\2\2\u0194\u0196\n\f\2\2\u0195\u0194\3\2\2\2\u0196")
        buf.write("\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2")
        buf.write("\u0198\u019a\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u019b\b")
        buf.write("?\2\2\u019b~\3\2\2\2\"\2\u00ec\u00f1\u00f6\u00f8\u00fc")
        buf.write("\u00ff\u0103\u010a\u010e\u0113\u011b\u011e\u0125\u0129")
        buf.write("\u0131\u0134\u013b\u013f\u0146\u0149\u014e\u0153\u015b")
        buf.write("\u0160\u0168\u016d\u0172\u0176\u0181\u018b\u0197\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class ShapeExpressionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    CONCAT = 4
    UNION = 5
    LEFTPAREN = 6
    RIGHTPAREN = 7
    CONSTANT = 8
    LINE = 9
    EXPONENTIAL = 10
    SINE = 11
    SINC = 12
    PARAM = 13
    DURATION = 14
    CONSTRAINT = 15
    EULER = 16
    EXP = 17
    MINUS = 18
    PLUS = 19
    LSQBRACKET = 20
    RSQBRACKET = 21
    LEQ = 22
    GEQ = 23
    LESS = 24
    GREATER = 25
    EQ = 26
    NEQ = 27
    COMMA = 28
    IN = 29
    IntegerLiteral = 30
    RealLiteral = 31
    Identifier = 32
    LINE_TERMINATOR = 33
    WHITESPACE = 34
    COMMENT = 35
    LINE_COMMENT = 36

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "';'", "'*'", "'.'", "'join'", "'('", "')'", "'const'", 
            "'line'", "'exp'", "'sine'", "'sinc'", "'param'", "'duration'", 
            "'constraint'", "'EULER'", "'**'", "'-'", "'+'", "'['", "']'", 
            "'<='", "'>='", "'<'", "'>'", "'=='", "'!='", "','", "'in'" ]

    symbolicNames = [ "<INVALID>",
            "CONCAT", "UNION", "LEFTPAREN", "RIGHTPAREN", "CONSTANT", "LINE", 
            "EXPONENTIAL", "SINE", "SINC", "PARAM", "DURATION", "CONSTRAINT", 
            "EULER", "EXP", "MINUS", "PLUS", "LSQBRACKET", "RSQBRACKET", 
            "LEQ", "GEQ", "LESS", "GREATER", "EQ", "NEQ", "COMMA", "IN", 
            "IntegerLiteral", "RealLiteral", "Identifier", "LINE_TERMINATOR", 
            "WHITESPACE", "COMMENT", "LINE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "CONCAT", "UNION", "LEFTPAREN", 
                  "RIGHTPAREN", "CONSTANT", "LINE", "EXPONENTIAL", "SINE", 
                  "SINC", "PARAM", "DURATION", "CONSTRAINT", "EULER", "EXP", 
                  "MINUS", "PLUS", "LSQBRACKET", "RSQBRACKET", "LEQ", "GEQ", 
                  "LESS", "GREATER", "EQ", "NEQ", "COMMA", "IN", "IntegerLiteral", 
                  "DecimalNumeral", "Digits", "Digit", "NonZeroDigit", "DigitsAndUnderscores", 
                  "DigitOrUnderscore", "Underscores", "HexNumeral", "HexDigits", 
                  "HexDigit", "HexDigitsAndUnderscores", "HexDigitOrUnderscore", 
                  "BinaryNumeral", "BinaryDigits", "BinaryDigit", "BinaryDigitsAndUnderscores", 
                  "BinaryDigitOrUnderscore", "RealLiteral", "DecimalRealLiteral", 
                  "ExponentPart", "ExponentIndicator", "SignedInteger", 
                  "Sign", "Identifier", "IdentifierStart", "IdentifierPart", 
                  "LetterOrUnderscore", "Letter", "LINE_TERMINATOR", "WHITESPACE", 
                  "COMMENT", "LINE_COMMENT" ]

    grammarFileName = "ShapeExpression.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


