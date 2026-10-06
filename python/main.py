def main():
	import os
	dirname = os.path.dirname(__file__)
	import pandas

	parsed = []
	count=0

	for i in sorted(os.listdir(os.path.join(dirname,'../data/original'))):
		count+=1
		if count==-1:
			break
		file = pandas.read_excel('data/original/'+i, sheet_name=None)
		print(i)
		for name, df in file.items():
			val = df[df.eq('Bertioga').any(axis=1)]
			if val.empty:
				continue
			#parsed.append(val)

	return parsed
main()