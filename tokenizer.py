# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 12:13:56 2018

@author: ASUS
"""

from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
from io import BytesIO

def decistmt(s, keywords):
    
    result = []
    g = tokenize(BytesIO(s.encode('utf-8')).readline)
    #BytesIO(s.encode('utf-8')).readline)  # tokenize the string
    toktemp = ""
    for toknum, tokval, tok1, tok2, tok3 in g:
        if tokval == "$":
            toktemp = "$"
            #continue
        else:
            if toknum == 59:
                continue
            print(toknum," _______ ",tokval)
            if toknum == 3:
                tokval = "DATA"
            elif toknum == 1:
                if (toktemp+tokval) not in keys:
                    tokval = "VAR"
            elif toknum == 53:
                if tokval == ".":
                    tokval = "DOT"
                elif tokval == ",":
                    tokval = "COMMA"
                elif tokval == ")":
                    tokval = "RPAR"
                elif tokval == "(":
                    tokval = "LPAR"
                elif tokval == "{":
                    tokval = "LBRACE"
                elif tokval == "}":
                    tokval = "RBRACE"
                elif tokval == "[":
                    tokval = "LSQB"
                elif tokval == "]":
                    tokval = "RSQB"
                elif tokval == ":":
                    tokval = "COLON"
                elif tokval == ";":
                    tokval = "SEMICOLON"
                elif tokval == "/":
                    tokval = "SLASH"
                else:
                    tokval = tokval
            elif toknum == 0:
                
                tokval = "EOL"
                
            
            result.append(toktemp+tokval)
            toktemp=""
    #return untokenize(result).decode('utf-8')
    print(result)

keys = []

keys = [line.rstrip('\n') for line in open("keywords.txt","r")]
#print(keys)

fo = open("data.txt", "r")
line = fo.readline()
decistmt(line, keys)