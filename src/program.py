# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:54:34 2022

This is the syllabary program class used in parser.py

@author: zacos
"""

class Command():
    def __init__(self):
        self.head
        self.num
        
    def get_command(self):
        output = self.head.contents
        output += ' * '
        output += self.num.contents
        return output
        
class Rule():
    def __init__(self):
        self.head
        self.body
        
    def add_out(self, new_out):
        self.body.append(new_out)
        
    def get_rule(self):
        output = self.head.contents
        output += ' -> '
        for el in self.body:
            output += el.contents + ' | '
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
            found = self.check_comm(el.head)
            if found == False:
                print('Command head not found in rules')
            
    def check_comm(self,comm):
        found = False
        for el in self.rules:
            if comm == el.head:
                found = True
        
        return found