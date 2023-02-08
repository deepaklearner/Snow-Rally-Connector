# https://levelup.gitconnected.com/simple-api-using-flask-bc1b7486af88
# flask --app api run
# python api.py

from flask import Flask, jsonify, request

# initialize our Flask application
app= Flask(__name__)

@app.route("/")
def index():
    return "Hi Deepak"

@app.route("/create_defect", methods=["POST"])
def createDefect():
    if request.method == 'POST':
    '''
    lets create json data from SNOW
    {
    "problem_num":"'+num+'",
    "sh_desc": "'+sh_desc+'"
    "desc": "'+desc+'"
    } 
    '''

        posted_data = request.get_json()
        data = posted_data['data']
        print("Triggered from SNOW ", data)

@app.route("/name", methods=["POST"])
def setName():
    if request.method=='POST':

        posted_data = request.get_json()
        data = posted_data['data']
        print("Triggered from SNOW ", data)
        return jsonify(str("Successfully stored  " + str(data)))

@app.route("/message", methods=["GET"])
def message():
    posted_data = request.get_json()
    name = posted_data['name']
    return jsonify(" Hope you are having a good time " +  name + "!!!")

#  main thread of execution to start the server
if __name__=='__main__':
   app.run(host="localhost",port=80)

