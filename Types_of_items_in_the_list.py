# program to print what types of items are present in the string
datalist = [1452, 11.23, 1+2j, True, 'something',
            (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for item in datalist:
    print(item, type(item))
