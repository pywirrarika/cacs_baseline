# Baseline for Computational Approaches for Code-Switching class

This baseline provides simple methods for classification and sequence tagging.

## Usage

The train command has the following syntax. At training-time, you have to specify the name of the training, dev, and test files. Also, the file where the model and binary data file is going to be stored needs to be specified (--model, --data_file). These two files are important for prediction. The two tasks that can be used: tagging and classification. You have to specify the task (-tk). Details for each method are provided below.

```
usage: train.py [-h] -tk {tagging,classification}
                [-tc TOKEN_COLUMN FOR TAGGING)] -lc LABEL_COLUMN
                [-txc TEXT_COLUMN] --train TRAIN [--test TEST] --dev DEV
                [--sentence_boundry (for tagging {empty_line,new_row_number}]
                [--new_line_column_number NEW_LINE_COLUMN_NUMBER] --model
                MODEL --data_file DATA_FILE
```
Example:
```
python train.py --task classification --train /home/users2/magerml/share/cs_datasets/sentiment/es-en/train.tsv --dev /home/users2/magerml/share/cs_datasets/sentiment/es-en/dev.tsv  --model model_classify.bin --data_file data_file_classify.bin -txc 2 -lc 1
```

For prediction, you only need to specify the binary data file, the model data file, task, and output file.
```
usage: predict.py [-h] -tk {tagging,classification} --model MODEL --data_file
                  DATA_FILE --data_split {dev,test} --output_file OUTPUT_FILE
```

## Tasks
There are differences for each task. Labels and text/words should be separated by a tab character (\t) and be on the same line. 

### Tagging

Please, use -tk tagging. Then you have to specify what column number (0..n) contains a label (-lc) and what column contains the word to be tagged (-tc). Please use an empty line to separate training instances (--sentence_boundary empty line).

### Classification

Use -tk classification. Then you have to specifiy what column number (0..n) contains a label (-lc) and what column contain the text to be classified (txc).

### Split and tagging

Use the tagging method for tag all labels, and split the words randomly according to the number of predicted tags. Composed tags should contain two or more tags separated with a space character. i.e., "ES WIX" is one single tag, and the presence of one space character means that it has to be segmented one time. 
