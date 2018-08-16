import json
import unicodedata
import pprint

def load_json():
	id_json_input = json.loads(open('/complete_path/id_report_2.json').read())
	#pprint json.dumps(config)
	#pprint.pprint(id_json_input)
	return id_json_input
	

def calc_score(id_json_input):
	#print(id_json_input["id_report"]["summary"])
	critical_score = id_json_input["id_report"]["summary"]["critical"]
	high_score = id_json_input["id_report"]["summary"]["High"]
	medium_score = id_json_input["id_report"]["summary"]["Medium"]
	low_score = id_json_input["id_report"]["summary"]["Low"] 
	score = 0

	if critical_score > 0:
		score = 0
	elif high_score > 0:
		score = 0
	elif medium_score > 0:
		score = 50
	elif low_score > 0:
		score = 100
	
	return score
	

def find_description(id):
	sample_dict =	{
	  "id-2014-0114": "green",
	  "id-2016-4858": "yellow",
	  "id-2018-1000180": "blue",
	  "id-2016-4859": "white",
	  "id-2013-7394": "saffron",
	  "id-2013-6771": "red"
	}

	critical_dict = {}
	for i in critical_list:
		if i in sample_dict:
			critical_dict[i]= sample_dict[i]
		else:
			critical_dict[i]="No Description foound"
			

	print critical_dict
	

def group_id_by_severity(id_json_input):
	critical_list = []
	high_list = []
	medium_list = []
	low_list = []
	id_asset_json = id_json_input["id_report"]["id_asset"]
	for i in id_asset_json:
		for j in i["id"]:
			severity = j["severity"]
			id_id = j["id"]
			
			if severity == "Critical":
				critical_list.append(str(id_id))
			if severity == "High":
				high_list.append(str(id_id))
			if severity == "Medium":
				medium_list.append(str(id_id))
			if severity == "Low":
				low_list.append(str(id_id))

	return critical_list, high_list, medium_list, low_list
	
def create_json(score, critical_list, high_list, medium_list, low_list):
		
	output_json ={
			'Score': score,
			'Critical': critical_list,
			'High': high_list,
			'Medium': medium_list,
			'Low': low_list
		}	
	
	output = json.dumps(output_json)
	return output
	
if __name__== "__main__":
	id_json_input = load_json()
	score = calc_score(id_json_input)
	c, h, m , l = group_id_by_severity(id_json_input)
	pprint.pprint(create_json(score, c, h, m , l))
	#pprint.pprint(json.loads(create_json(score, c, h, m , l)))



