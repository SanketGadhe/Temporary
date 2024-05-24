import os
print('Process id before fork',os.getpid())
pid=os.fork()
if(pid==0):
    print('After fork Child Process ID',os.getpid())
elif(pid==-1):
    print('Fork Failed')
else:
    print('After fork Parent Process ID',os.getpid())
