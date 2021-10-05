from TRAD import *
import pandas as pd

with open('all_data.txt', 'r', encoding='utf-8', errors='ignore') as file:
	file_contents = file.readlines()

	label = []
	title = []
	word_count = []
	sentence_count = []
	phrase_count = []
	average_word_length = []
	average_sentence_length = []
	average_word_syll_count = []
	polysyll_count = []

	for item in file_contents:
		parsed_text = item.split(',',2)
		parsed_text[2] = parsed_text[2].strip()

		print(parsed_text[0], parsed_text[1])

		title.append(parsed_text[0])
		label.append(parsed_text[1])
		word_count.append(word_count_per_doc(item))
		sentence_count.append(sentence_count_per_doc(item))
		phrase_count.append(ave_phrase_count_per_doc(item))
		average_word_length.append(ave_word_length(item))
		average_sentence_length.append(word_count_per_sentence(item))
		average_word_syll_count.append(ave_syllable_count_of_word(item))
		polysyll_count.append(polysyll_count_per_doc(item))

df = pd.DataFrame(list(zip(title, word_count, sentence_count, phrase_count, average_word_length, average_sentence_length, average_word_syll_count, polysyll_count, label)),columns=['book_title','word_count','sentence_count', 'phrase_count_per_sentence', 'average_word_len', 'average_sentence_len', 'average_syllable_count', 'polysyll_count', 'grade_level'])

df.to_csv('trad.csv',index=False)

print('\nFEATURE EXTRACTION DONE')