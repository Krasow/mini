import sys
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_dir = sys.argv[1]

data = {"File": [], "Processes": [], "Time": [], "Modularity": [], "Iterations":[], "MODS":[]}
outspec = data_dir + "/*.out"
for fname in glob.glob(outspec):
    print(fname)
    for l in open(fname).readlines():
        if "Average total time" in l:
            s = l.split(":")[-1].split(",")
            data["Time"].append(float(s[0]))
            data["Processes"].append(float(s[1]))
        if "Modularity, #Iterations" in l:
            s = l.split(":")[-1].split(",")
            data["Modularity"].append(float(s[0]))
            data["Iterations"].append(float(s[1]))
        if "MODS" in l:
            s = l.split(":")[-1]
            data["MODS"].append(float(s))
        if "File:" in l:
            s = l.split(":")[-1]
            data["File"].append(s.strip())


df = pd.DataFrame.from_dict(data)
print(df)
