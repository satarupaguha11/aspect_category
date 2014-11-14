import json,string
fin =open('../data/yelp_training_set/yelp_training_set_review.json','r')
#fin =open('../data/yelp_training_set/untitled.json','r')
fout = open('../data/yelp_training_set/yelp_review_text.txt','w')
exclude = set(string.punctuation) - set('-')
for line in fin:
	temp = line.split("\"text\":")[1].split("\"type\":")[0].lower()
	sentence = ''.join(ch for ch in temp if ch not in exclude)
	fout.write(sentence+'\n')
#json_obj = json.load(fin)
#print json_obj["text"]
