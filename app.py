#-------Flask Hello World--------#

# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorators to link the function  to a url 
@app.route("/")
@app.route("/hello")

# define the view using a function, which return as string 
def hello_world():
	return "Hello, World!"

#Start the development server using the run() method

if __name__ == "__main__":
	app.run()
	