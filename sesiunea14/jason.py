import json
with open("documente/employ.json") as my_json_file:
    employs = json.load(my_json_file)
    print(employs)

