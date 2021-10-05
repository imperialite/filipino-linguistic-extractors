## Filipino Text Linguistic Feature Extractors

This repository contains scripts for extracting linguistic features from Filipino texts. The scripts were created for Joseph's MSCS thesis in readability assessment of children's books. The complete list of linguistic features including the formulas and descriptions are uploaded with this repo. I advise you to check the document first before running the codes.

For `TRAD`, `SYLL`, and `LM`, I'm fairly certain you are not going to encounter any dependency issues as most scripts just rely on string manipulation.  However, I you want to use `LEX` and `MORPH`, you need to setup the the following:

 - JDK8 or any latest-ish version of JDK should work.
 - Lastest version of [Stanford POS Tagger](https://nlp.stanford.edu/software/tagger.shtml) from the CoreNLP suite. Make sure to read how to set this up on your device.
 - Download the two Filipino models for the POS Tagger from Go and Nocon (2017)'s paper [here](https://github.com/matthewgo/FilipinoStanfordPOSTagger) and load them by reading the instruction at Stanford's [FAQ website](https://nlp.stanford.edu/software/pos-tagger-faq.html).


## Disclaimer
The scripts uploaded were customized to the needs of the previous research where the these were created. You are free to change or tinker with some of the code according to your own research. For example, in `LEX` and `MORPH`, I don't calculate features for all sentence but only for a random subset. You may change this as you like but take caution that it might take a long time to finish parsing.

You may also update some of the features if you feel like it. For example, for extracting language model features in `LM`, I used an old literal way of calculating perplexity by scratch derived from this [repo](https://github.com/BigFav/n-grams). This can be easily done efficiently with some open-source library like NLTK or Spacy, I believe.



## Credits

If you find this repository useful, please cite the following papers:

> Imperial, J. M., & Ong, E. (2021). Diverse Linguistic Features for Assessing Reading Difficulty of Educational Filipino Texts. _arXiv preprint arXiv:2108.00241_.
> 
> Imperial, J. M., & Ong, E. (2020). Exploring Hybrid Linguistic Feature Sets To Measure Filipino Text Readability. In _2020 International Conference on Asian Language Processing (IALP)_ (pp. 175-180). IEEE.
> 
> Imperial, J. M., & Ong, E. (2021). Application of Lexical Features Towards Improvement of Filipino Readability Identification of Children's Literature. _arXiv preprint arXiv:2101.10537_.


## Contact
If there is something you want to tell me about, you may contact me using the following information:

**Joseph Marvin Imperial**<br/>
jrimperial@national-u.edu.ph<br/>
www.josephimperial.com



