# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:41:16 2022

@authors: natrium
          Varis
          Christian
          Luanqi

HW 2. custom assembly emulator
"""

#ToDo:
    #flags into enum
    #output formatting
    #input parsing for passing file
    #GUI (low low priority)
    #branching and stack (low low low priority)

import re

from tabulate import tabulate

#code
code_string = "ldi a,5\nldi b,10\nadd b\nst a,var1\nadi 5\nst a,var2"
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


def stringify(curr_step, register, instruction):
    """A function to stringify the register object
    """
    data = []
    for k, v in register.items():
        v = 0 if v == "" else v
        data.append([curr_step, f"${k}", '0x{0:0{1}X}'.format(v,8)])
    print(f"\n{instruction}")
    print(tabulate(data, headers=["Step", "Register", "Value"], tablefmt="pretty"))
    input("\nPress Enter to continue...")
    
#interpret and run the code
i = 0
for instruction in instructions:

    stringify(i, regs, instruction)
    i += 1
    instruction = re.split(' |,| ,', instruction) #to hold different pieces of current instruction
    
    #register operations
    if instruction[0] == "ld":
        regs[instruction[1]] = int(regs[instruction[2]])
        continue
    if instruction[0] == "ldi":
        regs[instruction[1]] = int(instruction[2])
        continue
    
    #arithmetic operations
    if instruction[0] == "add":
        regs["a"] = int(regs["a"]) + int(regs[instruction[1]]) #add a and other reg (check bounds of register for error handling)
        continue
    if instruction[0] == "adi":
        regs["a"] = int(regs["a"]) + int(instruction[1]) #add reg a and immediate
        continue
    if instruction[0] == "sub":
        regs["a"] = int(regs["a"]) - int(regs[instruction[1]]) #subtract given reg from a and store in a
        continue
    if instruction[0] == "subi":
        regs["a"] = int(regs["a"]) - int(instruction[1]) #subtract immediate from reg a
        continue
    if instruction[0] == "mul": 
        regs["a"] = int(regs["a"]) * int(regs[instruction[1]]) #multiply a by given reg
        continue
    if instruction[0] == "muli":
        regs["a"] = int(regs["a"]) * int(instruction[1]) #multiply a by immediate
        continue
        
    #data operations
    if instruction[0] == "st":
        mem[instruction[2]] = regs[instruction[1]]
        continue
    if instruction[0] == "ld":
        regs[instruction[1]] = mem[instruction[2]]
        continue
    
    #bitwise operations
    if instruction[0] == "shl":
        regs[instruction[1]] = int(regs[instruction[1]]) << int(instruction[2])
        continue
    if instruction[0] == "shr":
        regs[instruction[1]] = int(regs[instruction[1]]) >> int(instruction[2])
        continue
    if instruction[0] == "and":
        regs["a"] = int(regs["a"]) & int(regs[instruction[1]])
        continue
    if instruction[0] == "andi":
        regs["a"] = int(regs["a"]) & int(instruction[1])
        continue
    if instruction[0] == "or":
        regs["a"] = int(regs["a"]) | int(regs[instruction[1]])
        continue
    if instruction[0] == "ori":
        regs["a"] = int(regs["a"]) | int(instruction[1])
        continue
    if instruction[0] == "xor":
        regs["a"] = int(regs["a"]) ^ int(regs[instruction[1]])
        continue
    if instruction[0] == "xori":
        regs["a"] = int(regs["a"]) ^ int(instruction[1])
        continue
    if instruction[0] == "comp":
        regs["a"] =  ~ int(regs[instruction[1]])
        continue
    if instruction[0] == "compi":
        regs["a"] =  ~ int(instruction[1])
        continue
        
    #branching operations (this is where stack comes in) UNNEEDED