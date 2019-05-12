CRIME_TYPE_PATH = "../CrimeType"
with open(CRIME_TYPE_PATH+"/out_directory/part-r-00000") as f:
    lines = f.readlines()
    labels = []
    values = []
    for line in lines:
        sline = line.split("\t")
        if sline[0] != "Description":
            labels.append(sline[0])
            values.append(int(sline[1].replace("\n","")))
    print(labels,values)