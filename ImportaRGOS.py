##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: John.Fay@duke.edu (for ENV859)
##---------------------------------------------------------------------


# Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'V:\ARGOSTracking\data\ARGOSdata\1997dg.txt'
outputFC = 'V:\ARGOSTracking\scratch\ARGOStrack.shp'

#Open the ARGOS data file for reading
inputFileObj = open(inputFile.'r')

#Get the first line so we can loop
lineString = inputFileObj.readline()
-while lineString:

    if "Date" in lineString:
        print(lineString)

     #Get the next line
    lineString = inputFileObj.readline()
    
