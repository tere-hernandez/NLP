import spacy
from spacy_grammar.grammar import Grammar

message = "I live in Mexico. My mom lives in Spain. I heat my country, but my mom loves your home."
message = "We can elaborate this distinction as follow."

nlp = spacy.load('en_core_web_sm')
grammar = Grammar(nlp)
nlp.add_pipe(grammar)
doc = nlp(message)
print([i._.g_as_follow_as_follows for i in doc])

doc = nlp('I can haz cheeseburger.')
doc._.has_grammar_error  # True