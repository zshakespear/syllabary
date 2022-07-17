# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:56:09 2022

This code is meant to provide the backbone of the Syllabary Parser.
It takes the CS236 code as a model

@author: zacos
"""
from enum import Enum, auto

class tokenType(Enum):
    TERMINAL = auto()
    NONTERMINAL = auto()
    RULES = auto()
    COLON = auto()
    OR = auto()
    TIMES = auto()
    NUM = auto()
    NEW_LINE = auto()
    ARROW = auto()
    UNDEFINED = auto()
    
class token():
       
    def __init__(self, tokenType, contents, lineNum):
       self.type = tokenType
       self.contents = contents
       self.lineNum = lineNum