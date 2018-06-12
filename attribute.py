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


make_string_unique = str(random.randrange(0, 10000000000001, 2))

# Variables to modify
key = 'fs_attribute ' + make_string_unique
name = 'FS attribute ' + make_string_unique
description = 'This is s a fs attr description' + make_string_unique


headers = {
    'user-agent': 'application/json',
    'Authorization': 'Bearer ' + token,
}

import requests
import json


def create_attribute():
    url = base_url + '/attributes'

    attribute = {
        'key': key,
        'project_id': project_id,
        'archived': False,
        'description': 'A new attribute',
        'name': name,
    }

    et.print_request_details('POST', url, attribute, headers)

    r = requests.post(url, data=json.dumps(attribute), headers=headers)

    j = r.json()
    et.print_response_details(r.status_code, j)
    return j['id']


def update_attribute(id):
    url = base_url + '/attributes/' + str(id)

    attribute = {
        'key': key + '_updated',
        'project_id': project_id,
        'archived': False,
        'description': description + ' - updated',
        'name': name + ' - updated',
    }

    et.print_request_details('PATCH', url, attribute, headers)

    r = requests.patch(url, data=json.dumps(attribute), headers=headers)

    j = r.json()
    et.print_response_details(r.status_code, j)

et.print_new_method('Create a new attribute')
id = create_attribute()

et.print_new_method('Update the attribute')
update_attribute(id)
