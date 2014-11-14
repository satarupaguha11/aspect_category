#python prediction.py modelName
from sklearn.linear_model import LogisticRegression
import sys,scipy.io,pickle
from collections import defaultdict

modelName = sys.argv[1]
aspects = ['service','price','miscellaneous','food','ambience']
predicted_labels = defaultdict()
predicted_probabilities = defaultdict()
for aspect_name in aspects:
	print aspect_name
	model = pickle.load(open('../data/models_'+modelName+'/'+aspect_name+'.pkl','r'))
	feature_file=scipy.io.loadmat('../data/features_'+modelName+'/test/'+aspect_name+'.mat')
	X = feature_file['data']
	predicted_labels[aspect_name] = model.predict(X)
	#predicted_probabilities[aspect_name] = model.predict_proba(X)
	pickle.dump(predicted_labels,open('../data/predicted_labels_'+modelName+'.pkl','w'))
	#pickle.dump(predicted_probabilities,open('../data/predicted_probabilities.pkl','w'))
	print aspect_name+' done'
	
