# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:41:16 2022

@author: natrium

HW 2. custom assembly emulator
"""

#code
code_string = ""
instructions = []

#stack
stack = [] #list. can use stack.append() and stack.pop()

#flags
bool overflow #overflow "bit"
bool remainder #remainder "bit" (for jump instructions)

#registers (just three, cause it's my favorite number). dictionary, key is register, value is register value
regs = {"a": "", "b": "", "c": ""}

#memory
dict mem = {} #dictionary. key is variable name, value is, well, value. should already be generically typed (ie. accept any variable type)

#function to parse the code
def parse ():
    instructions = code_string.splitlines() #split based on line
    
#interpret and run the code
def run():
    for instruction in instructions []
        instruction = instruction.split(' ') #to hold different pieces of current instruction
        
        #arithmetic operations
        if instruction[0] == "add":
            regs["a"] = regs["a"] + regs[instruction[1]] #add a and other reg (check bounds of register for error handling)
        if instruction[0] == "adi":
            regs["a"] = regs["a"] + instruction[1] #add reg a and immediate
        if instruction[0] == "sub":
            regs["a"] = regs["a"] - regs[instruction[1]] #subtract given reg from a and store in a
        if instruction[0] == "subi":
            regs["a"] = regs["a"] - instruction[1] #subtract immediate from reg a
        if instruction[0] == "mul": 
            regs["a"] = regs["a"] * regs[instruction[1]] #multiply a by given reg
        if instruction[0] == "muli":
            regs["a"] = regs["a"] * instruction[1] #multiply a by immediate
            
        #data operations
        if instruction[0] == "st":
            mem[instruction[2]] = regs[instruction[1]]
        if instruction[0] == "ld":
            regs[instruction[1]] = mem[instruction[2]]
        
        #bitwise operations
        
        #branching operations (this is where stack comes in)