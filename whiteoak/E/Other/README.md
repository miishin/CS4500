Testing is a bit awkward because there is one command (./xctp 12345) to run 
in one window and another (netcat) to run in the other. 

Output returned was captured by doing (for example):

cat n-in.json | nc hostname port > testn-out.json 

Then the output file can be compared to our test case:

diff testn-out.json n-out.json -w

As for ./xtcp, quick tests (in inputtests.sh) check if a string instead 
of a port number, if multiple args are caught, and if invalid port numbers 
(numbers less than 1024 or greater than 65535) are caught. 

Some extra tests in ctests/ are used to check for correctness for assignment "C" 
because we had to rewrite it in Python for this project since we wrote it in other 
langauges with our old partners. 
