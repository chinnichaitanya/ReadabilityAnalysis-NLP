# Import all dependencies
import nltk
from textstat.textstat import textstat
from practnlptools.tools import Annotator
from nltk.stem import WordNetLemmatizer

annotator=Annotator()
# import a text document
with open('test.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

with open('awl_scores.txt', 'r') as myfile:
    awl_words=myfile.read().replace('\n', '\t')
    # awl_words=myfile.read()
tokens = awl_words.split('\t')
awl_header_words_dict = {}
for token in tokens:
	split_token = token.split(' ')
	list_num = int(split_token[1])
	if(list_num%2 == 0):
		awl_header_words_dict[split_token[0]] = list_num/2
	else:
		awl_header_words_dict[split_token[0]] = int(list_num/2) +1

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

# Lemmatize the given text and search in AWL headwords
wordnet_lemmatizer = WordNetLemmatizer()
lemmatized_tokens=[]
for token in tokens:
	lemmatized_tokens.append(wordnet_lemmatizer.lemmatize(token))

# Convert the unicode lemmatized tokens into regular strings
for i in range(0,len(lemmatized_tokens)):
	lemmatized_tokens[i] = str(lemmatized_tokens[i])
print lemmatized_tokens
awl_score = 0
for token in lemmatized_tokens:
	if token in awl_header_words_dict:
		awl_score += awl_header_words_dict[token]
awl_score = 1.0*awl_score/len(lemmatized_tokens)

print awl_score
# Finish all the features in the list including dictionary

# Train the model today itself.
