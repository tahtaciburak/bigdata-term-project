from flask import Flask, render_template
from flask import jsonify

import os
app = Flask(__name__)

CRIME_TYPE_PATH="../CrimeType"
ARREST_TYPE_PATH="../Arrest"
YEAR_PATH="../Year"
FBI_CODE_PATH="../FBICode"

@app.route("/")
def main():
    return render_template('index.html')

########FBICODE START
@app.route("/fbi_code/start")
def start_fbi_code():
    os.system("cd ../FBICode && ls && ./run.sh")
    return "bitti"

@app.route("/fbi_code")
def get_fbi_code_data():
    labels = []
    values = []
    try:
        with open(FBI_CODE_PATH+"/out_directory/part-r-00000") as f:
            lines = f.readlines()
            for line in lines:
                sline = line.split("\t")
                if sline[0] != "FBI Code":
                    labels.append(sline[0])
                    values.append(int(sline[1].replace("\n","")))
    except:
        labels = []
        values = []
    return jsonify({"labels":labels,"values":values})

@app.route("/fbi_code/delete")
def delete_dbi_code_data():
    os.system("rm -fr "+FBI_CODE_PATH+"/out_directory")
########FBICODE END


########YEAR START
@app.route("/year/start")
def start_year():
    os.system("cd ../Year && ls && ./run.sh")
    return "bitti" 

@app.route("/year")
def get_year_data():
    labels = []
    values = []
    try:
        with open(YEAR_PATH+"/out_directory/part-r-00000") as f:
            lines = f.readlines()
            for line in lines:
                sline = line.split("\t")
                if sline[0] != "Updated On":
                    labels.append(sline[0])
                    values.append(int(sline[1].replace("\n","")))
    except:
        labels = []
        values = []
    return jsonify({"labels":labels,"values":values}) 

@app.route("/year/delete")
def delete_year_data():
    os.system("rm -fr "+YEAR_PATH+"/out_directory")
########YEAR END

########ARREST START
@app.route("/arrest_type/start")
def start_arrest_type():
    os.system("cd ../Arrest && ls && ./run.sh")
    return "bitti" 

@app.route("/arrest_type")
def get_arrest_type_data():
    labels = []
    values = []
    try:
        with open(ARREST_TYPE_PATH+"/out_directory/part-r-00000") as f:
            lines = f.readlines()
            for line in lines:
                sline = line.split("\t")
                if sline[0] != "Arrest":
                    labels.append(sline[0])
                    values.append(int(sline[1].replace("\n","")))
    except:
        labels = []
        values = []
    return jsonify({"labels":labels,"values":values}) 

@app.route("/arrest_type/delete")
def delete_arrest_type_data():
    os.system("rm -fr "+ARREST_TYPE_PATH+"/out_directory")
########ARREST END

########CRIME START
@app.route("/crime_type/start")
def start_crime_type():
    os.system("cd ../CrimeType && ls && ./run.sh")
    return "bitti"

@app.route("/crime_type")
def get_crime_type_data():
    labels = []
    values = []
    try:
        with open(CRIME_TYPE_PATH+"/out_directory/part-r-00000") as f:
            lines = f.readlines()
            for line in lines:
                sline = line.split("\t")
                if sline[0] != "Description":
                    labels.append(sline[0])
                    values.append(int(sline[1].replace("\n","")))
    except:
        labels = []
        values = []
    return jsonify({"labels":labels,"values":values})

@app.route("/crime_type/delete")
def delete_crime_type_data():
    os.system("rm -fr "+CRIME_TYPE_PATH+"/out_directory")
########CRIME END

if __name__ == "__main__":
    app.run()
