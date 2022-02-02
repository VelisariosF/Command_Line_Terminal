from posixpath import split
from random import choice
import sys
import subprocess
import keyboard
import FilesHelper

def interface():
    commandsList = FilesHelper.loadCommandsList("commandsList.txt")
    command = str(input("> "))
    while True :
       if(command.split(" ")[0] == "q"):
           break
       elif (not(command.split(" ")[0] in commandsList) and not(command =="")):
            print(f"try some of the below commands: ")
            for cmd in commandsList:
                print(f"--{cmd}")
            command = str(input("> ")) 
       else:
            p = subprocess.run(f'python subprocess.py {command}', shell=True)
            break
         
                    
    return command

if __name__=="__main__":
     
     print("To exit press q! Have Fun!!")
     while  interface() != "q":
           continue
        
        
    

