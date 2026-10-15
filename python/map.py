import sys
import os
dirname = os.path.dirname(__file__)
import pandas
import json

city_name=''
state_name=''
time_range_start=0
time_range_end=0

try:city_name=sys.argv[1]
except:city_name='Bertioga'
try:state_name=sys.argv[2]
except:state_name="SP"
try:time_range_start=int(sys.argv[3])
except:time_range_start=0
try:time_range_end=int(sys.argv[4])
except:time_range_end=0

parsed={
	'city':'',
	'years':[],
	'path':'',
	}
parsed['city']=city_name

parsed['path']='/data/map/'+city_name

if(city_name!=''):
	for filename in sorted(os.listdir(os.path.join(dirname,'../data/map',city_name,'original'))):
		year=''
		for l in filename:
			if(l.isnumeric()):
				year+=l
		if(year.isnumeric()==False):
			continue
		year=int(year)
		if(year<time_range_start or year>time_range_end and time_range_end!=0):
			continue
		parsed['years'].append(year)
print(json.dumps(parsed,ensure_ascii=False))
sys.stdout.flush()