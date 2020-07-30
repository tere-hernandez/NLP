import stanza

# Inizializing stanza
# stanza.download('em')
message = 'I live in Mexico'
nlp = stanza.Pipeline('en', processors='tokenize,pos')
doc = nlp(message)


# set java path
import os

java_path = r'C:\Program Files\Java\jdk1.8.0_161\bin\java.exe'
os.environ['JAVAHOME'] = java_path

from nltk.parse.stanford import StanfordParser

scp = StanfordParser(path_to_jar='C:/Users/carvi/Documents/Proyectos/NLP/stanford-parser-4.0.0/stanford-parser.jar',
                     path_to_models_jar='C:/Users/carvi/Documents/Proyectos/NLP/stanford-parser-4.0.0/stanford-parser-4.0.0-models.jar')

result = list(scp.raw_parse(message))
print(result[0])


from nltk.parse.corenlp import CoreNLPParser
prueba = CoreNLPParser.parse(message)
print(prueba)