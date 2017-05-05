import MeCab

class WordProcessing:

    def __init__(self):
        self.tagger = MeCab.Tagger("-Ochasen")
    
    def separate_words(self, sentence):
        words = []
        for i in self.tagger.parse(sentence).split("\n"):
            parsed = i.split("\t")
            if len(parsed) == 6:
                if parsed[3].startswith("名詞") | parsed[3].startswith("動詞") | parsed[3].startswith("形容詞"):
                    words.append(parsed[2])
        
        return words
