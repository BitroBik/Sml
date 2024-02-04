def process(content, indent=''):
    process_data = ''
    
    for c in content:
        if c.type == 'Tag':
            process_data += f'\n{indent}{c.name}'
            process_data += process(c.content, f'{indent}  ')
        else:
            process_data += f'\n{indent}{c.text}'
    
    return process_data

class Tag:
    def __init__(self, name, content=[]):
        self.name = name
        self.content = content
        self.type = 'Tag'

class Text:
    def __init__(self, text):
        self.text = text
        self.type = 'Text'

class Code:
    def __init__(self, content=[]):
        self.content = content
        
    def Run(self):
        print(process(self.content).lstrip())
