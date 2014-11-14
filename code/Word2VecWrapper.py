from gensim.models import word2vec
from nltk.tokenize import RegexpTokenizer
stops = set('for a of the and to in , . \" \'' .split())

def train_amazon(textFiles, modelpath, clusters=20):
    tokenizer = RegexpTokenizer(r'\w+')
    for t in textFiles:
        lines = open(t, "r").readlines()
        lines = [l.strip() for l in lines]
        sentences = []
        for l in lines:
            if "review/text" in l:
                thisSentence = []
                l = l[14:]
                lineTokens = tokenizer.tokenize(l)
                for w in lineTokens:
                    if w not in stops and len(w) > 1:
                        thisSentence.append(w.lower())
                sentences.append(thisSentence)        
    model = word2vec.Word2Vec(sentences, size=clusters, window=5)
    model.save_word2vec_format(modelpath, binary=True)    

def train_yelp(textFiles, modelpath, clusters=20):
    print 'in function'
    tokenizer = RegexpTokenizer(r'\w+')
    for t in textFiles:
        print 'reading  lines from file'
        lines = open(t, "r").readlines()
        lines = [l.strip() for l in lines]
        sentences = []
        count=0
        for l in lines:
            count+=1
            print count
            thisSentence = []
            lineTokens = tokenizer.tokenize(l)
            for w in lineTokens:
                if w not in stops and len(w) > 1:
                    thisSentence.append(w.lower())
            sentences.append(thisSentence)        
    model = word2vec.Word2Vec(sentences, size=clusters, window=5)
    model.save_word2vec_format(modelpath, binary=True)

def loadVecModel(modelpath = "../data/word2vec.model"):
    model = word2vec.Word2Vec.load_word2vec_format(modelpath, binary=True)
    return model

def getVector(model, term):
    return model.syn0[model.vocab[term].index]

def trainClusters(model, textPath = "../data/Rest_clean_sentences.csvC"):
    lines = open(textPath,"r").readlines()
    lines = [l.strip() for l in lines]  
    for line in lines:
        for term in line.split():
            #print term
            if term.lower() not in stops and len(term)>1:
                print getVector(model, term.lower())

def test():
    model = loadVecModel("Cell_500.model")
    print model.most_similar(["webcam", "camera"], ["autofocus"])

def main():
#     train(["Cell_Phones_&_Accessories.txt"], "Cell_500.model", 500)
    train_yelp(['../data/yelp_training_set/yelp_review_text.txt'], "../data/yelp_review.model", 20)
    
    
if __name__ == '__main__':
    main()
