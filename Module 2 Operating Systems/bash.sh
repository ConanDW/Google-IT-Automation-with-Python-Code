$bober = "Bober kurwa"
# > - Redirect, overwrite >> - redirect, append, < - redirect to standard input, 2> - redirect to stderr

echo "Contents of a file" > test.txt

cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head

#"ctrl + c, for SIGINT, or stop cleanly", "ctrl + z for SIGSTOP or stop imeditatly", "fg to run again cleanly"
# "ps ax to get all process use ex below"
ps ax | grep ping
kill 4619
#cut is a command that extracts fields from a data file. Two examples are:

cut -f1 -d”,” addressbook.csv #This command extracts the first field from a .csv file.

cut -c1-3,5-7,9-12 phones.txt #This command extracts only the digits from a list of phone numbers.

id #for permisions
free -h #free memory

: '

ps: lists the processes executing in the current terminal for the current user

ps ax: lists all processes currently executing for all users  

ps e: shows the environment for the processes listed  

kill PID: sends the SIGTERM signal to the process identified by PID

fg: causes a job that was stopped or in the background to return to the foreground

bg: causes a job that was stopped to go to the background

jobs: lists the jobs currently running or stopped

top: shows the processes currently using the most CPU time (press "q" to quit)  

command > file: redirects standard output, overwrites file

command >> file: redirects standard output, appends to file

command < file: redirects standard input from file

command 2> file: redirects standard error to file

command1 | command2: connects the output of command1 to the input of command2

'
