import sys
sys.path.append(".")

        
def convert_to_int(value):
    """it must be used in the value that const the string %
    """
    for index in range(len(value)):
        if value[index] == '%':
            position = index
            break
        
    return int(value[0:position])