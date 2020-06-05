# tofu-sentiment-analysis

This repository is for the sentiment analysis part of the [tool](scraper.pgrond.nl) developed for the TOFU project, led by [Dr. Tamara Metze-Burghouts](https://www.linkedin.com/in/tamara-metze-0a9b354/) of Wageningen University and Research. This project was done as an internship, for european credits, at the University of Amsterdam, supervised by [Prof. dr. Paul Groth](https://github.com/pgroth).

## What is the TOFU project?

The [TOFU](https://www.wur.nl/en/Research-Results/Chair-groups/Social-Sciences/Public-Administration-and-Policy-Group/Research/Research-Projects-of-the-Public-Administration-and-Policy-Group/TOFU-Traveling-of-Framed-Facts-and-Uncertainties.htm) project aims to better understand and democratize the mechanisms underlying so termed
TOFUs (travelling of framed facts and uncertainties). In order to improve responsible research and
innovation, they are developing two digital tools to study, reflect on, and experiment with TOFUs, and
their governance. They are co-creating these reflective tools with stakeholders of possibly controversial technological innovations in the transition to sustainable energy and to sustainable food. The tools are: <br />
(1) The ‘TOFU-crawler’ to map networks of TOFUs, and to analyze how they travel, which become
dominant, and what governance strategies of national, international and transnational actors are to cope with these TOFUs. <br />
(2) The digital ‘dashboard of imagination’ that is a reflective instrument to help industry, govern-
mental actors, activists and NGO’s, but also scholars in responsible research and innovation to improve their interactions by addressing the TOFUs more explicitly and reflectively to enhance democratic technological innovations.

### What is this repository adding to the TOFU project?

Currently the TOFU tools work together as follows: <br />
(1) The ’TOFU-crawler’ scrapes websites of relevant actors to find articles concerning a domain a
researcher is interested in, for example: wind energy. The scraper finds all relevant pages/articles based on keywords provided by the researchers and passes the images and text of the page to the ’dashboard of imagination’. <br />
(2) The ’dashboard of imagination’ displays all the images the crawler provided it with on a scale
of ’Dream’ to ’Nightmare’. ’Dream’ being that the author of the article thinks the technology or novel
food is a dream come while true, while ’Nightmare’ means that the author thinks the technology is the
worst thing that possibly could have happened. This is were this repository comes in, the ranking of images is done by analysing the textual context, the article, in which an image is displayed. The analysing is done via sentiment analysis, a binary text classification task. In addition to the ranking of the images, frames used in the articles will be analysed as well, the frames WUR are interested in right now are: economic, health, environmental. This will be a multi-label text classification task. So on the dashboard every image gets a sentiment score and a frame score.

## Installing

Download the repository

```
git clone https://github.com/roel-kuiper/tofu-sentiment-analysis.git
```

The models need to be downloaded, from [this](https://drive.google.com/open?id=17s48ApEm3b6-MvCgT_HDNANQASBH6o27) location, and placed in the predicting directory (!) in order for the tool to work.
All files can be downloaded as well from [Zenodo](placeholder TODO)

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

The accuracy of the models was tested by predicting on labeled data provided by the WUR researchers at the TOFU project ([demonstration](evaluation/predictwur.ipynb)). Unfortunately, my laptop does not have a GPU, therefore the training time and speed of inference of all transformer based models will be slower than normal. So if we keep that in mind we can still see that, as expected, more extensively pretrained models take longer to train additional data on, but at the same time also perform better. For the TOFU project however speed of inference is not as important, since the inferencing can de done during the scraping pause. 


![](evaluation/trainingtime.png)

![](evaluation/inference.png)

![](evaluation/accuracy.png)

Specs of my laptop:
Memory: 7,6 GiB
Processor: Intel® Core™ i5-6200U CPU @ 2.30GHz × 4 
Graphics: Intel® HD Graphics 520 (Skylake GT2)
#### Additions

##### Data augmentation
Since we are working with a small dataset it is interesting to look at options to artificially enlarge the dataset to improve accuracy. Unfortunately since BERT based models are massively pretrained data augmentation did not improve performance. [Notebook](additions/augmentation)

##### Labeling functions
In order to easily implement new topics to the tool labeling functions were tested. Potentially reducing the time required to label a training set. The TOFU researchers provided bins of words that are relevant to the frames used in this project. Combining the bins of words with the labeling functions I attempted to create sufficient labeling for the frame and sentiment analysis.

![](evaluation/lf.png)

As of right now, I do not feel that the labels can be compared to the hand labeled data. This means that if an additional frame needs to be added to the tool, training data will be hand labeled. [Notebook](https://github.com/roel-kuiper/tofu-sentiment-analysis/tree/master/additions/labeling%20functions)
##### Cleaning data
The data was cleaned to work better with BERT based models, [this](https://www.kaggle.com/kyakovlev/preprocessing-bert-public) notebook was used to clean the data.
## Author

* [Roel Kuiper](https://github.com/roel-kuiper)


## Special thanks to:

* [Prof. dr. Paul Groth](https://github.com/pgroth)
* [Dr. Tamara Metze-Burghouts](https://www.linkedin.com/in/tamara-metze-0a9b354/)
* [Dr. Elaine Texeira Rabello](https://www.linkedin.com/in/erabello/)
* [Efrat Gommeh](https://www.linkedin.com/in/efrat-gommeh-86267313/)
* Eduardo Rojas Padilla

