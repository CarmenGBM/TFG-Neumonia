import pandas as pd
import os.path
from os import path
import random
import shutil

#Read the csv file where the dicom data is saved
df=pd.read_csv("stage_2_train_labels.csv")
#Counter for negative diagnosis in pneumonia
negative=0
#Counter for positive diagnosis in pneumonia
positive=0
positive_train=0
positive_test=0
negative_train=0
negative_test=0
test_neumonia = open("/home/ubuntu/NASH/dataset/training_data/test_neumonia.txt","w")
train_neumonia = open("/home/ubuntu/NASH/dataset/training_data/train_neumonia.txt","w")

#For each object in the csv file
for i in range(len(df)) :
    #Name of each file
    the_file="/home/ubuntu/NASH/dataset/training_data/"+df.loc[i, "patientId"]+".dcm.npy" 
    #IN case the file exists
    if (path.exists(the_file)):
        # x is the diagnosis read in the file
        x=df.loc[i, "Target"]
        #In case x is positive diagnosis in pneumonia
        if (x==1):
            #Counter sums one
            positive+=1
            if (positive %2 ==0):
            #Prints the object and the diagnosis
                 positive_train+=1
                 train_neumonia.write(the_file  + " " + str(x) + "\n")
            else:
                 positive_test+=1
                 test_neumonia.write(the_file + " " + str(x) + "\n")
        #In case x is negative diagnosis
        else:
            #Counter sums one
            negative+=1
            if (negative %2 ==0 ):
                 negative_train+=1
                 train_neumonia.write(the_file + " " + str(x) + "\n")
            else:
                 negative_test+=1
                 test_neumonia.write(the_file + " " + str(x) + "\n")

print("Positivos train --> " , positive_train)
print("Positivos test --> " , positive_test)
print("Negative train --> " , negative_train)
print("Negative test --> " , negative_test)
