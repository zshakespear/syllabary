# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:53:27 2022

This is the parser of syllabary. It's job is to make sure that the grammar
rules of syllabary are followed. It also initializes the syllabary program object

@author: zacos
"""

import lexer as l
import tokens as t
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
            raise Exception(str(target_token)+' not found')
        
    def rules_list(self):
        self.check()
        if(self.tokens[0].type == t.tokenType.NONTERMINAL):
            self.rule()
            self.rules_list()
        else:
            return
        
    def commands_list(self):
        try:
            self.check()
            if(self.tokens[0].type == t.tokenType.NONTERMINAL):
                self.command()
                self.commands_list()
            else:
                return
        except Exception:
            return
        
    def rule(self):
        self.check()
        new_rule = p.Rule()
        new_rule.head = self.match(t.tokenType.NONTERMINAL)
        self.match(t.tokenType.ARROW)
        new_rule.add_out(self.product())
        self.product_list(new_rule)
        self.match(t.tokenType.COMMA)
        self.program.add_rule(new_rule)
        
    def command(self):
        self.check()
        new_command = p.Command()
        new_command.head = self.match(t.tokenType.NONTERMINAL)
        self.match(t.tokenType.TIMES)
        new_command.num = self.match(t.tokenType.NUM)
        self.program.add_command(new_command)
        
    def product(self):
        self.check()
        if (self.tokens[0].type == t.tokenType.TERMINAL):
            return self.match(t.tokenType.TERMINAL)
        if (self.tokens[0].type == t.tokenType.NONTERMINAL):
            return self.match(t.tokenType.NONTERMINAL)
        if self.tokens[0].type == t.tokenType.OR:
            return self.match(t.tokenType.OR)
        raise Exception("Expected Terminal or Nonterminal, found: "+str(self.tokens[0].type))
     
    #FIXME: product_list currently adds OR to the product list. 
    #FIXME: product_list currently runs across lines. So we need to add a character to terminate a rule. Should we add a new character or should we reuse a character we already have?
    def product_list(self, rule):
        self.check()
        if (self.tokens[0].type == t.tokenType.TERMINAL 
            or self.tokens[0].type == t.tokenType.NONTERMINAL
            or self.tokens[0].type == t.tokenType.OR):
            rule.add_out(self.product())
            self.product_list(rule)
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
    test_string = "RULES:\n\tSOME -> SOMETHING,\n\t SOMETHING -> l | j | k,\nCOMMANDS:\n\tSOME * 5"
    lexer = l.Lexer()
    lexer.run(test_string)
    token_list = lexer.tokens
    par = Parser(token_list)
    try:
        par.run()
    except Exception as inst:
            print('Test 1 Failed: ')
            print(inst)
    else:
         for el in par.program.rules:
             print(el.get_rule())
         for el in par.program.commands:
             print(el.get_command())
             
ProgramTest()