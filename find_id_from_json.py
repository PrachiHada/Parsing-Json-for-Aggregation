import json
import unicodedata
import pprint

def load_json(id):
	id_json_input = json.loads(open('/complete_path/id-1.0-2016.json').read())
	id_list = id_json_input["id_Items"]
	for i in id_list:
		if i["id"]["id_data_meta"]["ID"] == id:
			summary = i["id"]["description"]["description_data"][0]["value"]
	return summary
	

	
if __name__== "__main__":
	id_summary = load_json("id-2016-7051")
	print(id_summary)
	
	



