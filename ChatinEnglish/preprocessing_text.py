import nltk

class preprocessing_text():

    def expand_contractions(message):
        from contractions import contractions_dict
        from nltk.corpus import re

        contractions_pattern = re.compile('({})'.format('|'.join(contractions_dict.keys())),
                                          flags=re.IGNORECASE | re.DOTALL)

        def expand_match(contraction):
            match = contraction.group(0)
            first_char = match[0]
            expanded_contraction = contractions_dict.get(match) \
                if contractions_dict.get(match) \
                else contractions_dict.get(match.lower())
            expanded_contraction = expanded_contraction
            return expanded_contraction

        expanded_text = contractions_pattern.sub(expand_match, message)
        expanded_text = re.sub("'", "", expanded_text)
        return expanded_text


    # Método para tokenizar la frase de entrada del usuario
    def tokenize_message(message, re=False):
        message = expand_contractions(message)
        if re:
            # The message will be tokenize with Regular Expressions
            from nltk import re
            # For regular expression:
            # '[ \t\n]+' matches one or more space, tab (\t) or newline (\n)
            # abbreviation, \s, which means any whitespace character
            # '\W+' split the input on anything other than a word character
            # Important: the letter r (meaning "raw"), which instructs the Python interpreter to treat the string literally,
            # rather than processing any backslashed characters it contains.
            #return re.split(r'\s+', message)
            pattern = r'''(?x)     # set flag to allow verbose regexps
            (?:[A-Z]\.)+       # abbreviations, e.g. U.S.A.
            | \w+(?:-\w+)*       # words with optional internal hyphens
            | \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
            | \.\.\.             # ellipsis
            | [][.,;"'?():-_`]   # these are separate tokens; includes ], [
            '''

            # return re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", message.lower())
            return nltk.regexp_tokenize(message.lower(), pattern)
        else:
            # Tokenization by sentence and word
            from nltk import tokenize
            return tokenize.word_tokenize(message.lower())


    def unusual_words(message_tokenized):
        text_vocab = set([w.lower() for w in message_tokenized if w.isalpha()])
        print(text_vocab)
        english_vocab = set([w.lower() for w in nltk.corpus.words.words()])
        print(type(english_vocab))
        unusual = text_vocab - english_vocab
        return sorted(unusual)


    def spelling_check(message_tokenized):
        from autocorrect import Speller
        spell = Speller(lang="en")
        word_list = [[word, spell(word)] for word in unusual_words(message_tokenized)]
        return word_list


    def is_english_word_with_corpus_words(message_tokenized):
        from nltk.corpus import words
        english_vocab = set(word.lower() for word in words.words("en"))
        word_list = [[word, word in english_vocab] for word in message_tokenized]
        return word_list


    def is_english_stop_word(message_tokenized):
        from nltk.corpus import stopwords
        stopwords = stopwords.words('english')
        word_list = [[word, word in stopwords] for word in message_tokenized]
        return word_list


    def is_word_a_name(message_tokenized):
        from nltk.corpus import names
        listnames = set(word.lower() for word in names.words())
        word_list = [[word, word in listnames] for word in message_tokenized]
        return word_list


    def is_english_word_with_synonymset(message_tokenized):
        from nltk.corpus import wordnet
        word_list = [[word, wordnet.synsets(word)] for word in message_tokenized]
        # for obtain the list of synonym set (synset)
        # print(wordnet.synset('populate.v.01').lemma_names())
        # for obtain the definition of word
        # print(wordnet.synset('populate.v.01').definition())
        # for get some examples
        # print(wordnet.synset('populate.v.01').examples())
        return word_list




    # Objetivo: Encontrar sinónimos de las palabras de un mensaje
    def search_synsets(message_tokenized):
        from nltk.corpus import wordnet

        output = []

        for word in message_tokenized:
            listsynsets = []
            for synset in wordnet.synsets(word):
                listsynsets.append(synset.lemma_names())
            output.append([word, listsynsets])

        return output


    # Write conversation in output file
    def write_output_file(filename, text):
        with open(filename, "w") as f:
            f.write(text)
            f.close()


#if __name__ == "__main__":




