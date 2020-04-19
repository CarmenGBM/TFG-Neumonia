import pandas as pd
import os.path
from os import path

#Read the csv file where the dicom data is saved
df=pd.read_csv("stage_2_train_labels.csv")
#Counter for positive diagnosis in pneumonia
positive=0
#COunter for negative diagnosis in pneumonia
negative=0
final_negative=0
#For each object in the csv file
for i in range(len(df)) :
	#Name of each file
	the_file="/home/ubuntu/NASH/dataset/training_data/"+df.loc[i, "patientId"]+".dcm.npy" 
	#IN case the file exists
	if (path.exists(the_file)):
		# x is the diagnosis read in the file
		x=df.loc[i, "Target"]
		# y es the name of the file 
		y=df.loc[i, "patientId"]
		#In case x is positive diagnosis in pneumonia
		if (x==1):
			#Counter sums one
			positive+=1
			#Prints the object and the diagnosis
			print(the_file, df.loc[i, "Target"])
		#In case x is negative diagnosis
		else:
			#Counter sums one
			negative+=1
			if (negative %2 ==0 ):
				print(the_file, df.loc[i, "Target"])
				final_negative+=1
			else:
				print(the_file+"_test",  df.loc[i, "Target"])
print("Positiva --> " , positive)
print("Negative --> ",  final_negative)
