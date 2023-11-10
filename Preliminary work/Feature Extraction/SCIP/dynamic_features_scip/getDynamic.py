from pyscipopt import Model
import os, glob 
import os.path
import sys
import subprocess
import re

#files = glob.glob("/mnt/c/Users/Jasmin/Documents/MSc-Thesis/Data/test_mip/*", recursive=True)
#output_dir = glob.glob("/mnt/c/Users/Jasmin/Documents/MSc-Thesis/Data/test_output/")

files = glob.glob("/mnt/c/Users/Jasmin/Documents/MSc-Thesis/Data/mips10k_mnistnet/*", recursive=True)
output_dir = glob.glob("/mnt/c/Users/Jasmin/Documents/MSc-Thesis/Data/ExtractedFeatures/dynamic_features_nodelimit1_mnistnet/")


for filename in files:
    
    with open(filename, 'r', encoding = 'utf-8') as f: 
        lpname = filename.split(".lp")[0].split("/")[-1] 
        
        lpnumber = int(re.findall(r'\d+', lpname)[0])
        #print('lpnumber:', lpnumber)
        # Set the range of lp's you would like to extract (1 to 1000)
        if 1000 >= lpnumber >= 1:
            print('lpname:', lpname)
            model = Model(lpname)
            # Set node limit to 1
            model.setParam('limits/nodes', 1)
            # Read LP problem
            model.readProblem(filename)
            # solve the lp problem
            model.optimize()
            # print solving statistics
            model.printStatistics()
            # Output dynamic features
            outputFileName = lpname + '.txt'
            outfile = output_dir[0] + outputFileName

            # write statistics to outfile
            model.writeStatistics(filename=outfile)
        else: 
            pass
         

    f.close()
