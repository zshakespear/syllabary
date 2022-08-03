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


def main(input_path, output_path):
    print('you haven\'t defined main yet!')
    
def exe_test():
    test_string = "RULES:\n\tSOME -> SOMETHING\n\tSOMETHING -> l | j | k\nCOMMANDS:\n\tSOME * 5"
    lexer = l.Lexer()
    lexer.run(test_string)
    token_list = lexer.tokens
    parse = p.Parser(token_list)
    parse.run()
    parse.program.exe()