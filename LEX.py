from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
from TRAD import word_count_per_doc, sentence_count_per_doc, cleaner
import os, math, re

unique_tokens = []

# MAIN FUNCTIONS
# Type Token Ratio (TTR)
def type_token_ratio(text):
    global unique_tokens
    unique_tokens = unique_tokentype_identifier(text)   # T - unique word types
    total_tokens = 0                                    # N - total tokens in a text

    total_tokens = word_count_per_doc(text)
    if total_tokens == 0:
        return 0

    return len(unique_tokens) / total_tokens            #return T/N

# Root TTR
def root_type_token_ratio(text):
    global unique_tokens
    #unique_tokens = unique_tokentype_identifier(text)   
    total_tokens = 0                                    

    total_tokens = word_count_per_doc(text)
    if total_tokens == 0:
        return 0

    return len(unique_tokens) / (math.sqrt(total_tokens))   #return T/√N

# Corrected TTR
def corr_type_token_ratio(text):
    global unique_tokens
    #unique_tokens = unique_tokentype_identifier(text)   
    total_tokens = 0                                    

    total_tokens = word_count_per_doc(text)
    if total_tokens == 0:
        return 0

    return len(unique_tokens) / (math.sqrt(2*total_tokens)) #return T/√2N


# Bilogarithmic TTR
def log_type_token_ratio(text):
    global unique_tokens
    #unique_tokens = unique_tokentype_identifier(text)   
    total_tokens = 0                                    

    total_tokens = word_count_per_doc(text)
    if total_tokens == 0:
        return 0

    return math.log10(len(unique_tokens)) / (math.log10(total_tokens))  #return log T/ log N


# Noun-Token Ratio
def noun_token_ratio(text):
    splitted = re.split('[?.]+', text)
    splitted = [i for i in splitted if i]   #removes empty strings in list

    noun_counter = 0
    for i in splitted:
        i = i.strip()
        tagged_text = pos_tagger.tag(word_tokenize(i))
        for x in tagged_text:
            if '|' not in x[0]:
                pos = x[1].split('|')[1]
                if pos == 'NNC' or pos == 'NNP' or pos == 'NNPA':
                    noun_counter += 1

    word_count = word_count_per_doc(text)
    print("Word Count:",word_count)
    if word_count == 0:
        return 0
    return (noun_counter/word_count)


# Verb-Token Ratio
def verb_token_ratio(text):
    splitted = re.split('[?.]+', text)
    splitted = [i for i in splitted if i]   #removes empty strings in list

    verb_counter = 0
    for i in splitted:
        i = i.strip()
        tagged_text = pos_tagger.tag(word_tokenize(i))
        for x in tagged_text:
            if '|' not in x[0]:
                pos = x[1].split('|')[1]
                if pos[:2] == 'VB':
                    verb_counter += 1

    word_count = word_count_per_doc(text)
    print("Word Count:",word_count)
    if word_count == 0:
        return 0
    return (verb_counter/word_count_per_doc(text))


# Lexical Density
def lexical_density(text):
    splitted = re.split('[?.]+', text)
    splitted = [i for i in splitted if i]   #removes empty strings in list

    lexical_item_counter = 0
    for i in splitted:
        i = i.strip()
        tagged_text = pos_tagger.tag(word_tokenize(i))
        for x in tagged_text:
            if '|' not in x[0]:
                pos = x[1].split('|')[1]
                if pos[:2] == 'VB' or pos[:2] == 'NN' or pos[:2] == 'JJ' or pos[:2] == 'RB':
                    lexical_item_counter += 1

    word_count = word_count_per_doc(text)
    print("Word Count:",word_count)
    if word_count == 0:
        return 0
    return (lexical_item_counter/word_count_per_doc(text))


# Foreign Word Counter
def foreign_word_counter(text):
    splitted = re.split('[?.]+', text)
    splitted = [i for i in splitted if i]   #removes empty strings in list

    foreign_word_counter = 0
    for i in splitted:
        i = i.strip()
        tagged_text = pos_tagger.tag(word_tokenize(i))
        for x in tagged_text:
            if '|' not in x[0]:
                pos = x[1].split('|')[1]
                if pos == 'FW':
                    foreign_word_counter += 1

    word_count = word_count_per_doc(text)
    print("Word Count:",word_count)
    if word_count == 0:
        return 0
    return (foreign_word_counter/word_count_per_doc(text))

# Compound Word Ratio
def compound_word_ratio(text):
    splitted = re.split('[?.]+', text)
    splitted = [i for i in splitted if i]   #removes empty strings in list

    compound_counter = 0
    for i in splitted:
        i = i.strip()
        splitted_sents = i.split()
        for item in splitted_sents:
            tagged_text = pos_tagger.tag(word_tokenize(item))
            #print(tagged_text)

            tag = tagged_text[0]
            if tag[0] != '':
                compound_counter += 1

    word_count = word_count_per_doc(text)
    print("Word Count:",word_count)
    if word_count == 0:
        return 0
    return (compound_counter/word_count_per_doc(text))


#UTILITY FUNCTIONS
#returns the T
def unique_tokentype_identifier(text):
    tagged_text = pos_tagger.tag([text.lower()])
    global unique_tokens
    unique_tokens = []

    for i in tagged_text:
        if '|' not in i[0]:
            pos = i[1].split('|')[1]
            if pos not in unique_tokens:
                unique_tokens.append(pos)

    return unique_tokens


java_path = "C:\\Program Files\\Java\\jdk1.8.0_111\\bin"
#java_path = "C:\\Program Files\\Java\\jdk-10.0.2\\bin"

os.environ['JAVAHOME'] = java_path

#for my laptop
stanford_dir = "C:\\Users\\CCS\\Documents\\MSCS\\THESIS\\stanford-postagger-2018-10-16"

#for my PC at NU
#stanford_dir = "C:\\Users\\jrimperial\\Documents\\MSCS\\THESIS\\POS Tagging\\stanford-postagger-full-2018-10-16\\stanford-postagger-full-2018-10-16"

modelfile = stanford_dir + "\\models\\filipino-left5words-owlqn2-distsim-pref6-inf2.tagger"
jarfile = stanford_dir+"\\stanford-postagger.jar"

pos_tagger=StanfordPOSTagger(modelfile,jarfile,java_options="-Xmx4G")