def process(content, indent=''):
    process_data = ''

    for c in content:
        if c.type == 'Tag':
            process_data += f'\n{indent}{c.name}'
            process_data += process(c.content, f'{indent}  ')
        elif c.type == 'Entry':
            process_data += f'\n{indent}{c.name}{input(c.text)}'
            print('')
        elif c.type == 'Text':
            process_data += f'\n{indent}{c.text}'

    return process_data

class Tag:
    def __init__(self, name, content=[]):
        self.name = name
        self.content = content
        self.type = 'Tag'

class Entry:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.type = 'Entry'
    
class Text:
    def __init__(self, text):
        self.text = text
        self.type = 'Text'

class Code:
    def __init__(self, content=[]):
        self.content = content
        
    def Run(self):
        print(process(self.content).lstrip())