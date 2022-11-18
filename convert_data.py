'''
Module: convert_data

Functions in this module can be used to convert the string data values accessed from the yahoo finance page into correct float values.
'''

def convert_large(x):
    '''
    This function is used to convert a large number in string version to floats.

    Args:
        x (string): the string version of the number.

    Returns:
        x (float): the float version of x
    '''
    if x[-1] == 'T':
        return round(float(x[:-1]) * 1000000000000)
    elif x[-1] == 'B':
        return round(float(x[:-1]) * 1000000000)
    elif x[-1] == 'M':
        return round(float(x[:-1]) * 1000000)
    else:
        return round(float(x.replace(',', '')))

def convert_small(x):
    '''
    This function is used to convert small numbers represented by strings into floats.

    Args:
        x (string): the string version of the number.

    Returns:
        x (float): the float version of x
    '''
    if x == 'N/A':
        return None
    else:
        return float(x)

def convert_percentages(x):
    '''
    This function is used to convert percentages represented by strings into floats.

    Args:
        x (string): the string version of the number.

    Returns:
        x (float): the float version of x
    '''
    return float(x[:-1])

def convert(x):
    '''
    This function is used to convert a string version of a number into a flooat version.

    Args:
        x (string): the string version of the number.

    Returns:
        x (float): the float version of x
    '''
    if '%' in x:
        return convert_percentages(x)
    elif 'T' in x or 'B' in x or 'M' in x:
        return convert_large(x)
    else:
        return convert_small(x)