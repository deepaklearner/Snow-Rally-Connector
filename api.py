# https://levelup.gitconnected.com/simple-api-using-flask-bc1b7486af88
# flask --app api run
# python api.py

from flask import Flask, jsonify, request
from create_story import create_rally_defect, mapping_snow_problem_to_rally_defect

# initialize our Flask application
app= Flask(__name__)

@app.route("/")
def index():
    return "Hi Deepak"

@app.route("/create_defect", methods=["POST"])
def createDefect():
    if request.method == 'POST':
        data_from_SNOW = request.get_json()
        print("Triggered from SNOW ", data_from_SNOW)

        snow_assignmentgrp = data_from_SNOW['assignment_grp']
        snow_problem_number = data_from_SNOW['num']
        problem_sys_id = data_from_SNOW['sys_id']
        defect_correlation_id = data_from_SNOW['defect_correlation_id']
        snow_problem_sh_desc = data_from_SNOW['sh_desc']
        snow_problem_desc = data_from_SNOW['desc']
        snow_problem_state = data_from_SNOW['state']
        snow_problem_priority = data_from_SNOW['priority']
        snow_problem_impact = data_from_SNOW['impact']

        rally_project, rally_defect_title, rally_defect_description, rally_defect_state, rally_defect_sstate = \
            mapping_snow_problem_to_rally_defect(snow_assignmentgrp, snow_problem_sh_desc, snow_problem_desc,
                                                 snow_problem_number, snow_problem_state, snow_problem_priority,
                                                 snow_problem_impact)

        create_rally_defect(rally_project, problem_sys_id, rally_defect_title, rally_defect_description, rally_defect_state,
                            rally_defect_sstate, defect_correlation_id)

        return jsonify(str("Successfully created Defect in Rally"))

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

