from flask import Flask
from flask import send_file
from ics import Calendar, Event
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/get-cal")
def get_cal():
    c = Calendar()
    e = Event()
    e.name = "My cool event"
    e.begin = '2019-11-11 00:00:00'
    c.events.add(e)
    with open('my.ics', 'w') as my_file:
        my_file.writelines(c)
    return send_file("my.ics", mimetype="text/calendar", as_attachment=True)


port = int(os.environ.get("PORT", 5000))
app.run(debug=True, port=port)
