# Import all dependencies
import nltk
from textstat.textstat import textstat
from practnlptools.tools import Annotator
annotator=Annotator()
# import a text document
with open('test_small.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
# print data
# Tokenize the doc & find the total number of words
tokens = nltk.word_tokenize(data)
print len(tokens)
# Tokens include punctuations. Do we have to eliminate them in our analysis?
# average number of syllables per word
words = []
char_count = 0 
for token in tokens:
	if token.isalpha():
		char_count += len(token)
		words.append(token)
# print average num_syllables
print char_count
avg_syllables = 0
for word in words:
	avg_syllables += textstat.syllable_count(word)
if (len(words) != 0):
	avg_syllables = 1.0*avg_syllables/len(words)
	avg_char_count = 1.0*char_count/len(words)
# average number of characters
print avg_syllables,avg_char_count
# identify number of lexical types (POS Tagging)
pos_tags = annotator.getAnnotations(data)['pos']
print pos_tags
distinct_tags = []
word_types = 0
for tag in pos_tags:
	if tag[1].isalpha():
		if not (tag[1] in distinct_tags):
			word_types +=1
			distinct_tags.append(tag[1])
print word_types
# feature: typical_token_ration
typical_token_ration = 1.0*word_types/len(words)
print typical_token_ration
# print nltk.pos_tag(data)
# Search for academic word list
# 