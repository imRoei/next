def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    sentence = sentence.split()
    return ' '.join(list(words[word] for word in sentence))
print(translate("el gato esta en la casa"))
