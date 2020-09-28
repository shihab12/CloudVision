import pandas as pd
import numpy as np

import glob, os

print("Max detected for {}, {}, {}, {}, {}, {}, {}, {}".format('camera', 'traffic light',  'car','bus',  'truck',  'person', 'bicycle', 'total'))
for f in glob.glob("data_out/*.csv"):
    #f = "data_out/GEN100.csv"
    df =  pd.read_csv(f)
    df['total'] = df['traffic light']+  df['car'] +df ['bus']+  df['truck']+  df['person'] + df['bicycle']
    print("{}, {}, {}, {}, {}, {}, {}, {}".format(f, max(df['traffic light']),  max(df['car']),max(df ['bus']),  max(df['truck']),  max(df['person']), max(df['bicycle']), max(df['total']))) 
