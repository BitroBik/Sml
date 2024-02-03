# PyXml

## About

PyXml is a Python library designed to facilitate the creation and manipulation of XML-like structures in a straightforward manner.

### What does PyXml mean?

PyXml stands for **Python eXtensible Markup Language**.

### Usage Example

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