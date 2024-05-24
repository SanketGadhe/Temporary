import os
import time
p = os.fork()
if p == 0:
    print(f"\nI am a child process with PID: {os.getpid()}")
    time.sleep(1)
    print(f"\nI am the parent of child process with PID: {os.getpid()}")
else:
    print(f"\nI am a parent process with PID: {os.getpid()}")
    print(f"\nI am the parent's parent process with PID: {os.getpid()}")

