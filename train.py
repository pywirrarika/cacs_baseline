import argparse
import pickle

from dataloader import TaggingData, ClassifyData
from voting import MajorityVote
from bow import BOW

if __name__ == "__main__":
    task_types = ('tagging', 'classification',)
    sentence_boundry = ('empty_line', 'new_row_number')

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-tk', '--task', choices=task_types,
                        required=True, help="Task we are trining")
    parser.add_argument('-tc', '--token_column', type=int,
                        help="Set the number of the column where the \
                        tags are set", default="2", required=False)
    parser.add_argument('-lc', '--label_column', type=int, help="Set the\
                        number of the column where the tokens are set",
                        required=True)
    parser.add_argument('-txc', '--text_column', type=int,
                        help="Set the number of the column where the tags \
                        are set  (for classification)", default="2")
    parser.add_argument('--train', help="Train file", required=True)
    parser.add_argument('--test', help="Test file", default="")
    parser.add_argument('--dev', help="Development set",
                        required=True)
    parser.add_argument('--sentence_boundry', choices=sentence_boundry,
                        help="How to split sentences")
    parser.add_argument('--new_line_column_number', type=int,
                        help="Specfiy if --sentence_boundary=new_row_number")
    parser.add_argument('--model', help="Name of the model file",
                        required=True)
    parser.add_argument('--data_file', help="Name of the model file",
                        required=True)

    args = parser.parse_args()
    for arg in vars(args):
        print(arg, getattr(args, arg))

    if args.task in ("tagging"):

        data = TaggingData(args)

        model = MajorityVote()
        model.train(data)

        print("Storing model and data")
        with open(args.model, "wb") as F:
            pickle.dump(model, F)
        with open(args.data_file, "wb") as F:
            pickle.dump(data, F)

    elif args.task in ("classification"):
        data = ClassifyData(args)
        model = BOW()
        model.train(data)


        print("Storing model and data")
        with open(args.model, "wb") as F:
            pickle.dump(model, F)
        with open(args.data_file, "wb") as F:
            pickle.dump(data, F)


