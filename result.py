import example_tools as et

settings = et.load_settings()
if not settings:
    settings = {}

token = ('token' in settings and settings['token']) or raw_input(
    "Please enter a valid personal token (https://app.optimizely.com/v2/profile/api): ")
base_url = ('base_url' in settings and settings[
            'base_url']) or 'https://api.optimizely.com/v2'
experiment_id = ('experiment_id' in settings and settings['experiment_id']) or int(
    raw_input("Please provide an Experiment ID: "))


headers = {
    'user-agent': 'application/json',
    'Authorization': 'Bearer ' + token,
}

import requests
import json
import pprint


def create_result():

    url = base_url + '/experiments/' + str(experiment_id) + '/results'
    et.print_request_details('GET', url, {}, headers)
    r = requests.get(url, headers=headers)
    print r.text 
    j = r.json()
    et.print_response_details(r.status_code, j)


    url = base_url + '/experiments/' + str(experiment_id) + '/timeseries'
    et.print_request_details('GET', url, {}, headers)
    r = requests.get(url, headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)


    url = base_url + '/export/experiments/' + str(experiment_id) + '/results/csv'
    et.print_request_details('GET', url, {}, headers)
    r = requests.get(url, headers=headers)
    et.print_response_details(r.status_code, {})
    print(r.text)

et.print_new_method('Get experiment results')
create_result()
