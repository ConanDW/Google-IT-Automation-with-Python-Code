import psutil
import subprocess
psutil.cpu_percent() #grab cpu usage
psutil.disk_io_counters() #grab byte read and byte write
psutil.net_io_counters()


src = "<source-path>" # replace <source-path> with the source directory
dest = "<destination-path>" # replace <destination-path> with the destination directory
subprocess.call(["rsync", "-arq", src, dest]) #use rsync in python
