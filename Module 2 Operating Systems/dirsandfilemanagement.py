import os 
import datetime
os.remove("novel.txt")

os.rename("first_draft.txt", "finished.txt")


os.path.exists("finished.txt")

os.path.exists("userlist.txt")


os.path.getsize("finish.txt") #size is in bites

os.path.getmtime("spider.txt") #unix time stamp
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp) #get actual date
os.path.abspath("spider.txt") #get absolute path

print(os.getcwd) #get pwd
os.mkdir("new_dir")
os.chdir("new_dir")
os.getcwd()
os.rmdir("new_dir")
os.listdir("new_dir") #list files and sub dirs

#find out if file or di
dir = "new_dir"
for name in os.listdir(dir):
  fullname = os.path.join(dir, name) #allows us to bypass windows and linux differences in file paths 
  if os.path.isdir(fullname):
    print("{} is a file".format(fullname))
  else:
    print("{} is a file".format(fullname))