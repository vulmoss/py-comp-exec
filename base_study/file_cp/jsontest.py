#!/usr/bin/env python3

import json

courses = [{
   'user_id':1000,
   'name':'Shiyanlou',
    'pass':10,
     'study_time':50,
  },
{
   'user_id':2000,
    'name':'Lou',
     'pass':15,
     'study_time':171,
 }]

json.dumps(courses)
with open('./test/jsontest.json','w') as f:
    f.write(json.dumps(courses))

