##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2024
## Author: fd83@duke.edu
##---------------------------------------------------------------------

# Import packages
import sys, os, arcpy 

# Set input varible (Hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/997dg.txt'
outputFC = 'V:/ARGOSTracking/Scratch/ARGOStrack.shp'