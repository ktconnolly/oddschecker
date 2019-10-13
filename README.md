# oddschecker

Simple class for getting prices from Oddschecker.

Usage 

```
o = Oddschecker('https://www.oddschecker.com/football/english/premier-league/norwich-v-chelsea/winner')

o.get_prices()

# or

o.get_prices(['Bet365', 'Skybet', 'William Hill'])
```

Example output
```
defaultdict(<class 'list'>,
            {'Chelsea': [Book(name='Bet365', price=1.8),
                         Book(name='Skybet', price=1.8),
                         Book(name='William Hill', price=1.8)],
             'Draw':    [Book(name='Skybet', price=4.0),
                         Book(name='William Hill', price=3.9),
                         Book(name='Bet365', price=3.75)],
             'Norwich': [Book(name='Bet365', price=4.33),
                         Book(name='William Hill', price=4.2),
                         Book(name='Skybet', price=4.0)]})
```
