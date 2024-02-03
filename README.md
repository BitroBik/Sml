# PyXml

## About

PyXml is a Python library designed to facilitate the creation and manipulation of XML-like structures in a straightforward manner.

### What does PyXml mean?

PyXml stands for **Python eXtensible Markup Language**.

## Code Overview

Let's delve into the core components of PyXml:

### `Tag` Class

The `Tag` class represents XML-like tags and is defined as follows:

```python
class Tag:
    def __init__(self, name, content=[]):
        """
        Initializes a Tag with a given name and optional content.

        Args:
            name (str): The name of the tag.
            content (list): A list containing Text or nested Tag objects.
        """
        self.name = name
        self.content = content
        self.type = 'Tag'
```

### `Text` Class

The `Text` class represents plain text within the PyXml structure:

```python
class Text:
    def __init__(self, text):
        """
        Initializes a Text object with the provided text.

        Args:
            text (str): The plain text content.
        """
        self.text = text
        self.type = 'Text'
```

### `Code` Class

The `Code` class orchestrates the processing and printing of PyXml content:

```python
class Code:
    def __init__(self, content=[]):
        """
        Initializes a Code object with a list of PyXml content.

        Args:
            content (list): A list of Tag or Text objects forming the PyXml structure.
        """
        self.content = content
        
    def Run(self):
        """
        Processes and prints the PyXml content.
        """
        print(process(self.content).lstrip())
```

### Processing Function

The `process` function recursively processes the PyXml content, ensuring proper indentation:

```python
def process(content, indent=''):
    """
    Recursively processes PyXml content and returns a formatted string.

    Args:
        content (list): A list of Tag or Text objects.
        indent (str): The current indentation level.

    Returns:
        str: Formatted string representing the processed PyXml content.
    """
    processed_data = ''
    
    for c in content:
        if c.type == 'Tag':
            processed_data += f'\n{indent}{c.name}'
            processed_data += process(c.content, f'{indent}  ')
        else:
            processed_data += f'\n{indent}{c.text}'
    
    return processed_data
```

## Usage Example

Let's see how to use PyXml to create a structured XML-like document:

```python
from PyXml import pyxml as px

# Define PyXml elements
Fork = px.Text('Fork - Stab the food')
Spoon = px.Text('Spoon - Get the food')
Mirror = px.Text('Mirror - To look to yourself')
Bed = px.Text('Bed - Where would you sleep')
Land = px.Text('Land - a book name Land')
Sea = px.Text('Sea - A book name Sea')
Coin = px.Text('Coin - Currency')
Cash = px.Text('Cash - Currency')

Kitchen = px.Tag('Kitchen', [Fork, Spoon])
Bedroom = px.Tag('Bedroom', [Bed, Mirror])
Shelf = px.Tag('Shelf', [Sea, Land])
CashRegister = px.Tag('Cash Register', [Cash, Coin])

House = px.Tag('House', [Bedroom, Kitchen])
BookStore = px.Tag('Book Store', [CashRegister, Shelf])

City = px.Tag('Neyo City', [BookStore, House])

# Create a PyXml code instance and run it
Xml = px.Code([City])
Xml.Run()
```

This code will generate a structured PyXml document representing a fictional city with a bookstore and a house.