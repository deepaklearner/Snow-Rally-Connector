from pyral import Rally
import sys

RALLY_NAME = 'rally1.rallydev.com'
RALLY_API_KEY = '_1iKyJD6XRoakADK4LwWSuDsuW0TtCEJupM7z4xbd85g'

project = 'Project_Test'
rally = Rally(RALLY_NAME, apikey=RALLY_API_KEY, workspace='Workspace 1', project=project)

proj = rally.getProject()

# get the first (and hopefully only) user whose DisplayName is 'Sartorious Submitter'
user = rally.getUserInfo(name='deepak raushan').pop(0)

severity = "Major Problem"
priority = "Low"
description = "sample description by Rani"

defect_data = { "Project" : proj.ref, "SubmittedBy" : user.ref,
                "Name" : "short desc", "Severity" : severity, "Priority" : priority,
                "State" : "Open", "ScheduleState" : "Defined",
                "Description" : description }
try:
    defect = rally.create('Defect', defect_data)
except Exception as e:
    print(e)
    sys.exit(1)
print("Defect created, ObjectID: %s  FormattedID: %s" % (defect.oid, defect.FormattedID))