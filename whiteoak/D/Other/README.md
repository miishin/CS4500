test.sh is a quick bash script that will run the following:

A blank argument:
./xgui
 
A negative integer:
./xgui -1 

A string instead of an integer:
./xgui "string"

Multiple args:
./xgui 100 100

A good input (this is the only one that should display anything):
./xgui 100

The first four should have the program print out 
"usage: ./xgui positve-integer" and error. 

The last test will just run normally
