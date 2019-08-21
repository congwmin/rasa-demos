## greeting
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## thanks
* thanks
  - utter_thanks

## query weather without date and location
* query_weather
  - utter_ask_date
* provide_date{"date": "today"}
  - utter_ask_location
* provide_location{"location": "Beijing"}
  - utter_weather

## query weather without location with datd
* query_weather{"date": "today"}
  - utter_ask_location
* provide_location{"location": "Beijing"}
  - utter_weather

## query weather without datd with location
* query_weather{"location": "Beijing"}
  - utter_ask_date
* provide_date{"date": "today"}
  - utter_weather

## query weather with data and location
* query_weather{"date": "today", "location": "Beijing"}
  - utter_weather

## book_ticket with toCity, fromCity, date
* book_ticket{"toCity": "Beijing", "fromCity": "Seattle", "date": "today"}
  - utter_confirm_book_ticket

## book ticket with toCity, fromCity without date
* book_ticket{"toCity": "Beijing", "fromCity": "Seattle"}
  - utter_ask_date
* provide_date
  - utter_confirm_book_ticket

## book ticket with date without toCity, fromCity
* book_ticket{"date": "today"}
  - utter_ask_toCity
* provide_toCity{"toCity": "Seattle"}
  - utter_ask_fromCity
* provde_fromCity{"fromCity": "Beijing"}
  - utter_confirm_book_ticket

## book ticket without toCity, fromCity, date
* book_ticket
  - utter_ask_toCity
* provide_toCity{"toCity": "Seattle"}
  - utter_ask_fromCity
* provide_fromCity{"fromCity": "Beijing"}
  - utter_ask_date
* provide_date
  - utter_confirm_book_ticket

## New Story

* query_weather
    - utter_ask_date
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_weather

## New Story

* query_weather
    - utter_ask_date
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather

## New Story

* query_weather{"date":"today","location":"Beijing"}
    - slot{"date":"today"}
    - slot{"location":"Beijing"}
    - utter_weather
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_weather

## New Story

* query_weather{"location":"Suzhou","date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - slot{"location":"Suzhou"}
    - utter_weather
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_weather
* provide_location{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_weather

## New Story

* book_ticket{"toCity":"Beijing","date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - slot{"toCity":"Beijing"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Suzhou"}
    - slot{"fromCity":"Suzhou"}
    - utter_confirm_book_ticket

## New Story

* book_ticket
    - utter_ask_toCity
* provide_toCity{"toCity":"Suzhou"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_ask_date
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"fromCity":"Beijing","toCity":"Suzhou"}
    - slot{"fromCity":"Beijing"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* provide_date{"date":"next week"}
    - slot{"date":"next week"}
    - utter_confirm_book_ticket
* thanks
    - utter_thanks

## New Story

* query_weather{"date":"today","location":"Beijing"}
    - slot{"date":"today"}
    - slot{"location":"Beijing"}
    - utter_weather
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_weather
* query_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather

## New Story

* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_weather

## New Story

* query_weather{"location":"Beijing","date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - slot{"location":"Beijing"}
    - utter_weather
* query_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather

## New Story

* query_weather{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_ask_date
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_weather
* provide_location{"location":"Seattle"}
    - slot{"location":"Seattle"}
    - utter_weather
* query_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather

## New Story

* query_weather{"date":"today","location":"Beijing"}
    - slot{"date":"today"}
    - slot{"location":"Beijing"}
    - utter_weather
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_weather
* query_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather
* query_weather{"location":"Seattle"}
    - slot{"location":"Seattle"}
    - utter_weather

## New Story

* book_ticket{"toCity":"Beijing","date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - slot{"toCity":"Beijing"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Suzhou"}
    - slot{"fromCity":"Suzhou"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_toCity
* provide_toCity{"toCity":"Seattle"}
    - slot{"toCity":"Seattle"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_ask_date
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_toCity
* provide_toCity{"toCity":"Seattle"}
    - slot{"toCity":"Seattle"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"fromCity":"Beijing","toCity":"Suzhou"}
    - slot{"fromCity":"Beijing"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* query_weather{"location":"Suzhou","date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - slot{"location":"Suzhou"}
    - utter_weather
* book_ticket{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"fromCity":"Beijing","toCity":"Suzhou"}
    - slot{"fromCity":"Beijing"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* query_weather{"location":"Suzhou","date":"today"}
    - slot{"date":"today"}
    - slot{"location":"Suzhou"}
    - utter_weather
* book_ticket{"date":"today"}
    - slot{"date":"today"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"toCity":"Suzhou"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_confirm_book_ticket

## New Story

* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_weather

## New Story

* query_weather{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_ask_date
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_weather
* query_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather
* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_weather

## New Story

* query_weather{"location":"Beijing","date":"today"}
    - slot{"date":"today"}
    - slot{"location":"Beijing"}
    - utter_weather
* book_ticket{"toCity":"Beijing","date":"today"}
    - slot{"date":"today"}
    - slot{"toCity":"Beijing"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Suzhou"}
    - slot{"fromCity":"Suzhou"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"toCity":"Suzhou"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* query_weather{"location":"Beijing","date":"today"}
    - slot{"date":"today"}
    - slot{"location":"Beijing"}
    - utter_weather
* book_ticket{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"toCity":"Seattle"}
    - slot{"toCity":"Seattle"}
    - utter_ask_date
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_confirm_book_ticket

## New Story

* book_ticket
    - utter_ask_toCity
* provide_toCity{"fromCity":"Suzhou"}
    - slot{"fromCity":"Suzhou"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_ask_date
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"fromCity":"Beijing","toCity":"Suzhou"}
    - slot{"fromCity":"Beijing"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* query_weather{"location":"Suzhou","date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - slot{"location":"Suzhou"}
    - utter_weather
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_weather
* book_ticket{"date":"today"}
    - slot{"date":"today"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"fromCity":"Beijing","toCity":"Suzhou"}
    - slot{"fromCity":"Beijing"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"toCity":"Beijing"}
    - slot{"toCity":"Beijing"}
    - utter_ask_date
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_fromCity
* provide_fromCity{"toCity":"Seattle"}
    - slot{"toCity":"Seattle"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"toCity":"Suzhou"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* query_weather{"location":"Suzhou","date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - slot{"location":"Suzhou"}
    - utter_weather
* book_ticket{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_confirm_book_ticket

## New Story

* greet
    - utter_greet
* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_weather
* thanks
    - utter_thanks

## New Story

* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_weather

## New Story

* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"toCity":"Seattle"}
    - slot{"toCity":"Seattle"}
    - utter_weather

## New Story

* query_weather
    - utter_ask_date
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_weather

## New Story

* query_weather
    - utter_ask_date
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_weather

## New Story

* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_weather

## New Story

* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_weather

## New Story

* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"fromCity":"Suzhou"}
    - slot{"fromCity":"Suzhou"}
    - utter_weather

## New Story

* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"fromCity":"Suzhou"}
    - slot{"fromCity":"Suzhou"}
    - utter_weather

## New Story

* query_weather{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_ask_date
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_weather
* query_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_weather

## New Story

* query_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_ask_date
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_weather

## New Story

* query_weather
    - utter_ask_date
* provide_date{"date":"next week"}
    - slot{"date":"next week"}
    - utter_ask_location
* provide_location{"fromCity":"Suzhou"}
    - slot{"fromCity":"Suzhou"}
    - utter_weather

## New Story

* query_weather{"date":"next week"}
    - slot{"date":"next week"}
    - utter_ask_location
* provide_location{"fromCity":"Suzhou"}
    - slot{"fromCity":"Suzhou"}
    - utter_weather

## New Story

* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_weather

## New Story

* book_ticket
    - utter_ask_toCity
* provide_toCity{"toCity":"Seattle"}
    - slot{"toCity":"Seattle"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_ask_date
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_confirm_book_ticket

## New Story

* query_weather{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_ask_date
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_weather
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_weather

## New Story

* book_ticket{"toCity":"Suzhou"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* query_weather{"location":"Suzhou","date":"today"}
    - slot{"date":"today"}
    - slot{"location":"Suzhou"}
    - utter_weather
* book_ticket{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_confirm_book_ticket

## New Story

* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_weather

## Generated Story 9206744629121256667
* query_weather{"date": "today"}
    - slot{"date": "today"}
    - utter_ask_location
* provide_location{"toCity": "Beijing"}
    - slot{"toCity": "Beijing"}
    - rewind
* provide_location{"toCity": "Beijing", "location": "Beijing"}
    - slot{"location": "Beijing"}
    - slot{"toCity": "Beijing"}
    - rewind
* provide_location{"toCity": "Beijing"}
    - slot{"toCity": "Beijing"}
    - rewind
* provide_location{"toCity": "Beijing"}
    - slot{"toCity": "Beijing"}
    - rewind
* provide_location{"location": "Beijing"}
    - slot{"location": "Beijing"}
    - utter_weather

## New Story

* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_weather

## New Story

* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather

## New Story

* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"location":"Suzhou"}
    - slot{"location":"Suzhou"}

## New Story

* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"location":"Seattle"}
    - slot{"location":"Seattle"}
    - utter_weather

## New Story

* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_weather

## New Story

* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather

## New Story

* book_ticket{"toCity":"Suzhou"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_confirm_book_ticket
* thanks
    - utter_thanks

## New Story

* book_ticket{"fromCity":"Beijing","toCity":"Suzhou"}
    - slot{"fromCity":"Beijing"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* query_weather{"location":"Suzhou","date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - slot{"location":"Suzhou"}
    - utter_weather
* book_ticket{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_confirm_book_ticket

## New Story

* greet
    - utter_greet
* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_weather
* query_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather

## New Story

* greet
    - utter_greet
* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_weather
* thanks
    - utter_thanks

## New Story

* book_ticket{"toCity":"Suzhou"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_confirm_book_ticket
* thanks
    - utter_thanks

## New Story

* book_ticket{"toCity":"Suzhou"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* query_weather{"location":"Suzhou","date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - slot{"location":"Suzhou"}
    - utter_weather
* book_ticket{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_confirm_book_ticket

## New Story

* query_weather
    - utter_ask_date
* book_ticket{"fromCity":"Suzhou","toCity":"Seattle","date":"today"}
    - slot{"date":"today"}
    - slot{"fromCity":"Suzhou"}
    - slot{"toCity":"Seattle"}
    - utter_confirm_book_ticket
* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* provide_location{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_weather

## New Story

* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_ask_location
* book_ticket{"fromCity":"Beijing","toCity":"Suzhou"}
    - slot{"fromCity":"Beijing"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_confirm_book_ticket
* query_weather{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_weather

## New Story

* query_weather{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_ask_date
* book_ticket{"fromCity":"Seattle","toCity":"Beijing","date":"today"}
    - slot{"date":"today"}
    - slot{"fromCity":"Seattle"}
    - slot{"toCity":"Beijing"}
    - utter_confirm_book_ticket
* query_weather{"date":"today"}
    - slot{"date":"today"}
    - utter_weather

## New Story

* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_weather
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_weather
* provide_date{"date":"next week"}
    - slot{"date":"next week"}
    - utter_weather
* query_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather

## New Story

* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_weather
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_weather
* query_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather

## New Story

* query_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_location
* provide_location{"location":"Beijing"}
    - slot{"location":"Beijing"}
    - utter_weather
* provide_date{"date":"today"}
    - slot{"date":"today"}
    - utter_weather
* query_weather{"location":"Suzhou"}
    - slot{"location":"Suzhou"}
    - utter_weather

## New Story

* book_ticket{"toCity":"Suzhou"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* provide_date{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_confirm_book_ticket

## New Story

* book_ticket{"toCity":"Suzhou"}
    - slot{"toCity":"Suzhou"}
    - utter_ask_date
* query_weather{"location":"Suzhou","date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - slot{"location":"Suzhou"}
    - utter_weather
* book_ticket{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - utter_ask_fromCity
* provide_fromCity{"fromCity":"Beijing"}
    - slot{"fromCity":"Beijing"}
    - utter_confirm_book_ticket
