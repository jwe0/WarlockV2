from colorama import Fore
from datetime import datetime

def info(content, show=True):
    message = f"[{datetime.now().strftime("%H:%M:%S")}] | [{Fore.BLUE}INFO{Fore.RESET}]    | {content}"
    if show:
        print(message)
    return message

def warning(content, show=True):
    message = f"[{datetime.now().strftime("%H:%M:%S")}] | [{Fore.YELLOW}WARNING{Fore.RESET}] | {content}"
    if show:
        print(message)
    return message

def error(content, show=True):
    message = f"[{datetime.now().strftime("%H:%M:%S")}] | [{Fore.RED}ERROR{Fore.RESET}]   | {content}"
    if show:
        print(message)
    return message

def success(content, show=True):
    message = f"[{datetime.now().strftime("%H:%M:%S")}] | [{Fore.GREEN}SUCCESS{Fore.RESET}] | {content}"
    if show:
        print(message)
    return message

def inpt(content, show=False):
    message = f"[{datetime.now().strftime("%H:%M:%S")}] | [{Fore.CYAN}INPUT{Fore.RESET}]   | {content}: "
    return input(message)

def log(mode="info", content="Test!!", show=True):
    functions = {
        "info"    : info,
        "warning" : warning,
        "error"   : error,
        "input"   : inpt,
        "success" : success
    }
    if mode.lower() not in functions:
        error("Invalid log mode")
        exit()
    return functions[mode](content, show)