# isolate r data from data files

from numpy import loadtxt
from math import pow

f=open("newfiles.dat","r")
fnames=f.read()
f.close()

names = fnames.splitlines()

for name in names:
	data = loadtxt(name)
	r_data = data[:,0]
	rho_data = data[:,2]
	for i in range(len(rho_data)):
		 if rho_data[i]==max(rho_data):
		 	print(r_data[i])
		 	break
