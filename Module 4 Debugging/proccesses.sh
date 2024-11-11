for pid in $(pidof ffmpeg); do renice 19 $pid; done; #19 is the lowest process priority you can do, renice reassigns priority for running processes.
#nice does it for not runing. pidoff grabs a process pid via name

for pid in $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done; done;