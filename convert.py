import pydicom
import dicom_numpy
import glob
import numpy as np
import ntpath



lstFilesDCM=glob.glob("*.dcm")


for i in lstFilesDCM:
    ds = pydicom.read_file(i)
    filename=ntpath.basename(i)
    ConstPixelDims = (int(ds.Rows), int(ds.Columns))
    ArrayDicom = np.zeros(ConstPixelDims, dtype=ds.pixel_array.dtype)
    ArrayDicom[:, :] = ds.pixel_array
    final_array=np.stack((ArrayDicom,)*3, axis=-1)
    np.save(filename, final_array)
