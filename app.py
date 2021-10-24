#-----Flask Hello World-----#

#import Flask class from the flask package
from flask import Flask

#create the app object
app= Flask(__name__)

#use decorator to link a function to a URL
@app.route("/")
@app.route("/hello")

#define the view using a function which returns a string
#this function is called by both / and by /hello
def hello_world():
	#the controller will render this simple text on the screen
	return("Hello World") 

@app.route("/test/<search_query>")
def search(search_query):
	return (search_query)

@app.route("/integer/<int:value>")
def int_type(value):
	print (value+1)   #the value is printed on the terminal 
	return ("Correct") #the text is returned to the controller for html-ization

@app.route("/float/<float:value>")
def float_type(value):
	print (value+1)
	return ("Correct")

@app.route("/path/<path:value>")
def path_type(value):
	print (value)
	return ("Correct")


#start the dev server using the run() method
if __name__ == "__main__":
	app.run()
