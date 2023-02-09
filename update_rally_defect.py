def update_rally_defect(description_data,defect_num,correlation_id):
    # Need to install requests package for python
    # easy_install requests
    import requests

    # Set the request parameters
    url = 'https://dev97102.service-now.com/api/now/table/problem/f10ea5a607b02110f1c9f1d08c1ed09f'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'admin'
    pwd = 'eEp7GCif=0%I'

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    description_data_with_defect = description_data + defect_num

    # Do the HTTP request
    response = requests.put(url, auth=(user, pwd), headers=headers,
                            data='{"description": "'+description_data_with_defect+'", "correlation_id": "'+correlation_id+'"   }')

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()