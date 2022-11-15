'''
Module: convert_data

Functions in this module can be used to convert the string data values accessed from the yahoo finance page into correct float values.
'''

def convert_large(x):           # Convert large numbers represented by strings into floats
    if x[-1] == 'T':
        return round(float(x[:-1]) * 1000000000000)
    elif x[-1] == 'B':
        return round(float(x[:-1]) * 1000000000)
    elif x[-1] == 'M':
        return round(float(x[:-1]) * 1000000)
    else:
        return round(float(x.replace(',', '')))

def convert_small(x):           # Convert small numbers represented by strings into floats
    if x == 'N/A':
        return None
    else:
        return float(x)

def convert_percentages(x):     # Convert percentages represented by strings into floats
    return float(x[:-1])

def convert(x):

    if '%' in x:
        return convert_percentages(x)
    elif 'T' in x or 'B' in x or 'M' in x:
        return convert_large(x)
    else:
        return convert_small(x)