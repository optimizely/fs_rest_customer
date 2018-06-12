import example_tools as et

settings = et.load_settings()
if not settings:
    settings = {}

token = ('token' in settings and settings['token']) or raw_input(
    "Please enter a valid personal token (https://app.optimizely.com/v2/profile/api): ")
base_url = ('base_url' in settings and settings[
            'base_url']) or 'https://api.optimizely.com/v2'

import random
make_string_unique = str(random.randrange(0, 10000000000001, 2))

name = 'full_stack project' + make_string_unique
description = 'My REST API FS project' + make_string_unique

headers = {
    'user-agent': 'application/json',
    'Authorization': 'Bearer ' + token,
}

import requests
import json
import pprint


def create_project():
    url = base_url + '/projects'

    project = {
        'name': name,
        'confidence_threshold': 0.9,
        'description': description,
        'platform': 'custom',
        'sdks': ['python'],
        'status': 'active',
    }
    et.print_request_details('POST', url, project, headers)
    r = requests.post(url, data=json.dumps(project), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)
    return r.json()['id']


def update_project(id):
    url = base_url + '/projects/' + str(id)

    project = {
        'name': name + "_updated",
        'confidence_threshold': 0.9,
        'description': description + "_updated",
        'platform': 'custom',
        'sdks': ['python'],
        'status': 'active',
    }
    et.print_request_details('PATCH', url, project, headers)
    r = requests.patch(url, data=json.dumps(project), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)

et.print_new_method('Create a new project')
id = create_project()

et.print_new_method('Update the project')
update_project(id)
