import sys
import os
dirname = os.path.dirname(__file__)
import pandas
import json

city_name=''
state_name=''
time_range_start=0
time_range_end=0

try:state_name=sys.argv[2]
except:state_name="SP"
try:city_name=sys.argv[1].split(",")
except:city_name=['Bertioga',"Santos"]

parsed={
	'cidades':{},
	'years':[]
	}
for city in city_name:
	parsed['cidades'][city]={}

for filename in sorted(os.listdir(os.path.join(dirname,'../data/original/csv'))):
	df = pandas.read_csv('data/original/csv/'+filename,sep=',')

	year=''
	for l in filename:
		if(l.isnumeric()):
			year+=l
	parsed['years'].append(int(year))

	for city in city_name:
		try:
			city_data = df[(df.iloc[:,3]==city)&(df.iloc[:,0]==state_name)].iloc[:,[3,4]]
		except:
			continue

		for a, b in city_data.items():
			for i in b:
				parsed['cidades'][city][year]=i.replace(" ","").replace(",","").replace(".","")
print(json.dumps(parsed,ensure_ascii=False))
sys.stdout.flush()