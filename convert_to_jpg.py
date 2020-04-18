import matplotlib.pyplot as plt
import matplotlib.image as mpimage
import pydicom as dicom
import os

#Mark True if we want to obtain JPG format, in other case, it will be  in PNG 
JPG = True
#Specify the dicom folder
folder_path = "home/ubuntu/NASH/dataset/examples_dicom/"
#Create the output folder path
os.mkdir("home/ubuntu/NASH/dataset/examples_dicom/jpg_pictures/")
#Specify the output jpg/png folder path
jpg_folder_path = "home/ubuntu/NASH/dataset/examples_dicom/jpg_pictures/"
#For each imaage in the folder path
for n, image in enumerate(images_path):
    #Read each dicom file
    ds = dicom.dcmread(os.path.join(folder_path, image))
    #Read the dimension of the dicom file
    pixel_array_numpy = ds.pixel.array
    #In case we want JPG images, JPG is True
    if JPG == True:
        #Change format from dicom to JPG
        image = image.replace('.dcm', '.jpg')
    #If we want a PNG format inseatd of JPG, so JPG is been set as False
    else
        image = image.replace('.dcm', '.png')
    #Save the new image in the output folder
    plt.imsave(os.path.join(jpg_folder_path, image), ds.pixel_array, cmap=plt.cm.gray)
