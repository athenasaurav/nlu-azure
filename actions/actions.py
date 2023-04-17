# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List
import requests
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Form, AllSlotsReset, Restarted

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text="I am really sorry, I didn't get that. Can you please rephrase it? I am still learning. I am a bot who need more testers. I am connected to RASA NLU engine andd Azure api for voice."
        url = "http://43.204.162.18:5006/generate"

        payload = json.dumps({
        "sentence": "{}".format(text),
        "speaker": "en-IN-NeerjaNeural"
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        response = response.json()
        dispatcher.utter_message(text=response['url'])
        return []


