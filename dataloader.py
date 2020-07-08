class ClassifyData:
    def __init__(self, args):
        self.args = args
        self.label_column = args.label_column
        self.text_column = args.text_column
        self.row_number = ''
        self.data = dict()
        self.file_path = dict()

        if args.dev:
            self.data['dev'] = list()
            self.file_path['dev'] = args.dev,

        if args.train:
            self.data['train'] = list()
            self.file_path['train'] = args.train,

        if args.test:
            self.data['test'] = list()
            self.file_path['test'] = args.test,

        self.print_args()

        print("Loading datasets: ")
        for key in self.data.keys():
            print(" * ", key)
            self.data[key] = self._load(self.file_path[key])


    def _load(self, file_name):
        """
        This function loads the dataset and returns a parsed list of lists
        """
        print("Openining", file_name)
        with open(file_name[0]) as F:
            return self._parse(F)

    def _parse(self, data):
        instance = list()

        for line in data:
            if line.startswith("#"):
                continue
            if not line.strip():
                continue

            line = line.strip().split("\t")

            print(self.label_column, line)
            text = line[self.text_column].lower().split()
            label = line[self.label_column]

            instance.append((text, label))

        return instance

    def print_args(self):
        options = vars(self.args)
        print("Used arguemnts:")
        for opt, arg in options.items():
            print(opt, ":", arg)


class TaggingData:
    def __init__(self, args):
        self.args = args
        self.label_column = args.label_column
        self.token_column = args.token_column
        self.row_number = ''


        self.data = {'dev': list(),
                     'train': list()}
        file_paths = {'dev': args.dev,
                      'train': args.train}

        if args.test:
            self.data['test'] = list()
            file_paths['test'] = args.test

        self.print_args()
        print("Loading datasets: ")
        for key in self.data.keys():
            print(" * ", key)
            self.data[key] = self._load(file_paths[key])

        self.print_data_stats()

    def _load(self, file_name):
        """
        This function loads the dataset and returns a parsed list of lists
        """
        with open(file_name) as F:
            return self._parse(F)

    def _parse(self, data):
        """
        Takes a file pointer and parse it accorind to the command line
        options.
        """
        parsed = list()
        instance = list()
        for line in data:
            line = line.strip().split("\t")
            new_line_flag, skip_line_flag = self._end_of_sentence(line)
            if new_line_flag:
                parsed.append(instance)
                instance = list()
                if skip_line_flag:
                    continue

            token = line[self.token_column]
            label = line[self.label_column]


            instance.append((token, label))


        return parsed

    def _end_of_sentence(self, line):
        if self.args.sentence_boundry == "empty_line":
            if not line[0]:
                return True, True
        if self.args.sentence_boundry == "new_row_number":
            if line[self.args.new_line_column_number] != self.row_number:
                self.row_number = line[self.args.new_line_column_number]
                return True, False
        return False, False

    def print_args(self):
        options = vars(self.args)
        print("Used arguemnts:")
        for opt, arg in options.items():
            print(opt, ":", arg)

    def print_data_stats(self):
        """
        Print dataset stats. We exclude test.
        """
        for key in ['train', 'dev']:
            print("Total instances:", len(self.data[key]))
