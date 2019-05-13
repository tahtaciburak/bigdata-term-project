LATITUDE_PATH="../LocationAverageLatitude"
LONGITUDE_PATH="../LocationAverageLongitude"

try:
    with open(LATITUDE_PATH+"/out_directory/part-r-00000") as f:
        lines = f.readlines()
        cur_line = lines[0]
        cur_line = float(cur_line.replace("\n","").replace("\t","").replace(" ",""))
        latitude = cur_line

    with open(LONGITUDE_PATH+"/out_directory/part-r-00000") as f:
        lines = f.readlines()
        cur_line = lines[0]
        cur_line = float(cur_line.replace("\n","").replace("\t","").replace(" ",""))
        longitude = cur_line
                
except:
    latitude = 0
    longitude = 0
print({"latitude":latitude,"values":longitude})