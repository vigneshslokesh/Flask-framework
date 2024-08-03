from flask import Flask

app = Flask(__name__)

@app.route("/")
def multiply_by_three():
    num = int(input("Enter a number"))
    print(num*3)

if __name__ == "__main__":
    app.run()