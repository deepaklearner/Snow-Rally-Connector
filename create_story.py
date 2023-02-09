from pyral import Rally
import sys

def create_rally_defect(rally_project, rally_defect_title, rally_defect_description, rally_defect_state, rally_defect_sstate):

    RALLY_NAME = 'rally1.rallydev.com'
    RALLY_API_KEY = '_1iKyJD6XRoakADK4LwWSuDsuW0TtCEJupM7z4xbd85g'

    rally = Rally(RALLY_NAME, apikey=RALLY_API_KEY, workspace='Workspace 1', project=rally_project)

    proj = rally.getProject()

    # get the first (and hopefully only) user whose DisplayName is 'Sartorious Submitter'
    user = rally.getUserInfo(name='deepak raushan').pop(0)

    defect_data = { "Project" : proj.ref,
                    "State" : rally_defect_state,
                    "ScheduleState" : rally_defect_sstate,
                    "Name" : rally_defect_title,
                    "Description" : rally_defect_description}

    try:
        defect = rally.create('Defect', defect_data)
    except Exception as e:
        print(e)
        sys.exit(1)
    print("Defect created, ObjectID: %s  FormattedID: %s" % (defect.oid, defect.FormattedID))

# Mapping function
def mapping_snow_problem_to_rally_defect(snow_assignmentgrp,snow_problem_sh_desc,snow_problem_desc,snow_problem_state,snow_problem_priority,snow_problem_impact):

    if snow_assignmentgrp == "DEEPAK-PROD-SUPPORT":
        rally_project = 'Project_Test' #rally_project, rally_defect_tower, rally_defect_team, rally_defect_lead
        rally_defect_title = snow_problem_sh_desc
        rally_defect_description = snow_problem_desc + " " + snow_problem_number
    if snow_problem_state == "New":
        rally_defect_state = "Open"
        rally_defect_sstate = "Defined"
    if snow_problem_priority == "5": rally_defect_priority ="Normal"
    if snow_problem_impact == "3": rally_defect_severity="Major Problem"
    #snow_problem_work_notes = "sample work notes" #rally_defect_discussion
    #snow_defect_attachment - to do later
    return rally_project, rally_defect_title, rally_defect_description, rally_defect_state, rally_defect_sstate

# Test data
snow_assignmentgrp = "DEEPAK-PROD-SUPPORT"
snow_problem_number = "PRB0040001"
snow_problem_sh_desc = "Test problem updated 1"
snow_problem_desc = "Test problem updated 1"
snow_problem_state = "New"
snow_problem_priority = "5"
snow_problem_impact = "3"

rally_project, rally_defect_title, rally_defect_description, rally_defect_state, rally_defect_sstate = \
    mapping_snow_problem_to_rally_defect(snow_assignmentgrp,snow_problem_sh_desc,snow_problem_desc,snow_problem_state,snow_problem_priority,snow_problem_impact)

create_rally_defect(rally_project, rally_defect_title, rally_defect_description, rally_defect_state, rally_defect_sstate)