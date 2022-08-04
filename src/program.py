# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:54:34 2022

This is the syllabary program class used in parser.py

@author: zacos
"""
import tokens as t
import random as r

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
        self.body = [[]]
        self.ind = 0
        
    def add_opt(self):
        self.body.append([])
        self.ind += 1
        
    def add_out(self, new_out):
        self.body[self.ind].append(new_out)
        
    def get_rule(self):
        output = self.head.contents
        output += ' -> '
        ind = 0
        for el in self.body:
            for subel in el:
                output += subel.contents
            if(ind != len(self.body)-1):
                output += ' | '
            ind += 1
        return output

class SylProgram():
    def __init__(self):
        self.rules = []
        self.commands = []
        
    def add_rule(self, rule):
        self.rules.append(rule)
        
    def add_command(self, command):
        self.commands.append(command)
        
    def exe(self,out_path):
        f = open(out_path, 'w')
        for el in self.commands:
            for i in range(int(el.num.contents)):
                f.write (self.eval_comm(el.head))
                f.write("\n")
        f.close()
        #         outstack = [el.head]
        #         ind = 0
        #         while(is_terminal(outstack) == False):
        #             if(outstack[ind].type == t.tokenType.TERMINAL):
        #                 ind += 1
        #             else:
        #                 tar_comm = outstack[ind]
        #                 outstack.pop(ind)
        #                 int_result = self.eval_comm(tar_comm)
        #                 for j in range(len(int_result)):
        #                     outstack.insert(ind, int_result)
                
    
    def eval_comm(self, token):
        outlist = []
        self.replace(token,outlist)
        return(stack_to_string(outlist))

        
    def replace(self, token, outlist):
        if token.type == t.tokenType.TERMINAL:
            outlist.append(token.contents)
        else:
            if token.type == t.tokenType.LAMBDA:
                pass
            else:
                prod = self.rule_out(token)
                for el in prod:
                    self.replace(el, outlist)
                
    def rule_out(self, comm):
        rule_to_use = self.check_comm(comm)
        rand_lim = len(rule_to_use.body) - 1
        rand_out = r.randint(0,rand_lim)
        return rule_to_use.body[rand_out]
        
    def check_comm(self, comm):
        for el in self.rules:
            # print (el.head.contents)
            
            if comm.type == el.head.type and comm.contents == el.head.contents:
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
        out += stack[i]
    return out
    
