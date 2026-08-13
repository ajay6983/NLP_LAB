from nltk.tokenize import sent_tokenize,word_tokenize
text ="Hello Mr.Smith,How are you doing today? The weather is great and python is awesome..."
print(word_tokenize(text))
print(sent_tokenize(text))