# Impact of news on stock


## Motivation

This project is the Capstone project for Udacity course Data Scientist Nanodegree. The objective here is to find the impact of the news on stock movements. It worth mentioning that Kaggle also is running a similar competition, and this project is not relevant to that by no means. Neither the data nor the algorithms.
It worth mentioning that Kaggle also is running a similar competition, and this project is not relevant to that by no means. Neither the data nor the algorithms.

## Usage example

This can be served as a backend for any webpage that tries to make draw parallels between stock movement and news
## Disclaimer:

This analysis should NOT be taken as financial advice. Needless to say, that market complexities cannot be captured by general analysis.

## Requirements

The major libraries used in these projects are:
1. numpy,
2. pandas,
3. scickitlearn,
4. Django,
5. Djangorestframework
6. Scrapy
7. Spacy
8. NLTK


## File structure

This project has three major components:

- Scraping news: For this purpose, Scrappy library is used in python. Every 1 hour a Crontab job automatically reads news from few news pages.

- prediction using ML algorithms: Current note book shows some fundamental ML approaches, that I had taken in in order to come up with a reasonable model.

- Serving the results in a backend server: The data is stored in a Linux based virtual private server, using Django Rest Framework.

## Project results

The final back-end can be found in the following url:


http://134.209.177.21/

it contains two endpoints; news in which news has been stored. Here up and down fields actually are the probability prediction of the ML model (developed in this notebook) based on the news content. For example, "up"=0.6 means that the news content is 60% likely to be a positive news associated with increasing stock.

The other endpoint entity where the entities of each news has been stored for statistical purposes./
