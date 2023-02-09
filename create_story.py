from pyral import Rally
import sys

def create_defect(project, name, description, state, sstate):

    RALLY_NAME = 'rally1.rallydev.com'
    RALLY_API_KEY = '_1iKyJD6XRoakADK4LwWSuDsuW0TtCEJupM7z4xbd85g'

    rally = Rally(RALLY_NAME, apikey=RALLY_API_KEY, workspace='Workspace 1', project=project)

    proj = rally.getProject()

    # get the first (and hopefully only) user whose DisplayName is 'Sartorious Submitter'
    user = rally.getUserInfo(name='deepak raushan').pop(0)

    # Mapping details #
    # SNOW

    defect_data = { "Project" : proj.ref,
                    "State" : state,
                    "ScheduleState" : sstate,
                    "Name" : name,
                    "Description" : description}

    try:
        defect = rally.create('Defect', defect_data)
    except Exception as e:
        print(e)
        sys.exit(1)
    print("Defect created, ObjectID: %s  FormattedID: %s" % (defect.oid, defect.FormattedID))

create_defect(project = 'Project_Test', name="Title 1", description = "Description 1", state = "Open",sstate = "Defined")