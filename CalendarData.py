from __future__ import print_function

import IO
import datetime
import os

import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

__num_days = ['0',]

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
    return credentials


def get_data():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='#contacts@group.v.calendar.google.com', timeMin=now, maxResults=20, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    eventsResult = service.events().list(
        calendarId='en.usa#holiday@group.v.calendar.google.com', timeMin=now, maxResults=20, singleEvents=True,
        orderBy='startTime').execute()
    events.extend(eventsResult.get('items', []))

    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=20, singleEvents=True,
        orderBy='startTime').execute()
    events.extend(eventsResult.get('items', []))

    events = sorted(events, key=sort)

    stored_events=""
    if not events:
        stored_events = '-1:No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        days = get_dif(start)
        if not stored_events.__contains__(event['summary']):
            stored_events += repr(days) + ":" + event['summary'] + "\n"
    stored_events.strip()
    IO.write("data/events", stored_events)


def get_dif(start):
    parts = start.split("-")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2].split("T")[0])
    d1 = datetime.date(year, month, day)
    d2 = datetime.date.today()
    d3 = d1-d2
    return d3.days


def sort(event):
    return event['start'].get('dateTime', event['start'].get('date'))
