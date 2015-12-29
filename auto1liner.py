#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys,os,platform
out = ""
print("""
 ┼─┼─┬  ╔═╗╦ ╦╔═╗╦  ╦  ╔═╗╔═╗╔╦╗╔═╗          
─┼─┼─│  ╚═╗╠═╣║╣ ║  ║  ║  ║ ║ ║║║╣           
     o  ╚═╝╩ ╩╚═╝╩═╝╩═╝╚═╝╚═╝═╩╝╚═╝          
        ┌─┐┬ ┬┌┬┐┌─┐   ┌─┐┌┐┌┌─┐┬  ┬┌┐┌┌─┐┬─┐
        ├─┤│ │ │ │ │───│ ││││├┤ │  ││││├┤ ├┬┘
        ┴ ┴└─┘ ┴ └─┘   └─┘┘└┘└─┘┴─┘┴┘└┘└─┘┴└─

$ echo 'For those times when you need to write a script' > evil;
$ echo   'on a remote system, but you don't have a'      >> evil;
$ echo       'text editor, tty, etc...'                  >> evil            
""")

# Why does everone still write everything in python2.x?
def getVersion():
    version = platform.python_version()
    if version < '3.2':
        print("Python 3.2 or later is required. You are running version %s ." % version)
        sys.exit(1)

# Commands are also written to file on your local machine for backup

def write(cmd, out:)
    if not os.path.isfile(out):
        d = open(out, 'w+')
    else:
        d = open(out, 'a')
    d.write(cmd)
    d.close()
    n = open(out, 'r').readline()
    print(n)

# first command should not append
def main():
    a = ("_EOS_", "_eos_")
    out = str(input("Enter the name of script to write: " ))
    print("When finsished, type '_EOS_' to close.")
    intext = open('oneliner-out','w+').readline()
    print(intext)
    run = "0"
    cmd = str(input("Enter a command: "))
    cmd = ("echo " + "'" + (cmd)+ "' > " + (out) + ";")
    write(cmd, out)

    while run == "0":
        cmd = str(input("Enter a command: "))
        if cmd in set (a):
            run = "1"
            # strip the last semicolon as our one liner is done
            with open(out, 'rb+') as filehandle:
                filehandle.seek(-1, os.SEEK_END)
                filehandle.truncate()
            t = open(out, 'r').readline()
            cmd = "\n" # to keep things pretty
            write(cmd, out)
        
        else:
            #cmd = ("echo " + '"' + (cmd)+ '" >> ' + (out) + ";") # if you'd rather double quotes
            cmd = ("echo " + "'" + (cmd)+ "' >> " + (out) + ";")
            write(cmd, out)
            
getVersion()
main()
