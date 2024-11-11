
#!/usr/bin/env python3

import sys
import subprocess
path = "/home/student@7dba33ea494d"
with open(sys.argv[1], "r") as f:
        for filename in f.readlines():
                OldFilename = filename.strip()
                NewFilename = OldFilename.replace("jane", "jdoe")
                subprocess.run(["mv",path+OldFilename,path+NewFilename])
        f.close()
        