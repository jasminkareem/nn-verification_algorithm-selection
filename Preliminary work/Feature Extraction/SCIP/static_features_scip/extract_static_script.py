import os, glob 
import os.path
import sys
import subprocess

    
# list all files including subfolders
#files = glob.glob("/mnt/c/Users/Jasmin/Documents/MSc-Thesis/Data/test_mip/*", recursive=True)
#output_dir = glob.glob("/mnt/c/Users/Jasmin/Documents/MSc-Thesis/Data/test_output/")
files = glob.glob("/mnt/c/Users/Jasmin/Documents/MSc-Thesis/Data/all_mips_mnistnet/*", recursive=True)
output_dir = glob.glob("/mnt/c/Users/Jasmin/Documents/MSc-Thesis/Data/ExtractedFeatures/extracted_features_presolve_default_scip_mnistnet/")
    
for filename in files:
    with open(filename, 'r', encoding = 'utf-8') as f:
        settingsCmd = " -s /mnt/c/Users/Jasmin/Documents/MSc-Thesis/Feature_Extraction/feature_extractor/settings/presolv-default.set"
        command = "./feature-extractor -p " + filename  + settingsCmd
        outputFileName = filename.split(".lp")[0].split("/")[-1] + ".txt"
        print(outputFileName)
        result = subprocess.run([command], shell=True, capture_output=True, text=True)
        outfile = output_dir[0] + outputFileName
        with open(outfile, "w") as out:
            out.write(result.stdout)
            out.close()

    f.close()



