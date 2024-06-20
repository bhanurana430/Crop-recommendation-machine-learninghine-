import pandas as pd 
import numpy as np 
import os 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("Crop_recommendation.csv")
print(df.head())

print(df.describe())