# convert json to csv

import arcpy, os, shutil, numpy, json, codecs

fields = {
    'request' : [ \
        'id', \
        'master', \
        'addDate', \
        'addDateUnix', \
        'lastAction', \
        'lastActionUnix', \
        'dept', \
        'displayDate', \
        'displayLastAction', \
        'status', \
        'streetId', \
        'streetName', \
        'streetNum', \
        'crossStreetId', \
        'crossStreetName', \
        'cityId', \
        'cityName', \
        'district', \
        'comments', \
        'privateNotes', \
        'submitter', \
        'typeId', \
        'typeName', \
        'priorityValue', \
        'latitude', \
        'longitude', \
        'aggregatorId', \
        'aggregatorInfo', \
        'origin', \
        'priorityToDisplay' \
    ],
    'activity' : [ \
        'actDate', \
        'actDateUnix', \
        'attachments', \
        'code', \
        'codeDesc', \
        'comments', \
        'displayDate', \
        'id', \
        'notify', \
        'requestId', \
        'routeId', \
        'user', \
        'files', \
        'isEditable' \
    ],
    'attachment' : [ \
        'createDateUnix', \
        'createDate', \
        'fileName', \
        'id', \
        'parent', \
        'parentType', \
        'size', \
        'user' \
    ],
    'submitter' : [ \
        'id', \
        'firstName', \
        'lastName', \
        'middleInitial', \
        'address', \
        'address2', \
        'city', \
        'state', \
        'zip', \
        'email', \
        'phone', \
        'phoneExt', \
        'altPhone', \
        'altPhoneExt', \
        'password', \
        'aggregatorId', \
        'verified', \
        'banned', \
        'twitterId', \
        'twitterScreenName', \
        'notifyEmail', \
        'notifyPhone', \
        'notifyAltPhone', \
        'notifyMail', \
        'notifyPush', \
        'notifyPhoneSms', \
        'notifyAltPhoneSms' \
    ]
}

def escaped(inputStr):
    # return inputStr
    return inputStr.translate(str.maketrans({ \
        # "]":  r"\]", \
        # "^":  r"\^", \
        # "$":  r"\$", \
        # "*":  r"\*", \
        # ".":  r"\.", \
        # "/":  r"\/",\

        # so far, I've seen carriage returns, line feeds, and double-quotes that can mess up records. '\'' is escaped just in case
        "\r": r"\r", \
        "\n": r"\n", \
        "\\": r"\\", \
        '\"': r'\"'  \
    }))

# reads a json file path then creates a fgdb for that json file in 'workspace'
# the json file contains json data that is returned from the requests/dump method
def write_json_file_to_csv(workspace, json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
        for key in data:
            if key == 'deleted':
                continue

            output_filepath = workspace + r'\\' + key.upper() + '.csv'

            print('Writing' + output_filepath)

            # delete file if it exists
            if os.path.exists(output_filepath):
                os.unlink(output_filepath)

            with codecs.open(output_filepath, 'w', encoding='utf8') as file:
                # write header
                for i in range(len(fields[key]) - 1):
                    file.write(escaped(fields[key][i]) + ',')
                file.write(escaped(fields[key][-1]) + '\n')

                # write records
                for i in range(len(data[key])):
                    record = data[key][i]

                    # print(record)

                    for j in range(len(fields[key]) - 1):
                        # print(j)
                        file.write('"' + escaped(str(record[fields[key][j]])) + '",')
                    file.write('"' + escaped(str(record[fields[key][-1]])) + '"\n')

            print('{} records written.\n'.format(len(data[key])))

workspace = os.path.dirname(__file__) + r'\request_data'

write_json_file_to_csv(workspace, workspace + r'\response.json')