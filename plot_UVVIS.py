#!/usr/bin/python
# Anna Tomberg
# Plot UV-VIS spectrum from orca_mapspc using *.out.abs.dat file generated by orca_mapscp

# Last updated : 05-01-2015

import sys
import matplotlib.pyplot as plt


# ------------- GET INPUT FILE ------------- #	
if len(sys.argv) <= 1:
	name = raw_input("Enter path to input: ")
else:
	name = sys.argv[1] 

# ---------------- GET DATA ---------------- #		
fo = open(name, "r")
lines = fo.readlines()
fo.close()

wavelength = []
intensity = []
electric_dipole = []
magnetic_dipole = []
quadrupole = []

for line in lines:
	t = line.split()	
	if len(t) == 5:
		wavelength.append(t[0])
		intensity.append(t[1])
		electric_dipole.append(t[2])
		magnetic_dipole.append(t[3])
		quadrupole.append(t[4])
# ------------------------------------------ #


# ------------- PLOTTING STUFF ------------- #			

plt.figure()
plt.plot(wavelength,intensity, 'r-')	
plt.title("Absorption Spectrum")
plt.show()

