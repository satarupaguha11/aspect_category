import pickle,re,string,os
from collections import defaultdict

def find_unigrams(sentence):
	unigrams = [word.lower() for word in re.split('\W+',sentence) if word!='']
	return unigrams

def find_bigrams(unigrams):
	bigrams = []
	for i in range(len(unigrams)-1):
		string = unigrams[i]+' '+unigrams[i+1]
		bigrams.append(string)
	return bigrams

def create_vocabulary():
	exclude = set(string.punctuation) - set('-')
	path = '../data/input/train/'
	
	for filename in os.listdir(path):
		print path,filename
		fin = open(path+filename,'r')
		vocab_dict = defaultdict()
		count = 0
		for line in fin:
			sentence = line.split('\t')[0]
			sentence = ''.join(ch for ch in sentence if ch not in exclude)
			unigrams = find_unigrams(sentence)
			#bigrams = find_bigrams(unigrams)
			#unigrams_bigrams = unigrams+bigrams
			for word in unigrams:
				if word.lower() not in vocab_dict:
					vocab_dict[word.lower()]=count
					count+=1

		fin.close()
		fin = open('../data/input/test/'+filename,'r')

		for line in fin:
			sentence = line.split('\t')[0]
			sentence = ''.join(ch for ch in sentence if ch not in exclude)
			unigrams = find_unigrams(sentence)
			#bigrams = find_bigrams(unigrams)
			#unigrams_bigrams = unigrams+bigrams
			for word in unigrams:
				if word.lower() not in vocab_dict:
					vocab_dict[word.lower()] = count
					count+=1
		fin.close()
		pickle.dump(vocab_dict,open('../data/vocabulary/'+filename+'.pkl','w'))
create_vocabulary()