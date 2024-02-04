def process(content, up, indent=''):
    process_data = ''

    for c in content:
        if c.type == 'Tag':
            if c.attributes == '':
                process_data += f'\n{indent}{c.name}'
                process_data += process(c.content, up, f'{indent}{up}')
            else:
                process_data += f'\n{indent}{c.name}[{c.attributes}]'
                process_data += process(c.content, up, f'{indent}{up}')
        elif c.type == 'Entry':
            process_data += f'\n{indent}{c.name}{input(c.text)}'
            print('')
        elif c.type == 'Text':
            if c.attributes == '':
                process_data += f'\n{indent}{c.text}'
            else:
                process_data += f'\n{indent}{c.text}[{c.attributes}]'
        elif c.type == 'Code':
            process_data = 'Cannot Nest Code only Tag'
            break
            
    return process_data

class Tag:
    def __init__(self, name, content=[], attributes=''):
        self.name = name
        self.content = content
        self.attributes = attributes
        self.type = 'Tag'

class Entry:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.type = 'Entry'
    
class Text:
    def __init__(self, text, attributes=''):
        self.text = text
        self.attributes = attributes
        self.type = 'Text'

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