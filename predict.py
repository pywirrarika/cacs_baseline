import argparse
import pickle

from accuracy import accuracy

if __name__ == "__main__":
    task_types = ('tagging', 'classification',)
    data_splits = ('dev', 'test',)

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-tk', '--task', choices=task_types,
                        required=True, help="Task we are trining")
    parser.add_argument('--model', help="Name of the model file",
                        required=True)
    parser.add_argument('--data_file', help="Name of the model file",
                        required=True)
    parser.add_argument('--data_split', help="Name of the predict split",
                        choices=data_splits, required=True)
    parser.add_argument('--output_file', help="Name of the output file",
                        required=True)

    args = parser.parse_args()

    if args.task in ("tagging"):
        print("Loading model and data")
        with open(args.model, "rb") as F:
            model = pickle.load(F)
        with open(args.data_file, "rb") as F:
            data = pickle.load(F)


        print("Predicting")
        F = open(args.output_file, "w")
        results = list()
        sent_res = list()
        for instance in data.data[args.data_split]:
            for token, label in instance:
                predict = model.predict(token)
                print(token, label, predict, sep="\t", file=F)
                sent_res.append((token, label, predict))
            print(file=F)
            results.append(sent_res)

        print("Evaluation")
        print(len(results))
        print("Acc.:", round(accuracy(results)*100,2), "%")

    else:
        pass
