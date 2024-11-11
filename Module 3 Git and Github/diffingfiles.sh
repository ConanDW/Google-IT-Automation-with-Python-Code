diff rearrange1.py reagreeange2.py #diff shows the difference between two files
diff -u validations.py validations2.py #-u is human readable
diff -u old_file new_file > change.diff
patch cpu_usage.py < cpu_usage.diff #use this to apply changes through diff