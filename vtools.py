#!/bin/env python3

import re
import os
import signal
import sys

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
    print("\n\n|x| Leaving program...")
    sys.exit(1)

signal.signal(signal.SIGINT, sig_handler)

# Hexa functions

def hExA():
    
    print("\n|i| Select an option or you don't know how to read")
    print("\n1. Hexadecimal to string\n2. String to Hexadecimal")
    
    option = int(input("➤ "))
    
    # Convert Hexadecimal to String function ** NOT CREATED YET

    def hexaToStr():
        print("not created yet")

    # Convert String to Hexadecimal

    def strToHexa():

        text = input("\n|~| Insert text to convert: ")
        
        hex_word = ""

        for letter in text:
            hex_word += hex(ord(letter))[2::]

        print(hex_word)

    
    if(option == 1):
        hexaToStr()
    elif(option == 2):
        strToHexa()
    else:
        print("\n\n|!| Select a valid option\n")


# ROT13 function

def rOt13():
    
    text = input("|~| Insert text to convert: ")

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

    print(new_text)

# Menu for options

def menu():

    print(banner)
    print("\n\n|i| Select one option from below.\n")
    print("1. ROT13\n2. Hexadecimal\n3.more")

    option = int(input("\n➤ "))

    if(option == 1):
        rOt13()
    elif(option == 2):
        hExA()

# Main function calling only the menu

def main():
    menu()

if __name__ == "__main__":
    main()
