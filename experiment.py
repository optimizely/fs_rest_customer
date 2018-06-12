# Overal notes:
# The Class level description talks about campaigns, which aren't relevant
# or FS

import random

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
event_id = ('event_id' in settings and settings['event_id']) or int(
    raw_input("Please provide an Event ID: "))
feature_id = ('feature_id' in settings and settings['feature_id']) or raw_input(
    "Please provide an Feature ID (leave empty to create an experiment without a feature): ")
variable_values = ('variable_values' in settings and settings[
                   'variable_values'])

has_features = False

if feature_id == '':
    feature_id = None
else:
    feature_id = int(feature_id)

if feature_id and not variable_values:
    variable_values = []
    while True:
        key = raw_input(
            "Please provide a variable key (or hit enter without a value to stop adding): ")
        if key == '':
            break
        else:
            value = raw_input("Please provide a variable value: ")
        variable_values.append({
            key: value
        })

variables = {}
if feature_id: 
    for variable in variable_values:
        for key in variable:
            variables[key] = variable[key]


make_string_unique = str(random.randrange(0, 10000000000001, 2))

# Variables to modify
key = 'fs_exp_' + make_string_unique
description = 'This is s a fs exp description' + make_string_unique
variation_key = 'var_name_' + make_string_unique


headers = {
    'user-agent': 'application/json',
    'Authorization': 'Bearer ' + token,
}

import requests
import json
import pprint


def create_experiment():
    url = base_url + '/experiments'

    experiment = {
        'project_id': project_id,
        'type': 'a/b',
        'description': description,
        'holdback': 5000,
        'archived': False,
        'key': key,
        "metrics": [
            {
                "aggregator": "unique",
                "event_id": event_id,
                "scope": "visitor",
                "winning_direction": "increasing"
            }
        ],
        "multivariate_traffic_policy": "full_factorial",
        "variations": [
            {
                "weight": 10000,
                "archived": False,
                "description": "blabla",
                "key": variation_key
            }
        ]
    }

    if feature_id:
        experiment['feature_id'] = feature_id
        if len(variable_values) > 0:
            experiment['variations'][0]['variable_values'] = variables

    et.print_request_details('POST', url, experiment, headers)
    r = requests.post(url, data=json.dumps(experiment), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)

    return (j['id'], j['variations'][0]['variation_id'])


def update_start_experiment(id, variation_id):
    url = base_url + '/experiments/' + str(id) + '?action=start'

    experiment = {
        'project_id': project_id,
        'type': 'a/b',
        'description': description + "_updated",
        'holdback': 5000,
        'archived': False,
        'key': key + "_updated",
        "metrics": [
            {
                "aggregator": "unique",
                "event_id": event_id,
                "scope": "visitor",
                "winning_direction": "increasing"
            }
        ],
        "multivariate_traffic_policy": "full_factorial",
        "variations": [
            {
                "weight": 10000,
                "archived": False,
                "description": "blabla",
                "key": variation_key + '_updated',
                "variation_id": variation_id
            }
        ]
    }

    if feature_id:
        experiment['feature_id'] = feature_id
        if len(variable_values) > 0:
            experiment['variations'][0]['variable_values'] = variables
            experiment['variations'][0]['feature_enabled'] = True

    et.print_request_details('PATCH', url, experiment, headers)
    r = requests.patch(url, data=json.dumps(experiment), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)


def pause_experiment(id):
    url = base_url + '/experiments/' + str(id) + '?action=pause'

    experiment = {}

    et.print_request_details('PATCH', url, experiment, headers)
    r = requests.patch(url, data=json.dumps(experiment), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)
    return r.json()


def update_experiment_2(id, variation_id):
    url = base_url + '/experiments/' + str(id) + ''

    experiment = {
        'project_id': project_id,
        'type': 'a/b',
        'description': description + "_updated_2",
        'holdback': 5000,
        'archived': False,
        'key': key + "_updated_2",
        "metrics": [
            {
                "aggregator": "unique",
                "event_id": event_id,
                "scope": "visitor",
                "winning_direction": "increasing"
            }
        ],
        "multivariate_traffic_policy": "full_factorial",
        "variations": [
            {
                "weight": 10000,
                "archived": False,
                "description": "blabla_2",
                "key": variation_key + '_updated_2',
                "variation_id": variation_id
            }
        ]
    }

    if feature_id:
        experiment['feature_id'] = feature_id
        if len(variable_values) > 0:
            experiment['variations'][0]['variable_values'] = variables
            experiment['variations'][0]['feature_enabled'] = True

    et.print_request_details('PATCH', url, experiment, headers)
    r = requests.patch(url, data=json.dumps(experiment), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)

et.print_new_method('Create a new experiment')
id, variation_id = create_experiment()

et.print_new_method('Update and start the experiment')
update_start_experiment(id, variation_id)

et.print_new_method('Pause the experiment')
pause_experiment(id)

et.print_new_method('Update the experiment #2')
update_experiment_2(id, variation_id)
