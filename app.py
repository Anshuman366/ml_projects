from flask import Flask
import sys
from housing.logger import logging
from housing.exception import Housing_exception

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("This is the custome exception check")
    except Exception as e:
        housing= Housing_exception(e,sys)
        logging.info(housing.get_detailed_error_message(e,sys))
        logging.info("This is my logging module check")
    return "This is my first Machine Learning project"

if __name__=="__main__":
    app.run(debug=True,port=5000)