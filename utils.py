# Log levels to be set for special print functions
DEBUG = True
INFO = True

def print_debug(statement):
    if (DEBUG):
        print(statement)

def print_info(statement):
    if (INFO):
        print(statement)
