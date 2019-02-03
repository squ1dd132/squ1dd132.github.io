from __future__ import print_function
import os, time
import sys

class InputType:
    Nothing = 1
    Stars = 2
    Hash = 3

def in_idle():
    try:
        return sys.stdin.__module__.startswith('idlelib')
    except AttributeError:
        return True

#if(in_idle()):
#    print("Please launch me from the terminal!")
#    os._exit(0)


def win():
    return os.name == "nt"

class IO:
    @classmethod
    def getch(cls):
        if win():
            import msvcrt
            return msvcrt.getch()
        else:
            if os.name != "posix":
                print("Sorry, your system is not supported.")
                os._exit(0)
            import tty, sys, termios
            #Get the stdin file descriptor.
            stdin = sys.stdin.fileno()
            settings = termios.tcgetattr(stdin)
            try:
                tty.setraw(stdin)
                ch = sys.stdin.read(1)
            finally: #Don't handle exceptions, just clean up whether or not it threw something.
                termios.tcsetattr(stdin, termios.TCSADRAIN, settings)
                
            return chr(ord(ch))

class PasswordInput:
    @classmethod
    def GetPass(cls, type = 1):
        password = ""
        while True:
            character = IO.getch()
            if(character > chr(31)):
                printChar = ""
                
                if(type == 2):
                    printChar = "*"
                elif(type == 3):
                    printChar = "#"
                
                print(printChar, end='')
                password += str(character)
            else:
                break
            
        print("")
        return password
print("Enter your password: ", end = "")
print(PasswordInput.GetPass(InputType.Nothing))
print("Enter your password: ", end = "")
print(PasswordInput.GetPass(InputType.Stars))
print("Enter your password: ", end = "")
print(PasswordInput.GetPass(InputType.Hash))
