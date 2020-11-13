#!/usr/bin/python
# Anna Tomberg
# Plot info from orca run using *.out file

# Last updated : 02-12-2015

import sys
import re
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# ------------- GET INPUT FILE ------------- #	
if len(sys.argv) <= 1:
	name = raw_input("Enter path to input: ")
else:
	name = sys.argv[1] 
	
fo = open(name, "r")
# ------------------------------------------ #


# -------------- EXTRACT INFO -------------- #	
counter = 0
Energy = []

E_change = []
E_threshold = []

MaxStep = []
MaxStep_threshold = []

MaxGrad = []
MaxGrad_threshold = []

RMSStep = []
RMSStep_threshold = []

RMSGrad = []
RMSGrad_threshold = []

E_1st_SCF_cycle = []
Change_1st_SCF_cycle = []

lines = fo.readlines()
fo.close()

for line in lines:
	counter += 1
	
	if line.startswith("FINAL SINGLE POINT ENERGY"):	#ENERGY (1)
		Energy.append(line.split()[4])
		
	elif line.startswith("          Energy change"):	#ENERGY CHANGE (2)
		E_change.append(line.split()[2])
		E_threshold.append(line.split()[3])
		
	elif line.startswith("          MAX gradient"):		#MAX GRADIENT (3)
		MaxGrad.append(line.split()[2])
		MaxGrad_threshold.append(line.split()[3])
		
	elif line.startswith("          MAX step"):			#MAX STEP (4)
		MaxStep.append(line.split()[2])
		MaxStep_threshold.append(line.split()[3])
		
	elif line.startswith("          RMS gradient"):		#RMS GRADIENT (5)
		RMSGrad.append(line.split()[2])
		RMSGrad_threshold.append(line.split()[3])
		
	elif line.startswith("          RMS step"):			#RSM STEP (6)
		RMSStep.append(line.split()[2])
		RMSStep_threshold.append(line.split()[3])
	
	elif line.startswith("                         !        ITERATION"):	#1st SCF cycle (7)
		E_1st_SCF_cycle.append(lines[counter+1].split()[3])
		Change_1st_SCF_cycle.append(lines[counter+2].split()[3])
# ------------------------------------------ #

#----------- str to float ------------------------- #

Energy=[float(i) for i in Energy]
E_change=[float(i) for i in E_change]
E_threshold=[float(i) for i in E_threshold]
MaxGrad=[float(i) for i in MaxGrad]
MaxGrad_threshold=[float(i) for i in MaxGrad_threshold]
MaxStep=[float(i) for i in MaxStep]
MaxStep_threshold=[float(i) for i in MaxStep_threshold]
RMSGrad=[float(i) for i in RMSGrad]
RMSGrad_threshold=[float(i) for i in RMSGrad_threshold]
RMSStep=[float(i) for i in RMSStep]
RMSStep_threshold=[float(i) for i in RMSStep_threshold]
E_1st_SCF_cycle=[float(i) for i in E_1st_SCF_cycle]
Change_1st_SCF_cycle=[float(i) for i in Change_1st_SCF_cycle]

# print(Energy)
# print(E_change)
# print(E_threshold)
#--------------------------------------------#

# ------------- PLOTTING STUFF ------------- #			
# If only SCF cycle, plot OPTION 1.
# If got passed 1st SCF cycle, plot OPTION 2.
# ------------------------------------------ #	

# OPTION 1:
if E_change == []:

	del Change_1st_SCF_cycle[0]
	
	plt.figure()
	
	ax = plt.subplot(211)	
	plt.title("1st SCF CYCLE Energy")
	ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
	ax.plot(list(range(1, len(E_1st_SCF_cycle)+1)), E_1st_SCF_cycle, 'ro-')
	
	plt.subplot(212)
	plt.title("1st SCF CYCLE Energy Change")
	plt.plot(list(range(1, len(Change_1st_SCF_cycle)+1)), Change_1st_SCF_cycle, 'bo-')


# OPTION 2:
else:
	plt.figure(figsize=(20,10))
	plt.subplot(321)
	plt.title("Energy Change")
	plt.plot(list(range(1, len(E_change)+1)), E_change, 'ro--', list(range(1, len(E_threshold)+1)), E_threshold, 'bo--')

	ax = plt.subplot(322)
	plt.title("SCF Energy")
	ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
	ax.plot(range(len(Energy)), Energy, 'ro--')

	plt.subplot(323)
	plt.title("Max Gradient")
	plt.plot(range(len(MaxGrad)), MaxGrad, 'go--', range(len(MaxGrad_threshold)), MaxGrad_threshold, 'bo--')

	plt.subplot(324)
	plt.title("Max Step")
	plt.plot(range(len(MaxStep)), MaxStep, 'go--', range(len(MaxStep_threshold)), MaxStep_threshold, 'bo--')

	plt.subplot(325)
	plt.title("RMS Gradient")
	plt.plot(range(len(RMSGrad)), RMSGrad, 'yo--', range(len(RMSGrad_threshold)), RMSGrad_threshold, 'bo--')

	plt.subplot(326)
	plt.title("RMS Gradient")
	plt.plot(range(len(RMSStep)), RMSStep, 'yo--', range(len(RMSStep_threshold)), RMSStep_threshold, 'bo--')

plt.show()

