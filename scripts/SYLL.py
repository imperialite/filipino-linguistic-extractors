from collections import Counter
from nltk import word_tokenize
import re
from TRAD import word_count_per_doc

# REGEX controller for combining CVC patterns
c = '([bcdfghjklmnpqrstvwxyz])'
v = '([aeiou])'

def get_consonant_cluster(text):
	cleaned = cleaner(text)
	word_count = word_count_per_doc(text)

	pattern = "([bcdfghjklmnpqrstvwxyz]{1}[bcdfghjklmnpqrstvwxyz]{1}[bcdfghjklmnpqrstvwxyz]*)"
	matches = len(re.findall(pattern, cleaned))
	return matches / word_count

def get_v(text):
	cleaned = cleaner(text)
	word_count = word_count_per_doc(text)

	pattern = v
	matches = len(re.findall(pattern, cleaned))
	return matches / word_count

def get_cv(text):
	cleaned = cleaner(text)
	word_count = word_count_per_doc(text)

	pattern = c+v
	matches = len(re.findall(pattern, cleaned))
	return matches / word_count

def get_vc(text):
	cleaned = cleaner(text)
	word_count = word_count_per_doc(text)

	pattern = v+c
	matches = len(re.findall(pattern, cleaned))
	return matches / word_count

def get_cvc(text):
	cleaned = cleaner(text)
	word_count = word_count_per_doc(text)

	pattern = c+v+c
	matches = len(re.findall(pattern, cleaned))
	return matches / word_count

def get_vcc(text):
	cleaned = cleaner(text)
	word_count = word_count_per_doc(text)

	pattern = v+c+c
	matches = len(re.findall(pattern, cleaned))
	return matches / word_count

def get_cvcc(text):
	cleaned = cleaner(text)
	word_count = word_count_per_doc(text)

	pattern = c+v+c+c
	matches = len(re.findall(pattern, cleaned))
	return matches / word_count

def get_ccvc(text):
	cleaned = cleaner(text)
	word_count = word_count_per_doc(text)

	pattern = c+c+v+c
	matches = len(re.findall(pattern, cleaned))
	return matches / word_count

def get_ccvcc(text):
	cleaned = cleaner(text)
	word_count = word_count_per_doc(text)

	pattern = c+c+v+c+c
	matches = len(re.findall(pattern, cleaned))
	return matches / word_count

def get_ccvccc(text):
	cleaned = cleaner(text)
	word_count = word_count_per_doc(text)

	pattern = c+c+v+c+c+c
	matches = len(re.findall(pattern, cleaned))
	return matches / word_count

#UTILITY FUNCTIONS
def cleaner(text):
	text = re.sub('[^a-zA-Z ]', '', str(text))
	text = re.sub(' +', ' ', str(text))
	cleaned_text = text.strip()
	cleaned_text = cleaned_text.lower()
	return cleaned_text

def word_length(text):
	return len(text)

def syllable_counter(text):
	syllable_counts = 0
	for char in text:
		if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
			syllable_counts += 1
	return syllable_counts
