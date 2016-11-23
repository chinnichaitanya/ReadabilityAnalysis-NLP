import csv
import glob
# Import all dependencies
import nltk
import numpy as np
import sys  
import re
reload(sys)  
sys.setdefaultencoding('utf8')
from textstat.textstat import textstat
from practnlptools.tools import Annotator
from nltk.stem import WordNetLemmatizer

annotator=Annotator()

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def remove_non_unicodes(text):
	return ''.join([i if ord(i) < 128 else '' for i in text])

with open('awl_scores.txt', 'r') as myfile:
	awl_words=myfile.read().replace('\n', '\t')
	tokens = awl_words.split('\t')
	awl_header_words_dict = {}
	for token in tokens:
		split_token = token.split(' ')
		# split_token = unicode(split_token, 'utf-8')
		list_num = int(split_token[1])
		if(list_num%2 == 0):
			awl_header_words_dict[split_token[0]] = list_num/2
		else:
			awl_header_words_dict[split_token[0]] = int(list_num/2) +1

folder_names = ['level2', 'level3', 'level4', 'gcse','ks3']
# folder_names = ['sample']
# class_level = 1
# import a text document
for i in range(0,len(folder_names)):
	print folder_names[i]
	lexical_train_with_filenames = []
	lexical_train = []
	class_level = i+1	
	for filename in glob.glob('../../../L2SCA-2016-06-30/test/'+str(folder_names[i])+'/*.txt'):
		with open(filename, 'r') as myfile:
			data=myfile.read().replace('\n', '')
			# testing_set=re.findall("\([A-Z]+\$? [^\)\(]+\)",data)
		# data = unicode(data,'utf-8')
		file_name_parts =filename.rstrip().split("/")
		file_name = file_name_parts[len(file_name_parts)-1] 
		# print data
		# Tokenize the doc & find the total number of words
		# print data
		# print testing_set
		data = remove_non_unicodes(data)
		data_ascii = is_ascii(data)
		if(data_ascii):
			tokens = nltk.word_tokenize(data)

			# print len(tokens)
			# Tokens include punctuations. Do we have to eliminate them in our analysis?
			# average number of syllables per word
			words = []
			char_count = 0 
			for token in tokens:
				if token.isalpha():
					char_count += len(token)
					words.append(token)
			# print average num_syllables
			# print char_count
			avg_syllables = 0
			for word in words:
				avg_syllables += textstat.syllable_count(word)
			if (len(words) != 0):
				avg_syllables = 1.0*avg_syllables/len(words)
				avg_char_count = 1.0*char_count/len(words)
			# average number of characters
			# print avg_syllables,avg_char_count
			# identify number of lexical types (POS Tagging)
			# print 'Hii'
			# print data
			# pos_tags = annotator.getAnnotations(data)
			# print pos_tags
			# pos_tags = pos_tags['pos']
			pos_tags = nltk.pos_tag(data)
			distinct_tags = []
			word_types = 0
			for tag in pos_tags:
				if tag[1].isalpha():
					if not (tag[1] in distinct_tags):
						word_types +=1
						distinct_tags.append(tag[1])
			# print word_types
			# feature: typical_token_ration
			typical_token_ration = 1.0*word_types/len(words)
			# print typical_token_ration
			# print nltk.pos_tag(data)
			# Search for academic word list

			# Lemmatize the given text and search in AWL headwords
			wordnet_lemmatizer = WordNetLemmatizer()
			lemmatized_tokens=[]
			# print file_name
			for token in tokens:
				if token.isalpha():
					lemmatized_tokens.append(wordnet_lemmatizer.lemmatize(token))

			# Convert the unicode lemmatized tokens into regular strings
			for j in range(0,len(lemmatized_tokens)):
				lemmatized_tokens[j] = str(lemmatized_tokens[j])
			# print lemmatized_tokens
			awl_score = 0
			for token in lemmatized_tokens:
				if token in awl_header_words_dict:
					awl_score += awl_header_words_dict[token]
			awl_score = 1.0*awl_score/len(lemmatized_tokens)

			# print awl_score
			# Finish all the features in the list including dictionary
			# Train the model today itself.
			lexical_train.append([round(avg_syllables,2),round(avg_char_count,2),len(tokens),round(typical_token_ration,4),round(awl_score,4),class_level])
			lexical_train_with_filenames.append([file_name,round(avg_syllables,2),round(avg_char_count,2),len(tokens),round(typical_token_ration,4),round(awl_score,4),class_level])
		else:
			print str(file_name)
	myfile = open('lexical_train_'+str(folder_names[i])+'.csv', 'wb')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(lexical_train)

	myfile = open('lexical_train_with_filenames_'+str(folder_names[i])+'.csv', 'wb')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(lexical_train_with_filenames)
