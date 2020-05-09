#This script counts the number of files with positive diagnosis and negative diagnosis in train.txt and val.txt files

import os.path
from os import path

#Read the txt file
train = open('train.txt','r')
val = open('val.txt','r')

#Counters for training
positive_train = 0
negative_train = 0
#Counters for validation
positive_val = 0
negative_val = 0
#Reading all lines from train.txt
list_train = train.readlines()
#Reading all lines from val.txt
list_val = val.readlines()
#For each line in train.txt
for i in list_train:
        #If the penultimate character of the line is 1 (positive diagnosis)
        if(i[-2]=="1"):
                #Counter positive sums one
                positive_train+=1
        #If the penultimate character of the line is 0 (negative diagnosis)
        if(i[-2]=="0"):
                #Negative counter sums one
                negative_train+=1
#For each line in val.txt
for i in list_val:
        #If the penultimate character of the line is 1 (positive diagnosis)
        if(i[-2]=="1"):
                #Counter sums one
                positive_val+=1
        #If the penultimate character is 0 (negative diagnosis)
        if(i[-2]=="0"):
                #Counter sums one
                negative_val+=1

#Print results
print("Positives train --> " , positive_train)
print("Negatives train --> " , negative_train)
print("Positives val --> " , positive_val)
print("Negatives val --> " , negative_val)


