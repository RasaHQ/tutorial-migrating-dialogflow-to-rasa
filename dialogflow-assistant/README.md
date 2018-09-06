# Place Finder assistant implemented in DialogFlow

This repository contains the code of the place finder assistant implemented in DialogFlow. If you want to fully replicate the tutorial [here](https://medium.com/rasa-blog/how-to-migrate-your-existing-google-dialogflow-assistant-to-rasa-412cd07f424a), you can load this assistant to DialogFlow.


## What's in this repository
The repository consists of the following files and directories:  

- **place_finder** directory contains the place_finder assistant data files exported from DialogFlow.  
- **dialogflow_webhook.py** the code of the custom webhook used to retrieve data from Google Places API.
- **dialogflow_webhook_response.py** contains the response configuration of the assistant.
- **credentials.yml** is a file where you should place your Google Places API key.

To run this assistant you will need a [Google Place API](https://developers.google.com/places/web-service/get-api-key) key which you should provide inside the credentials.yml file of these directories.

If you have any questions regarding the tutorial or this repository, please post them on the [Rasa Community Forum](https://forum.rasa.com)!
