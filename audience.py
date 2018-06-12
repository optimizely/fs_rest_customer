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
custom_audience_attribute = ('project_id' in settings and settings['custom_audience_attribute']) or int(
    raw_input("Please provide the name of a custom attribute: "))

import random

make_string_unique = str(random.randrange(0, 10000000000001, 2))

# Variables to modify
name = "Using a Full Stack attribute" + make_string_unique

headers = {
    'user-agent': 'application/json',
    'Authorization': 'Bearer ' + token,
}

import requests
import json
import pprint


def create_audience():
    url = base_url + '/audiences'

    audience = {
        "project_id": project_id,
        "archived": False,
        "conditions": '["and", ["or", ["or", {"name": "' + custom_audience_attribute + '", "type": "custom_attribute", "value": "full stack value"}], ["or", {"name": "' + custom_audience_attribute + '", "type": "custom_attribute", "value": "val 2"}]]]',
        "description": "Using a Full Stack attribute",
        "is_classic": False,
        "name": name,
        "segmentation": False
    }

    et.print_request_details('POST', url, audience, headers)
    r = requests.post(url, data=json.dumps(audience), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)
    return r.json()['id']


def update_audience(id):
    url = base_url + '/audiences/' + str(id)

    audience = {
        "project_id": project_id,
        "archived": False,
        "conditions": '["and", ["or", ["or", {"name": "' + custom_audience_attribute + '", "type": "custom_attribute", "value": "full stack value"}], ["or", {"name": "' + custom_audience_attribute + '", "type": "custom_attribute", "value": "val 2"}]]]',
        "description": "Using a Full Stack attribute",
        "is_classic": False,
        "name": name + '_updated',
        "segmentation": False
    }

    et.print_request_details('PATCH', url, audience, headers)
    r = requests.patch(url, data=json.dumps(audience), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)

et.print_new_method('Create a new audience')
id = create_audience()

et.print_new_method('Update the audience')
update_audience(id)
