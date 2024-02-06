# PXML

## About

PXML is a Python library designed to facilitate the creation and manipulation of XML-like structures in a straightforward manner.

### What does PXMl mean?

PXML stands for **Python eXtensible Markup Language**.

### Usage Example

Let's see how to use PyXml to create a structured XML-like document:

```python
from PyXml import pyxml as px

# Define PXML elements
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

# Create a PXML code instance and run it
Xml = px.Code('Xml', [City])
Xml.Run()
```
**Output**
```Output
Neyo City
  Book Store
    Cash Register
      Cash -  Currency
      Coin - Currency
    Shelf
      Sea - A book name Sea
      Land - A book name Land
  House
    Bedroom
      Bed - Where would you sleep
      Mirror - To look to yourself
    Kitchen
      Spoon - Get the food
      Fork - Stab the food
```

This code will generate a structured PXML document representing a fictional city with a bookstore and a house.

```python
from PyXml import pyxml as px

# Define PXML elements
Name = px.Entry('Name - ', 'Your Name: ')

Info = px.Tag('Database', [Name])

# Create a PXML code instance and run it
Xml = px.Code('Xml', [Info])
Xml.Run()
```
**Output**
```Output
Your Name: Bitro

Database
  Name - Bitro
```

This code present the new class name Entry and how it work and generated.

## More Usage Examle

Wiki:
[Pyxml Wiki]https://pyxmlwiki.w3spaces.com/