import json
import unicodedata
import pprint
import id_summary_dict

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

	if id in id_summary_dict.id_summary:
		desc = id_summary_dict.id_summary[id]
	else:
		desc ="No Description found"
		
	'''
		sample_dict =	{
	  "id-2014-0114": "green",
	  "id-2016-4858": "yellow",
	  "id-2018-1000180": "blue",
	  "id-2016-4859": "white",
	  "id-2013-7394": "saffron",
	  "id-2013-6771": "red"
	}
	
	if id in sample_dict:
		desc = sample_dict[id]
	else:
		desc ="No Description found"
	'''	
	return desc
	

def group_id_by_severity(id_json_input):
	critical_dict = {}
	high_dict = {}
	medium_dict = {}
	low_dict = {}
	id_asset_json = id_json_input["id_report"]["id_asset"]
	for i in id_asset_json:
		for j in i["id"]:
			severity = j["severity"]
			id_id = j["id"]
			description = find_description(id_id)
			
			if severity == "Critical":
				critical_dict[str(id_id)] = description
			if severity == "High":
				high_dict[str(id_id)] = description
			if severity == "Medium":
				medium_dict[str(id_id)] = description
			if severity == "Low":
				low_dict[str(id_id)] = description

	return critical_dict, high_dict, medium_dict, low_dict
	
def create_json(score, critical_dict, high_dict, medium_dict, low_dict):
		
	output_json ={
			'Score': score,
			'Critical': critical_dict,
			'High': high_dict,
			'Medium': medium_dict,
			'Low': low_dict
		}	
	
	output = json.dumps(output_json)
	return output
	
if __name__== "__main__":
	id_json_input = load_json()
	score = calc_score(id_json_input)
	c, h, m , l = group_id_by_severity(id_json_input)
	#pprint.pprint(create_json(score, c, h, m , l)) 
	pprint.pprint(json.loads(create_json(score, c, h, m , l)))
	



