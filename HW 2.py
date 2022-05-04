# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:41:16 2022

@author: natrium

HW 2. custom assembly emulator
"""

import re

#code
code_string = "ldi a,5\nldi b,10\nadd b\nadi 5"
instructions = []

#stack
stack = [] #list. can use stack.append() and stack.pop()

#flags
overflow = False #overflow "bit"
remainder = False #remainder "bit" (for jump instructions)

#registers (just three, cause it's my favorite number). dictionary, key is register, value is register value
regs = {"a": "", "b": "", "c": ""}

#memory
mem = {} #dictionary. key is variable name, value is, well, value. should already be generically typed (ie. accept any variable type)

#parse the code
instructions = code_string.split("\n") #split based on line
    
#interpret and run the code
for instruction in instructions: 
    instruction = re.split(' |,| ,', instruction) #to hold different pieces of current instruction
    
    #register operations
    if instruction[0] == "ld":
        regs[instruction[1]] = regs[instruction[2]]
    if instruction[0] == "ldi":
        regs[instruction[1]] = instruction[2]
    
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
    if instruction[0] == "shl":
        regs[instruction[1]] = regs[instruction[1]] << instruction[2]
    if instruction[0] == "shr":
        regs[instruction[1]] = regs[instruction[1]] >> instruction[2]
    if instruction[0] == "and":
        regs["a"] = regs["a"] & regs[instruction[1]]
    if instruction[0] == "andi":
        regs["a"] = regs["a"] & instruction[1]
    if instruction[0] == "or":
        regs["a"] = regs["a"] | regs[instruction[1]]
    if instruction[0] == "ori":
        regs["a"] = regs["a"] | instruction[1]
    if instruction[0] == "xor":
        regs["a"] = regs["a"] ^ regs[instruction[1]]
    if instruction[0] == "xori":
        regs["a"] = regs["a"] ^ instruction[1]
    if instruction[0] == "comp":
        regs["a"] =  ~ regs[instruction[1]]
    if instruction[0] == "compi":
        regs["a"] =  ~ instruction[1]
        
        
        
    #branching operations (this is where stack comes in)