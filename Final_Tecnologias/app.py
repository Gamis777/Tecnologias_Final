from flask import Flask, render_template, request, redirect, url_for
from calendar import calendar
from pprint import pprint
from Google import Create_Service

app=Flask(__name__)
cliente_secret='client_secret.json'
name_API='CalendarTC'
version_API='v3'
url_scope=['http://CalendarTC.com']

service = Create_Service(cliente_secret, name_API, version_API, url_scope)

@app.route('/newevent', methods=['POST'])
def create_evento():
    print(request.json)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":   
    app.run(port=8085, debug=True)