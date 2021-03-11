# Cards
Simple card drawer using web sockets. Allows you to draw a random card
and each person currently visiting website will have it updated. 
Written in Flask using Flask-SocketIO.

Unable to find a basic card drawer during COVID-19 pandemic I decided to
write one myself.

To run it using virtualenv:

```sh
python3 -m venv venv
source venv/bin/activate
pip3 install requirements.txt
python3 flask-cards.py
```
The app should be available at `localhost:1234` :) 
