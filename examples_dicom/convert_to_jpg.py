import matplotlib.pyplot as plt
import matplotlib.image as mpimage
import pydicom as dicom
import glob
import os

#Mark True if we want to obtain JPG format, in other case, it will be  in PNG 
JPG = True
#Specify the dicom folder
lstFilesDCM=glob.glob("*.dcm")
#Specify the output jpg/png folder path
jpg_folder_path = "/home/ubuntu/NASH/dataset/examples_dicom/"
#For each image in the folder path
for i in lstFilesDCM:
    #Read each dicom file
    ds = dicom.read_file(i)
    #Read the dimension of the dicom file
    pixel_array_numpy = ds.pixel_array
    #In case we want JPG images, JPG is True
    if JPG == True:
        #Change format from dicom to JPG
        i = i.replace('.dcm', '.jpg')
    #If we want a PNG format instead of JPG, so JPG is been set as False
    else:
        i = i.replace('.dcm', '.png')
    #Save the new image in the output folder
    plt.imsave(os.path.join(jpg_folder_path, i), ds.pixel_array, cmap=plt.cm.gray)
