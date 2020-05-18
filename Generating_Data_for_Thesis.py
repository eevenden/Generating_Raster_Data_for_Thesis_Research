#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Author: Emily Evenden
#May 18, 2020

#Import necessary libraries
import numpy as np
from PIL import Image
import os


# In[3]:


#Set Working Directory to Folder of Choice. Make sure to double the backslashes.
dir = os.chdir("C:\\Users\\Emily\\Documents\\Masters_Research\\Proposal\\Data\\Jupyter_Notebook_Data")


# In[4]:


#Generate Base Array of Ones to build other Files. The dimensions of this array is 100 rows by 110 columns. 
#It is integer data type. It is ordered as 'C' or contiguous. 
#For this project, the value "1" represents the category "non-Agriculture."

a = np.empty((100,110), int, 'C')
np.copyto(a, 1, casting='unsafe')
print (a)


# In[5]:


#This first section creates an array to represent Soil Types. 
#This is the categorical driver that will be entered into the MLP neural network.
#The first 10 rows are already assigned to the value "1", aka Soil 1
#The next 20 rows are assigned to the value "2", aka Soil 2
a[10:30,:]= 2
#The next 30 rows are assigned to the value "3", aka Soil 3
a[30:60,:]= 3
#The next rows are assigned to the value "4", aka Soil 4
a[60:100,:]= 4
print (a)


# In[6]:


#Output the adjusted array as a separate .png file
im = Image.fromarray(a)
im.save("JN_Soil_Type.png")


# In[7]:


#The second section generates a map of Agriculture at Time 1 Data. The first 10 columns are "Agriculture" and the remaining 100 columns are "non-Agriculture." 
#This line assigns every row of the first 10 columns to the value 2.
#For this project, the value "2" represents "Agriculture."
a[:,:]=1
a[:, 0:10]=2
print (a)


# In[8]:


#Assign the array to a variable and create a .png file with the dimensions and values of the array. 
#This will appear in the output folder.

im = Image.fromarray(a)
im.save("JN_Time1.png")


# In[9]:


#This cell creates an array which represents Time 2 where each soil category has an uniform empirical probability.
#It assigns every row for columns 11-60 to the value 2. 
#This increase in value 2 between Time 1 and Time 2 represents agricultural expansion. 
a[:, 10:61]=2
print (a)


# In[10]:


#Output the adjusted array as a separate .png file
im = Image.fromarray(a)
im.save("JN_Time2_UniformEP.png")


# In[11]:


#This cell is an example of how to create a Time 2 array where the amount of agricultural expansion corresponds with soil type.
#This example specifically creates the Half-Monotonic Scenario.
#To change the amount of Agricultural in Time 2, adjust the columns.

#Return the base array to the Time 1 format
a[:,:]=1
a[:, 0:10]=2

#The first 10 rows are already assigned to the value "1", aka Soil 1
a[0:10,10:70] = 2
#The next 20 rows are assigned to the value "2", aka Soil 2
a[10:30,10:60]= 2
#The next 30 rows are assigned to the value "3", aka Soil 3
a[30:60,10:50]= 2
#The next rows are assigned to the value "4", aka Soil 4
a[60:100,10:40]= 2
print (a)


# In[12]:


#Output the adjusted array as a separate .png file
im = Image.fromarray(a)
im.save("JN_Time2_Half_Monotonic.png")


# In[ ]:




