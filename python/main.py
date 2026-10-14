import sys
import os
dirname = os.path.dirname(__file__)
import pandas
import json

city_name=''
state_name=''
time_range_start=0
time_range_end=0

try:city_name=sys.argv[1].split(",")
except:city_name=['Bertioga',"Santos"]
try:state_name=sys.argv[2]
except:state_name="SP"
try:time_range_start=int(sys.argv[3])
except:time_range_start=0
try:time_range_end=int(sys.argv[4])
except:time_range_end=0

parsed={
	'cidades':{},
	'years':[]
	}
for city in city_name:
	parsed['cidades'][city]={}

for filename in sorted(os.listdir(os.path.join(dirname,'../data/original/csv'))):
	year=''
	for l in filename:
		if(l.isnumeric()):
			year+=l
	year=int(year)
	if(year<time_range_start or year>time_range_end and time_range_end!=0):
		continue

	df = pandas.read_csv('data/original/csv/'+filename,sep=',')

	parsed['years'].append(year)

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