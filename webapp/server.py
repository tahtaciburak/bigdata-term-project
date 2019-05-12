from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/crime")
def get_crime_data():
    
if __name__ == "__main__":
    app.run()
