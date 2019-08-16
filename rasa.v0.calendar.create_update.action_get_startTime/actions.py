from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.executor import CollectingDispatcher


#class ActionHelloWorld(Action):
#
#    def name(self) -> Text:
#        return "action_hello_world"
#
#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#        dispatcher.utter_message("Hello World!")
#
#        return []

class ActionGetStartTime(Action):

    def name(self) -> Text:
        return "action_get_startTime"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("here")
        startTime = tracker.get_slot('startTime')
        dispatcher.utter_message("The start time is {}".format(str(startTime)))

        return []


