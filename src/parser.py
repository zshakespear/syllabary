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
    
    #FIXME: rules_list takes a newRule object but it isn't given here! 
    def run(self):
        self.match(t.tokenType.RULES)
        self.match(t.tokenType.COLON)
        self.rules_list()
        self.match(t.tokenType.COMMANDS)
        self.match(t.tokenType.COLON)
        self.check()
        self.commands_list()
    
    def check(self):
        if len(self.tokens) == 0:
            raise Exception('ran out of tokens')
        
    def match(self, target_token):
        self.check()
        if self.tokens[0].type == target_token:
            output = self.tokens[0]
            self.tokens.pop(0)
            return output
        else:
            raise Exception(str(target_token)+'not found')
        
    def rules_list(self, newRule):
        self.check()
        if(self.tokens[0] == t.tokenType.NONTERMINAL):
            newRule.append(self.rule())
            self.rules_list(newRule)
        else:
            return
        
    def commands_list(self):
        if(self.tokens[0] == t.tokenType.NONTERMINAL):
            self.command()
            self.commands_list()
        else:
            return
        
    def rule(self):
        self.check()
        new_rule = p.Rule()
        new_rule.head = self.match(t.tokenType.NONTERMINAL)
        self.match(t.tokenType.ARROW)
        new_rule.body.append(self.product())
        self.product_list(new_rule)
        
    def command(self):
        self.check()
        self.match(t.tokenType.NONTERMINAL)
        self.match(t.tokenType.TIMES)
        self.match(t.tokenType.NUM)
        
    def product(self):
        self.check()
        if (self.tokens[0] == t.tokenType.TERMINAL):
            self.match(t.tokenType.TERMINAL)
        if (self.tokens[0] == t.tokenType.NONTERMINAL):
            self.match(t.tokenType.NONTERMINAL)
    # FIXME: product_list up above takes a rule input and this doesn't receive it. 
    def product_list(self):
        self.check()
        if (self.tokens[0] == t.tokenType.TERMINAl 
            or self.tokens[0] == t.tokenType.NONTERMINAL
            or self.tokens[0] == t.tokenType.OR):
            self.product()
            self.product_list()
        else:
            return
        
def MatchTest():
    try:
        token_list = [t.token(t.tokenType.RULES,'RULES',0),
                      t.token(t.tokenType.COLON,':',0),
                      t.token(t.tokenType.COMMANDS,'COMMANDS',1),
                      t.token(t.tokenType.COLON,':',1),
                      t.token(t.tokenType.NONTERMINAL,'SYL',2)]
        p = Parser(token_list)
        p.run()
        
    except Exception:
        print('Test 1 Failed')
    else:
        for el in p.tokens:
            print(el.type)
    try:
        token_list = [t.token(t.tokenType.RULES,'RULES',0),
                      t.token(t.tokenType.COLON,':',0)]
        p = Parser(token_list)
        p.run()
    except Exception:
        print('Test 2 Failed')
    else:
        print('Something\'s wrong')
    
    try:
        token_list = [t.token(t.tokenType.COMMANDS,'COMMANDS',1),
                      t.token(t.tokenType.COLON,':',1)]
        p = Parser(token_list)
        p.run()
    except Exception:
        print('Test 3 Failed')
    else:
        print('Something\'s wrong')
        
def ProgramTest():
    test_string = "RULES:\n\tSOME -> SOMETHING\nCOMMANDS:\n\tSOME * 5"
    lexer = l.Lexer()
    lexer.run(test_string)
    token_list = lexer.tokens
    p = Parser(token_list)
    try:
        p.run()
    except Exception as inst:
            print('Test 1 Failed: ')
            print(inst)
    else:
         for el in p.program.rules:
             print(el.get_rule())
         for el in p.program.commands:
             print(el.get_command())
             
ProgramTest()