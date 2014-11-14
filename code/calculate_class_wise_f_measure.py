
import sys,pickle
from itertools import *

aspect = sys.argv[1]
f_actual = open('../data/input/test/'+aspect,'r')
#print len(f_actual.readlines())
predicted_labels = pickle.load(open('../data/predicted_labels.pkl','r'))

true_pos = 0
false_pos = 0
false_neg = 0
for lineno,line in enumerate(f_actual):
	actual_line = int(line.split('\t')[1].strip())
	predicted_line = predicted_labels[aspect][lineno]
	if predicted_line == 1:
		if actual_line == 1:
			true_pos+=1
		else:
			false_pos +=1
	else:
		if predicted_line != -1:
			false_neg +=1

precision = true_pos/float(true_pos+false_pos)
recall = true_pos/float(true_pos+false_neg)
f_measure = 2*true_pos/float(2*true_pos+false_pos+false_neg)

print precision, recall, f_measure
