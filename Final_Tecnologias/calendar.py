from Google import Create_Service
from calendar import calendar
from pprint import pprint

cliente_secret='client_secret.json'
name_API='CalendarTC'
version_API='v3'
url_scope=['http://CalendarTC.com']

service = Create_Service(cliente_secret, name_API, version_API, url_scope)
request_body = {'summary': 'FinalTC'}
response = service.calendars().insert(body=request_body).execute()

NewEvent = {
  'summary': 'New Event Prueba', 'location': 'Universidad','description': 'Calendario final',
  'start': {'dateTime': '2022-07-09T09:00:00-05:00','timeZone': 'America/Arequipa',},
  'end': { 'dateTime': '2022-07-10T17:00:00-05:00', 'timeZone': 'America/Arequipa',},
  'conferenceData': { 'createRequest': { 'conferenceSolutionKey': { 'type': 'hangoutsMeet'}, 'requestId': "RandomString"}},
  'recurrence': [ 'RRULE:FREQ=DAILY;COUNT=5'],
  'attendees': [{'email': 'gpaccoh@ulasalle.edu.pe'}, {'email': 'jcorzol@ulasalle.edu.pe'},],
  'reminders': { 'useDefault': False, 'overrides': [ {'method': 'email', 'minutes': 24 * 60}, {'method': 'popup', 'minutes': 10},],},
}

event = service.events().insert(calendarId='primary',conferenceDataVersion=1, body=NewEvent).execute()
