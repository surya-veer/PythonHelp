import sys,os
os.makedir("suryaveer")
sys.stderr.write("I am an error \n")
sys.stderr.flush()
sys.stdout.write("I amm not an error!\n")

argList = sys.argv
#print(argList)
for ci in argList:
	print(ci)
