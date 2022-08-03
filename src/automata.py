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

#TODO: Fix the error handling here. 

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
        print('you didn\'t redefine run')
        self.s0()
        return self.curr_index, self.type, self.new_lines
        
    def s0(self):
        print('you didn\'t define s0')
        
    def it(self):
        if (self.curr() == '\n'):
            self.new_lines += 1
        self.curr_index += 1
        self.read_chars += 1
        
    def curr(self):
        return self.input_string[self.curr_index]
    
    def match(self, char):
        return self.curr() == char


    def error(self):
        self.curr_index = 0;
        self.new_lines = 0;
        self.read_chars = 0;
        self.type = t.tokenType.UNDEFINED
      
class CommaAutomaton(Automaton):
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.COMMA
        
    def run(self):
        self.type = t.tokenType.COMMA
        self.s0()
        return self.curr_index, self.type, self.new_lines
    def s0(self):
        if self.curr_index == len(self.input_string):
            return
        else:
            if self.match(","):
                self.it()
                return
            else:
                self.error()

 #FIXME: Terminals require spaces after them and don't do well with | characters       
class TerminalAutomaton(Automaton):
    
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.TERMINAL
        
    def run(self):
        self.type = t.tokenType.TERMINAL
        self.s0()
        return self.curr_index, self.type, self.new_lines
        
        
    def s0(self):
        if self.curr_index == len(self.input_string):
            return
        if self.curr().isalpha() == True and self.curr().islower() == True:
            self.it()
            self.s0()
        else:
            if self.curr().isspace() == True or self.match(':') or self.match(","):
                return
            else:
                self.error()

class NonTerminalAutomaton(Automaton):
    
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.NONTERMINAL
        
    def run(self):
        self.type = t.tokenType.NONTERMINAL
        self.s0()
        return self.curr_index, self.type, self.new_lines
        
    def s0(self):
        if self.curr_index == len(self.input_string):
            return
        if self.curr().isalpha() == True and self.curr().isupper() == True:
            self.it()
            self.s0()
        else:
            if self.curr().isspace() == True or self.match(","):
                return
            else:
                self.error()
            
class OrAutomaton(Automaton):
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.OR
        
    def run(self):
        self.type = t.tokenType.OR
        self.s0()
        return self.curr_index, self.type, self.new_lines
    
    def s0(self):
        if self.match('|'):
            self.it()
            return
        else:
            self.error()

class RulesAutomaton(Automaton):
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.RULES
        
    def run(self):
        self.type = t.tokenType.RULES
        self.s0()
        return self.curr_index, self.type, self.new_lines
    
    def s0(self):
        if self.match('R'):
            self.it()
            self.s1()
        else:
            self.error()
            
    def s1(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('U'):
            self.it()
            self.s2()
        else:
            self.error()
            
    def s2(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('L'):
            self.it()
            self.s3()
        else:
            self.error()
            
    def s3(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('E'):
            self.it()
            self.s4()
        else:
            self.error()
            
    def s4(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('S'):
            self.it()
            return
        else:
            self.error()

class ColonAutomaton(Automaton):
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.COLON
        
    def run(self):
        self.type = t.tokenType.COLON
        self.s0()
        return self.curr_index, self.type, self.new_lines
    
    def s0(self):
        if self.match(':'):
            self.it()
            return
        else:
            self.error()

class TimesAutomaton(Automaton):
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.TIMES
        
    def run(self):
        self.type = t.tokenType.TIMES
        self.s0()
        return self.curr_index, self.type, self.new_lines
    
    def s0(self):
        if self.match('*'):
            self.it()
            return
        else:
            self.error()

class NumAutomaton(Automaton):
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.NUM
        
    def run(self):
        self.type = t.tokenType.NUM
        self.s0()
        return self.curr_index, self.type, self.new_lines
    
    def s0(self):
        if self.curr_index == len(self.input_string):
            return
        if self.curr().isnumeric() == True:
            self.it()
            self.s0()
        else:
            if self.curr().isspace() == True:
                return
            else:
                self.error()

class ArrowAutomaton(Automaton):
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.ARROW
        
    def run(self):
        self.type = t.tokenType.ARROW
        self.s0()
        return self.curr_index, self.type, self.new_lines
    
    def s0(self):
        if self.match('-'):
            self.it()
            self.s1()
        else:
            self.error()
            
    def s1(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('>'):
            self.it()
            return
        else:
            self.error()

class CommandsAutomaton(Automaton):
    def __init__(self):
        super().__init__()
        self.type = t.tokenType.COMMANDS
        
    def run(self):
        self.type = t.tokenType.COMMANDS
        self.s0()
        return self.curr_index, self.type, self.new_lines
    
    def s0(self):
        if self.match('C'):
            self.it()
            self.s1();
        else:
            self.error()
            
    def s1(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('O'):
            self.it()
            self.s2()
        else:
            self.error()
            
    def s2(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('M'):
            self.it()
            self.s3()
        else:
            self.error()
            
    def s3(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('M'):
            self.it()
            self.s4()
        else:
            self.error()
            
    def s4(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('A'):
            self.it()
            self.s5()
        else:
            self.error()
            
    def s5(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('N'):
            self.it()
            self.s6()
        else:
            self.error()
            
    def s6(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('D'):
            self.it()
            self.s7()
        else:
            self.error()
    
    def s7(self):
        if self.curr_index == len(self.input_string):
            self.error()
            return
        if self.match('S'):
            self.it()
        else:
            self.error()

def run_Auto(automaton):
    output = automaton.run()
    for el in output:
        print(el)
    print('\n')
    
def Commands_Auto_Test():
    test_auto = CommandsAutomaton()
    test_auto.set_input('COMMANDS')
    run_Auto(test_auto)
    test_auto.set_input('Commands')
    run_Auto(test_auto)
    test_auto.set_input('COMMA')
    run_Auto(test_auto)
    
def Arrow_Auto_Test():
    test_auto = ArrowAutomaton()
    test_auto.set_input('->')
    run_Auto(test_auto)
    test_auto.set_input('-')
    run_Auto(test_auto)
    test_auto.set_input('>')
    run_Auto(test_auto)
    test_auto.set_input('-.>')
    run_Auto(test_auto)

def Num_Auto_Test():
    test_auto = NumAutomaton()
    test_auto.set_input('some string')
    run_Auto(test_auto)
    test_auto.set_input('123')
    run_Auto(test_auto)
    test_auto.set_input('12some string')
    run_Auto(test_auto)

def Times_Auto_Test():
    test_auto = TimesAutomaton()
    test_auto.set_input('some string')
    run_Auto(test_auto)
    test_auto.set_input('*')
    run_Auto(test_auto)
    test_auto.set_input('*some')
    run_Auto(test_auto)
    test_auto.set_input('* some')
    run_Auto(test_auto)

def Colon_Auto_Test():
    test_auto = ColonAutomaton()
    test_auto.set_input('some string')
    run_Auto(test_auto)
    test_auto.set_input(':')
    run_Auto(test_auto)
    test_auto.set_input(':some')
    run_Auto(test_auto)
    test_auto.set_input(': some')
    run_Auto(test_auto)
    
def Rules_Auto_Test():
    test_auto = RulesAutomaton()
    test_auto.set_input('rules')
    run_Auto(test_auto)
    test_auto.set_input('RULES')
    run_Auto(test_auto)
    test_auto.set_input('Rules')
    run_Auto(test_auto)
    test_auto.set_input('RU')
    run_Auto(test_auto)
        
def Or_Auto_Test():
    test_auto = OrAutomaton()
    test_auto.set_input('some string')
    run_Auto(test_auto)
    test_auto.set_input('|')
    run_Auto(test_auto)
    test_auto.set_input('|some string')
    run_Auto(test_auto)
    test_auto.set_input('| some string')
    run_Auto(test_auto)

def Terminal_Auto_Test():
    test_auto = TerminalAutomaton()
    test_auto.set_input('some string')
    run_Auto(test_auto)
    test_auto.set_input('soME string')
    run_Auto(test_auto)
    test_auto.set_input('SOme string')
    run_Auto(test_auto)
    test_auto.set_input('s0Me string')
    run_Auto(test_auto)

def NonTerminal_Auto_Test():
    test_auto = NonTerminalAutomaton()
    test_auto.set_input('some string')
    run_Auto(test_auto)
    test_auto.set_input('SOME string')
    run_Auto(test_auto)
    test_auto.set_input('SOme string')
    run_Auto(test_auto)
    test_auto.set_input( 'S0me string')
    run_Auto(test_auto)
    
        
def Test_Battery():
    Terminal_Auto_Test()
    NonTerminal_Auto_Test()
    Or_Auto_Test()
    Rules_Auto_Test()
    Colon_Auto_Test()
    Times_Auto_Test()
    Num_Auto_Test()
    Arrow_Auto_Test()
    Commands_Auto_Test()
    