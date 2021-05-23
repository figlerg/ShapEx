# Generated from C:/Users/giglerf/Documents/dev/ShapEx/parse/grammar\ShapeExpression.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2&")
        buf.write("\u019a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\5\37\u00eb\n\37\3")
        buf.write(" \3 \3 \5 \u00f0\n \3 \3 \3 \5 \u00f5\n \5 \u00f7\n \3")
        buf.write("!\3!\5!\u00fb\n!\3!\5!\u00fe\n!\3\"\3\"\5\"\u0102\n\"")
        buf.write("\3#\3#\3$\6$\u0107\n$\r$\16$\u0108\3%\3%\5%\u010d\n%\3")
        buf.write("&\6&\u0110\n&\r&\16&\u0111\3\'\3\'\3\'\3\'\3(\3(\5(\u011a")
        buf.write("\n(\3(\5(\u011d\n(\3)\3)\3*\6*\u0122\n*\r*\16*\u0123\3")
        buf.write("+\3+\5+\u0128\n+\3,\3,\3,\3,\3-\3-\5-\u0130\n-\3-\5-\u0133")
        buf.write("\n-\3.\3.\3/\6/\u0138\n/\r/\16/\u0139\3\60\3\60\5\60\u013e")
        buf.write("\n\60\3\61\3\61\3\62\3\62\3\62\5\62\u0145\n\62\3\62\5")
        buf.write("\62\u0148\n\62\3\62\3\62\3\62\5\62\u014d\n\62\3\62\3\62")
        buf.write("\3\62\5\62\u0152\n\62\3\63\3\63\3\63\3\64\3\64\3\65\5")
        buf.write("\65\u015a\n\65\3\65\6\65\u015d\n\65\r\65\16\65\u015e\3")
        buf.write("\66\3\66\3\67\3\67\7\67\u0165\n\67\f\67\16\67\u0168\13")
        buf.write("\67\38\38\58\u016c\n8\39\39\39\59\u0171\n9\3:\3:\5:\u0175")
        buf.write("\n:\3;\3;\3<\3<\3<\3<\3=\6=\u017e\n=\r=\16=\u017f\3=\3")
        buf.write("=\3>\3>\3>\3>\7>\u0188\n>\f>\16>\u018b\13>\3>\3>\3>\3")
        buf.write(">\3>\3?\3?\7?\u0194\n?\f?\16?\u0197\13?\3?\3?\3\u0189")
        buf.write("\2@\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?\2A\2C\2E\2G\2")
        buf.write("I\2K\2M\2O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a!c\2e\2g\2i\2k\2")
        buf.write("m\"o\2q\2s\2u\2w#y${%}&\3\2\r\3\2\63;\4\2ZZzz\5\2\62;")
        buf.write("CHch\4\2DDdd\3\2\62\63\4\2GGgg\4\2--//\4\2C\\c|\3\2\f")
        buf.write("\f\5\2\13\13\16\17\"\"\4\2\f\f\17\17\2\u01a1\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2a\3\2\2\2\2m\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177\3\2")
        buf.write("\2\2\5\u0081\3\2\2\2\7\u0083\3\2\2\2\t\u0085\3\2\2\2\13")
        buf.write("\u0087\3\2\2\2\r\u008c\3\2\2\2\17\u008e\3\2\2\2\21\u0090")
        buf.write("\3\2\2\2\23\u0096\3\2\2\2\25\u009b\3\2\2\2\27\u009f\3")
        buf.write("\2\2\2\31\u00a4\3\2\2\2\33\u00a9\3\2\2\2\35\u00af\3\2")
        buf.write("\2\2\37\u00b8\3\2\2\2!\u00c5\3\2\2\2#\u00c7\3\2\2\2%\u00ca")
        buf.write("\3\2\2\2\'\u00cc\3\2\2\2)\u00ce\3\2\2\2+\u00d0\3\2\2\2")
        buf.write("-\u00d2\3\2\2\2/\u00d5\3\2\2\2\61\u00d8\3\2\2\2\63\u00da")
        buf.write("\3\2\2\2\65\u00dc\3\2\2\2\67\u00df\3\2\2\29\u00e2\3\2")
        buf.write("\2\2;\u00e4\3\2\2\2=\u00ea\3\2\2\2?\u00f6\3\2\2\2A\u00f8")
        buf.write("\3\2\2\2C\u0101\3\2\2\2E\u0103\3\2\2\2G\u0106\3\2\2\2")
        buf.write("I\u010c\3\2\2\2K\u010f\3\2\2\2M\u0113\3\2\2\2O\u0117\3")
        buf.write("\2\2\2Q\u011e\3\2\2\2S\u0121\3\2\2\2U\u0127\3\2\2\2W\u0129")
        buf.write("\3\2\2\2Y\u012d\3\2\2\2[\u0134\3\2\2\2]\u0137\3\2\2\2")
        buf.write("_\u013d\3\2\2\2a\u013f\3\2\2\2c\u0151\3\2\2\2e\u0153\3")
        buf.write("\2\2\2g\u0156\3\2\2\2i\u0159\3\2\2\2k\u0160\3\2\2\2m\u0162")
        buf.write("\3\2\2\2o\u016b\3\2\2\2q\u0170\3\2\2\2s\u0174\3\2\2\2")
        buf.write("u\u0176\3\2\2\2w\u0178\3\2\2\2y\u017d\3\2\2\2{\u0183\3")
        buf.write("\2\2\2}\u0191\3\2\2\2\177\u0080\7<\2\2\u0080\4\3\2\2\2")
        buf.write("\u0081\u0082\7=\2\2\u0082\6\3\2\2\2\u0083\u0084\7,\2\2")
        buf.write("\u0084\b\3\2\2\2\u0085\u0086\7\60\2\2\u0086\n\3\2\2\2")
        buf.write("\u0087\u0088\7l\2\2\u0088\u0089\7q\2\2\u0089\u008a\7k")
        buf.write("\2\2\u008a\u008b\7p\2\2\u008b\f\3\2\2\2\u008c\u008d\7")
        buf.write("*\2\2\u008d\16\3\2\2\2\u008e\u008f\7+\2\2\u008f\20\3\2")
        buf.write("\2\2\u0090\u0091\7e\2\2\u0091\u0092\7q\2\2\u0092\u0093")
        buf.write("\7p\2\2\u0093\u0094\7u\2\2\u0094\u0095\7v\2\2\u0095\22")
        buf.write("\3\2\2\2\u0096\u0097\7n\2\2\u0097\u0098\7k\2\2\u0098\u0099")
        buf.write("\7p\2\2\u0099\u009a\7g\2\2\u009a\24\3\2\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\u009d\7z\2\2\u009d\u009e\7r\2\2\u009e\26")
        buf.write("\3\2\2\2\u009f\u00a0\7u\2\2\u00a0\u00a1\7k\2\2\u00a1\u00a2")
        buf.write("\7p\2\2\u00a2\u00a3\7g\2\2\u00a3\30\3\2\2\2\u00a4\u00a5")
        buf.write("\7u\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8")
        buf.write("\7e\2\2\u00a8\32\3\2\2\2\u00a9\u00aa\7r\2\2\u00aa\u00ab")
        buf.write("\7c\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7o\2\2\u00ae\34\3\2\2\2\u00af\u00b0\7f\2\2\u00b0\u00b1")
        buf.write("\7w\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4")
        buf.write("\7v\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7")
        buf.write("\7p\2\2\u00b7\36\3\2\2\2\u00b8\u00b9\7a\2\2\u00b9\u00ba")
        buf.write("\7a\2\2\u00ba\u00bb\7e\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd")
        buf.write("\7p\2\2\u00bd\u00be\7u\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0")
        buf.write("\7t\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\u00c4\7v\2\2\u00c4 \3\2\2\2\u00c5\u00c6")
        buf.write("\7g\2\2\u00c6\"\3\2\2\2\u00c7\u00c8\7,\2\2\u00c8\u00c9")
        buf.write("\7,\2\2\u00c9$\3\2\2\2\u00ca\u00cb\7/\2\2\u00cb&\3\2\2")
        buf.write("\2\u00cc\u00cd\7-\2\2\u00cd(\3\2\2\2\u00ce\u00cf\7]\2")
        buf.write("\2\u00cf*\3\2\2\2\u00d0\u00d1\7_\2\2\u00d1,\3\2\2\2\u00d2")
        buf.write("\u00d3\7>\2\2\u00d3\u00d4\7?\2\2\u00d4.\3\2\2\2\u00d5")
        buf.write("\u00d6\7@\2\2\u00d6\u00d7\7?\2\2\u00d7\60\3\2\2\2\u00d8")
        buf.write("\u00d9\7>\2\2\u00d9\62\3\2\2\2\u00da\u00db\7@\2\2\u00db")
        buf.write("\64\3\2\2\2\u00dc\u00dd\7?\2\2\u00dd\u00de\7?\2\2\u00de")
        buf.write("\66\3\2\2\2\u00df\u00e0\7#\2\2\u00e0\u00e1\7?\2\2\u00e1")
        buf.write("8\3\2\2\2\u00e2\u00e3\7.\2\2\u00e3:\3\2\2\2\u00e4\u00e5")
        buf.write("\7k\2\2\u00e5\u00e6\7p\2\2\u00e6<\3\2\2\2\u00e7\u00eb")
        buf.write("\5? \2\u00e8\u00eb\5M\'\2\u00e9\u00eb\5W,\2\u00ea\u00e7")
        buf.write("\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb")
        buf.write(">\3\2\2\2\u00ec\u00f7\7\62\2\2\u00ed\u00f4\5E#\2\u00ee")
        buf.write("\u00f0\5A!\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00f5\3\2\2\2\u00f1\u00f2\5K&\2\u00f2\u00f3\5A!\2\u00f3")
        buf.write("\u00f5\3\2\2\2\u00f4\u00ef\3\2\2\2\u00f4\u00f1\3\2\2\2")
        buf.write("\u00f5\u00f7\3\2\2\2\u00f6\u00ec\3\2\2\2\u00f6\u00ed\3")
        buf.write("\2\2\2\u00f7@\3\2\2\2\u00f8\u00fd\5C\"\2\u00f9\u00fb\5")
        buf.write("G$\2\u00fa\u00f9\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc")
        buf.write("\3\2\2\2\u00fc\u00fe\5C\"\2\u00fd\u00fa\3\2\2\2\u00fd")
        buf.write("\u00fe\3\2\2\2\u00feB\3\2\2\2\u00ff\u0102\7\62\2\2\u0100")
        buf.write("\u0102\5E#\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102")
        buf.write("D\3\2\2\2\u0103\u0104\t\2\2\2\u0104F\3\2\2\2\u0105\u0107")
        buf.write("\5I%\2\u0106\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0106")
        buf.write("\3\2\2\2\u0108\u0109\3\2\2\2\u0109H\3\2\2\2\u010a\u010d")
        buf.write("\5C\"\2\u010b\u010d\7a\2\2\u010c\u010a\3\2\2\2\u010c\u010b")
        buf.write("\3\2\2\2\u010dJ\3\2\2\2\u010e\u0110\7a\2\2\u010f\u010e")
        buf.write("\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u010f\3\2\2\2\u0111")
        buf.write("\u0112\3\2\2\2\u0112L\3\2\2\2\u0113\u0114\7\62\2\2\u0114")
        buf.write("\u0115\t\3\2\2\u0115\u0116\5O(\2\u0116N\3\2\2\2\u0117")
        buf.write("\u011c\5Q)\2\u0118\u011a\5S*\2\u0119\u0118\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d\5Q)\2\u011c")
        buf.write("\u0119\3\2\2\2\u011c\u011d\3\2\2\2\u011dP\3\2\2\2\u011e")
        buf.write("\u011f\t\4\2\2\u011fR\3\2\2\2\u0120\u0122\5U+\2\u0121")
        buf.write("\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0121\3\2\2\2")
        buf.write("\u0123\u0124\3\2\2\2\u0124T\3\2\2\2\u0125\u0128\5Q)\2")
        buf.write("\u0126\u0128\7a\2\2\u0127\u0125\3\2\2\2\u0127\u0126\3")
        buf.write("\2\2\2\u0128V\3\2\2\2\u0129\u012a\7\62\2\2\u012a\u012b")
        buf.write("\t\5\2\2\u012b\u012c\5Y-\2\u012cX\3\2\2\2\u012d\u0132")
        buf.write("\5[.\2\u012e\u0130\5]/\2\u012f\u012e\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0133\5[.\2\u0132\u012f")
        buf.write("\3\2\2\2\u0132\u0133\3\2\2\2\u0133Z\3\2\2\2\u0134\u0135")
        buf.write("\t\6\2\2\u0135\\\3\2\2\2\u0136\u0138\5_\60\2\u0137\u0136")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u0137\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013a^\3\2\2\2\u013b\u013e\5[.\2\u013c")
        buf.write("\u013e\7a\2\2\u013d\u013b\3\2\2\2\u013d\u013c\3\2\2\2")
        buf.write("\u013e`\3\2\2\2\u013f\u0140\5c\62\2\u0140b\3\2\2\2\u0141")
        buf.write("\u0142\5A!\2\u0142\u0144\7\60\2\2\u0143\u0145\5A!\2\u0144")
        buf.write("\u0143\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0147\3\2\2\2")
        buf.write("\u0146\u0148\5e\63\2\u0147\u0146\3\2\2\2\u0147\u0148\3")
        buf.write("\2\2\2\u0148\u0152\3\2\2\2\u0149\u014a\7\60\2\2\u014a")
        buf.write("\u014c\5A!\2\u014b\u014d\5e\63\2\u014c\u014b\3\2\2\2\u014c")
        buf.write("\u014d\3\2\2\2\u014d\u0152\3\2\2\2\u014e\u014f\5A!\2\u014f")
        buf.write("\u0150\5e\63\2\u0150\u0152\3\2\2\2\u0151\u0141\3\2\2\2")
        buf.write("\u0151\u0149\3\2\2\2\u0151\u014e\3\2\2\2\u0152d\3\2\2")
        buf.write("\2\u0153\u0154\5g\64\2\u0154\u0155\5i\65\2\u0155f\3\2")
        buf.write("\2\2\u0156\u0157\t\7\2\2\u0157h\3\2\2\2\u0158\u015a\5")
        buf.write("k\66\2\u0159\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015c")
        buf.write("\3\2\2\2\u015b\u015d\5C\"\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015fj\3\2\2\2\u0160\u0161\t\b\2\2\u0161l\3\2\2\2\u0162")
        buf.write("\u0166\5o8\2\u0163\u0165\5q9\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2")
        buf.write("\u0167n\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016c\5s:\2")
        buf.write("\u016a\u016c\7&\2\2\u016b\u0169\3\2\2\2\u016b\u016a\3")
        buf.write("\2\2\2\u016cp\3\2\2\2\u016d\u0171\5o8\2\u016e\u0171\5")
        buf.write("C\"\2\u016f\u0171\4\60\61\2\u0170\u016d\3\2\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171r\3\2\2\2\u0172")
        buf.write("\u0175\5u;\2\u0173\u0175\7a\2\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0173\3\2\2\2\u0175t\3\2\2\2\u0176\u0177\t\t\2\2\u0177")
        buf.write("v\3\2\2\2\u0178\u0179\t\n\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("\u017b\b<\2\2\u017bx\3\2\2\2\u017c\u017e\t\13\2\2\u017d")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\b")
        buf.write("=\2\2\u0182z\3\2\2\2\u0183\u0184\7\61\2\2\u0184\u0185")
        buf.write("\7,\2\2\u0185\u0189\3\2\2\2\u0186\u0188\13\2\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u018a\3\2\2\2")
        buf.write("\u0189\u0187\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u0189\3")
        buf.write("\2\2\2\u018c\u018d\7,\2\2\u018d\u018e\7\61\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u0190\b>\2\2\u0190|\3\2\2\2\u0191\u0195")
        buf.write("\7%\2\2\u0192\u0194\n\f\2\2\u0193\u0192\3\2\2\2\u0194")
        buf.write("\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u0198\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199\b")
        buf.write("?\2\2\u0199~\3\2\2\2\"\2\u00ea\u00ef\u00f4\u00f6\u00fa")
        buf.write("\u00fd\u0101\u0108\u010c\u0111\u0119\u011c\u0123\u0127")
        buf.write("\u012f\u0132\u0139\u013d\u0144\u0147\u014c\u0151\u0159")
        buf.write("\u015e\u0166\u016b\u0170\u0174\u017f\u0189\u0195\3\b\2")
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
            "'__constraint'", "'e'", "'**'", "'-'", "'+'", "'['", "']'", 
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


