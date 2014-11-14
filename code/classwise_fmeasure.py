
import sys,pickle
from itertools import *

aspect = sys.argv[1]
modelName = sys.argv[2]
f_actual = open('../data/input/test/'+aspect,'r')
predicted_labels = pickle.load(open('../data/predicted_labels_'+modelName+'.pkl','r'))

numerator = 0
denominator_system = 0
denominator_gold = 0
for lineno,line in enumerate(f_actual):
	actual_line = int(line.split('\t')[1].strip())
	predicted_line = predicted_labels[aspect][lineno]
	
	if predicted_line == 1:
		if actual_line == 1:
			numerator +=1
		denominator_system+=1
	if actual_line == 1:
		denominator_gold+=1

print denominator_system,denominator_gold

precision = numerator/float(denominator_system)
recall = numerator/float(denominator_gold)
f_measure = (2*precision*recall)/(precision+recall)

print precision, recall, f_measure