#python feature_generator.py train/test modelpath modelName(amazon/yelp)
import os,sys,nltk,pickle,scipy.io,string
from numpy import *
from sklearn.externals import joblib

split=sys.argv[1]
modelpath = sys.argv[2]
modelName = sys.argv[3]
path = '../data/input/'+split+'/'
import Word2VecWrapper
model = Word2VecWrapper.loadVecModel(modelpath)
#model = joblib.load('../data/word2vec.model')
#print model['good']
exclude = set(string.punctuation) - set('-')

for filename in os.listdir(path):
	print filename
	fin = open(path+filename,'r')
	file_lines = len(fin.readlines())
	fin = open(path+filename,'r')
	vocab_dict = pickle.load(open('../data/vocabulary/'+filename+'.pkl','r'))
	print len(vocab_dict)
	feature_matrix = zeros((file_lines,20*len(vocab_dict.keys())))
	labels_matrix = zeros((file_lines,1))
	print feature_matrix.shape
	for lineno,line in enumerate(fin):
		[sentence, label] = line.strip().split('\t')
		#print lineno
		sentence = ''.join(ch for ch in sentence if ch not in exclude)
		words = nltk.word_tokenize(sentence)
		for word in words:
			word = word.lower()
			if word in model and word in vocab_dict:
				#print word
				#print model[word.lower()][19]
				
				for i in range(20):
					feature_matrix[lineno][vocab_dict[word]+i] = model[word.lower()][i]
				
		labels_matrix[lineno] = label
	print 'now saving feature vector for'+filename
	scipy.io.savemat('../data/features_'+modelName+'/'+split+'/'+filename+'.mat', mdict={'data': feature_matrix, 'labels':labels_matrix})
	fin.close()
	print filename+' done'