# dls_tg_bot

## Description

Project is devoted to building Telegram bot, that will be able to receive photo and return recognized English text from it.


## Repo structure

* `bot/` - code for bot logic
* `code/notebooks/` - examples of inputs and outputs of NNs
* `code/tasks/` - bash scripts
* `code/text_recognizer/` - main directory with py scripts for datasets downloading and processing, defining architecture of NNs, saved weights
* `code/training/` - py scripts for training NNs and WandB sweeps
* `code/wandb/` - WandB logs


## Solution and problems

The datasets used for the solution are EMNIST and IAM. First one was used to test pipeline, it is expanded MNIST, that consists of figures and letters symbols. 

The IAM Handwriting Database contains forms of handwritten English text and has 13,353 isolated and labeled text lines. [1]

Datasets processing pipelines have been used from Fullstack Deep Learning bootcamp. [2]

Solution consists 2 consecutive NNs: first is CNN that detects rows regions on photo, second - LSTM with CTC loss that returns recognised symbols from cut rows. The experiments have been managed by Weights&Biases service. The weights of trained NNs. have been saved and deployment pipeline using Docker and AWS has been built. This was inspired by Youtube playlist of Gleb Mikhailov. [3] 

Thus, used technologies: tf.keras, Docker, AWS EC2, WandB, aoigram.

Currently, bot is operating asyncroniously, but the quality of recognized text is low, at least, at my tries. Maybe because sent photos are quite different from those used in training.

## TODO

* Add more augmentations and sophisticated NNs with more layers 
* Add Russian dataset
* Sophisticate bot logic
* Try Pytorch

## References
[1] http://www.fki.inf.unibe.ch/databases/iam-handwriting-database

[2] https://fullstackdeeplearning.com/

[3] https://www.youtube.com/watch?v=3ODGMMVYq78&list=PLQJ7ptkRY-xYLEAC5Y_sKqrJ9RA-U7Dja
