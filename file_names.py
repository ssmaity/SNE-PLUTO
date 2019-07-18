# isolate r data from data files

from numpy import loadtxt
from math import pow

f=open("files.dat","r")
fnames=f.read()
f.close()

names = fnames.splitlines()

for i in range(1,len(names)):
	print(names[i])
