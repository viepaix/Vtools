#!/bin/env python3

import re
import os
import signal
import sys
from colored import Fore,Back,Style

banner = """
                            ,----,                            
                          ,/   .`|                            
                        ,`   .'  :                    ,--,    
       ,---.          ;    ;     /                  ,--.'|    
      /__./|        .'___,/    ,'  ,---.     ,---.  |  | :    
 ,---.;  ; |        |    :     |  '   ,'\   '   ,'\ :  : '    
/___/ \  | |        ;    |.';  ; /   /   | /   /   ||  ' |    
\   ;  \ ' |        `----'  |  |.   ; ,. :.   ; ,. :'  | |    
 \   \  \: |            '   :  ;'   | |: :'   | |: :|  | :    
  ;   \  ' .            |   |  ''   | .; :'   | .; :'  : |__  
   \   \   '            '   :  ||   :    ||   :    ||  | '.'| 
    \   `  ;            ;   |.'  \   \  /  \   \  / ;  :    ; 
     :   \ |            '---'     `----'    `----'  |  ,   /  
      '---"                                          ---`-'   
                                                   by: Viepaix

"""

# CTRL + C Control


def sig_handler(sig, frame):
    print(f"\n\n{Fore.red}{Back.black}|x| Leaving program...{Style.reset}\n")
    sys.exit(1)

signal.signal(signal.SIGINT, sig_handler)

# Hexa functions

def hExA():
    
    print(f"\n{Fore.green}|i| Select an option or you don't know how to read{Style.reset}")
    print(f"\n{Fore.green}1. Hexadecimal to string\n2. String to Hexadecimal{Style.reset}")
    
    option = int(input("➤ "))
    
    # Convert Hexadecimal to String function

    def hexaToStr():
    
        text = input(f"\n{Fore.yellow}|~|{Fore.green} Insert Hexadecimal to convert: {Style.reset}")

        if (text == "0x0"):
            print(f"\n\n{Fore.red}|x| Not value for {text}{Style.reset}")
            hexaToStr()
        elif (text[:2] == "0x"):
            text = bytes.fromhex(text[2::]).decode("utf-8")
            print(f"\n{Fore.light_green}|~| Converted hexadecimal:{Style.reset}", text)
        elif not text:
            print(f"\n\n{Fore.red}|x| Insert a valid text{Style.reset}\n")
            hexaToStr()
        else:
            text = bytes.fromhex(text).decode("utf-8")
            print(f"\n{Fore.light_green}|~| Converted hexadecimal:{Style.reset} {text}")

    # Convert String to Hexadecimal

    def strToHexa():

        text = input(f"\n{Fore.yellow}|~| {Fore.green}Insert text to convert: {Style.reset}")
        hex_word = ""

        for letter in text:
            hex_word += hex(ord(letter))[2::]

        print(f"{Fore.light_green}|+| Converted text:{hex_word}")

    
    if(option == 1):
        hexaToStr()
    elif(option == 2):
        strToHexa()
    else:
        print("\n\n{Fore.red}|!| Select a valid option{Style.reset}\n")


# ROT13 function

def rOt13():
    
    text = input(f"{Fore.green}|~| Insert text to convert: {Style.reset}")

    new_text = ""

    pattern = r"[A-Za-z]"

    # Function to replace each character

    def replace(match):
        char = match.group(0)
        if 'A' <= char <= 'Z':
            return chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        if 'a' <= char <= 'z':
            return chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))

    new_text = re.sub(pattern, replace, text)

    print(f"\n{Fore.light_green}|+| Input text: {text}\n\n|+| Converted text: {new_text}{Style.reset}")

# base64 Converter ** NOT CREATED YET

def bAsE64():
    text = input("\n|~| Insert text to convert: ")
    print(f"{text}")

# binary Converter ** NOT FINISHED

def bInArY():

    def op1(convert):
        print(f"\n\tYour input: {convert}")
        print(f"\tConverted to binary: {bin(int(convert))[2::]}")

        cont = input(f"\nYou want to convert more? y/n: ")

        if(cont == "y"):
            pass
        elif(cont == "n"):
            exit(0)
        else:
            print(f"\n\n|x| {cont} is not a valid option")

    def op2():
        x = int(input("Number 1: "))
        y = int(input("Number 2: "))
        result = x ^ y
        print(result)

    print(f"\n|~| Options\n\t1. Get the binary of a number or string\n2. XOR Binary\n3. idk")

    option = int(input("\n➤ "))

    if(option == 1):
        while True:
            convert = input("\n\n|+| Get binary of: ")
            op1(convert)
    elif(option == 2):
        op2()
    else:
        print(f"\n\n|x| Option {option} not found!\n")

# Menu for options

def menu():

    print(f"{Fore.red}{Style.bold}{banner}{Style.reset}")
    print(f"\n\n{Fore.yellow}|i| {Fore.green}Select one option from below.{Style.reset}\n")
    print(f"{Fore.green}1. ROT13\n2. Hexadecimal\n3. Base64{Style.reset}\n4. Binary")

    option = int(input("\n➤ "))

    if(option == 1):
        rOt13()
    elif(option == 2):
        hExA()
    elif(option == 3):
        bAsE64()
    elif(option == 4):
        bInArY()
    else:
        print(f"\n\n{Fore.red}{Back.black}|x|Option not found{Style.reset}\n")

# Main function calling only the menu

def main():
    menu()

if __name__ == "__main__":
    main()
