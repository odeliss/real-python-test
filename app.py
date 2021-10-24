#-----Flask Hello World-----#

#import Flask class from the flask package
from flask import Flask

#create the app object
app= Flask(__name__)

#use decorator to link a function to a URL
@app.route("/")
@app.route("/hello")

#define the view using a function which returns a string
def hello_world():
	return("Hello World")

#start the dev server using the run() method
if __name__ == "__main__":
	app.run()
	