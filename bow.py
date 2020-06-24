from sklearn import tree
import numpy as np
import heapq
import random

class BOW:
    def __init__(self):
        self.freq = dict()
        self.label_counts = dict()
        self.top_tag = ""
        self.most_freq = list()
        self.bow_X = list()
        self.tags_Y = list()
        self.clf = None
        self.classes = list()

    def train(self, data):
        print("Training")
        self.data = data.data['train']

        self._count_freq()
        self._remove_top(1000)
        self._create_bow()
        self.clf = tree.DecisionTreeClassifier()
        print("Training..")
        self.clf = self.clf.fit(self.bow_X, self.tags_Y)
        print("Done!")

    def predict_split(self, data, data_split):
        print("Predicting")
        if data_split not in ["test", "dev"]:
            raise("Not calid prediction set")
        self.data = data.data[data_split]

        self._create_bow()
        pred = self.clf.predict(self.bow_X)
        pred = self.classes_to_tag(pred)
        return pred

    def predict_text():
        pass

    def classes_to_tag(self, pred):
        res = list()
        for inst in pred:
            indx = np.where(inst == 1)[0]
            if not indx:
                indx = random.randint(0,len(self.classes)-1)
            else:
                indx = int(indx)

            try:
                res.append(self.classes[int(indx)])
            except TypeError:
                import ipdb; ipdb.set_trace(context=0)

        return res


    def _count_freq(self):
        for text, tag in self.data:
            for word in text:
                if '@' in word or len(word) < 2:
                    continue
                if word in self.freq.keys():
                    self.freq[word] += 1
                else:
                    self.freq[word] = 1
            if tag not in self.classes:
                self.classes.append(tag)

    def _remove_top(self, top):
        self.most_freq = heapq.nlargest(top, self.freq, key=self.freq.get)

    def to_bow(self, text_list):
            instance = list()
            for word in self.most_freq:
                if word in text_list:
                    instance.append(1)
                else:
                    instance.append(0)
            return instance

    def _create_bow(self):
        self.tags_Y = list()
        self.bow_X = list()
        for text, tag in self.data:
            instance = self.to_bow(text)
            self.bow_X.append(instance)

            class_vec = list()
            for c in self.classes:
                if tag == c:
                    class_vec.append(1)
                else:
                    class_vec.append(0)
            self.tags_Y.append(class_vec)



