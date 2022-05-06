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
    #input parsing for passing file
    #GUI (low low priority)
    #branching and stack (low low low priority)

import re
import sys
import getopt

from tabulate import tabulate
from constants import (
    OPCODE,
    REGISTERS,
)

#parse input and import program from file
argv = sys.argv
arg_help = "-i, --input> - input file\n -h - help\n EXAMPLE: python \"HW 2.py\" -i test_program.txt"
input_file = ""

try:
    opts, args = getopt.getopt(argv[1:], "hi:", ["help", "input="])
except:
    print(arg_help)
    sys.exit(2)

for opt,arg in opts:
    if opt in ("-h", "--help"):
        print(arg_help)
        sys.exit(2)
    if opt in ("-i", "--input"):
        input_file = arg

file = open(input_file,"r")
code_string = file.read()

instructions = []

#stack
stack = [] #list. can use stack.append() and stack.pop()

#flags
overflow = False #overflow "bit"
remainder = False #remainder "bit" (for jump instructions)

#registers (just three, cause it's my favorite number). dictionary, key is register, value is register value
regs = {"a": "", "b": "", "c": ""}

#memory
mem = {"0b01":0b000000,"0b10":0b000000,"0b11":0b000000} #dictionary. key is variable name, value is, well, value. should already be generically typed (ie. accept any variable type)

#parse the code
instructions = code_string.split("\n") #split based on line


def stringify(curr_step, register, instruction, mem=mem):
    """A function to stringify the register object
    """
    data = []
    for k, v in register.items():
        v = 0 if v == "" else v
        data.append([curr_step, f"${k}", '0x{0:0{1}X}'.format(v,8), f"{REGISTERS.get(k)}", '0x{0:0{1}X}'.format(mem.get(REGISTERS.get(k)),8)])
    print("Registers:")
    print(tabulate(data, headers=["Step", "Register", "Value", "Memory", "Value"], tablefmt="pretty"))
    print(f"Instruction: {instruction}")
    print(f"OPCODE: {bin(OPCODE.get(instruction[0]))}")
    input("\nPress Enter to continue...\n")
    
#interpret and run the code
i = 0

#initial state
stringify(i, regs, ["noop"])
    
for instruction in instructions:

    instruction = re.split(' |,| ,', instruction) #to hold different pieces of current instruction
    
    match int(OPCODE.get(instruction[0])):
        #register operations
        case 0b000001:
            regs[instruction[1]] = int(regs[instruction[2]])
        case 0b000010:
            regs[instruction[1]] = int(instruction[2])
        #arithmetic operations
        case 0b000011:
            regs["a"] = int(regs["a"]) + int(regs[instruction[1]]) #add a and other reg (check bounds of register for error handling)
        case 0b000100:
           regs["a"] = int(regs["a"]) + int(instruction[1]) #add reg a and immediate
        case 0b000101:
            regs["a"] = int(regs["a"]) - int(regs[instruction[1]]) #subtract given reg from a and store in a
        case 0b000110:
            regs["a"] = int(regs["a"]) - int(instruction[1]) #subtract immediate from reg a
        case 0b000111:
            regs["a"] = int(regs["a"]) * int(regs[instruction[1]]) #multiply a by given reg
        case 0b001000:
            regs["a"] = int(regs["a"]) * int(instruction[1]) #multiply a by immediate
        #data operations
        case 0b001001:
            mem[instruction[2]] = int(regs[instruction[1]])
        case 0b001010:
            regs[instruction[1]] = mem[instruction[2]]
        #bitwise operations
        case 0b001011:
            regs[instruction[1]] = int(regs[instruction[1]]) << int(instruction[2])
        case 0b001100:
            regs[instruction[1]] = int(regs[instruction[1]]) >> int(instruction[2])
        case 0b001101:
            regs["a"] = int(regs["a"]) & int(regs[instruction[1]])
        case 0b001110:
            regs["a"] = int(regs["a"]) & int(instruction[1])
        case 0b001111:
            regs["a"] = int(regs["a"]) | int(regs[instruction[1]])
        case 0b010000:
            regs["a"] = int(regs["a"]) | int(instruction[1])
        case 0b010001:
            regs["a"] = int(regs["a"]) ^ int(regs[instruction[1]])
        case 0b010010:
            regs["a"] = int(regs["a"]) ^ int(instruction[1])
        case 0b010010:
            regs["a"] =  ~ int(regs[instruction[1]])
        case 0b010010:
            regs["a"] =  ~ int(instruction[1])
        
    #branching operations (this is where stack comes in) UNNEEDED
    
    stringify(i, regs, instruction)
    i += 1