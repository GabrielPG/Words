import spacy
import en_core_web_sm
import json

text_to_analyze = ( "Take this paragraph of text and return an alphabetized list of ALL unique words. "
                    "A unique word is any form of a word often communicated with essentially the same meaning. "
                    "For example, fish and fishes could be defined as a unique word by using their stem fish. " 
                    "For each unique word found in this entire paragraph, determine the how many times the word appears in total. "
                    "Also, provide an analysis of what unique sentence index position or positions the word is found. " 
                    "The following words should not be included in your analysis or result set: 'a', 'the', 'and', 'of', 'in', 'be', 'also' and 'as'. "
                    "Your final result MUST be displayed in a readable console output in the same format as the JSON sample object shown below.")

custom_stop_words = ["a", "the", "and", "of", "in", "be", "also", "as"]

def set_stop_words(nlp, stop_words, is_stop_word):
    for word in stop_words:
        lexeme = nlp.vocab[word]
        lexeme.is_stop = is_stop_word

def analyze_text(nlp, text):
    results = {}
    doc = nlp(text)
    for sentence_index, sentence in enumerate(doc.sents):
        sentence_doc = nlp(sentence.string.strip())
        for token in sentence_doc:
            if nlp.vocab[token.lemma_].is_stop or nlp.vocab[token.lemma_].is_punct:
                continue
            lemma = token.lemma_ if token.lemma_ != '-PRON-' else token.lower_ #https://github.com/explosion/spaCy/issues/962
            if not lemma in results:
                results[lemma] = {'word': lemma, 'total-occurrences': 0, 'sentence-indexes' : []}
            results[lemma]['total-occurrences'] += 1
            if not sentence_index in results[lemma]['sentence-indexes']:
                results[lemma]['sentence-indexes'].append(sentence_index)

    return {'results': [results[word] for word in sorted(results.keys())]}

def main():
    nlp = en_core_web_sm.load()
    set_stop_words(nlp, spacy.lang.en.STOP_WORDS, False)
    set_stop_words(nlp, custom_stop_words, True)
    results = analyze_text(nlp, text_to_analyze)
    print(json.dumps(results, indent=1))

main()