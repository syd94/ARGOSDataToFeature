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
while lineString:

    if "Date" in lineString:
        print(lineString)

        #split the line spring into a list
        lineList = lineString.split()
        
        #get attributes from first line
        tagID = lineList[0]

        #get the next line
        line2String = inputFileObj.readline()
        line2Data = line2String.split ()
        print(line2Data)

        #get attribute from second line
        obsLat = line2Data[2]
        obsLon = line2Data[5]
        print(tagID, obsLat, obsLon)
        break
    


     #Get the next line
    lineString = inputFileObj.readline()
    
#close the file object
inputFileObj.close()