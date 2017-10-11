
def print_failure(obj):
    print(failure(obj))

def print_success(obj):
    print(success(obj))

def print_message(obj):
    print(message(obj))

def print_header(obj):
    print(header(obj))

def get_input(obj):
    return input(bold(obj))

def success(obj):
    return TerminalColor.GREEN + str(obj) + TerminalColor.RESET

def failure(obj):
    return TerminalColor.RED + str(obj) + TerminalColor.RESET

def message(obj):
    return TerminalColor.BLUE + str(obj) + TerminalColor.RESET

def header(obj):
    return TerminalColor.BLUE + TerminalColor.BOLD + str(obj) + TerminalColor.RESET

def bold(obj):
    return TerminalColor.BOLD + str(obj) + TerminalColor.RESET

class TerminalColor:
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
