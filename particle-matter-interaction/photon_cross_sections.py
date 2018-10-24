#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt 

filename = 'Carbon.txt'

#f = open(filename,'r')

data = np.loadtxt(filename)

labels = ['Coherent (Rayleigh)', 'Incoherent (Compton)', 'Photoeffect', 'Pair production (nuclear)', 'Pair production (electron)'] 

plt.figure()

i=0
for l in labels:
	plt.plot(data[:,0], data[:,i+1], label=labels[i])
	i += 1

plt.xlabel('Energy [MeV]')
plt.ylabel('Cross-section $\mu$ [cm$^2$/g]')

leg=plt.legend(loc='best')
plt.xscale('log')
plt.yscale('log')
#plt.show()

plt.savefig("cross-sections.png")
