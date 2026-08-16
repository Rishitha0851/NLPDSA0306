import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')
word="car"
synsets=wordnet.synsets(word)

print("Word=",word)
print("number of synstes=",len(synsets))

for synset in synsets:
  print("\nsynset=",synset.name())
  print("definition=",synset.definition())
  print("examples=",synset.examples())

  synonyms=synset.lemmas()
  print("synonyms=",[lemma.name() for lemma in synonyms])