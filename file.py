from click import echo
import json

f = open("file.txt", "r")
to_dictionary = f.read().replace('=',' ')
with open('data.txt', 'w') as f:
    f.write(to_dictionary)


### Text file to JSON format

import json
# the file to be converted to json format
filename = 'data.txt'
 
# dictionary where the lines from
# text will be stored
dict1 = {}
 
# creating dictionary
with open(filename) as fh:
 
    for line in fh:
 
        # reads each line and trims of extra the spaces
        # and gives only the valid words
        command, description = line.strip().split(None, 1)
 
        dict1[command] = description.strip().replace('"\"',"")
 
# creating json file
# the JSON file is named as test1
out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()


f = open('test1.json')
f1 = open('test2.json')
data = json.load(f)
data2 = json.load(f1)
if data['APP_ENV'] == 'local':
    data['APP_ENV'] = 'Private'
if data['APP_DEBUG'] == 'true':
    data['APP_DEBUG'] = data2['DB_USERNAME']
with open('.env', 'w') as f:
    f.write(str(data).replace("{'",'').replace('"}"',' ').replace(":",'=').replace("'",'').replace(",",'\n').replace(' ','').rstrip())