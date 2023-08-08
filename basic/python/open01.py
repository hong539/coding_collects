# Why cant I create a directory in /sys
# https://askubuntu.com/questions/341939/why-cant-i-create-a-directory-in-sys
with open('./sys/debug/logfile', 'r') as f:
    content = f.read()
    print(content)
