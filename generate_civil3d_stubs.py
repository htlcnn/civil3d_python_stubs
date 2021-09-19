from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from pathlib import Path
import time

from bs4 import BeautifulSoup
import requests


def help_url(_id):
    return 'https://help.autodesk.com/cloudhelp/2020/ENU/Civil3D-API/files/html/{}.htm'.format(_id)


def indent(lines, levels=1):
    return '\n'.join([(4 *' '*levels + line) for line in lines.splitlines()])


def get_detail_page(api_id):
    url = help_url(api_id)
    while True:
        try:
            r = requests.Session().get(url)
            break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
        
    soup = BeautifulSoup(r.text)
    return soup


def get_child(parent, children_data_type=''):
    '''
    Get child with 'children_data_type' in parent['ttl']
    return first child if multiple children are found
    '''
    if not children_data_type:
        return parent['children'][0]
    for member in parent['children']:
        if children_data_type in member['ttl']:
            return member
        

def get_children(parent, children_data_type=''):
    '''
    Get children with 'children_data_type' in parent['ttl']
    If only one child is found, return [child]
    '''
    if not children_data_type:
        return parent['children']
    ret = []
    for member in parent['children']:
        if children_data_type in member['ttl']:
            ret.append(member)
    return ret

        
def parse_properties(properties):
    '''
    Generate code for properties
    '''
    ret = []
    syntax = '{} = None'
    for prop in get_children(properties, 'Property'):
        name = prop['ttl'].split('Property')[0].strip()
        ret.append(syntax.format(name))

    return '\n'.join(ret)


def group_method_by_name(methods):
    group = {}
    for method in methods:
        name = method['ttl'].split()[0]
        # have overloads
        if method['children']:
            overloads = method['children']
        else:
            overloads = [method]
            
        group[name] = overloads

    return group


def get_method_docstring(method):
    soup = get_detail_page(method['id'])
    
    # method name
    name = soup.select_one('.head-block').text.split()[0]

    # parameters
    parameters = []
    for p in soup.select('#parameters dl'):
        p_name = p.select_one('dt').text
        p_type = p.select_one('.nolink')
        if not p_type:
            p_type = p.select_one('a')
        p_type = p_type.text
        # get parameter description, if it is a <br /> tag, get its text.
        p_description = list(p.select_one('dd').children)[-1]
        try:
            p_description = p_description.text
        except:
            pass
        
        parameters.append({
            'name': p_name,
            'type': p_type,
            'description': p_description
        })

    # return type
    return_type = soup.select_one('#syntaxSection .codeblock a')
    if not return_type:
        return_type = soup.select_one('#syntaxSection .codeblock')
        return_type = return_type.text.split(name)[0].split()[-1]
    else:
        return_type = return_type.text

    if return_type == 'void':
        return_type = ''

    ### build docstring
    docstring = []

    # syntax
    method_syntax = []
    method_syntax.append(name)
    method_syntax.append('(')
    method_syntax.append(', '.join('{name}: {type}'.format(**p) for p in parameters))
    method_syntax.append(')')
    if return_type:
        method_syntax.append(' -> {}'.format(return_type))

    docstring.append(''.join(method_syntax))
    
    # description
    description = soup.select_one('#mainBody p')
    if description:
        docstring.append(indent(description.text.strip()))
    
    # remarks    
    remarks = soup.select_one('#remarksSection')
    if remarks:
        remarks = remarks.text.strip()
        docstring.append(indent('Remarks: {}'.format(remarks)))
        
    # parameters
    for p in parameters:        
        if p['description']:
            p_docstring = '{name}: {type} - {description}'
        else:
            p_docstring = '{name}: {type}'            
        docstring.append(indent(p_docstring.format(**p)))

    return '\n'.join(docstring)


def parse_methods(methods):
    syntax = []
    for name, group in group_method_by_name(methods).items():
        syntax.append('def {}(self):'.format(name))
        syntax.append(indent('"""'))
        for method_overload in group:
            overload_docstring = get_method_docstring(method_overload)
            syntax.append(indent(overload_docstring))
        syntax.append(indent('"""'))
        syntax.append(indent('pass'))
        syntax.append('\n')
    return '\n'.join(syntax)


def parse_enum(enum):
    url = help_url(enum['id'])
    while True:
        try:
            r = requests.Session().get(url)
            break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    soup = BeautifulSoup(r.text)
    
    ret = []
    
    name = enum['ttl'].split()[0]
    def_line = 'class {}(object):'.format(name)
    ret.append(def_line)
    
    rows = soup.select('#membersSection table tr')
    for row in rows:
        if not row.select('td'):
            continue
        _, name, value, _ = row.select('td')
        if value.text.isnumeric():
            line = "{} = {}"
        else:
            line = "{} = '{}'"
        ret.append(indent(line.format(name.text, value.text)))
        
    return '\n'.join(ret)


def get_class_parent(cls):
    url = help_url(cls['id'])
    while True:
        try:
            r = requests.Session().get(url)
            break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    soup = BeautifulSoup(r.text)
    
    # parent is Civil object
    parent = soup.select_one('#familySection>a')
    
    # parent is not Civil object (often System.Object)
    if not parent:
        parent = soup.select_one('#familySection .nolink')
        if not parent:
            return ''
        # parent is System.Object
        if parent.text.strip().endswith('Object'):
            return 'object'
        else:
            return parent.text
    
    # if parent contains overload info, get only class name
    if '<' in parent.text:
        return parent.text.split('<')[0].split('.')[-1].strip()
    else:
        return parent.text.split('.')[-1].strip()


def get_constructor_docstring(constructor):
    constructor_docstring = []
    
    # have overloads
    if constructor['children']:
        for constructor_overload in constructor['children']:
            soup = get_detail_page(constructor_overload['id'])
            name = constructor_overload['ttl'].split('Constructor')[0]
            parameters = []
            for p in soup.select('#parameters dl'):
                parameter_name = p.select_one('dt').text
                parameter_type = p.select_one('dd').text.strip('Type: ').split('.')[-1]
                parameters.append('{}: {}'.format(parameter_name, parameter_type))
            if parameters:
                parameters = ', '.join(parameters)
            else:
                parameters = ''
            constructor_docstring.append('{}({})'.format(
                name.strip(),
                parameters
            ))
    else:
        soup = get_detail_page(constructor['id'])
        name = constructor['ttl'].split('Constructor')[0]
        parameters = []
        for p in soup.select('#parameters dl'):
            parameter_name = p.select_one('dt').text
            parameter_type = p.select_one('dd').text.strip('Type: ').split('.')[-1]
            parameters.append('{}: {}'.format(parameter_name, parameter_type))
        if parameters:
            parameters = ', '.join(parameters)
        else:
            parameters = ''
        constructor_docstring.append('{}({})'.format(
            name.strip(),
            parameters
        ))
    
    
def get_class_docstring(cls):
    soup = get_detail_page(cls['id'])
    
    # Description
    description = soup.select_one('#mainBody>p')
    if description:
        description = description.text.strip()
    else:
        description = ''
    # Constructors
    constructor = get_child(cls, 'Constructor')
    if constructor:
        constructor_docstring = get_constructor_docstring(constructor)
    else:
        constructor_docstring = ''
        
    ### build docstring
    docstring = []
    docstring.append('"""')
    docstring.append(description)
    if constructor_docstring:
        docstring.append('\n\n'.join(constructor_docstring).strip())
    docstring.append('"""')
    
    return '\n'.join(docstring)


def parse_class(cls):
    syntax = []
    
    # def_line    
    name = cls['ttl'].split()[0]
    if '<' in name:
        name = name.split('<')[0]
    elif '(' in name:
        name = name.split('(')[0]
    parent = get_class_parent(cls)
    def_line = 'class {}({}):'.format(name, parent)
    syntax.append(def_line)
    
    # docstring
    docstring = get_class_docstring(cls)
    syntax.append(indent(docstring))
    
    # properties
    
    properties = get_child(cls, 'Properties')
    if properties:
        properties_syntax = parse_properties(properties)
        syntax.append(indent(properties_syntax))

    # methods
    methods = get_child(cls, 'Methods')
    if methods:
        methods = get_children(methods, 'Method')
        methods_syntax = parse_methods(methods)
        syntax.append(indent(methods_syntax))
        
    syntax.append(indent('pass'))

    return '\n'.join(syntax)


def parse_child(child):
    if 'Enumeration' in child:
        content = parse_enum(child)
    else:
        # all other data types: Class, Interface, Structure
        # are considered classes in python
        content = parse_class(child)
    return content


def get_namespaces(json_url):
    r = requests.Session().get(json_url)
    for child in r.json()['books']:
        if child['ttl'] == 'API Reference Guide':
            return child['children']


def main():
    namespaces = get_namespaces('https://help.autodesk.com/view/CIV3D/2020/ENU/data/toctree.json')
    for ns in namespaces:
        name = ns['ttl'].split()[0]
        print('*'*80)
        print(name)
        folder_path = name.replace('.', '/')
        Path(folder_path).mkdir(parents=True, exist_ok=True)
        results = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_result = {executor.submit(parse_child, child): child['ttl'] for child in ns['children']}
            for future in as_completed(future_result):
                name = future_result[future].split()[0]
                print('Done {}'.format(future_result[future]))
                try:
                    content = future.result()
                    results.append({
                        'name': name,
                        'content': content
                    })
                except Exception as e:
                    print(e)

        results.sort(key=lambda x:x['name'])

        with open(os.path.join(folder_path, '__init__.py'), 'w') as f:
            f.write('\n\n'.join(r['content'] for r in results))
            
            
if __name__ == '__main__':
    main()