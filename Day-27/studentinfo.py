import json 
'''
with open("data.json",'r') as file:
  data = json.load(file)

data["username"]="anjana"
data["Skills"].append("flask")

with open("data.json",'w') as file:
    json.dump(data,file,indent=4)
    '''

student = {
  "name": "amani",
  "age": 22,
  "course": "Python"
}

json_data = json.dumps(student)   
print(json_data)
print(type(json_data))

student = json.loads(json_data)
print(student)
print(type(student))