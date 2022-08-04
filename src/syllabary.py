# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 12:08:04 2022

This is the code that puts syllabary together.

It will take the path of the command file and the desired output file
and then run the syllabary program constructed by the parser

@author: zacos
"""
import lexer as l
import parser as p
from program import stack_to_string as sts


def main(input_path, output_path):
    f = open(input_path,'r')
    in_string = f.read()
    f.close()
    lex = l.Lexer()
    lex.run(in_string)
    token_list = lex.tokens
    par = p.Parser(token_list)
    par.run()
    par.program.exe(output_path)
    
def exe_test(output_path):
    test_string = "RULES:\n\tSOME -> SOMETHING SOMETHING,\n\tSOMETHING -> l | j | k,\nCOMMANDS:\n\tSOME * 5"
    lexer = l.Lexer()
    lexer.run(test_string)
    token_list = lexer.tokens
    parse = p.Parser(token_list)
    parse.run()
    parse.program.exe(output_path)
    
def match_test(output_path):
    test_string = 'RULES:\n\tSOME -> SOMETHING SOMETHING lambda, \n\tSOMETHING -> l | j | k,\nCOMMANDS:\n\tSOME * 5'
    lexer = l.Lexer()
    lexer.run(test_string)
    token_list = lexer.tokens
    par = p.Parser(token_list)
    par.run()
    outlist = []
    comm = par.program.commands[0].head
    par.program.replace(comm,outlist)
    print(sts(outlist))
    return