import nltk
from nltk import parse
from stat_parser import Parser
from spacy.lang.en import English


def testing_stat_parser(message):
    parser = Parser()
    return parser.parse(message)

def testing_spacy(message):
    nlp = English()
    doc = nlp(message)
    output = []

    for sent in doc:
        output.append(sent)

    return output

message = "I live in Mexico. My mom lives in Spain. I heat my country, but my mom loves your home."

# Tokens
tokens = nltk.word_tokenize(message)
print('tokens: ', tokens)

# Tags
tags = nltk.pos_tag(tokens)
print('tags: ', tags)

# Identify name entities
entities = nltk.chunk.ne_chunk(tags)
# entities.draw()

# Testing stat_parser
print('\n\ntesting_stat_parser: \n', testing_stat_parser(message))

# Testing spacy
print('\n\ntesting_spacy: \n', testing_spacy(message))


