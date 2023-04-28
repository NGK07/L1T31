import spacy

nlp = spacy.load('en_core_web_sm') # assigning the English SpaCy model to the variable 'nlp'

# 5 example sentences which are then assigned to a new variable after being casted to 'nlp'

sentence_1 = "The old man the boat"

nlp_sentence_1 = nlp(sentence_1)

sentence_2 = "The cotton clothing is usually made of grows in Mississippi."

nlp_sentence_2 = nlp(sentence_2)

sentence_3 = "The rat the cat the dog chased killed ate the cheese."

nlp_sentence_3 = nlp(sentence_3)

sentence_4 = "Stirling, which is a historic city in Scotland, is famous for its imposing castle that overlooks the town and draws many visitors every year, some of whom claim to have seen ghosts that roam the halls at night."

nlp_sentence_4 = nlp(sentence_4)

sentence_5 = "I told the girl, India, the cat scratched Bob would help her."

nlp_sentence_5 = nlp(sentence_5)

gardenpathSentences = [nlp_sentence_1, nlp_sentence_2, nlp_sentence_3, nlp_sentence_4, nlp_sentence_5]

for i in gardenpathSentences: # iterates through all the elements of the list
    print([token.orth_ for token in i if not token.is_punct | token.is_space]) # prints all the different tokens in the sentence except for punctuation and white spaces

    print([(x, x.label_, x.label) for x in i.ents]) # Entities are identified using .ents method for every element in the list. Additional token attributes are also accessed through x.label_ and x.label.

# In the last sentence, the girl's name is India, but SpaCy has given it an entity of a geographical location - this is unexpected as I was referring to the girl named India, not the country.