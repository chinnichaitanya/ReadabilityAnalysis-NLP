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

print awl_header_words_dict

