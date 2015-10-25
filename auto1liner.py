#!/usr/bin/python env


print("""

─┼─┼─┬  ╔═╗╦ ╦╔═╗╦  ╦  ╔═╗╔═╗╔╦╗╔═╗          
─┼─┼─│  ╚═╗╠═╣║╣ ║  ║  ║  ║ ║ ║║║╣           
     o  ╚═╝╩ ╩╚═╝╩═╝╩═╝╚═╝╚═╝═╩╝╚═╝          
        ┌─┐┬ ┬┌┬┐┌─┐   ┌─┐┌┐┌┌─┐┬  ┬┌┐┌┌─┐┬─┐
        ├─┤│ │ │ │ │───│ ││││├┤ │  ││││├┤ ├┬┘
        ┴ ┴└─┘ ┴ └─┘   └─┘┘└┘└─┘┴─┘┴┘└┘└─┘┴└─
          Ever need to write a script and
            you dont have a text editor
            (for whatever reason...)?


""")


a = ("OK", "ok")
out = str(input("Enter the name of script to write :"))
print("Enter commands, one line at a time. (Enter OK or ok when done).")
print("touch %s ;" % out)
run = "0"
while run == "0":
    cmd = str(input(": "))
    if cmd in set (a):
        run = "1"
    else:
       print("echo " + '"' + (cmd)+ '" >> ' + (out) + ";")
