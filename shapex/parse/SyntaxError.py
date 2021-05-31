from antlr4 import *
from antlr4.error.ErrorStrategy import BailErrorStrategy


# this actually throws if parser encounters invalid syntax and gives some error message.
# inspired by https://stackoverflow.com/questions/60263601/how-can-i-fail-on-first-syntax-error-in-a-python-antlr-generated-parser-while-ke
class HardSyntaxErrorStrategy(BailErrorStrategy):
    def recover(self, recognizer: Parser, e: RecognitionException):
        recognizer._errHandler.reportError(recognizer, e)
        super().recover(recognizer, e)
