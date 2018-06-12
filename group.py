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

experiment_id = ('experiment_id' in settings and settings['experiment_id']) or int(
    raw_input("Please provide an Experiment ID: "))


import random
make_string_unique = str(random.randrange(0, 10000000000001, 2))
name = 'FS group' + make_string_unique

headers = {
    'user-agent': 'application/json',
    'Authorization': 'Bearer ' + token,
}

import requests
import json
import pprint


def create_group():
    url = base_url + '/groups'

    group = {
        'project_id': project_id,
        'archived': False,
        'description': 'A new group',
        'name': name,
        'entities': [
            {
                "id": experiment_id,
                "kind": "Experiment",
                "weight": 5000
            }
        ]
    }
    et.print_request_details('POST', url, group, headers)
    r = requests.post(url, data=json.dumps(group), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)
    return r.json()['id']


def update_group(id):
    url = base_url + '/groups/' + str(id)

    group = {
        'project_id': project_id,
        'archived': False,
        'description': 'A new group updated',
        'name': name + ' updated',
        'entities': [
            {
                "id": experiment_id,
                "kind": "Experiment",
                "weight": 5000
            }
        ]
    }
    et.print_request_details('PATCH', url, group, headers)
    r = requests.patch(url, data=json.dumps(group), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)

et.print_new_method('Create a new group')
id = create_group()

et.print_new_method('Update the group')
update_group(id)
