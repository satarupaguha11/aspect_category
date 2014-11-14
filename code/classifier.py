from sklearn.linear_model import LogisticRegression
import scipy.io, sys,pickle
from numpy import *
aspects = list()
aspects.append(sys.argv[1])
modelName=sys.argv[2]
#aspects = ['service','price','miscellaneous','food','ambience']
for aspect in aspects:
	feature_file = scipy.io.loadmat('../data/features_'+modelName+'/'+'/train/'+aspect+'.mat')
	X = feature_file['data']
	Y = feature_file['labels']
	print 'features loaded'
	n_samples = Y.size
	#print n_samples
	Y = reshape(Y,(n_samples,))
	print 'feature vector reshaped'
	logreg = LogisticRegression(penalty='l2', dual=False, tol=0.00001, C=0.04, fit_intercept=True, intercept_scaling=1, class_weight='auto', random_state=None)
	print 'fitting the model'
	clf = logreg.fit(X, Y)
	print 'model fitted'
	pickle.dump(clf, open('../data/models_'+modelName+'/'+aspect+'.pkl','w'))
	print 'model saved'
	