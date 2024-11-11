import subprocess

subprocess.run(["date"])
subprocess.run(["sleep", "2"])
result = subprocess.run(["sleep", "file_not_real"])
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split()) # can also do it with stderr
print(result.returncode)
print(result.stdout)
print(result.stderr)

import os
my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/"], env=my_env)

result = subprocess.run(["my_app"], env=my_env)