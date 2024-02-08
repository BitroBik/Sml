# SML

## About

SML is a Python library designed to facilitate the creation and manipulation of XML-like structures in a straightforward manner.

### What does SMl mean?

SML stands for **Structure Markup Language**.

### Usage Example

Let's see how to use SML to create a structured XML-like document:

```python
from Sml import sml as sm

# Define SML elements
Fork = sm.Text('Fork', 'Stab the food')
Spoon = sm.Text('Spoon', 'Get the food')
Mirror = sm.Text('Mirror', 'To look to yourself')
Bed = sm.Text('Bed', 'Where would you sleep')
Land = sm.Text('Land', 'a book name Land')
Sea = sm.Text('Sea', 'A book name Sea')
Coin = sm.Text('Coin', 'Currency')
Cash = sm.Text('Cash', 'Currency')

Kitchen = sm.Tag('Kitchen', [Fork, Spoon])
Bedroom = sm.Tag('Bedroom', [Bed, Mirror])
Shelf = sm.Tag('Shelf', [Sea, Land])
CashRegister = sm.Tag('Cash Register', [Cash, Coin])

House = sm.Tag('House', [Bedroom, Kitchen])
BookStore = sm.Tag('Book Store', [CashRegister, Shelf])

City = sm.Tag('Neyo City', [BookStore, House])

# Create a SML code instance and run it
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

This code will generate a structured representing a fictional city with a bookstore and a house.

```python
from Sml import sml as sm

# Define SML elements
Name = sm.Entry('Name - ', 'Your Name: ')

Info = sm.Tag('Database', [Name])

# Create a SML code instance and run it
Xml = sm.Code('Xml', [Info])
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

YouTube:
[BitroBik](https://youtube.com/@Bitrobik)