from flask import Flask

# WSGI app is created 
app =Flask(__name__) #WSGI standard interacting with the server  <starting point of our function which gets executed in our py file>

@app.route('/') #decorator with the binding with function arg-(URL) (/ - root url)
def welcome(): #binding function
    num = int(input("Enter a number"))
    return print(num*3)

@app.route('/members') 
def members():
    return 'Welcome to my Flask framework members'

if __name__ == "__main__":
    app.run()   