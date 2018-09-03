# How to migrate your existing Google DialogFlow assistant to Rasa

This repository contains the code of the example assistant used to demonstrate the migration from DialogFlow to Rasa in a blogpost:


## What's in this repository
The repository consists of two directories:  

- **dialogflow-assistant** contains the files of the place_finder assistant implementation in DialogFlow.  
- **rasa-assistant** contains the files of the same assistant migrated to Rasa.   

To run this assistant you will need a [Google Place API](https://developers.google.com/places/web-service/get-api-key) key which you should provide inside the credentials.yml file of these directories.


## Setup and installation

In order to Run this assistant on Rasa, you will need Rasa NLU, Rasa Core libraries and few additional dependencies. You can install them all by running the following command:  

```
pip install -r requirements.txt
```  

You also need to install a spaCy English language model. You can install it by running:  

```
python -m spacy download en
```  

If you have any questions regarding the tutorial or this repository, please post them on the [Rasa Community Forum](https://forum.rasa.com)!
