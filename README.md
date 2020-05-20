# tofu-sentiment-analysis

## What is it?

Difference in performance of generic sentiment analysis compared to topic specific sentiment analysis. Results will be used for the TOFU project.

## What is it supposed to do?

## Installing

Download the repository

```
git clone https://github.com/roel-kuiper/tofu-sentiment-analysis.git
```

The models need to be downloaded from:

```
a link
```

### Requirements

General libraries:

* numpy
* pandas
* glob

LSTM exclusive:

* gensim
* tensorflow
* keras

(Distil)BERT exclusive:

* [ktrain](https://github.com/amaiya/ktrain)

RoBERTa exclusive:

* [simpletransformers](https://github.com/ThilinaRajapakse/simpletransformers)

Data augmentation and labeling functions exclusive:

* textblob
* nltk
* snorkel
* re

## Running the tool

For all trained models a simple demo can be found under [predicting](https://github.com/roel-kuiper/tofu-sentiment-analysis/predicting). 
The best performing model is RoBerta, running this [demo](https://github.com/roel-kuiper/tofu-sentiment-analysis/blob/master/predicting/RoBERTa%20predicting.ipynb) will output the following results:

```
- - - - - - - - - - - - - - - -
articles/dummy article 1

Sentiment: 62.1%

- - - - - - - - - - - - - - - -

Economic frame: 82.8%
Health frame: 0.0%
Environment frame: 17.2%

- - - - - - - - - - - - - - - -

- - - - - - - - - - - - - - - -
articles/dummy article 2

Sentiment: 0.0%

- - - - - - - - - - - - - - - -

Economic frame: 25.0%
Health frame: 75.0%
Environment frame: 0.0%

- - - - - - - - - - - - - - - -
```

### Performance evaluation

The accuracy of the models was tested by predicting on labeled data provided by the WUR researchers at the TOFU project. The specs of my laptop: TODO

## Author

* [Roel Kuiper](https://github.com/roel-kuiper)


## Special thanks to:

* [Prof. Paul Groth](https://github.com/pgroth)
* [Dr. Tamara Metze-Burghouts](https://www.linkedin.com/in/tamara-metze-0a9b354/)
* [Dr. Elaine Texeira Rabello](https://www.linkedin.com/in/erabello/)
* Eduardo Rojas Padilla
* [Efrat Gommeh](https://www.linkedin.com/in/efrat-gommeh-86267313/)
