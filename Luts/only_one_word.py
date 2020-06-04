import re
text = open('only_one_word.txt').read()
text_a = re.sub(r'[\W\d]', ' ', text)
words = sorted(text_a.lower().split())
print(len(words))
print(len(sorted(set(words), key=words.index)))
words = "\n".join(sorted(set(words), key=words.index))
file = open('only_one_word.txt2', 'w')
file.write(words)
file.close()