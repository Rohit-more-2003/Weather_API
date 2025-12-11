from flask import Flask, render_template
import pandas as pd

app = Flask("Website")

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

#df = pd.read_csv()
@app.route("/")  #@-decorator prefix, route connects with corresponding files
def home():
	return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
	#In given files station id of 6 numbers
	#zfill gives out numbers with 0s as prefix to give out (x) length (int) number.
	filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
	
	df = pd.read_csv(filename, skiprows=20,
	                 parse_dates=["    DATE"])
	
	temperature = df.loc[df["    DATE"] == str(date)]["   TG"].squeeze() / 10
	
	return {"station": station,
	        "date": date,
	        "temperature": temperature}


@app.route("/api/v1/<station>")
def all_data(station):
	filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
	df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"]) #parse_dates changes the date from string to date, time
	
	result = df.to_dict(orient="records")
	return result


@app.route("/api/v1/annual/<station>/<year>")
def yearly(station, year):
	filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
	df = pd.read_csv(filename, skiprows=20)
	
	#parse_dates makes the date&time accessible as date&time format instead of string format
	#But here we are using year as condition, so remove parse_dates parameter to access date
	#as a string
	df["    DATE"] = df["    DATE"].astype(str)
	
	result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
	return result


if __name__ == "__main__":  #__name__ == __main__ only if the current file is being run
	app.run(debug=True) #port=5*** argument added if multiple flask apps are to run
	#default port value is 5000.
	
#This program is written so we understand about data analysis and visualization