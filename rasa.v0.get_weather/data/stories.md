## greet
* greet
  - utter_greet

## thanks
* thanks
  - utter_thanks

## ask weather
* ask_weather
  - utter_getWeather

## greet + ask weather
* greet
  - utter_greet
* ask_weather
  - utter_getWeather

## ask weather + thanks
* ask_weather
  - utter_getWeather
* thanks
  - utter_thanks

## New Story

* ask_weather{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_getWeather
* ask_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_getWeather

## New Story

* ask_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_getWeather

## New Story

* ask_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_getWeather
* ask_weather{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_getWeather
* ask_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_getWeather
* ask_weather{"location":"Beijing","date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - slot{"location":"Beijing"}
    - utter_getWeather
