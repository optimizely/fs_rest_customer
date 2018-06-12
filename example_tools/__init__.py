import yaml
import json

def load_settings():
    f = open('.settings.yaml', 'r')
    settings = f.read()
    return yaml.load(settings)


def colors():
    return {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[91m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m'
    }

def pprint(obj):
    print json.dumps(obj, indent=4, sort_keys=True)

def pretty_code(code):
    s = colors()['OKGREEN']
    w = colors()['WARNING']
    f = colors()['FAIL']
    e = colors()['ENDC']    
    if code >= 200 and code < 300:
        return s + str(code) + e;
    if code >= 400 and code < 500:
        return w + str(code) + e;
    if code >= 500 and code < 600:
        return f + str(code) + e;


def print_request_details(method, url, data, headers):
    b = colors()['BOLD']
    u = colors()['UNDERLINE']
    e = colors()['ENDC']
    print b + u + "Request:" + e
    print method + " " + url
    print b + 'headers: ' + e
    pprint(headers)
    print b + 'body:' + e
    pprint(data)

def print_response_details(code, data):
    b = colors()['BOLD']
    u = colors()['UNDERLINE']
    e = colors()['ENDC']    
    print b + u + 'Response:\n' + e + pretty_code(code)
    print b + 'body:' + e
    pprint(data)

def print_new_method(s):
    c = colors()
    print c['OKBLUE'] + c['BOLD'] + '\n' + s + c['ENDC']



