#!/bin/bash
line="-----------------"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; UPTIME; echo $line


echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finish: $(date)"

if grep "127.0.0.1" /etc/hosts; then
    echo "Everything is ok"
else 
    echo "ERROR: LOCAHOST NOT IN HOSTS FILE"
fi

if test -n "$PATH"; then echo "PATH is empty"; fi

if [ -n "$PATH" ]; then echo "Your path is empty"; fi
n=1
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1))
done

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
    sleep $n
    ((n+=1))
    echo "Retry #$n"
done

for fruit in apple, pear, grape; do 
    echo "The fruit is $fruit"
done

basename index.htm .html #use basename to get the file name without extension
for file in *.HTM; do 
    name=$(basename "$file" .HTM)
    mv "$file" "$name.html" #use echo for -whatif in pwsh ex: echo  mv "$file" "$name.html"
done

for logfile in /var/log/*log; do 
    echo "Processing $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done