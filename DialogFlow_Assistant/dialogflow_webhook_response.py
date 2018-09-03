import json

def empty_response(text):
    response = json.dumps({"fulfillmentText": text
                , "fulfillmentMessages": [
                  {
                    "text": {
                      "text": [
                        text
                        ]
                    }
                  }
                ]})
    return response


def place_response(text, session, address, opening_hours, rating):
    response = json.dumps({"fulfillmentText": text
                , "fulfillmentMessages": [
                  {
                    "text": {
                      "text": [
                        text
                        ]
                    }
                  }
                ],
                "outputContexts": [
                    {
                        "name": session + '/contexts/address',
                        "lifespanCount": 5,
                        "parameters": {
                            "param": address
                        }
                    },
                    {
                        "name": session + '/contexts/opening_hours',
                        "lifespanCount": 5,
                        "parameters": {
                            "param": opening_hours
                        }
                    },
                    {
                        "name": session + '/contexts/rating',
                        "lifespanCount": 5,
                        "parameters": {
                            "param": rating
                        }
                    }
                ]
            })

    return response