import example_tools as et

settings = et.load_settings()
if not settings:
    settings = {}

token = ('token' in settings and settings['token']) or raw_input(
    "Please enter a valid personal token (https://app.optimizely.com/v2/profile/api): ")
base_url = ('base_url' in settings and settings[
            'base_url']) or 'https://api.optimizely.com/v2'
project_id = ('project_id' in settings and settings['project_id']) or int(
    raw_input("Please provide a Project ID: "))

import random
make_string_unique = str(random.randrange(0, 10000000000001, 2))

# Variables to modify
key = "full_stack_event_" + make_string_unique
name = 'FS event' + make_string_unique

headers = {
    'user-agent': 'application/json',
    'Authorization': 'Bearer ' + token,
}

import requests
import json
import pprint


def create_event():
    url = base_url + '/projects/' + str(project_id) + '/custom_events'

    event = {
        'key': key,
        "event_type": "custom",
        'archived': False,
        'description': 'A new event',
        'name': name,
        "category": "add_to_cart"
    }

    et.print_request_details('POST', url, event, headers)
    r = requests.post(url, data=json.dumps(event), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)
    return r.json()['id']


def update_event(id):
    url = base_url + '/projects/' + \
        str(project_id) + '/custom_events/' + str(id)

    event = {
        'key': key + '_updated',
        "event_type": "custom",
        'archived': False,
        'description': 'A new event' + '_updated',
        'name': 'FS event' + '_updated',
        "category": "add_to_cart"
    }

    et.print_request_details('PATCH', url, event, headers)
    r = requests.patch(url, data=json.dumps(event), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)
    return r.json()['id']

et.print_new_method('Create a new event')
id = create_event()

et.print_new_method('Update the event')
update_event(id)
