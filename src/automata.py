# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 12:50:01 2022

This code creates all of the automata we are going to use for our lexer
and parser.

The automata receives an input string and then goes through the string, 
matching characters as it goes. If it gets to the end of the end of its
sequence, it will return the number of characters read and the type of
token it read. It will also return the number of new lines.  

@author: zacos
"""
import tokens as t

class Automaton():
    
    def __init__(self):
        self.curr_index = 0
        self.new_lines = 0
        self.type = t.tokenType.UNDEFINED
        self.read_chars = 0
        self.input_string = ''
        
    def set_input(self,input_string):
        self.input_string = input_string
        self.curr_index = 0
        self.new_lines = 0
        self.read_chars = 0
        
    def run(self):
        self.s0()
        return self.curr_index, self.type, self.new_lines
        
    def s0(self):
        print('yout didn\'t define s0')
        
    def it(self):
        if (self.curr() == '\n'):
            self.new_lines += 1
        self.curr_index += 1
        self.read_chars += 1
        
    def curr(self):
        return self.input_string[self.curr_index]
    
    def error(self):
        self.curr_index = 0;
        self.new_lines = 0;
        self.read_chars = 0;
        return self.read_chars, t.tokenType.UNDEFINED, self.new_lines
        
        
class TerminalAutomaton(Automaton):
    #FIXME: Automata accepts any number of characters, not characters broken up by a space
    
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.TERMINAL
        
    def s0(self):
        if self.curr().isalpha() == True and self.curr().islower() == True:
            self.it()
            self.s0()

class NonTerminalAutomaton(Automaton):
    #FIXME: See TerminalAutomaton's FIXME
    
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.NONTERMINAL
        
    def s0(self):
        if self.curr().isalpha() == True and self.curr().isupper() == True:
            self.it()
            self.s0()
            
class OrAutomaton(Automaton):
    pass

class RulesAutomaton(Automaton):
    pass

class ColonAutomaton(Automaton):
    pass

class TimesAutomaton(Automaton):
    pass

class NumAutomaton(Automaton):
    pass

class NewLineAutomaton(Automaton):
    pass

class ArrowAutomaton(Automaton):
    pass

def run_Auto(automaton):
    output = automaton.run()
    for el in output:
        print(el)

def Auto_Test():
    test_auto = NonTerminalAutomaton()
    test_auto.set_input('some string')
    run_Auto(test_auto)
    test_auto.set_input('SOME string')
    run_Auto(test_auto)
    test_auto.set_input('SOme string')
    run_Auto(test_auto)
    test_auto.set_input( 'S0me string')
    run_Auto(test_auto)
    
        
Auto_Test()