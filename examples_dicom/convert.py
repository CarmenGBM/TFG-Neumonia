import pydicom
import dicom_numpy
import glob
import numpy as np
import ntpath

#This scripts transform dicom data in a numpy array. Reads each dicom file of the folder and transforms them in a numpy file

#Read all dicom files in the folder
lstFilesDCM=glob.glob("*.dcm")

#For each dicom file in the folder
for i in lstFilesDCM:
    #Read each dicom file in object -ds-
    ds = pydicom.read_file(i)
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
