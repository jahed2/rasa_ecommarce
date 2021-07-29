# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionService(Action):

#     def name(self) -> Text:
#         return "action_service"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         buttons=[
#             {"payload":"/docs", "title":"Documentation"},
#             {"payload":"/vedio", "title":"vedio content"},
#         ]

#         dispatcher.utter_message(text="Hello World!")

#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher

class ValidateRestaurantForm(Action):
    def name(self)-> Text:
        return "user_details_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    )->List[EventType]:
       required_slots = ["name","number","address"]

       for slot_name in required_slots:
           if tracker.slots.get(slot_name) is None:
               #the slot is not filled yet,Request the user to filled this slot next
               return [SlotSet("requested_slot",slot_name)]
       return [SlotSet("requested_slot",None)]

class ActionSubmit(Action):
    def name(self) ->Text:
        return "action_submit"
    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",

    ) -> List[Dict[Text,Any]]:
       dispatcher.utter_message(template="utter_details_thanks",
                                Name=tracker.get_slot("name"),
                                Mobile_number=tracker.get_slot("number"),
                                Address=tracker.get_slot("address"))