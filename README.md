# auto1liner
A (completely useless) python script for generating *nux "one-liner" commands. It's useful for situations when you have a shell, but you're not on a TTY, or for whatever reason you can't use vi or nano, but you need to write a script to the remote system.

# Example:



echo "#!/bin/bash" >> out.sh;echo "while true" >> out.sh;echo "do" >> out.sh;echo "./tmp/evilstuff" >> out.sh;echo "sleep 1000" >> out.sh;echo "done" >> out.sh; ./out.sh


