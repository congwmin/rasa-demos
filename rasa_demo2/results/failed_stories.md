## New Story
* query_weather{"date": "today"}
    - slot{"date": "today"}
    - slot{"date": "today"}
    - utter_ask_location
* provide_location{"location": "Suzhou"}
    - slot{"location": "Suzhou"}
    - slot{"location": "Suzhou"}
    - action_listen   <!-- predicted: utter_weather -->


