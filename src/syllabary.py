# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 13:23:26 2022

The purpose of this code is to create syllables which can be used to construct
fictional languages

@author: zacos
"""

import pandas as pd
import random as r

class Syl:
    def __init__(self, onset, vowel, coda):
        self.onset = onset
        self.vowel = vowel
        self.coda = coda
        
    def getSyl(self):
        return self.onset+self.vowel+self.coda

class ranSyl(Syl):
    def __init__(self, possList):
        poss = pd.read_csv(possList)
        # Unpacking the possibilities
        possOnset = poss['onset']
        possOnset = possOnset[possOnset.notna()]
        possVowel = poss['vowel']
        possVowel = possVowel[possVowel.notna()]
        possCoda = poss['coda']
        possCoda = possCoda[possCoda.notna()]
        # Random phonemes
        onsetNum = len(possOnset)
        vowelNum = len(possVowel)
        codaNum = len(possCoda)
        onsetRan = r.randint(0, onsetNum - 1)
        vowelRan = r.randint(0, vowelNum - 1)
        codaRan = r.randint(0, codaNum - 1)
        # Assignment
        self.onset = possOnset.iloc[onsetRan]
        self.vowel = possVowel.iloc[vowelRan]
        self.coda = possCoda.iloc[codaRan]
        

def ran_syl(file):
    test = ranSyl(file)
    return test.getSyl()
    
def syl_list(file):
    #Loading the test file
    poss = pd.read_csv(file)
    #Splitting the test file
    possOnset = poss['onset']
    possOnset = possOnset[possOnset.notna()]
    possVowel = poss['vowel']
    possVowel = possVowel[possVowel.notna()]
    possCoda = poss['coda']
    possCoda = possCoda[possCoda.notna()]
    #Getting the lengths
    onsetLen = len(possOnset)
    vowelLen = len(possVowel)
    codaLen = len(possCoda)
    #Nested for loop
    sylLib = []
    for i in range(0,onsetLen):
        for j in range(0, vowelLen):
            for k in range(0, codaLen):
                sylLib.append(Syl(possOnset.iloc[i], possVowel.iloc[j], possCoda.iloc[k]))
        
    return sylLib

def ran_word(file):
    wordSyl = r.randint(1,3)
    word = []
    outword = ''
    for i in range(0, wordSyl):
        word.append(ranSyl(file))
    
    for i in range(0, len(word)):
        outword += word[i].getSyl()
    
    return outword
    
def word_lib(file):
    sylLib = syl_list(file)
    wordLib = [[],[],[]]
    iterLen = range(0, len(sylLib) - 1)
    
    for i in iterLen:
        wordLib[0].append(sylLib[i].getSyl())
    
    for i in iterLen:
        for j in iterLen:
            wordLib[1].append(sylLib[i].getSyl() + sylLib[j].getSyl())
            
    for i in iterLen:
        for j in iterLen:
            for k in iterLen:
                wordLib[2].append(sylLib[i].getSyl() + sylLib[j].getSyl() + sylLib[k].getSyl())
                
    return wordLib
            
        
    
