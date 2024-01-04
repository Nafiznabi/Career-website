from flask import Flask

#creating an object named flask
#simply importing an class Flask and creating an object for it
#creating an flask application
app=Flask(__name__)   #creating an variable name app for flask application
 #creating/registering  an route to the application
@app.route("/")  #route to an empty route
def hello():
  return "hello Nafiz"
#whenever the url / is assecced then then hello world runs

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)

