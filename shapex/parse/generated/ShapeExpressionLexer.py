# Generated from C:/Users/giglerf/Documents/dev/dev_code/ShapEx/shapex/parse/grammar\ShapeExpression.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2&")
        buf.write("\u01a2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0091")
        buf.write("\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\5\37\u00f3\n\37\3 \3 \3 \5 ")
        buf.write("\u00f8\n \3 \3 \3 \5 \u00fd\n \5 \u00ff\n \3!\3!\5!\u0103")
        buf.write("\n!\3!\5!\u0106\n!\3\"\3\"\5\"\u010a\n\"\3#\3#\3$\6$\u010f")
        buf.write("\n$\r$\16$\u0110\3%\3%\5%\u0115\n%\3&\6&\u0118\n&\r&\16")
        buf.write("&\u0119\3\'\3\'\3\'\3\'\3(\3(\5(\u0122\n(\3(\5(\u0125")
        buf.write("\n(\3)\3)\3*\6*\u012a\n*\r*\16*\u012b\3+\3+\5+\u0130\n")
        buf.write("+\3,\3,\3,\3,\3-\3-\5-\u0138\n-\3-\5-\u013b\n-\3.\3.\3")
        buf.write("/\6/\u0140\n/\r/\16/\u0141\3\60\3\60\5\60\u0146\n\60\3")
        buf.write("\61\3\61\3\62\3\62\3\62\5\62\u014d\n\62\3\62\5\62\u0150")
        buf.write("\n\62\3\62\3\62\3\62\5\62\u0155\n\62\3\62\3\62\3\62\5")
        buf.write("\62\u015a\n\62\3\63\3\63\3\63\3\64\3\64\3\65\5\65\u0162")
        buf.write("\n\65\3\65\6\65\u0165\n\65\r\65\16\65\u0166\3\66\3\66")
        buf.write("\3\67\3\67\7\67\u016d\n\67\f\67\16\67\u0170\13\67\38\3")
        buf.write("8\58\u0174\n8\39\39\39\59\u0179\n9\3:\3:\5:\u017d\n:\3")
        buf.write(";\3;\3<\3<\3<\3<\3=\6=\u0186\n=\r=\16=\u0187\3=\3=\3>")
        buf.write("\3>\3>\3>\7>\u0190\n>\f>\16>\u0193\13>\3>\3>\3>\3>\3>")
        buf.write("\3?\3?\7?\u019c\n?\f?\16?\u019f\13?\3?\3?\3\u0191\2@\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?\2A\2C\2E\2G\2I\2K\2M")
        buf.write("\2O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a!c\2e\2g\2i\2k\2m\"o\2q")
        buf.write("\2s\2u\2w#y${%}&\3\2\r\3\2\63;\4\2ZZzz\5\2\62;CHch\4\2")
        buf.write("DDdd\3\2\62\63\4\2GGgg\4\2--//\4\2C\\c|\3\2\f\f\5\2\13")
        buf.write("\13\16\17\"\"\4\2\f\f\17\17\2\u01aa\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2a\3\2\2\2\2m\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177\3\2\2\2\5")
        buf.write("\u0081\3\2\2\2\7\u0083\3\2\2\2\t\u0085\3\2\2\2\13\u0090")
        buf.write("\3\2\2\2\r\u0092\3\2\2\2\17\u0094\3\2\2\2\21\u0096\3\2")
        buf.write("\2\2\23\u009c\3\2\2\2\25\u00a1\3\2\2\2\27\u00a5\3\2\2")
        buf.write("\2\31\u00aa\3\2\2\2\33\u00af\3\2\2\2\35\u00b5\3\2\2\2")
        buf.write("\37\u00be\3\2\2\2!\u00c9\3\2\2\2#\u00cf\3\2\2\2%\u00d2")
        buf.write("\3\2\2\2\'\u00d4\3\2\2\2)\u00d6\3\2\2\2+\u00d8\3\2\2\2")
        buf.write("-\u00da\3\2\2\2/\u00dd\3\2\2\2\61\u00e0\3\2\2\2\63\u00e2")
        buf.write("\3\2\2\2\65\u00e4\3\2\2\2\67\u00e7\3\2\2\29\u00ea\3\2")
        buf.write("\2\2;\u00ec\3\2\2\2=\u00f2\3\2\2\2?\u00fe\3\2\2\2A\u0100")
        buf.write("\3\2\2\2C\u0109\3\2\2\2E\u010b\3\2\2\2G\u010e\3\2\2\2")
        buf.write("I\u0114\3\2\2\2K\u0117\3\2\2\2M\u011b\3\2\2\2O\u011f\3")
        buf.write("\2\2\2Q\u0126\3\2\2\2S\u0129\3\2\2\2U\u012f\3\2\2\2W\u0131")
        buf.write("\3\2\2\2Y\u0135\3\2\2\2[\u013c\3\2\2\2]\u013f\3\2\2\2")
        buf.write("_\u0145\3\2\2\2a\u0147\3\2\2\2c\u0159\3\2\2\2e\u015b\3")
        buf.write("\2\2\2g\u015e\3\2\2\2i\u0161\3\2\2\2k\u0168\3\2\2\2m\u016a")
        buf.write("\3\2\2\2o\u0173\3\2\2\2q\u0178\3\2\2\2s\u017c\3\2\2\2")
        buf.write("u\u017e\3\2\2\2w\u0180\3\2\2\2y\u0185\3\2\2\2{\u018b\3")
        buf.write("\2\2\2}\u0199\3\2\2\2\177\u0080\7<\2\2\u0080\4\3\2\2\2")
        buf.write("\u0081\u0082\7=\2\2\u0082\6\3\2\2\2\u0083\u0084\7,\2\2")
        buf.write("\u0084\b\3\2\2\2\u0085\u0086\7\60\2\2\u0086\n\3\2\2\2")
        buf.write("\u0087\u0088\7w\2\2\u0088\u0089\7p\2\2\u0089\u008a\7k")
        buf.write("\2\2\u008a\u008b\7q\2\2\u008b\u0091\7p\2\2\u008c\u008d")
        buf.write("\7l\2\2\u008d\u008e\7q\2\2\u008e\u008f\7k\2\2\u008f\u0091")
        buf.write("\7p\2\2\u0090\u0087\3\2\2\2\u0090\u008c\3\2\2\2\u0091")
        buf.write("\f\3\2\2\2\u0092\u0093\7*\2\2\u0093\16\3\2\2\2\u0094\u0095")
        buf.write("\7+\2\2\u0095\20\3\2\2\2\u0096\u0097\7e\2\2\u0097\u0098")
        buf.write("\7q\2\2\u0098\u0099\7p\2\2\u0099\u009a\7u\2\2\u009a\u009b")
        buf.write("\7v\2\2\u009b\22\3\2\2\2\u009c\u009d\7n\2\2\u009d\u009e")
        buf.write("\7k\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7g\2\2\u00a0\24")
        buf.write("\3\2\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7z\2\2\u00a3\u00a4")
        buf.write("\7r\2\2\u00a4\26\3\2\2\2\u00a5\u00a6\7u\2\2\u00a6\u00a7")
        buf.write("\7k\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7g\2\2\u00a9\30")
        buf.write("\3\2\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7e\2\2\u00ae\32\3\2\2\2\u00af\u00b0")
        buf.write("\7r\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3")
        buf.write("\7c\2\2\u00b3\u00b4\7o\2\2\u00b4\34\3\2\2\2\u00b5\u00b6")
        buf.write("\7f\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9")
        buf.write("\7c\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7p\2\2\u00bd\36\3\2\2\2\u00be\u00bf")
        buf.write("\7e\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2")
        buf.write("\7u\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5")
        buf.write("\7c\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8 \3\2\2\2\u00c9\u00ca\7G\2\2\u00ca\u00cb")
        buf.write("\7W\2\2\u00cb\u00cc\7N\2\2\u00cc\u00cd\7G\2\2\u00cd\u00ce")
        buf.write("\7T\2\2\u00ce\"\3\2\2\2\u00cf\u00d0\7,\2\2\u00d0\u00d1")
        buf.write("\7,\2\2\u00d1$\3\2\2\2\u00d2\u00d3\7/\2\2\u00d3&\3\2\2")
        buf.write("\2\u00d4\u00d5\7-\2\2\u00d5(\3\2\2\2\u00d6\u00d7\7]\2")
        buf.write("\2\u00d7*\3\2\2\2\u00d8\u00d9\7_\2\2\u00d9,\3\2\2\2\u00da")
        buf.write("\u00db\7>\2\2\u00db\u00dc\7?\2\2\u00dc.\3\2\2\2\u00dd")
        buf.write("\u00de\7@\2\2\u00de\u00df\7?\2\2\u00df\60\3\2\2\2\u00e0")
        buf.write("\u00e1\7>\2\2\u00e1\62\3\2\2\2\u00e2\u00e3\7@\2\2\u00e3")
        buf.write("\64\3\2\2\2\u00e4\u00e5\7?\2\2\u00e5\u00e6\7?\2\2\u00e6")
        buf.write("\66\3\2\2\2\u00e7\u00e8\7#\2\2\u00e8\u00e9\7?\2\2\u00e9")
        buf.write("8\3\2\2\2\u00ea\u00eb\7.\2\2\u00eb:\3\2\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7p\2\2\u00ee<\3\2\2\2\u00ef\u00f3")
        buf.write("\5? \2\u00f0\u00f3\5M\'\2\u00f1\u00f3\5W,\2\u00f2\u00ef")
        buf.write("\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3")
        buf.write(">\3\2\2\2\u00f4\u00ff\7\62\2\2\u00f5\u00fc\5E#\2\u00f6")
        buf.write("\u00f8\5A!\2\u00f7\u00f6\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("\u00fd\3\2\2\2\u00f9\u00fa\5K&\2\u00fa\u00fb\5A!\2\u00fb")
        buf.write("\u00fd\3\2\2\2\u00fc\u00f7\3\2\2\2\u00fc\u00f9\3\2\2\2")
        buf.write("\u00fd\u00ff\3\2\2\2\u00fe\u00f4\3\2\2\2\u00fe\u00f5\3")
        buf.write("\2\2\2\u00ff@\3\2\2\2\u0100\u0105\5C\"\2\u0101\u0103\5")
        buf.write("G$\2\u0102\u0101\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104")
        buf.write("\3\2\2\2\u0104\u0106\5C\"\2\u0105\u0102\3\2\2\2\u0105")
        buf.write("\u0106\3\2\2\2\u0106B\3\2\2\2\u0107\u010a\7\62\2\2\u0108")
        buf.write("\u010a\5E#\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a")
        buf.write("D\3\2\2\2\u010b\u010c\t\2\2\2\u010cF\3\2\2\2\u010d\u010f")
        buf.write("\5I%\2\u010e\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0110\u0111\3\2\2\2\u0111H\3\2\2\2\u0112\u0115")
        buf.write("\5C\"\2\u0113\u0115\7a\2\2\u0114\u0112\3\2\2\2\u0114\u0113")
        buf.write("\3\2\2\2\u0115J\3\2\2\2\u0116\u0118\7a\2\2\u0117\u0116")
        buf.write("\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u0117\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011aL\3\2\2\2\u011b\u011c\7\62\2\2\u011c")
        buf.write("\u011d\t\3\2\2\u011d\u011e\5O(\2\u011eN\3\2\2\2\u011f")
        buf.write("\u0124\5Q)\2\u0120\u0122\5S*\2\u0121\u0120\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0125\5Q)\2\u0124")
        buf.write("\u0121\3\2\2\2\u0124\u0125\3\2\2\2\u0125P\3\2\2\2\u0126")
        buf.write("\u0127\t\4\2\2\u0127R\3\2\2\2\u0128\u012a\5U+\2\u0129")
        buf.write("\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u0129\3\2\2\2")
        buf.write("\u012b\u012c\3\2\2\2\u012cT\3\2\2\2\u012d\u0130\5Q)\2")
        buf.write("\u012e\u0130\7a\2\2\u012f\u012d\3\2\2\2\u012f\u012e\3")
        buf.write("\2\2\2\u0130V\3\2\2\2\u0131\u0132\7\62\2\2\u0132\u0133")
        buf.write("\t\5\2\2\u0133\u0134\5Y-\2\u0134X\3\2\2\2\u0135\u013a")
        buf.write("\5[.\2\u0136\u0138\5]/\2\u0137\u0136\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\5[.\2\u013a\u0137")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013bZ\3\2\2\2\u013c\u013d")
        buf.write("\t\6\2\2\u013d\\\3\2\2\2\u013e\u0140\5_\60\2\u013f\u013e")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142^\3\2\2\2\u0143\u0146\5[.\2\u0144")
        buf.write("\u0146\7a\2\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2")
        buf.write("\u0146`\3\2\2\2\u0147\u0148\5c\62\2\u0148b\3\2\2\2\u0149")
        buf.write("\u014a\5A!\2\u014a\u014c\7\60\2\2\u014b\u014d\5A!\2\u014c")
        buf.write("\u014b\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2")
        buf.write("\u014e\u0150\5e\63\2\u014f\u014e\3\2\2\2\u014f\u0150\3")
        buf.write("\2\2\2\u0150\u015a\3\2\2\2\u0151\u0152\7\60\2\2\u0152")
        buf.write("\u0154\5A!\2\u0153\u0155\5e\63\2\u0154\u0153\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155\u015a\3\2\2\2\u0156\u0157\5A!\2\u0157")
        buf.write("\u0158\5e\63\2\u0158\u015a\3\2\2\2\u0159\u0149\3\2\2\2")
        buf.write("\u0159\u0151\3\2\2\2\u0159\u0156\3\2\2\2\u015ad\3\2\2")
        buf.write("\2\u015b\u015c\5g\64\2\u015c\u015d\5i\65\2\u015df\3\2")
        buf.write("\2\2\u015e\u015f\t\7\2\2\u015fh\3\2\2\2\u0160\u0162\5")
        buf.write("k\66\2\u0161\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164")
        buf.write("\3\2\2\2\u0163\u0165\5C\"\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2")
        buf.write("\u0167j\3\2\2\2\u0168\u0169\t\b\2\2\u0169l\3\2\2\2\u016a")
        buf.write("\u016e\5o8\2\u016b\u016d\5q9\2\u016c\u016b\3\2\2\2\u016d")
        buf.write("\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016fn\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0174\5s:\2")
        buf.write("\u0172\u0174\7&\2\2\u0173\u0171\3\2\2\2\u0173\u0172\3")
        buf.write("\2\2\2\u0174p\3\2\2\2\u0175\u0179\5o8\2\u0176\u0179\5")
        buf.write("C\"\2\u0177\u0179\4\60\61\2\u0178\u0175\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179r\3\2\2\2\u017a")
        buf.write("\u017d\5u;\2\u017b\u017d\7a\2\2\u017c\u017a\3\2\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017dt\3\2\2\2\u017e\u017f\t\t\2\2\u017f")
        buf.write("v\3\2\2\2\u0180\u0181\t\n\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0183\b<\2\2\u0183x\3\2\2\2\u0184\u0186\t\13\2\2\u0185")
        buf.write("\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\b")
        buf.write("=\2\2\u018az\3\2\2\2\u018b\u018c\7\61\2\2\u018c\u018d")
        buf.write("\7,\2\2\u018d\u0191\3\2\2\2\u018e\u0190\13\2\2\2\u018f")
        buf.write("\u018e\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0191\u018f\3\2\2\2\u0192\u0194\3\2\2\2\u0193\u0191\3")
        buf.write("\2\2\2\u0194\u0195\7,\2\2\u0195\u0196\7\61\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197\u0198\b>\2\2\u0198|\3\2\2\2\u0199\u019d")
        buf.write("\7%\2\2\u019a\u019c\n\f\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write("\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019e\u01a0\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a1\b")
        buf.write("?\2\2\u01a1~\3\2\2\2#\2\u0090\u00f2\u00f7\u00fc\u00fe")
        buf.write("\u0102\u0105\u0109\u0110\u0114\u0119\u0121\u0124\u012b")
        buf.write("\u012f\u0137\u013a\u0141\u0145\u014c\u014f\u0154\u0159")
        buf.write("\u0161\u0166\u016e\u0173\u0178\u017c\u0187\u0191\u019d")
        buf.write("\3\b\2\2")
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
            "':'", "';'", "'*'", "'.'", "'('", "')'", "'const'", "'line'", 
            "'exp'", "'sine'", "'sinc'", "'param'", "'duration'", "'constraint'", 
            "'EULER'", "'**'", "'-'", "'+'", "'['", "']'", "'<='", "'>='", 
            "'<'", "'>'", "'=='", "'!='", "','", "'in'" ]

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


