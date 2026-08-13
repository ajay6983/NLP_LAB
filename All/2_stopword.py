from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
text ="Hello Mr.Smith,How are you doing today? The weather is great and python is awesome..."
words=word_tokenize(text)
stop_words =set(stopwords.words('english'))
print(stop_words)
print(words)
filtered_sentence = []
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence)