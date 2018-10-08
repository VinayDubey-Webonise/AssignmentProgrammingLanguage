'''
******For this perticular scenario we have a small game which tests your memory******

Language: python
Why python : Considering this perticular scenario

            1) Python Memory management for the small programs is more efficient. 
               Python Virtual Machine handles the memory needed and decides where it'll be placed in the memory layout.
               
            2) Large amount of third party modules.
            
            3) More suitable for single thread program like this perticular game.
        
            4) Cross platform support. Below program can easily be converted to a Windows executable program and can be 
               used as a native Windows program.

'''
from time import sleep 
from os import system,name
from random import randrange
    
def clear_window():
    if name == "nt":
        system('cls')
    else:
        system('clear')


print("Remember the digits flashing on the screen")

clear_window() # function to clear the window before printing new number

list_of_no=[]

for i in range(4):
    list_of_no.append(randrange(10,50,3))

for i in list_of_no:
    clear_window()
    print(i);
    sleep(2);

print("Enter the sequence of number you've seen:")

did_failed="no"

for i in list_of_no:
    print(i)
    if(int(input("enter your no."))!=i):
        clear_window()
        print("Agh! your memory is not sharp enough")
        did_failed="yes"
        break
    

if(did_failed=="no"):
    clear_window()
    print("Wooo! your memory is sharp")



'''
****Line no. 29:****

        calling print() will push the function to stack 

        stack ={printf(),}
        top=0

        Once printf() returns char stream, pop the stack with printf()
        top =-1
        stack={}

****Line no. 30****

        push clear_window() to the top of the stack
        stack ={clear_window(),}
        top = 0

        push system() to stack
        stack = {clear_window(), system()}
        top = 1 

        system(cls)/system(clear) will clear the screen
        pop system() from stack
        stack = {clear_window()}
        top = 0

        pop clear_window() from stack
        stack = {}
        top = -1

****Line no. 35****

        push list_of_no.append() to stack
        stack= {list_of_no.append(), randrange()}
 
        range=0
        list_of_no [23] Assuming the random numbers

        pop randrange()
        stack = {list_of_no.append()}
        pop list_of_no.append()
        stack = {}

        push list_of_no.append() to stack
        stack= {list_of_no.append(), randrange()}

        range=1
        list_of_no [23,64]

        pop randrange()
        stack = {list_of_no.append()}
        pop list_of_no.append()
        stack = {}

        push list_of_no.append() to stack
        stack= {list_of_no.append(), randrange()}

        range=2
        list_of_no [23,64,55]

        pop randrange()
        stack = {list_of_no.append()}
        pop list_of_no.append()
        stack = {}

        push list_of_no.append() to stack
        stack= {list_of_no.append(), randrange()}

        range=3
        list_of_no [23,64,55,7]

        pop randrange()
        stack = {list_of_no.append()}
        pop list_of_no.append()
        stack = {}

****Line no. 38****

        push clear_window() to the top of the stack
        stack ={clear_window()}
        top = 0

        push system() to stack
        stack = {clear_window(), system()}
        top = 1 

        system(cls)/system(clear) will clear the screen
        pop system() from stack
        stack = {clear_window()}
        top = 0

        pop clear_window() from stack
        stack = {}
        top = -1


        calling print() will push the function to stack 

        stack ={printf(),}
        top=0

        Once printf() returns char stream, pop the stack with printf()
        top =-1
        stack={}

****Line no. 47****

        calling print() will push the function to stack 

        stack ={printf(),}
        top=0

        Once printf() returns char stream, pop the stack with printf()
        top =-1
        stack={}
        
        push input() on stack for input stream.
        Check if value matches to the list_of_no[0]
        
        Repeats the process for 4 times and break if user enters mismatch value
        
        push clear_window() to the top of the stack
        stack ={clear_window()}
        top = 0

        push system() to stack
        stack = {clear_window(), system()}
        top = 1 

        system(cls)/system(clear) will clear the screen
        pop system() from stack
        stack = {clear_window()}
        top = 0

        pop clear_window() from stack
        stack = {}
        top = -1

'''


