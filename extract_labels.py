import pandas as pd
import os.path
from os import path

df=pd.read_csv("stage_2_train_labels.csv")
positive=0
negative=0
final_negative=0
for i in range(len(df)) :
	the_file="/home/ubuntu/NASH/dataset/training_data/"+df.loc[i, "patientId"]+".dcm.npy" 
	if (path.exists(the_file)):
		x=df.loc[i, "Target"]
		y=df.loc[i, "patientId"]
		if (x==1):

			positive+=1
			print(the_file, df.loc[i, "Target"])

		else:
			negative+=1
			if (negative %2 ==0 ):
				print(the_file, df.loc[i, "Target"])
				final_negative+=1
			else:
				print(the_file+"_test",  df.loc[i, "Target"])
print("Positiva --> " , positive)
print("Negative --> ",  final_negative)
