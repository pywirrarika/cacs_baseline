
DATA_PATH= #Path to datafile

python train.py --task tagging \
  --token_column 4 \
  --label_column 5 \
  --train $DATA_PATH/calcs_train.tsv \
  --dev $DATA_PATH/calcs_dev.tsv \
  --sentence_boundry new_row_number \
  --new_line_column_number 0 \
  --model model.bin \
  --data_file data.bin
