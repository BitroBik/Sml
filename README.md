# PyXml

## About

PyXml is a Python library designed to facilitate the creation and manipulation of XML-like structures in a straightforward manner.

### What does PyXml mean?

PyXml stands for **Python eXtensible Markup Language**.

## Code Overview

Let's delve into the core components of PyXml:

### `Tag` Class

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