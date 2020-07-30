from stat_parser import Parser
import nltk
from preprocessing_text import tokenize_message, spelling_check

def chat_with_robo():
    parser = Parser()

    flag = True
    print("The instructions for talk with me: \n",
          "If you want finish the conversation, please type thanks or bye.\n")
    print("ROBO: Hi, my name is Robo.")
    while flag == True:
        message = input()
        message = message.lower()

        if message != 'bye':
            # Analyzing the input
            print('\nvocabulary: ', nltk.tokenize(message))
            print('\nword frequency: ' + nltk.FreqDist(nltk.tokenize(message)).most_common(10))

            # -----------
            # add part-of-speech tags to text
            # -----------
            # Tagging message with basic nltk tokenize
            print(nltk.pos_tag(nltk.word_tokenize(message)))
            # Tiene problemas con la identificación del pronombre 'I', lo pone como noun (sustantivo)

            # Tagging message

            # trace = 1: then the parser will report the steps that it takes as it parses a text.
            # rd_parser = nltk.RecursiveDescentParser(, trace = 1)

            # Review grammar
            # rd_parser = nltk.RecursiveDescentParser(nltk.ChartParser)
            rd_parser = parser.parse(message)

            i = 1

            for tree_struc in rd_parser:
                print(str(i) + 'tree_struc: ', tree_struc)

                wrong_syntax = 1
                s = tree_struc
                wrong_syntax = 0
                print("\n Correct Grammar")
                i += 1
            if wrong_syntax == 1:
                print("\n Wrong Grammar")

                # write_output_file(...

        else:
            flag = False
            print("ROBO: Bye! take care..")



message = "Hi, I'm Tere (but you can tel me Te). " \
          "This is my hause. I've live here since 2001 with Teresa, my mom. When we arived here, the town was groging"
message_tok = tokenize_message(message)


print('message: ', message, '\nspelling_check: ', spelling_check(message_tok))

#print(message, '\nTokenize with NLTK module: ', message_tok, '\nTokenize with re: ', tokenize_message(message, True))

# Lemmatization
#wordlemma = nltk.WordNetLemmatizer()
#print([wordlemma.lemmatize(w) for w in message_tok])

"""
words_validated_corpusWord = is_english_word_with_corpus_words(message_tok)
print(words_validated_corpusWord)
words_validated_stopWords = is_english_stop_word(message_tok)
words_validated_names = is_word_a_name(message_tok)
words_validated_synonymset = is_english_word_with_synonymset(message_tok)
words_with_synsets = search_synsets(message_tok)

"""


