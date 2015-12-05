#!/usr/bin/python env
import sys,os

print("""
 ┼─┼─┬  ╔═╗╦ ╦╔═╗╦  ╦  ╔═╗╔═╗╔╦╗╔═╗          
─┼─┼─│  ╚═╗╠═╣║╣ ║  ║  ║  ║ ║ ║║║╣           
     o  ╚═╝╩ ╩╚═╝╩═╝╩═╝╚═╝╚═╝═╩╝╚═╝          
        ┌─┐┬ ┬┌┬┐┌─┐   ┌─┐┌┐┌┌─┐┬  ┬┌┐┌┌─┐┬─┐
        ├─┤│ │ │ │ │───│ ││││├┤ │  ││││├┤ ├┬┘
        ┴ ┴└─┘ ┴ └─┘   └─┘┘└┘└─┘┴─┘┴┘└┘└─┘┴└─
          Ever need to write a script and
            you dont have a text editor?
             A python script to write 
              shell scripts using
               nothing but the
                echo command!
                 
            
""")


a = ("_EOS_", "_eos_")
out = str(input("Enter the name of script to write :"))
print("When finsished, type '_EOS_' to close.")
intext = open('oneliner-out','w+').readline()
print(intext)


def write(cmd):
    #cmd = ("echo " + '"' + (cmd)+ '" >> ' + (out) + ";")
    d = open(out, 'a')
    d.write(cmd)
    d.close()
    n = open(out, 'r').readline()
    print(n)

# first command should not append

def main():
    run = "0"
    cmd = str(input("Enter a command: "))
    cmd = ("echo " + '"' + (cmd)+ '" > ' + (out) + ";")
    write(cmd)

    while run == "0":
        cmd = str(input("Enter a command: "))
        if cmd in set (a):
            run = "1"
            t = open(out, 'r').readline()
        
        else:
            cmd = ("echo " + '"' + (cmd)+ '" >> ' + (out) + ";")
            write(cmd)
       
main()
