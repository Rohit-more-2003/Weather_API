from flask import Flask, render_template

app = Flask("Website")


@app.route("/")  #@-decorator prefix, route connects with corresponding files
def home():
	return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
	temperature = 23
	return {"station": station,
	        "date": date,
	        "temperature": temperature}


if __name__ == "__main__":  #__name__ == __main__ only if the current file is being run
	app.run(debug=True) #port=5*** argument added if multiple flask apps are to run
	#default port value is 5000.