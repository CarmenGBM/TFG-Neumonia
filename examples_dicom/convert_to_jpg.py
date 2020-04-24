import matplotlib.pyplot as plt
import matplotlib.image as mpimage
import pydicom
import ntpath
import numpy as np
import dicom_numpy
import glob
import os

#Mark True if we want to obtain NUMPY format, in other case, it will be in JPG
NUMPY = False
#Specify the dicom folder
lstFilesDCM=glob.glob("*.dcm")
#Specify the output jpg/png folder path
jpg_folder_path = "/home/ubuntu/NASH/dataset/examples_dicom/"
#For each image in the folder path
for i in lstFilesDCM:
    #Read each dicom file
    ds = pydicom.read_file(i)
    if (NUMPY == True):    
        #Maps filename with the base name of each dicom file in the folder 
        filename=ntpath.basename(i)
        #Load spaceing values:  dimension of dicom's  rows and columns
        ConstPixelDims = (int(ds.Rows), int(ds.Columns))
        #Array is sized based on -ConstPixelDims-
        ArrayDicom = np.zeros(ConstPixelDims, dtype=ds.pixel_array.dtype)
        #Store gross  image data
        ArrayDicom[:,:] = ds.pixel_array
        #Stacks in final_array array three times ArrayDicom, due to color images RBG
        final_array=np.stack((ArrayDicom,)*3, axis=-1)
        #Save numpy file with the file name and the array
        np.save(filename, final_array)
    else:
        #Read the dimension of the dicom file
        pixel_array_numpy = ds.pixel_array
        #Change format from dicom to JPG
        i = i.replace('.dcm', '.jpg')
       #Save the new image in the output folder
        plt.imsave(os.path.join(jpg_folder_path, i), ds.pixel_array, cmap=plt.cm.gray)
