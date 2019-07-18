# plot of numerical data

from numpy import loadtxt, log, linspace
import matplotlib.pyplot as plt

tdata = linspace(0.0001,0.001,10)
rdata = loadtxt('rdata.dat')

pc = 3.086e18
yr = 3.15e7	
t = pc/1.e5

plt.plot(tdata*t/yr,rdata,'b.')
plt.xlabel('time (in yr)')
plt.ylabel('distance (in pc)')
plt.title('Distance vs Time graph of Supernova explosion')
plt.savefig('t-r.png')
