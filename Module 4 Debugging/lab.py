#!/usr/bin/env python3


import subprocess
from multiprocessing import Pool
import os

cwd = os.getcwd()
src = os.path.join(cwd, "data/prod/")
dest = os.path.join(cwd, "data/prod_backup/")
files = next(os.walk(src))[1]


def run(file):
  local = os.path.join(src, file)
  subprocess.call(["rsync", "-arq", local, dest])


p = Pool(len(files))
p.map(run, files)