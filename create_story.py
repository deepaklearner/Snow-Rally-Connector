from pyral import Rally
import sys

def create_defect(rally_project, rally_defect_title, rally_defect_description, rally_defect_state, rally_defect_sstate):

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

# Mapping details
snow_assignmentgrp = "DEEPAK-PROD-SUPPORT"
snow_problem_sh_desc =

create_defect(rally_project = 'Project_Test', rally_defect_title="Title 1", rally_defect_description = "Description 1",
              rally_defect_state = "Open",rally_defect_sstate = "Defined")