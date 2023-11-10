import os, glob 
import os.path
import sys
import subprocess
import re
import pandas as pd
import numpy as np

from collections import defaultdict
from itertools import chain
from operator import methodcaller



#### Output all 10k text files into a csv (not clean yet) ####


files = glob.glob("/mnt/c/Users/Jasmin/Documents/MSc-Thesis/Data/ExtractedFeatures/dynamic_features_nodelimit1_mnistnet/*", recursive=True)
#Data\ExtractedFeatures\190623_dynamic_features_nodelimit1
output_dir = glob.glob("/mnt/c/Users/Jasmin/Documents/MSc-Thesis/Data/")[0]

#files = glob.glob("/mnt/c/Users/Jasmin/Documents/MSc-Thesis/Data/mips10k/all_mips/*", recursive=True)


def df_column_uniquify(df):
    df_columns = df.columns
    new_columns = []
    for item in df_columns:
        counter = 0
        newitem = item
        while newitem in new_columns:
            counter += 1
            newitem = "{}_{}".format(item, counter)
        new_columns.append(newitem)
    df.columns = new_columns
    return df


'''

list_of_dicts = []
all_data  = defaultdict(list)

for filename in files:
    lpname = filename.split(".txt")[0].split("/")[-1]
    print(lpname)
    output_list = []
    with open(filename, 'r', encoding = 'utf-8') as f: 
        lines = f.readlines()
        for i in range(len(lines)):
            outline = lines[i].split(':')
            output_list.append(outline)
    f.close()
    
    cols = [item[0] for item in output_list]
    info = [item[1] for item in output_list]
    data = pd.DataFrame(info).T
    data.columns = cols
    data = df_column_uniquify(data)
    data = data.to_dict(orient='list')
    list_of_dicts.append(data)


# iterate dictionary items
#print(list_of_dicts)
dict_items = map(methodcaller('items'), list_of_dicts)
for k, v in chain.from_iterable(dict_items):
    all_data[k].extend(v)

lengths = {key:len(value) for key,value in all_data.items()}
print(lengths)

'''


# Create the dataset with mip_1
for filename in files:
    lpname = filename.split(".txt")[0].split("/")[-1]
    if lpname == 'mip_1':
        print(lpname)
        output_list = []
        with open(filename, 'r', encoding = 'utf-8') as f: 
            lines = f.readlines()
            for i in range(len(lines)):
                outline = lines[i].split(':')
                output_list.append(outline)
        f.close()
    
        cols = [item[0] for item in output_list]
        info = [item[1] for item in output_list]
        data = pd.DataFrame(info).T
        data.columns = cols
        data = df_column_uniquify(data)
    else:
        pass


# Parse through the rest of the data and continueously merge dataframes
for filename in files:
    lpname = filename.split(".txt")[0].split("/")[-1]
    if lpname != 'mip_1':
        print(lpname)
        output_list = []
        with open(filename, 'r', encoding = 'utf-8') as f: 
            lines = f.readlines()
            for i in range(len(lines)):
                outline = lines[i].split(':')
                output_list.append(outline)
        f.close()
    
        cols = [item[0] for item in output_list]
        info = [item[1] for item in output_list]
        mip_instance_data = pd.DataFrame(info).T
        mip_instance_data.columns = cols
        mip_instance_data = df_column_uniquify(mip_instance_data)

        #row_list = mip_instance_data.loc[0, :].values.flatten().tolist()

        data = pd.concat([data, mip_instance_data], ignore_index=True)
        #print('concat data: ',data)
        

        #data.loc[len(data.index)] = row_list
        


    else:
        pass




#print(data.head())
data.to_csv(output_dir + 'dynamic10k_output_mnistnet.csv')



