import csv

def csv_dict_reader(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Misol fayl: users.csv
# users.csv:
# name,age,city
# John,25,New York
# Alice,30,Los Angeles
# Bob,35,Chicago

data = csv_dict_reader('users.csv')
for row in data:
    print(row)
```

```python
import csv

def csv_dict_reader(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

# Misol fayl: users.csv
# users.csv:
# name,age,city
# John,25,New York
# Alice,30,Los Angeles
# Bob,35,Chicago

data = csv_dict_reader('users.csv')
for row in data:
    print(row)
