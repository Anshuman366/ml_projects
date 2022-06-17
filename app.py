from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "This is my first Machine Learning project"

if __name__=="__main__":
    app.run(debug=True,port=5000)