# tofu-sentiment-analysis

Difference in performance of generic sentiment analysis compared to topic specific sentiment analysis. Results will be used for the TOFU project.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Installing

Download the repository

```
git clone TODO
```

The models can be downloaded from:

```
a link
```

## Running the tool

Demo of tool, with best performing model (RoBERTa):
```
from simpletransformers.classification import ClassificationModel
import pandas as pd
import glob

# return the predicted labels
def analyse(article):
    paragraphs = [par for par in article.split('\n') if str(par) != '' and len(par)>75]
    sen, raw_sen = sentiment_model.predict(paragraphs)
    frame, raw_frame = frame_model.predict(paragraphs)
    eco, hea, env = get_credible(raw_frame, frame)
    sen_score = round(sum(sen)/len(sen)*100,1)
    return sen_score, eco, hea, env

# returns the frame scores for confident predictions only
def get_credible(raw_f, f):
    cred = [f[i] for i in range(len(f)) if raw_f[i][f[i]] > 2]
    eco = get_per(cred, 0)
    hea = get_per(cred, 1)
    env = get_per(cred, 2)
    return eco, hea, env

# percentage calculater - probably redundant and more easy to do
def get_per(l, n):
    try:
        tmp = round(l.count(n)/len(l)*100,1)
    except:
        tmp = 0
    return tmp

# load models
sentiment_model = ClassificationModel(
    "roberta",
    "models/sentiment/RoBERTa/outputs/",
    use_cuda=False
)

frame_model = ClassificationModel(
    "roberta",
    "models/frame/RoBERTa/outputs/",
    use_cuda=False
)

# predict
files = glob.glob('articles/*')

for file in files:
    article = open(file,'r').read()
    s_score, eco_score, hea_score, env_score = analyse(article)
    print('\n- - - - - - - - - - - - - - - -\n{}\n'.format(file))
    print('Sentiment: {}%'.format(s_score))
    print('\n- - - - - - - - - - - - - - - -\n')
    print('Economic frame: {}%\nHealth frame: {}%\nEnvironment frame: {}%'.format(eco_score, hea_score, env_score))
    print('\n- - - - - - - - - - - - - - - -\n')
```

Running this demo will output the following results:

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

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

Libraries used in this repository

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

## Author

* [Roel Kuiper](https://github.com/roel-kuiper)


## Special thanks to:

* [Prof. Paul Groth](https://github.com/pgroth)
* [Dr. Tamara Metze-Burghouts](https://www.linkedin.com/in/tamara-metze-0a9b354/)
* [Dr. Elaine Texeira Rabello](https://www.linkedin.com/in/erabello/)
* Eduardo Rojas Padilla
* [Efrat Gommeh](https://www.linkedin.com/in/efrat-gommeh-86267313/)
