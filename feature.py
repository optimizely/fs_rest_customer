# Overal notes:
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
audience_id = ('audience_id' in settings and settings['audience_id']) or int(
    raw_input("Please provide an Audience ID: "))


make_string_unique = str(random.randrange(0, 10000000000001, 2))

# Variables to modify
key = 'fs_feature_' + make_string_unique
description = 'This is s a fs feature description' + make_string_unique
variable_key = 'fs_feature_variable_' + make_string_unique
variable_description = 'This is s a fs feature variable description' + make_string_unique

headers = {
    'user-agent': 'application/json',
    'Authorization': 'Bearer ' + token,
}

import requests
import json
import pprint


def create_feature():
    url = base_url + '/features'

    feature = {
        "key": key,
        "project_id": project_id,
        "archived": False,
        "description": description,
        "environments": {
            "Production": {
                "rollout_rules": [
                    {
                        "audience_ids": [
                            audience_id
                        ],
                        "enabled": False,
                        "percentage_included": 100
                    }
                ]
            }
        },
        "variables": [
            {
                "default_value": "false",
                "key": variable_key,
                "type": "string",
                "archived": False,
                "description": variable_description
            }
        ]
    }
    et.print_request_details('POST', url, feature, headers)
    r = requests.post(url, data=json.dumps(feature), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)
    return j['id'], j['variables'][0]['id']


def update_feature(id, variable_id):
    url = base_url + '/features/' + str(id)

    feature = {
        "key": key + '_updated',
        "project_id": project_id,
        "archived": False,
        "description": description + '_updated',
        "environments": {
            "Production": {
                "rollout_rules": [
                    {
                        "audience_ids": [
                            audience_id
                        ],
                        "enabled": True,
                        "percentage_included": 1000
                    }
                ]
            }
        },
        "variables": [
            {
                "id": variable_id,
                "default_value": "true",
                "key": variable_key + '_updated',
                "type": "string",
                "archived": True,
                "description": variable_description + '_updated'
            }
        ]
    }
    et.print_request_details('PATCH', url, feature, headers)
    r = requests.patch(url, data=json.dumps(feature), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)
    return j['id']

et.print_new_method('Create a new feature')
(id, variable_id) = create_feature()

et.print_new_method('Update the feature')
update_feature(id, variable_id)
