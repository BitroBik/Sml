def process(content, up, indent=''):
    process_data = ''

    for c in content:
        if c.type == 'Tag':
            if c.attribute == {}:
                process_data += f'\n{indent}{c.name}'
                process_data += process(c.content, up, f'{indent}{up}')
            else:
                for key in c.attribute:
                    process_data += f'\n{indent}{c.name}[{key}="{c.attribute[key]}"]'
                    process_data += process(c.content, up, f'{indent}{up}')
        elif c.type == 'Entry':
            process_data += f'\n{indent}{c.name}{input(c.text)}'
            print('')
        elif c.type == 'Text':
            if c.attribute == {}:
                process_data += f'\n{indent}{c.name}-{c.text}'
            else:
                for key in c.attribute:
                    process_data += f'\n{indent}{c.name}[{key}="{c.attribute[key]}-{c.text}"]'
        elif c.type == 'Filter':
            if c.attribute == {}:
                process_data += f'\n{indent}{c.name}-{c.text}'
            else:
                for key in c.attribute:
                    process_data += f'\n{indent}{c.name}[{key}="{c.attribute[key]}-{c.text}"]'

        elif c.type == 'Condition':
            if c.condition:
               if c.attribute == {}:
                   process_data += f'\n{indent}{c.text}'
               else:
                   for key in c.attribute:
                       process_data += f'\n{indent}{c.text}[{key}="{c.attribute[key]}"]'              
        elif c.type == 'Code':
            process_data = 'Cannot Nest Code only Tag'
            break

    return process_data

def Xmlified(content, up, indent=''):
    process_data = ''

    for c in content:
        if c.type == 'Tag':
            if c.attribute == {}:
                process_data += f'\n{indent}<{c.name}>'
                process_data += Xmlified(c.content, up, f'{indent}{up}')
                process_data += f'\n{indent}</{c.name}>'
            else:
                for key in c.attribute:
                    process_data += f'\n{indent}<{c.name} {key}="{c.attribute[key]}">'
                    process_data += Xmlified(c.content, up, f'{indent}{up}')
                    process_data += f'\n{indent}</{c.name}>'
                    break
        elif c.type == 'Entry':
            process_data += f'\n{indent}<{c.name}>{input(c.text)}</{c.name}>'
            print('')
        elif c.type == 'Text':
            if c.attribute == {}:
                process_data += f'\n{indent}<{c.name}>{c.text}</{c.name}>'
            else:
                for key in c.attribute:
                    process_data += f'\n{indent}<{c.name} {key}="{c.attribute[key]}>{c.text}</{c.name}>"'
        elif c.type == 'Filter':
            if c.attribute == {}:
                process_data += f'\n{indent}<{c.name}>{c.text}</{c.name}>'
            else:
                for key in c.attribute:
                    process_data += f'\n{indent}<{c.name} {key}="{c.attribute[key]}>{c.text}</{c.name}>"'
        elif c.type == 'Condition':
            if c.condition:
                if c.attribute == {}:
                    process_data += f'\n{indent}<{c.name}>{c.text}</{c.name}>'
                else:
                    for key in c.attribute:
                        process_data += f'\n{indent}<{c.name} {key}="{c.attribute[key]}>{c.text}</{c.name}>"'
        elif c.type == 'Code':
            process_data = 'Cannot Nest Code only Tag'
            break

    return process_data

def Find(find, content):
    data = ''
            
    for c in content:
        if c.name == find:
            data += f'{c.name}'
            break
        else:
            if c.type == 'Tag':
                data += f'{c.name}/{Find(find, c.content)}'
    return data

def Filtering(filtered, content):
    data = []
    
    for c in content:
        if c.type == 'Filter' and c.filter == filtered:
            data.append(c.name)
        elif c.type == 'Tag':
            data.extend(Filtering(filtered, c.content))
    
    return data

class Filter:
    def __init__(self, name, text, filter, attribute={}):
        self.name = name
        self.text = text
        self.filter = filter
        self.attribute = attribute
        self.type = 'Filter'
        
        if isinstance(self.attribute, dict):
            pass
        else:
            self.attribute = {'Error':'self.attribute must be on a dictionary'}
      
class Hidden:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.type = 'Hidden'

class Tag:
    def __init__(self, name, content=[], attribute={}):
        self.name = name
        self.content = content
        self.attribute = attribute
        self.type = 'Tag'

        if isinstance(self.content, list):
            pass
        else:
            self.content = [content]
            print(f'self.content must be a list: {self.name}')
        if isinstance(self.attribute, dict):
            pass
        else:
            self.attribute = {'Error':'self.attribute must be on a dictionary'}

class Entry:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.type = 'Entry'

class Text:
    def __init__(self, name, text, attribute={}):
        self.name = name
        self.text = text
        self.attribute = attribute
        self.type = 'Text'

        if isinstance(self.attribute, dict):
            pass
        else:
            self.attribute = {'Error':'self.attribute must be on a dictionary'}

class Condition:
    def __init__(self, name, text, condition, attribute={}):
        self.name = name
        self.text = text
        self.condition = condition
        self.attribute = attribute
        self.type = 'Condition'

        if isinstance(self.attribute, dict):
            pass
        else:
            self.attribute = {'Error':'self.attribute must be on a dictionary'}

class Code:
    def __init__(self, name, content, up='  '):
        self.name = name
        self.up = up
        self.content = content
        self.will_run = True
        self.type = 'Code'

        if isinstance(self.up, str):
            pass
        else:
            self.will_run = False
            print(f'self.up must be a string: Code("{self.name}", [], "  ")')

        if isinstance(self.content, list):
            pass
        else:
            self.will_run = False
            print(f'self.content must be a list: [{content.name}]')

    def Run(self):
        if self.will_run:
            print(process(self.content, self.up).lstrip())

    def Turn_Xml(self):
        if self.will_run:
            print(Xmlified(self.content, self.up).lstrip())
    
    def Find(self, find):
        if self.will_run:
            try:
                print(Find(find, self.content))
            except RecursionError:
                print(f'Cannot find {find}')
    
    def Filter_Content(self, filter):
        if self.will_run:
            print(Filtering(filter, self.content))