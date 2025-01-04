# Word Frequency Counter

sentence = input("Enter a Sentence: ")

#split the sentence into words
words = sentence.split()

#initialize dictionary
word_count = {}

#count word frequence
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)