import pickle,sys

modelName = sys.argv[1]
predicted_labels = pickle.load(open('../data/predicted_labels_'+modelName+'.pkl','r'))
#predicted_probabilities = pickle.load(open('../data/predicted_probabilities.pkl','r'))
fin = f_actual = open('../data/input/test/food','r')
fout = open('../data/prediction_'+modelName,'w')
aspects = ['service','price','miscellaneous','food','ambience']
for lineno,line in enumerate(fin):
	sentence = line.split('\t')[0]
	predicted_aspects = list()
	for aspect in aspects:
		if predicted_labels[aspect][lineno] == 1:
			predicted_aspects.append(aspect)
	fout.write(sentence)
	if len(predicted_aspects)>0:
		for aspect in predicted_aspects:
			fout.write('\t'+aspect)
	else:
		fout.write('\tmiscellaneous')
		'''
		max_prob = 0
		for aspect in aspects:
			if predicted_probabilities[aspect][lineno][1]>max_prob:
				max_prob = predicted_probabilities[aspect][lineno][1]
				max_aspect = aspect
		print max_aspect
		fout.write('\t'+max_aspect)
		'''
	fout.write('\n')