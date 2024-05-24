import os
pid = os.fork()
print(pid)
if pid < 0:
    print("Fork failed")
elif pid == 0:
    os.execlp("/bin/ls", "ls")
else:
    os.wait()
    print("Child complete")