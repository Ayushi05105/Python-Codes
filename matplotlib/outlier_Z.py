import numpy as np
import matplotlib.pyplot as plt
#%matplotlib.inline

dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

def detect_outliers(data):
    outliers=[]
   # formula z=(observation - mean)/standard deviation

    threshold=3.5
    mean = np.mean(data)
    std = np.std(data)

    for i in data:
        z_score = (i-mean)/std
        if np.abs(z_score) > threshold:
             outliers.append(i)
    return outliers
            

            
        
outlier_pt = detect_outliers(dataset)
print("Outliers:" ,outlier_pt)
        

