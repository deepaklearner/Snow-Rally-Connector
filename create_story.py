from pyral import Rally
import sys

def create_defect(rally_project, rally_title, rally_description, rally_state, rally_sstate):

    RALLY_NAME = 'rally1.rallydev.com'
    RALLY_API_KEY = '_1iKyJD6XRoakADK4LwWSuDsuW0TtCEJupM7z4xbd85g'

    rally = Rally(RALLY_NAME, apikey=RALLY_API_KEY, workspace='Workspace 1', project=rally_project)

    proj = rally.getProject()

    # get the first (and hopefully only) user whose DisplayName is 'Sartorious Submitter'
    user = rally.getUserInfo(name='deepak raushan').pop(0)

    # Mapping details #
    # SNOW

    defect_data = { "Project" : proj.ref,
                    "State" : rally_state,
                    "ScheduleState" : rally_sstate,
                    "Name" : rally_title,
                    "Description" : rally_description}

    try:
        defect = rally.create('Defect', defect_data)
    except Exception as e:
        print(e)
        sys.exit(1)
    print("Defect created, ObjectID: %s  FormattedID: %s" % (defect.oid, defect.FormattedID))

create_defect(rally_project = 'Project_Test', rally__title="Title 1", rally_description = "Description 1", rally_state = "Open",rally_sstate = "Defined")