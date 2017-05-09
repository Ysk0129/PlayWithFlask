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
                    if len(parsed[2]) >= 2 or re.search(r'[一-龥]' ,parsed[2]) != None:
                        if re.search(r'[a-xA-Z0-9_!-/:-@[-`{-~]' ,parsed[2]) == None and re.match(r'[ぁ-ん]{2}' ,parsed[2]) == None:
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
