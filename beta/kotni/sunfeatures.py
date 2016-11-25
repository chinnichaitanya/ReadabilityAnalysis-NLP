import re
import glob
import csv
from textstat.textstat import textstat

def getWords(text):
    return re.compile('\w+').findall(text)

def calculate_phrase_length(i):
	temp_string = ''
	for char in lines[i]:
		if char is ' ':
			temp_string = temp_string + ' '
		else:
			break
	temp_string = temp_string +'  ['
	temp_np_len = 0
	j = i+1
	while(j<len(lines)):
		# print 'SOmething happening'
		if temp_string in lines[j]:
			temp_np_len += 1
			# print "Incrementing"
			j = j+ 1
		else:
			break
	return temp_np_len				

folder_names = ['level2_sundance', 'level3_sundance', 'level4_sundance', 'gcse_sundance','ks3_sundance']

for k in range(0,len(folder_names)):
	lexical_train = []
	for filename in glob.glob('test_sundance/'+str(folder_names[k])+'/*.sundance'):
		text_file = open(filename, "r")
		lines = text_file.readlines()
		# print lines
		np_count = 0
		pp_count = 0
		vp_count = 0
		np_len = []
		vp_len = []
		pp_len = []
		num_sentences = 0
		num_words = 0
		num_letters = 0
		num_syllables = 0
		file_name_parts =filename.rstrip().split("/")
		file_name = file_name_parts[len(file_name_parts)-1]
		name_of_file = file_name.strip('.sundance')+'.txt' 
		for i in range(0,len(lines)):
			if 'NP SEGMENT' in lines[i]:
				np_count += 1
				np_len.append(calculate_phrase_length(i))	
			elif 'VP SEGMENT' in lines[i]:
				vp_count += 1
				vp_len.append(calculate_phrase_length(i))	
			elif 'PP SEGMENT' in lines[i]:
				pp_count += 1
				pp_len.append(calculate_phrase_length(i))
			elif 'Original :' in lines[i]:
				# print "Entered here"
				num_sentences = num_sentences +1
				words = getWords(lines[i])
				num_words += len(words) - 1
				for word in words:
					num_syllables += textstat.syllable_count(word)
					num_letters += len(word)
				# print lines[i]
				# print words
		flesh_score = 206.835 - 1.015*(num_words/num_sentences) - 84.6*(num_syllables/num_words)
		L = 100.0*num_letters/num_words
		S = 100.0*num_sentences/num_words
		cli = 0.0588*L - 0.296*S -15.8
		# print "Actual feature values"
		# NP/S, VP/S, PP/S
		print folder_names[k], name_of_file
		if (len(np_len) == 0):
			num_np_len = 1 
		else:
			num_np_len = len(np_len)

		if (len(vp_len) == 0):
			num_vp_len = 1 
		else:
			num_vp_len = len(vp_len)
		
		if (len(pp_len) == 0):
			num_pp_len = 1 
		else:
			num_pp_len = len(pp_len)
			
		print num_sentences, num_words 
		# Filename,NP/S,VP/S,PP/S,NPlen,VPlen,PPlen,cli,fks
		lexical_train.append([name_of_file,round(1.0*np_count/num_sentences,2),round((1.0*vp_count/num_sentences),2),round((1.0*pp_count/num_sentences),2),round((1.0*sum(np_len)/num_np_len),2),round((1.0*sum(vp_len)/num_vp_len),2),round((1.0*sum(pp_len)/num_pp_len),2),round(cli,3),round(flesh_score,3)])
		# print "For your reference venki :P"
		# print "NP count, vp count, pp count"
		# print np_count,vp_count,pp_count
		# print "NP lengths"
		# print np_len
		# print "vp lengths"
		# print vp_len
		# print "pp lengths"
		# print pp_len
		# print len(lines)
		text_file.close()
	myfile = open('sundance_test'+str(folder_names[k])+'.csv', 'wb')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(lexical_train)