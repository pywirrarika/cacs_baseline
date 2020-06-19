class MajorityVote:
    def __init__(self):
        self.freq = dict()
        self.label_counts = dict()
        self.top_tag = ""

    def train(self, data):
        print("Training")
        self.data = data.data['train']
        self._get_freq()

    def predict(self, token):
        if token in self.freq.keys():
            predict = max(self.freq[token],
                          key=(lambda key: self.freq[token][key]))
        else:
            predict = self.top_tag

        return predict


    def _get_freq(self):

        # Count the number of tags seen per word
        for instance in self.data:
            for token, label in instance:
                if token in self.freq.keys():
                    if label in self.freq[token]:
                        self.freq[token][label] += 1
                    else:
                        self.freq[token][label] = 1
                else:
                    self.freq[token] = dict()
                    self.freq[token][label] = 1

                if label in self.label_counts.keys():
                    self.label_counts[label] += 1
                else:
                    self.label_counts[label] = 1

        # Store default tag as the most common tag seen
        self.top_tag = max(self.label_counts,
                           key=(lambda key: self.label_counts[key]))
