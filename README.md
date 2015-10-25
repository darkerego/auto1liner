# auto1liner
A python script for generating *nux "one-liner" commands. It's useful for situations when you have a shell, but you're not on a TTY, or for whatever reason you can't use vi or nano, but you need to write a script to the remote system.

# Example:

Enter the name of script to write :out.sh
Enter commands, one line at a time. (Enter OK or ok when done).
touch out.sh ;
: #!/bin/bash
echo "#!/bin/bash" >> out.sh;
: while true
echo "while true" >> out.sh;
: do
echo "do" >> out.sh;
: ./tmp/evilstuff
echo "./tmp/evilstuff" >> out.sh;
: sleep 1000
echo "sleep 1000" >> out.sh;
: done
echo "done" >> out.sh;
: OK
>>> 

Now you copy and paste and you got:

echo "#!/bin/bash" >> out.sh;echo "while true" >> out.sh;echo "do" >> out.sh;echo "./tmp/evilstuff" >> out.sh;echo "sleep 1000" >> out.sh;echo "done" >> out.sh; ./out.sh

And wala!


