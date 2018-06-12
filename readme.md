# Optimizely Full Stack REST Tutorial

This tutorial enables you to quickly get started in your development efforts to programmatically create an Experiment using the Full Stack REST APIs. This Python programming sample demonstrates how to:

* Create a Project, Attribute, Event, Audience, and Experiment.
* Run, pause, and update an Experiment.  

## Prerequisites
* Python
* YAML and JSON libraries for Python

## Quick Start
This section shows you how to prepare, build, and run the sample project.

### Create an Account and Get a Token
In order to build and run the sample you must retrieve a token: 

1. Create a developer account at [app.optimizely.com](https://app.optimizely.com/v2/profile/api). Once logged in, the dashboard is displayed.
2. Click **Profile** on the bottom left hand corner of the navigation tree.
3. Select the **API Access** tab.
4. Click **Generate New Token**.
5. Enter a name for the new token on the popup and click **Create**. The website will redirect to the dashboard.
6. Copy the token value from the **Token** column on the dashboard.
7. Open **[.settings.yaml](./.settings.yaml)** in this package using a text editor.
8. Replace the token value in **[.settings.yaml](./.settings.yaml)** with the value obtained in Step 6. For example:

```yaml
token: "2:Ba4f4asdcasd1234....."

```

### Run the Python Scripts
The sample project consists of a series of Python scripts that invoke Optimizely's REST APIs to build the necessary components of an Experiment. As you run the scripts, you must copy various pieces of information (e.g. ID values) from the responses that are displayed on the screen and paste them into the appropriate parts of **[.settings.yaml](./.settings.yaml)**.

This section walks you through the scripts and the steps to copy and paste the data you need from the output.

#### Generate a Project
1. Run **[project.py](./project.py)**:

```
python project.py
```

2. Copy the value for `id` from the **Update the project** response:
```
Update the project
Request:
PATCH https://api.optimizely.com/v2/projects/10839870236
...

Response:
200
body:
{
    "account_id": 10761771283, 
    "confidence_threshold": 0.9, 
    "created": "2018-06-08T16:12:29.455700Z", 
    "id": 10839870236, // Copy this generated Project ID
    ...
}
```

3. Paste the ID value into the `project_id` field in **[.settings.yaml](./.settings.yaml)**:
```yaml
...
# Create a project ID by executing project.py
project_id: 10839870236 // Paste the Project ID here
...
```

#### Generate an Attribute
1. Run **attribute.py**:

```
python attribute.py
```

2. Copy the value for `name` from the **Update the attribute** response:
```
Update the attribute
Request:
PATCH https://api.optimizely.com/v2/attributes/10804487279
...

Response:
200
body:
{
    ... 
    "last_modified": "2018-06-08T16:13:40.378120Z", 
    "name": "FS attribute 4001593747014 - updated", // Copy this generated Attribute name
    "project_id": 10839870236
}
```
3. Paste the value into the `custom_audience_attribute` field in **[.settings.yaml](./.settings.yaml)**:
```yaml
# Create an attribute Name by executing attribute.py
custom_audience_attribute: FS attribute 4001593747014 - updated // Paste the name here
```

#### Generate an Event
1. Run **[event.py](./event.py)**:

```
python event.py
```

2. Copy the value for `id` from the **Update the event** response:

```
Update the event
Request:
PATCH https://api.optimizely.com/v2/projects/10839870236/custom_events/10843270186
...

Response:
200
body:
{
    "archived": false, 
    "category": "add_to_cart", 
    "created": "2018-06-08T16:14:36.952890Z", 
    "description": "A new event_updated", 
    "event_type": "custom", 
    "id": 10843270186, // Copy this generated ID
    ...
}
```

3. Paste the value into the `event_id` field in **[.settings.yaml](./.settings.yaml)**:

```yaml
# Create an event ID by executing event.py
event_id: 10843270186 // Paste the ID here
```

#### Generate an Audience
1. Run **[audience.py](./audience.py)**:

```
python audience.py
```

2. Copy the value for `id` from the **Update the audience** response:

```
Update the audience
Request:
PATCH https://api.optimizely.com/v2/audiences/10828513760
h...

Response:
200
body:
{
    "archived": false, 
    "conditions": "[\"and\", [\"or\", [\"or\...", 
    "created": "2018-06-08T16:15:02.745860Z", 
    "description": "Using a Full Stack attribute", 
    "id": 10828513760, // Copy this generated ID
    ...
}
```

3. Paste the value into the `audience_id` field in **[.settings.yaml](./.settings.yaml)**:

```yaml
# Create an audience ID by executing audience.py
audience_id: 10828513760 //Paste the ID here
```

#### Generate a Feature
1. Run **[feature.py](./feature.py)**:

```
python feature.py
```

2. Copy the value for `key` from the **Update the feature** response:

```
Update the feature
Request:
PATCH https://api.optimizely.com/v2/features/10839281466
...

Response:
200
body:
{
    "archived": false, 
    "created": "2018-06-08T16:16:04.143120Z", 
    "description": "This is s a fs feature description2458297709274_updated", 
    "environments": {
        "Production": {
        ...
        }
    }, 
    "id": 10839281466, 
    "key": "fs_feature_2458297709274_updated", // Copy this generated key
    ...
    ]
}
```

3. Paste the key under the `variable_values` field in **[.settings.yaml](./.settings.yaml)**:

```yaml
# Create an feature ID and variables by executing feature.py
# feature_id: 10756572576
# variable_values:
#   - fs_feature_2458297709274_updated  // Paste the key here
```

**Note:** Providing a Feature and Variable for an Experiment is optional. For this quickstart, this section can be commented out.

#### Generate an Experiment
1. Run **[experiment.py](./experiment.py)**:

```
python experiment.py
```

2. Press the **return** key when the following prompt appears:
```
Please provide an Feature ID (leave empty to create an experiment without a feature): 
```

3. Copy the value for `id` from the **Update the experiment #2** response:

```
Response:
Update the experiment #2
Request:
PATCH https://api.optimizely.com/v2/experiments/10834392320
...

200
body:
{
    "allocation_policy": "manual", 
    "audience_conditions": "everyone", 
    "campaign_id": 10802528852, 
    "changes": [], 
    "created": "2018-06-08T16:17:35.589410Z", 
    "description": "This is s a fs exp description3614128498008_updated_2", 
    "earliest": "2018-06-08T16:17:43.023580Z", 
    "holdback": 5000, 
    "id": 10834392320,  // Copy this generated ID
    ...
}
```

4. Paste the ID in the `experiment_id` field in **[.settings.yaml](./.settings.yaml)**:

```
# Create an experiment ID by executing experiment.py
experiment_id: 10834392320 // Paste the ID here
```

#### Run the Experiment
1. Save **[.settings.yaml](./.settings.yaml)**.

2. Run **[result.py](./result.py)**:

```
python result.py
```

The script runs the Experiment using the settings pasted into **[.settings.yaml](./.settings.yaml)** to generate results, run a time series, and retrieve and display the results (stored as CSV data) to the screen.

## Steps to Create the Sample 
The sample consists of a series of Python scripts that you execute to configure and run an Experiment. This section describes the important aspects of those scripts including helper functions, variables, and output. 

* [Develop the Helper Functions](#develop-the-helper-functions)
* [Create and Update an Optimizely Project](#create-and-update-an-optimizely-project)
* [Create and Update an Attribute to add to the Project](#create-and-update-an-attribute-to-add-to-the-project)
* [Create and Update an Event](#create-and-update-an-event)
* [Create and Update an Audience](#create-and-update-an-audience)
* [Create and Update a Feature](#create-and-update-a-feature)
* [Create and Run an Experiment](#create-and-run-an-experiment)
* [Get the Results of the Experiment](#get-the-results-of-the-experiment)

### Develop the Helper Functions
The purpose of running the individual scripts is to demonstrate the endpoints used to create and update the elements of an Experiment. Once you have created these elements and manually added their identifiers to **[.settings.yaml](./.settings.yaml)**, execute **[result.py](./result.py)** to run the experiment.

Each script reads values from **[.settings.yaml](./.settings.yaml)** using a helper module called `example_tools`. The source code for this is located in **[./example_tools/\_\_init\_\_.py](./example_tools/__init__.py)** and contains a number of important helper functions used by the scripts:
* `load_settings()`: Loads **[settings.yaml](./settings.yaml)** and returns a dictionary representing the key/value settings stored in that file.
* `print_request_details()`: Prints the details of a given REST request to the screen using different font colors.
* `print_response_details()`: Prints the details of a given REST response to the screen using different font colors.
* `print_new_method()`: Prints an action name to the screen (e.g. "Create a new event") in different font colors to make the output easier to read.

Each script imports `example_tools` at the top of the script. The scripts then invoke `load_settings()` to read **[.settings.yaml](./.settings.yaml)** and extract the necessary settings referencing each by name. For example:

```python
import example_tools as et

settings = et.load_settings()

token = ('token' in settings and settings['token']) or raw_input(
    "Please enter a valid personal token (https://app.optimizely.com/v2/profile/api): ")

base_url = ('base_url' in settings and settings[
            'base_url']) or 'https://api.optimizely.com/v2'

project_id = ('project_id' in settings and settings['project_id']) or int(raw_input("Please provide a Project ID: "))
```

Each script retrieves the token and base URL from the settings. The token ensures that you are authenticated to invoke endpoints on the specified base URL. Note that some scripts retrieve additional settings such as the project ID, as shown in the example above. 

### Create and Update an Optimizely Project

A [Project](https://help.optimizely.com/Set_Up_Optimizely/Manage_projects_in_Optimizely_X_Web) is a container for Experiments and is the first element that is created. 

**[project.py](./project.py)** starts by loading the token and base URL from the settings as described above. It then generates a new random number that is used to generate a unique project name and description:
```python
...
make_string_unique = str(random.randrange(0, 10000000000001, 2))

name = 'full_stack project' + make_string_unique
description = 'My REST API FS project' + make_string_unique

...
...
```

The script defines two helper methods: 
* `create_project()`: Creates a new Optimizely Project by invoking the [Create a Project](https://developers.optimizely.com/x/rest/v2/#create-a-project) endpoint and passing in the unique name and description generated above. The function then outputs the request and response to the screen and returns the ID of the new project:

```python
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
```

* `update_project()`: Updates the project that was created above by appending `_updated` to the name and description and invoking the [Update a Project](https://developers.optimizely.com/x/rest/v2/#update-a-project) endpoint passing in the ID of the project. The function then outputs the request and response to the screen:

```python
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
```

The script then invokes these two functions:

```python
et.print_new_method('Create a new project')
id = create_project()

et.print_new_method('Update the project')
update_project(id)
```

**Note:** Most of the scripts use the pattern of creating an entity followed by updating that entity.

### Create and Update an Attribute to add to the Project
An [Attribute](https://help.optimizely.com/Target_Your_Visitors/Custom_Attributes%3A_Capture_visitor_data_through_the_API_in_Optimizely_X) is an entity that allows you to segment a project. For this quickstart, **[attribute.py](./attribute.py)** is used to create and add one attribute to the Project.

The script starts by importing the token and base URL followed by the ID of the project that was created by **[project.py](./project.py)** and manually added to **[.settings.yaml](./.settings.yaml)**. It stores this ID in `project_id`:

```python
...
project_id = ('project_id' in settings and settings['project_id']) or int(
    raw_input("Please provide a Project ID: "))
...
```

The script then generates a new random number that is used to create a unique Attribute key, name, and description:
```python
...
make_string_unique = str(random.randrange(0, 10000000000001, 2))

# Variables to modify
key = 'fs_attribute ' + make_string_unique
name = 'FS attribute ' + make_string_unique
description = 'This is s a fs attr description' + make_string_unique
...
```

The script then defines two helper methods: 
* `create_attribute()`: Creates a new Attribute by invoking the [Create an Attribute](https://developers.optimizely.com/x/rest/v2/#create-an-attribute) endpoint and passing in the unique key, name, and description created above. The function then outputs the request and response to the screen and returns the ID of the new Attribute:

```python
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
```

* `update_project()`: Updates the Attribute that was created above by appending `_updated` to the key, name, and description and invoking the [Update an Attribute](https://developers.optimizely.com/x/rest/v2/#update-an-attribute) endpoint passing in the ID of the Attribute. The function then outputs the request and response to the screen:

```python
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
```

The script then invokes these two functions:

```python
et.print_new_method('Create a new attribute')
id = create_attribute()

et.print_new_method('Update the attribute')
update_attribute(id)
```

### Create and Update an Event
An [Event](https://help.optimizely.com/Measure_success%3A_Track_visitor_behaviors/Events%3A_Tracking_clicks%2C_pageviews%2C_and_other_visitor_actions) tracks an action that a visitor takes on a website. For this quickstart, **[event.py](./event.py)** is used to create and add one event to the Project.

The script starts by importing the token and base URL followed by the ID of the Project that was created by **[project.py](./project.py)** and manually added to **[.settings.yaml](./.settings.yaml)**. It stores this ID in `project_id`:

```python
...
project_id = ('project_id' in settings and settings['project_id']) or int(
    raw_input("Please provide a Project ID: "))
...
```

The script then generates a new random number that is used to create a unique attribute key and name:
```python
...
make_string_unique = str(random.randrange(0, 10000000000001, 2))

# Variables to modify
key = "full_stack_event_" + make_string_unique
name = 'FS event' + make_string_unique
...
```

The script then defines two helper methods: 
* `create_event()`: Creates a new Event by invoking the [Create a Custom Event](https://developers.optimizely.com/x/rest/v2/#create-a-custom-event) endpoint and passing in the unique key and name generated above. The function then outputs the request and response to the screen and returns the ID of the new Event:

```python
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
```

* `update_event()`: Updates the Event that was created above by appending `_updated` to the key and name and invoking the [Update a Custom Event](https://developers.optimizely.com/x/rest/v2/#update-a-custom-event) endpoint passing in the ID of the Event created above. The function then outputs the request and response to the screen:

```python
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
```

The script then invokes these two functions:

```python
et.print_new_method('Create a new event')
id = create_event()

et.print_new_method('Update the event')
update_event(id)
```

### Create and Update an Audience
An [Audience](https://help.optimizely.com/Target_Your_Visitors/Audiences%3A_Choose_which_visitors_to_include) is a type of visitor who comes to your site. For this quickstart, **[audience.py](./audience.py)** is used to create and add one Audience to the Project.

The script starts by importing the token and base URL followed by the Project ID and Attribute name that were created by **[project.py](./project.py)** and **[attribute.py](./attribute.py)** respectively and manually added to **[.settings.yaml](./.settings.yaml)**. It stores these values in `project_id` and `custom_audience_attribute`:

```python
...
project_id = ('project_id' in settings and settings['project_id']) or int(
    raw_input("Please provide a Project ID: "))
custom_audience_attribute = ('project_id' in settings and settings['custom_audience_attribute']) or int(
    raw_input("Please provide the name of a custom attribute: "))
...
```

The script then generates a new random number that is used to create a unique Audience name:
```python
...
make_string_unique = str(random.randrange(0, 10000000000001, 2))

# Variables to modify
name = "Using a Full Stack attribute" + make_string_unique
...
```

The script then defines two helper methods: 
* `create_audience()`: Creates a new Audience by invoking the [Create an Audience](https://developers.optimizely.com/x/rest/v2/#create-an-audience) endpoint and passing in the Project ID and unique audience name generated above. The function then outputs the request and response to the screen and returns the ID of the new Audience:

```python
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
```

* `update_audience()`: Updates the Audience that was created above by appending `_updated` to the name and invoking the [Update an Audience](https://developers.optimizely.com/x/rest/v2/#update-an-audience) endpoint passing in the ID of the project and new name. The function then outputs the request and response to the screen:

```python
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
```

The script then invokes these two functions:

```python
et.print_new_method('Create a new audience')
id = create_audience()

et.print_new_method('Update the audience')
update_audience(id)
```

### Create and Update a Feature
A [Feature](https://help.optimizely.com/Build_Campaigns_and_Experiments/Create_and_deploy_features_and_feature_configurations) is a part of your website to test as part of an Experiment. For this quickstart, **[feature.py](./feature.py)** is used to create and add one Feature and one Variable for that Feature to the Project. A Variable is a parameter of your feature that you want to optimize.

The script starts by importing the token and base URL followed by the Project ID and Audience ID that were created by **[project.py](./project.py)** and **[audience.py](./audience.py)** respectively, and manually added to **[.settings.yaml](./.settings.yaml)**. It stores these values in `project_id` and `audience_id`:

```python
...
project_id = ('project_id' in settings and settings['project_id']) or int(
    raw_input("Please provide a Project ID: "))
audience_id = ('audience_id' in settings and settings['audience_id']) or int(
    raw_input("Please provide an Audience ID: "))
...
```

The script then generates a new random number that is used to create a unique keys and descriptions for the Feature and a Variable:
```python
...
make_string_unique = str(random.randrange(0, 10000000000001, 2))

# Variables to modify
key = 'fs_feature_' + make_string_unique
description = 'This is s a fs feature description' + make_string_unique
variable_key = 'fs_feature_variable_' + make_string_unique
variable_description = 'This is s a fs feature variable description' + make_string_unique
...
```

The script then defines two helper methods: 
* **create_feature**: Creates a new Feature by invoking the [Create a Feature](https://developers.optimizely.com/x/rest/v2/#create-a-feature) endpoint and passing in the Project ID and Audience ID created above. The function then outputs the request and response to the screen and returns the ID of the new Feature and that of the Variable added as part of the Feature:

```python
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
```

* **update_feature**: Updates the Feature and Variable that were created above by appending `_updated` to their key and descriptions and invoking the [Update a Feature](https://developers.optimizely.com/x/rest/v2/#update-a-feature) endpoint passing in the ID's of the Project, Feature, and Variable. The function then outputs the request and response to the screen:

```python
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
```

The script then invokes these two functions:
```python
et.print_new_method('Create a new feature')
(id, variable_id) = create_feature()

et.print_new_method('Update the feature')
update_feature(id, variable_id)
```



### Create and Run an Experiment
Creating an Experiment using **[experiment.py](./experiment.py)** is where everything from the previous steps comes together. An Experiment represents the tests to perform on your website and is the main purpose of the Optimizely platform. An Experiment contains one or *variations* describing different tests to run and can optionally contain one or more Features. 

For this quickstart, you will use **[experiment.py](./experiment.py)** to create and run a single Experiment.

The script starts by importing the token and base URL followed by the Project ID, Event ID, Feature ID, and Feature variables that were created by the previous scripts, and manually added to **[.settings.yaml](./.settings.yaml)**. It stores these values in `project_id`, `event_id`, `feature_id`, and `variable_values`:

```python
...
project_id = ('project_id' in settings and settings['project_id']) or int(
    raw_input("Please provide a Project ID: "))
event_id = ('event_id' in settings and settings['event_id']) or int(
    raw_input("Please provide an Event ID: "))
feature_id = ('feature_id' in settings and settings['feature_id']) or raw_input(
    "Please provide an Feature ID (leave empty to create an experiment without a feature): ")
variable_values = ('variable_values' in settings and settings[
                   'variable_values'])
...
```

Experiments can run without features and variables, so for simplicity, `feature_id` and `variable_values:` are commented out in **[.settings.yaml](./.settings.yaml)**. **[experiment.py](./experiment.py)** checks for the presence of a Feature ID and if not found, gives the user the option to enter one or or more variables at runtime:

```pythong
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
```

If a Feature ID was specified, then the code adds the feature's variable(s) to its `variables` dictionary:

```python
variables = {}
if feature_id: 
    for variable in variable_values:
        for key in variable:
            variables[key] = variable[key]
```


The script then generates a new random number that is used to create a unique Experiment key, description, and Variation key:

```python
make_string_unique = str(random.randrange(0, 10000000000001, 2))

# Variables to modify
key = 'fs_exp_' + make_string_unique
description = 'This is s a fs exp description' + make_string_unique
variation_key = 'var_name_' + make_string_unique
```

The script defines the following helper methods: 
* `create_experiment()`: Creates a new Experiment by invoking the [Create an Experiment](https://developers.optimizely.com/x/rest/v2/#create-an-experiment) endpoint and passing in the Project ID generated above. The function then outputs the request and response to the screen and returns the ID of the new Experiment and that of the Variation added:

```python
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
```

* `update_start_experiment()`: Updates the Experiment's description and Variation key that were created above by appending `_updated` to their key and descriptions and invoking the [Update an Experiment](https://developers.optimizely.com/x/rest/v2/#update-an-experiment) endpoint passing in the ID of the Project. The function also starts execution of the Experiment by appending `?action=start` to the endpoint's URL and checks if any features are available to add as variations. Then function then outputs the request and response to the screen:

```python
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
```

* `pause_experiment()`: Pauses the execution of the Experiment so that it can be updated by a subsequent endpoint. The function includes the Experiment ID in the URL and appends `?action=pause` before re-invoking the [Update an Experiment](https://developers.optimizely.com/x/rest/v2/#update-an-experiment) endpoint:

```python
def pause_experiment(id):
    url = base_url + '/experiments/' + str(id) + '?action=pause'

    experiment = {}

    et.print_request_details('PATCH', url, experiment, headers)
    r = requests.patch(url, data=json.dumps(experiment), headers=headers)
    j = r.json()
    et.print_response_details(r.status_code, j)
    return r.json()
```

* `update_experiment_2()`: Demonstrates how to update a paused Experiment using the [Update an Experiment](https://developers.optimizely.com/x/rest/v2/#update-an-experiment) endpoint.

### Get the Results of the Experiment
After you have run the Experiment, you can retrieve its results. 

For this quickstart, **[results.py](./results.py)** gets the results, a timeseries, stores the results as CSV data, and displays them to the screen.

The script starts by importing the token and base URL, followed by the Experiment ID that was created by **[experiment.py](./experiment.py)** and manually added to **[.settings.yaml](./.settings.yaml)**. It stores this value in `experiment_id`:

```python
...
experiment_id = ('experiment_id' in settings and settings['experiment_id']) or int(
    raw_input("Please provide an Experiment ID: "))
...
```

The script then defines one helper method: 
* `create_result()`: Retrieves results using the [Get Experiment Results](https://developers.optimizely.com/x/rest/v2/#get-experiment-results) endpoint, a time series using the [Get Experiment results time series](https://developers.optimizely.com/x/rest/v2/#get-experiment-results-time-series) endpoint, and the results as CSV data using the [Get Experiment results as a CSV](https://developers.optimizely.com/x/rest/v2/#get-experiment-results-as-a-csv) endpoint. The functions then output the requests and responses to the screen to display these results.

The script then invokes this function:
```python
et.print_new_method('Get experiment results')
create_result()
```

Here is a portion of the results that are displayed on the screen:

```
Get experiment results
Request:
GET https://api.optimizely.com/v2/experiments/10834392320/results
headers: 
{
    "Authorization": "Bearer 2:Abc21231234....", 
    "user-agent": "application/json"
}
body:
{}
{  
   "confidence_threshold":0.9,
   "end_time":"2018-06-08T16:17:47.000000Z",
   "experiment_id":10834392320,
   "metrics":[  
      {  
         "aggregator":"unique",
         "event_id":123456789,
         "name":"FS event_updated",
         "results":{  
            "10831751478":{  
               "is_baseline":true,
               "level":"variation",
               "samples":0,
               "value":0,
               "variation_id":"987654321"
            }
         },
         "scope":"visitor",
         "winning_direction":"increasing"
      }
   ],
   "reach":{  
      "baseline_count":0,
      "baseline_reach":0.0,
      "total_count":0,
      "treatment_count":0,
      "treatment_reach":0.0,
      "variations":{  
         "10831751478":{  
            "count":0,
            "variation_id":"987654321",
            "variation_reach":0.0
         }
      }
   },
   "start_time":"2018-06-08T16:17:43.000000Z",
   "stats_config":{  
      "confidence_level":0.9,
      "difference_type":"relative",
      "epoch_enabled":false
   }
}

Response:
200
body:
{
    "confidence_threshold": 0.9, 
    "end_time": "2018-06-08T16:17:47.000000Z", 
    "experiment_id": 10834392320, 
    "metrics": [
        {
            "aggregator": "unique", 
            "event_id": 123456789, 
            "name": "FS event_updated", 
            "results": {
                "10831751478": {
                    "is_baseline": true, 
                    "level": "variation", 
                    "samples": 0, 
                    "value": 0, 
                    "variation_id": "987654321"
                }
            }, 
            "scope": "visitor", 
            "winning_direction": "increasing"
        }
    ], 
    "reach": {
        "baseline_count": 0, 
        "baseline_reach": 0.0, 
        "total_count": 0, 
        "treatment_count": 0, 
        "treatment_reach": 0.0, 
        "variations": {
            "10831751478": {
                "count": 0, 
                "variation_id": "987654321", 
                "variation_reach": 0.0
            }
        }
    }, 
    "start_time": "2018-06-08T16:17:43.000000Z", 
    "stats_config": {
        "confidence_level": 0.9, 
        "difference_type": "relative", 
        "epoch_enabled": false
    }
}
...
```

