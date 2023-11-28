import json5
import json
import sys
import os
args = sys.argv[1:]
files = os.listdir("aws-iam-policies/docs")
for file in files:
    print(file)
    myfile = 'aws-iam-policies/docs/' + file
    with open(myfile, "r+") as resultsFile:
        jsonData = json5.load(resultsFile)
    writeRestrictedfile = 'aws-iam-policies/' + file.replace('-doc', '')
    with open(writeRestrictedfile, 'w') as f:
        json.dump(jsonData, f, indent=4)
    writeRestrictedManagedArnfile = 'aws-iam-policies/' + file.replace('-doc', '-managedARN')
    with open(writeRestrictedManagedArnfile, 'w') as managedArn:
        for sid in jsonData['Statement']:
            actionsList = sid['Action']
            if 'iam:PutRolePolicy' in actionsList:
                actionsList.remove('iam:PutRolePolicy')
                break
        json.dump(jsonData, managedArn, indent=4)