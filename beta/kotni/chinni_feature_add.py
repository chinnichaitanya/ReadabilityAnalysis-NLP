import pandas as pd
filenames = ['level2','level3','level4','gcse','ks3']
# filenames = ['level2']
for filename in filenames:
	df1  = pd.read_csv('out_all/test/'+filename+'.csv')
	df4  = pd.read_csv('out_sundance/test/'+filename+'.csv')
	result=pd.merge(df1, df4, on='Filename', how='inner')
	# result = result.drop(result.index)
	print result
	result.to_csv('out_final/test/'+filename+'.csv')
