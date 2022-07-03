import subprocess

res = subprocess.call(["ls","-l"])
print(res)

res1 = subprocess.call("ls -l",shell=True)
print(res1)