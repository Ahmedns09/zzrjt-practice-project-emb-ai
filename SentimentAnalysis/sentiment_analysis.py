"""
Provides access to the `sentiment_analyzer` function for 
performing sentiment analysis on the given text.
"""

import json
import requests

def sentiment_analyzer(text_to_analyse):
    '''
    Executing this function fetches and returns the sentiment 
    analysis score and label of the respective input, from the 
    Watson AI NLP Library.
    '''
    # URL of the sentiment analysis service
    url = (
        "https://sn-watson-sentiment-bert.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )
    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        # Extracting sentiment label and score from the response
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

    elif response.status_code == 500:
        label = None
        score = None

    else:
        label = None
        score = None

    # Returning a dictionary containing sentiment analysis results
    return {'label':label, 'score':score}
