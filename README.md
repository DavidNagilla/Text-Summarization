# Text-Summarization

Bidirectiona LSTM for text summarization

Training
Download the data and run the following scripts in this order:

python cnn_daily_load.py

python word2vec.py

python lstm_Attention.py


## dependencies

tensorflow, keras,sklearn

numpy, pandas, matplotlib

## LSTM encoder decoder architectural and trainig parameters:

batch_size = 50 

epochs = 20

hidden_units = 128

learning_rate = 0.005

clip_norm = 2.0

test_size = 0.2

optimizer = RMsprop

dropout = 0.2

