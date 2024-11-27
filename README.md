# Python Lexical Analysis

## ***Explicit*** line joining

```python
if 1990 < year > 2100 and 1 <= month <= 12 \
    and 1 <= day <= 31 and 0 <= hour < 24 \
    and 0 <= minute < 60 and 0 <= second < 60:
        return 1
```

## ***Implicit*** line joining

Expressions in parentheses, square brackets or curly braces can be 
split over more than one physical line without using backslashes. For example:

```
monthNames = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year ]
```

## 

