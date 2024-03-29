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

class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hey!")

        return []


class ActionGoodbye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Bye~")

        return []


class ActionThanks(Action):

    def name(self) -> Text:
        return "action_thanks"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("You are welcome:)")

        return []


class ActionCreateMeeting(Action):

    def name(self) -> Text:
        return "action_create_meeting"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        startTime = tracker.get_slot('startTime')
        endTime = tracker.get_slot('endTime')
        date = tracker.get_slot('date')
        slots = {}
        slots['startTime'] = startTime
        slots['endTime'] = endTime
        slots['date'] = date
        dispatcher.utter_message("You are intent to create a meeting. The slots are {}".format(slots))
    
        return []


class ActionUpdateMeeting(Action):

    def name(self) -> Text:
        return "action_update_meeting"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        startTime = tracker.get_slot('startTime')
        endTime = tracker.get_slot('endTime')
        date = tracker.get_slot('date')
        slots = {}
        slots['startTime'] = startTime
        slots['endTime'] = endTime
        slots['date'] = date
        dispatcher.utter_message("You are intent to update a meeting. The slots are {}".format(slots))
    
        return []


class ActionShowNextMeeting(Action):

    def name(self) -> Text:
        return "action_show_next_meeting"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        startTime = tracker.get_slot('startTime')
        endTime = tracker.get_slot('endTime')
        date = tracker.get_slot('date')
        slots = {}
        slots['startTime'] = startTime
        slots['endTime'] = endTime
        slots['date'] = date
        dispatcher.utter_message("You are intent to show next meeting. The slots are {}".format(slots))
    
        return []








