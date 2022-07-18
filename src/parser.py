# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:53:27 2022

This is the parser of syllabary. It's job is to make sure that the grammar
rules of syllabary are followed. It also initializes the syllabary program object

@author: zacos
"""

import lexer as l
import tokens as t
import automata as a
import program as p

class Parser():
    def __init__(self, token_list):
        self.program = p.SylProgram()
        self.tokens = token_list
        
    def run(self):
        self.match(t.tokenType.RULES)
        self.match(t.tokenType.COLON)
        self.rules_list()
        self.match(t.tokenType.COMMANDS)
        self.match(t.tokenType.COLON)
        self.commands_list()
        
        
    def match(self, target_token):
        if self.tokens[0].type == target_token:
            output = self.tokens[0]
            self.tokens.pop(0)
            return output
        else:
            raise Exception('token not found')
        
    def rules_list(self):
        if(self.tokens[0] == t.tokenType.NONTERMINAL):
            self.rule()
            self.rules_list()
        else:
            return
        
    def commands_list(self):
        if(self.tokens[0] == t.tokenType.NONTERMINAL):
            self.command()
            self.commands_list()
        else:
            return
        
    def rule(self):
        print('you haven\'t defined rule yet')
        
    def command(self):
        print('you havent defined command yet')
        
    def product(self):
        print('you havent defined product yet')
        
    def product_list(self):
        if (self.tokens[0] == t.tokenType.TERMINAl 
            or self.tokens[0] == t.tokenType.NONTERMINAL
            or self.tokens[0] == t.tokenType.OR):
            self.product()
            self.product_list()
        else:
            return
        
def MatchTest():
    token_list = [t.token(t.tokenType.RULES,'RULES',0),
                  t.token(t.tokenType.COLON,':',0),
                  t.token(t.tokenType.COMMANDS,'COMMANDS',1),
                  t.token(t.tokenType.COLON,':',1)]
    p = Parser(token_list)
    p.run()
    for el in p.tokens:
        print(el.type)
    