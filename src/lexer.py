# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:50:59 2022

This is the lexer of syllabary. Its purpose is to take a file and return
a list of tokens for the parser.

@author: zacos
"""

import automata as a
import tokens as t

#TODO: fix error handling

class Lexer():
    def __init__(self):
        self.automata = [a.ArrowAutomaton(),
                         a.ColonAutomaton(),
                         a.CommaAutomaton(),
                         a.CommandsAutomaton(),
                         a.LambdaAutomaton(),
                         a.NumAutomaton(),
                         a.OrAutomaton(),
                         a.RulesAutomaton(),
                         a.TerminalAutomaton(),
                         a.TimesAutomaton(),
                         a.NonTerminalAutomaton()]
        self.tokens = []
        
    def run(self, input_string):
        while len(input_string) > 0:
            while input_string[0].isspace():
                input_string = input_string[1:]
            for auto in self.automata:
                auto.set_input(input_string)
                [chars_read, token_type, dummy] = auto.run()
                if token_type != t.tokenType.UNDEFINED:
                    new_token = t.token(token_type, input_string[:chars_read], 0)
                    self.tokens.append(new_token)
                    input_string = input_string[chars_read:]
                    break
                
def LexerTest():
    test_lexer = Lexer()
    string = 'some string with numbers: 123 * 456 | NON, RULES COMMANDS'
    test_lexer.run(string)
    for el in test_lexer.tokens:
        print(el.type)
        