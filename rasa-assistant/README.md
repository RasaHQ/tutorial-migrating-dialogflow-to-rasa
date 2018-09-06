# Place Finder assistant migrated to Rasa

This repository contains the code of the place finder assistant migrated to Rasa. You should use these files if you want to follow along the tutorial published [here](https://medium.com/rasa-blog/how-to-migrate-your-existing-google-dialogflow-assistant-to-rasa-412cd07f424a).


## What's in this repository
The repository consists of the following files and directories:  

- **data** directory contains the NLU data exported from DialogFlow and stories.md file which contains training stories for Rasa Core model.  
- **actions.py** the code of the custom action used to retrieve data from Google Places API.
- **config.yml** contains the configuration of NLU processing pipeline.
- **credentials.yml** is a file where you should place your Google Places API key.
- **domain.yml** file contains the domain configuration of the assistant.
- **endpoints.yml** contains the webhook configuration for the custom action.

To run this assistant you will need a [Google Place API](https://developers.google.com/places/web-service/get-api-key) key which you should provide inside the credentials.yml file of these directories.

If you have any questions regarding the tutorial or this repository, please post them on the [Rasa Community Forum](https://forum.rasa.com)!
