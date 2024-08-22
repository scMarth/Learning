# starts or stops multiple services and runs the api calls to ags admin in parallel

import os, socket, sys
import concurrent.futures

import ags_admin_utils

# Ask for admin user name and password
username = 'admin'
password = os.environ["ATLAS_AGS_ADMIN_PASSWORD"]

foldernames = [
    'FOLDER_NAME1',
    'FOLDER_NAME2',
    'FOLDER_NAME3'
]

# get server name and the port
hostname = socket.gethostname()
serverName = socket.gethostbyname(hostname) # IPV4 Address
serverPort = 6443

token = ags_admin_utils.getToken(username, password, serverName, serverPort)

print('got token')
print('starting services...')

tasks = [] # Input parameters for each service

for folder in foldernames:

    service_data = ags_admin_utils.getServiceDataFromFolder(serverName, serverPort, token, folder)

    for data in service_data:
        # create input parameter for run tasks to start services
        task = (serverName, serverPort, token, folder, data['serviceName'], data['type'], 'start')
        tasks.append(task)

# Function to run a single task
def run_task(args):
    return ags_admin_utils.startStopService(*args)

# Using ThreadPoolExecutor to execute tasks in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Map the tasks to the executor
    futures = [executor.submit(run_task, task) for task in tasks]

    # Optionally, wait for the tasks to complete and gather results
    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
        except Exception as e:
            print("Task generated an exception:", e)