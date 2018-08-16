import glob
import errno
import json
import unicodedata
import pprint

path = '/complete_path/*.json' #note C:
files = glob.glob(path)
id_summary = {}
for name in files:
	print name
	id_json_input = json.loads(open(name).read())
	id_list = id_json_input["id_Items"]
	for i in id_list:
		key = i["id"]["id_data_meta"]["ID"]
		summary = i["id"]["description"]["description_data"][0]["value"]
		id_summary[key] = summary
'''		
for k,v in id_summary.items():
	print k, " : ", v, "\n"
'''

f= open("id_summary_dict.py","w+") #create file if it doesn't exist
f.write("id_summary=")
f.write(str(id_summary))
f.close
