from nltk.stem import PorterStemmer
ps=PorterStemmer()
example_words=["s is very important to be pythonly while you are pythoning with python.All pythoners have poorly pythond atleast once"]
for w in example_words:
    print(ps.stem(w))