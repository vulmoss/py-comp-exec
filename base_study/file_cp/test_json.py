import json

courses = {1:'Linux',2:'Vim',3:'Git'}
json.dumps(courses)
with open('courses.json','w') as f:
    f.write(json.dumps(courses))
with open('courses.json','w') as f:
    json.dump(courses,f)

