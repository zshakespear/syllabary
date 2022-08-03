# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:54:34 2022

This is the syllabary program class used in parser.py

@author: zacos
"""
import tokens as t

class Command():
    def __init__(self):
        self.head = []
        self.num = []
        
    def get_command(self):
        output = self.head.contents
        output += ' * '
        output += self.num.contents
        return output
        
class Rule():
    def __init__(self):
        self.head = []
        self.body = []
        
    def add_out(self, new_out):
        self.body.append(new_out)
        
    def get_rule(self):
        output = self.head.contents
        output += ' -> '
        for el in self.body:
            output += el.contents
        return output

class SylProgram():
    def __init__(self):
        self.rules = []
        self.commands = []
        
    def add_rule(self, rule):
        self.rules.append(rule)
        
    def add_command(self, command):
        self.commands.append(command)
        
    def exe(self):
        for el in self.commands:
            stack = [el.head]
            while is_terminal(stack) == False:
                rule_to_use = self.check_comm(stack[0].head)
                #FIXME: this doesn't handle ORs in the rule body correctly
                stack.append(rule_to_use.body)
                stack.pop
            #FIXME: This should write to an output file
            print(stack_to_string(stack))
                
                    
            
    def check_comm(self, comm):
        for el in self.rules:
            if comm == el.head:
                return el
        raise Exception('Command head not found in rules')
    
def is_terminal(stack):
    for el in stack:
        if el.type == t.tokenType.NONTERMINAL:
            return False
    return True

def stack_to_string(stack):
    out = ''
    for i in range(len(stack)):
        out += stack[i].contents
    return out
    
    
    