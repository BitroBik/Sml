class Tag:
    def __init__(self, name, content=[]):
        self.name = name
        self.content = content
        self.type = 'Tag'

class Msg:
    def __init__(self, text):
        self.text = text
        self.type = 'Msg'

class Code:
    def __init__(self, content=[]):
        self.content = content
        
        try:
            self.tag = {}
            for cont in self.content:
                if cont.type == 'Tag':
                    self.tag.update({cont.name: cont.content})
        except AttributeError as e:
            print(f'Unexpected Error: {e}')

    def Run(self):
        for key in self.tag:
            print(key)
            for msg in self.tag[key]:
                print(msg.text)