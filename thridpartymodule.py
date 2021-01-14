import os
import time
import pandas
data_path = "files/temps_today.csv"

if os.path.exists(data_path):
    with open(data_path) as myfile:
        data = pandas.read_csv(data_path)
        print(data)
        print(data.mean()["st1"])
           
    
else:
    print("Files doesn't exists")



    