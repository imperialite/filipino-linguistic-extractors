from collections import Counter
from nltk import word_tokenize
import re

#MAIN FUNCTIONS

#Total number of WORDS in a document
def word_count_per_doc(text):
	tokenized = word_tokenize(cleaner(text))
	return len(tokenized)

#Total number of SENTENCES in a document
def sentence_count_per_doc(text):
	text = text.replace('…','.')
	period_count = text.count('.')
	question_count = text.count('?')
	exclam_count = text.count('!')
	return period_count+question_count+exclam_count #fix this later

#Average number of WORDS in a SENTENCE
def word_count_per_sentence(text):
	word_count = word_count_per_doc(text)
	sentence_count = sentence_count_per_doc(text)
	if sentence_count == 0:
		sentence_count = 1
	return word_count_per_doc(text)/sentence_count_per_doc(text)

"""
#Average number of SENTENCES in a document
def avg_sentence_length_per_doc(text):
	splitted = text.split('.')
	splitted = [i for i in splitted if i] 	#removes empty strings in list
	word_count_list = []
	for i in splitted:
		word_count_list.append(word_count_per_doc(i))
	return sum(word_count_list) / len(word_count_list)
"""

#Average number of PHRASES per SENTENCE in a document
def ave_phrase_count_per_doc(text):
	splitted = text.split('.')
	splitted = [i for i in splitted if i] 	#removes empty strings in list
	phrase_counter = 0

	if ',' not in text:
		return phrase_counter

	for i in splitted:
		phrase_counter += i.count(',')
		phrase_counter += 1
	return phrase_counter / len(splitted)

#Average SYLLABLE COUNT of WORDS in a document
def ave_syllable_count_of_word(text):
	splitted = text.split('.')
	splitted = [i for i in splitted if i] 	#removes empty strings in list
	total_syllable_count = 0
	for i in splitted:
		splitted_sent = word_tokenize(cleaner(i))
		for n in splitted_sent:
			total_syllable_count += syllable_counter(n)
	return total_syllable_count / word_count_per_doc(text)

#Average WORD LENGTH
def ave_word_length(text):
	cleaned = cleaner(text)
	tokenized = word_tokenize(cleaned)
	word_length = 0
	for i in tokenized:
		word_length += len(i)
	return word_length / word_count_per_doc(text)

#Number of POLYSYLLABLE WORDS in a document
def polysyll_count_per_doc(text):
	cleaned = cleaner(text)
	splitted = word_tokenize(cleaned)
	polysyll_counter = 0
	for i in splitted:
		syll_count = syllable_counter(i)
		if syll_count > 4:
			polysyll_counter += 1
	return polysyll_counter


#UTILITY FUNCTIONS
def cleaner(text):
	text = re.sub('[^a-zA-Z ]', '', str(text))
	text = re.sub(' +', ' ', str(text))
	cleaned_text = text.strip()
	return cleaned_text

def word_length(text):
	return len(text)

def syllable_counter(text):
	syllable_counts = 0
	for char in text:
		if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
			syllable_counts += 1
	return syllable_counts

"""
text = "Ito ang halimaw ng mga kulay.  Ngayong araw  gumising siyang kakaiba ang pakiramdam  nalilito  tuliro… Hindi niya alam kung ano ang mali sa kaniya.  Nalilito ka na naman? Hindi ka na natuto.  Anong gulo ang ginawa mo sa iyong mga damdamin!"


print('Word Count:', word_count_per_doc(text))
print('Average Phrase Count:',ave_phrase_count_per_doc(text))
print('Sentence Count:',sentence_count_per_doc(text))
print('Average Word Length:', ave_word_length(text))
print('Average Sentence Length:',word_count_per_sentence(text))
print('Average Word Syllable Count:',ave_syllable_count_of_word(text))
print('Polysyllabic Word Count:',polysyll_count_per_doc(text))
"""
