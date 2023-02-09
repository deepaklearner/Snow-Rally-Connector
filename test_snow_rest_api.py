#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
problem_sys_id = "b7f8f8e70738e110f1c9f1d08c1ed025"
url = "https://dev97102.service-now.com/api/now/table/problem/" + problem_sys_id

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'eEp7GCif=0%I'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

description_data = "abcd"
defect_num = "dE10"
correlation_id = "DE10"
description_data_with_defect_and_correlation_id = description_data  + defect_num

# Do the HTTP request
response = requests.put(url, auth=(user, pwd), headers=headers ,
                        data='{"correlation_id":"'+correlation_id+'","description":"'+description_data_with_defect_and_correlation_id+'"}')

# (      '{"assignment_grp":"'+assignment_grp+'",'+
# 							   '"num":"'+num+'",' +
# 						       '"sys_id":"'+sys_id+'",' +
# 						       '"defect_correlation_id":"'+defect_correlation_id+'",' +
# 							   '"sh_desc":"'+sh_desc+'",' +
# 							   '"desc":"'+desc+'",' +
# 						       '"state":"'+state+'",' +
# 						      '"priority":"'+priority+'",' +
# 							   '"impact":"'+impact+'"}'
# 							   );

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)