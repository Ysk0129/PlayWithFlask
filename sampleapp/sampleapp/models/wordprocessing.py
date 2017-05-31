import MeCab
import re
from sklearn.feature_extraction.text import CountVectorizer

class WordProcessing:

    def __init__(self):
        self.tagger = MeCab.Tagger("-Ochasen")
    
    def separate_words(self, sentence):
        words = []
        for i in self.tagger.parse(sentence).split("\n"):
            parsed = i.split("\t")
            if len(parsed) == 6:
                if parsed[3].startswith("名詞") | parsed[3].startswith("動詞") | parsed[3].startswith("形容詞"):
                    
                    invalid_pattern = re.compile(r"([a-xA-Z0-9_!-/:-@[-`{-~]+)|([ぁ-ん]{1,2})")
                    valid_pattern = re.compile(r"(.{2,})|([一-龥].*)")
                    if re.fullmatch(valid_pattern, parsed[2]) is not None and re.fullmatch(invalid_pattern, parsed[2]) is None:
                        words.append(parsed[2])

        return words

    def count_words(self, words):
        if len(words) < 1:
            return []

        vec = CountVectorizer()
        vec.fit(words)
        terms = vec.get_feature_names()
        words_str = " ".join(words)
        transform = vec.transform([words_str])
        words_dic = dict(zip(terms, transform.toarray()[0]))
        return sorted(words_dic.items(), reverse=True, key=lambda x: x[1])
