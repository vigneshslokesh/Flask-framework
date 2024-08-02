from flask import Flask

# WSGI app is created 
app =Flask(__name__) #WSGI standard interacting with the server

@app.route('/') #decorator with the binding with function arg-(URL) (/ - root url)
def welcome(): #binding function
    return 'Welcome to my Flask framework'

@app.route('/members') 
def members():
    return 'Welcome to my Flask framework members'

if __name__ == "__main__":
    app.run()   