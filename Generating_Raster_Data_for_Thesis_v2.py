#!/usr/bin/env python
# coding: utf-8


#Title: Generating Raster Data for Thesis
#Author: Emily Evenden
#May 18, 2020

#####Part 1: Import necessary libraries. 
#The numpy library creates arrays. The PIL library converts arrays in to PNG images. The OS library allows the user to set their working directory.
#You may need to install these libraries using conda install or pip install to run this script.
#This script will output files as .PNG. To open these in TerrSet, you will need to use the GDAL Conversion tool and transform them to .RST.

import numpy as np
from PIL import Image
import os

#Set Working Directory to Folder of Choice. Make sure to double the backslashes.
dir = os.chdir("C:\\Users\\Emily\\Documents\\Masters_Research\\Proposal\\Data\\Jupyter_Notebook_Data")


#####Part 2: Generate Base Array of Ones to build other Files. The dimensions of this array is 100 rows by 110 columns. 
#It is integer data type. It is ordered as 'C' or contiguous. 
#For this project, the value "1" represents the category "non-Agriculture."

#Creates an empty array with the dimension requested
a = np.empty((100,110), int, 'C')
#Fills every position within the array with "1"
np.copyto(a, 1, casting='unsafe')
#Check point to make sure it worked
print (a)


#####Part 3: Created Categorical Variable of Soil Type
#This first section creates an array to represent different Soil Types.
#Soil types will act as the categorical independent variable entered into the MLP neural network.

#This section uses the array created above. This means the first 10 rows are already assigned to the value "1", aka Soil 1.

#The next 20 rows are assigned to the value "2", aka Soil 2
a[10:30,:]= 2
#The next 30 rows are assigned to the value "3", aka Soil 3
a[30:60,:]= 3
#The next 40 rows are assigned to the value "4", aka Soil 4
a[60:100,:]= 4
print (a)

#Output the adjusted "Soil Type" array as a .png file. You will find this in the working folder you assigned above.
im = Image.fromarray(a)
#Change the image name here
im.save("JN_Soil_Type_Arthimetic.png")


#####Part 4: Generate Quantitative Geometric Soil Type Variable
#This is the another independent variable.
#The file is almost the same as the original Soil Type file, but Soil type 3 changes to '4' and Soil Type 4 is changed to "8".

#Assign the old Soil Type 3 to '4'
a[30:60,:]= 4
#The next rows are assigned to the value "8", aka Soil 4
a[60:100,:]= 8
print (a)

#Output the adjusted array as a separate .png file
im = Image.fromarray(a)
#Change the image name here
im.save("JN_Soil_Type_Geometric.png")


#####Part 5: Generates a map of Agriculture at Time 1
#The first 10 columns are "Agriculture" and the remaining 100 columns are "non-Agriculture." 
#This line assigns every row of the first 10 columns to the value 2.
#For this project, the value "2" represents "Agriculture."

#This resets the array we created so every position is 1. 
a[:,:]=1
#Set the first 10 columns to 2, aka "Agriculture".
a[:, 0:10]=2
#Check point
print (a)

#Assign the Agriculture at Time 1 array to a variable and create a .png file. 
im = Image.fromarray(a)
#Change file name here
im.save("JN_Time1.png")


#####Part 5: Generate 4 Maps of Agriculture at Time 2 based on Soil Type.
#This cell is an example of how to create a Time 2 array where the amount of agricultural expansion corresponds with soil type.
##This cell creates the Half-Monotonic Case.
#To change the amount of Agricultural in Time 2, adjust the columns. This allows you to create different scenarios.

#Return the base array to the Time 1 format
a[:,:]=1
a[:, 0:10]=2

#The first 10 rows & 60 columns are assigned to the value "2" for Soil 1.
a[0:10,10:70] = 2
#The next 20 rows & 50 columns are assigned to the value "2" for Soil 2.
a[10:30,10:60]= 2
#The next 30 rows & 40 columns are assigned to the value "2" for Soil 3.
a[30:60,10:50]= 2
#The next 40 rows & 30 columns are assigned to the value "2" for Soil 4. 
a[60:100,10:40]= 2
#Check point
print (a)

#Output the adjusted array as a separate .png file
im = Image.fromarray(a)
#Change file name here
im.save("JN_Time2_Half_Monotonic.png")


##This cell creates the Quarter-Monotonic Case.
#Return the base array to the Time 1 format
a[:,:]=1
a[:, 0:10]=2

#The first 10 rows & 35 columns are assigned to the value "2" for Soil 1.
a[0:10,10:45]=2
#The next 20 rows & 30 columns are assigned to the value "2" for Soil 2.
a[10:30,10:40]= 2
#The next 30 rows & 25 columns are assigned to the value "2" for Soil 3.
a[30:60,10:35]= 2
#The next 40 rows & 20 columns are assigned to the value "2" for Soil 4. 
a[60:100,10:30]= 2
#Check point
print (a)


#Output the adjusted array as a separate .png file
im = Image.fromarray(a)
#Change file name here
im.save("JN_Time2_Quarter_Monotonic.png")


##This cell creates the Cubic Case.
#Return the base array to the Time 1 format
a[:,:]=1
a[:, 0:10]=2

#The first 10 rows & 60 columns are assigned to the value "2" for Soil 1.
a[0:10,10:70] = 2
#The next 20 rows & 30 columns are assigned to the value "2" for Soil 2.
a[10:30,10:40]= 2
#The next 30 rows & 60 columns are assigned to the value "2" for Soil 3.
a[30:60,10:70]= 2
#The next 40 rows & 50 columns are assigned to the value "2" for Soil 4. 
a[60:100,10:60]= 2
#Check point
print (a)

#Output the adjusted array as a separate .png file
im = Image.fromarray(a)
#Change file name here
im.save("JN_Time2_Cubic.png")


##This cell creates the Uniform Empirical Probability Case.
#It assigns every row for columns 11-60 to the value 2. 
#This resets the array to Time 1
a[:,:]=1
a[:, 0:10]=2

#We assign the next 50 columns to  between Time 1 and Time 2 represents agricultural expansion. This creates a uniform empirical probability for each soil.
a[:, 10:60]=2
print (a)

#Output the adjusted array as a separate .png file
im = Image.fromarray(a)
#Change file name here.
im.save("JN_Time2_UniformEP.png")

