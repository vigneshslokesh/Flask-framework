from flask import Flask

# WSGI app is created 
app =Flask(__name__) #WSGI standard interacting with the server

@app.route('/') #decorator with the binding with function
def welcome():
    return 'Welcome to my Flask framework'

if __name__ == "__main__":
    app.run()